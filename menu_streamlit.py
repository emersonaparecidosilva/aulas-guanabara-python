"""
Navegador de exercícios (versão Streamlit) - roda no Streamlit Cloud.

Como o Streamlit Cloud não tem terminal interativo, o exercício é executado
via subprocess com um "runner" que substitui o input():
  - se houver uma resposta guardada, ela é entregue ao programa;
  - se não houver, o runner encerra com o código 87 ("aguardando entrada").
O menu então mostra o que já foi impresso e pede a próxima resposta.
A cada resposta nova o exercício é reexecutado do zero com todas as respostas
(replay), usando uma semente fixa no random para o resultado ser repetível.
"""
import os
import random
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
IGNORAR = {".git", ".venv", "venv", "__pycache__", ".github", ".streamlit", ".idea", ".vscode", "modulos"}
ARQUIVOS_IGNORADOS = {"menu.py", "menu_gui.py", "menu_streamlit.py", "streamlit_app.py"}
TIMEOUT_SEGUNDOS = 15
CODIGO_AGUARDANDO = 87

st.set_page_config(page_title="Exercícios - Curso de Python", page_icon="🐍", layout="wide")

# Código que roda dentro do subprocess, antes do exercício.
RUNNER = r'''
import builtins, os, random, runpy, sys, time

caminho, seed = sys.argv[1], int(sys.argv[2])
sys.argv = [caminho]
sys.path.insert(0, os.path.dirname(caminho))
random.seed(seed)

# replay rápido: sem esperas
time.sleep = lambda s=0: None

# ignora limpar tela do Windows/Linux
_system = os.system
os.system = lambda c: 0 if str(c).strip().lower() in ("cls", "clear") else _system(c)

def _input(prompt=""):
    sys.stdout.write(str(prompt))
    sys.stdout.flush()
    linha = sys.stdin.readline()
    if linha == "":
        sys.stdout.flush()
        os._exit(87)  # acabaram as respostas: aguardando entrada
    linha = linha.rstrip("\r\n")
    sys.stdout.write(linha + "\n")  # ecoa a resposta, como num terminal
    return linha

builtins.input = _input
runpy.run_path(caminho, run_name="__main__")
'''


# ---------- utilidades ----------
def ordem_natural(nome: str):
    """Ordena 'ex2' antes de 'ex10'."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", nome)]


def caminho_seguro(rel: str) -> Path:
    """Garante que o caminho nunca saia da pasta raiz do projeto."""
    p = (ROOT / rel).resolve()
    if p != ROOT and ROOT not in p.parents:
        return ROOT
    return p


def listar(pasta: Path):
    pastas, arquivos = [], []
    for item in pasta.iterdir():
        if item.name in IGNORAR or item.name.startswith("."):
            continue
        if item.is_dir():
            pastas.append(item)
        elif item.suffix == ".py" and not eh_menu(item):
            arquivos.append(item)
    pastas.sort(key=lambda p: ordem_natural(p.name))
    arquivos.sort(key=lambda p: ordem_natural(p.name))
    return pastas, arquivos


def eh_menu(arquivo: Path) -> bool:
    """Os próprios menus (só na raiz) não aparecem na lista de exercícios."""
    return arquivo.parent == ROOT and arquivo.name in ARQUIVOS_IGNORADOS


def normalizar(texto: str) -> str:
    """Minúsculas e sem acentos, para a busca achar 'extenso' em 'Extensão'."""
    sem_acento = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in sem_acento if unicodedata.category(c) != "Mn")


def buscar(termo: str, limite: int = 200):
    """Busca por nome em TODAS as subpastas. Retorna (pastas, arquivos)."""
    termo = normalizar(termo)
    pastas, arquivos = [], []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR and not d.startswith(".")]
        base = Path(dirpath)
        for d in dirnames:
            if termo in normalizar(d):
                pastas.append(base / d)
        for f in filenames:
            caminho = base / f
            if caminho.suffix == ".py" and not f.startswith(".") and not eh_menu(caminho):
                if termo in normalizar(f):
                    arquivos.append(caminho)
    chave = lambda p: ordem_natural(str(p.relative_to(ROOT)))
    pastas.sort(key=chave)
    arquivos.sort(key=chave)
    return pastas[:limite], arquivos[:limite]


@st.cache_data(show_spinner=False, ttl=600)
def executar(caminho: str, entradas: tuple, seed: int):
    """Roda o exercício com as respostas já dadas. Retorna (stdout, stderr, codigo)."""
    arquivo = Path(caminho)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
    stdin = "".join(e + "\n" for e in entradas)
    try:
        r = subprocess.run(
            [sys.executable, "-c", RUNNER, str(arquivo), str(seed)],
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(arquivo.parent),
            env=env,
            timeout=TIMEOUT_SEGUNDOS,
        )
        return r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired as e:
        saida = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        return saida, f"⏱️ Tempo limite de {TIMEOUT_SEGUNDOS}s excedido (laço infinito?).", -1


# ---------- estado ----------
st.session_state.setdefault("pasta", "")        # caminho relativo à raiz
st.session_state.setdefault("arquivo", None)    # .py selecionado (relativo)
st.session_state.setdefault("sessoes", {})      # {arquivo: {"entradas": [...], "seed": int}}


def ir_para(rel: str):
    st.session_state.pasta = rel
    st.session_state.arquivo = None


def abrir(rel: str):
    st.session_state.arquivo = rel


def abrir_resultado(rel_pasta: str, rel_arquivo: str):
    """Abre um arquivo achado na busca, já posicionando a navegação na pasta dele."""
    st.session_state.pasta = rel_pasta
    st.session_state.arquivo = rel_arquivo


def enviar_resposta(rel: str):
    resposta = st.session_state.get(f"resp_{rel}", "")
    st.session_state.sessoes[rel]["entradas"].append(resposta)


# ---------- interface ----------
st.title("🐍 Navegador de Exercícios - Curso de Python")

pasta_atual = caminho_seguro(st.session_state.pasta)
rel_atual = "" if pasta_atual == ROOT else str(pasta_atual.relative_to(ROOT))

col_nav, col_main = st.columns([1, 2], gap="large")

with col_nav:
    st.caption("📂 /" + rel_atual.replace("\\", "/"))

    if pasta_atual != ROOT:
        pai = pasta_atual.parent
        rel_pai = "" if pai == ROOT else str(pai.relative_to(ROOT))
        st.button("⬅️ Voltar", on_click=ir_para, args=(rel_pai,), use_container_width=True)

    busca = st.text_input("🔍 Buscar em todas as pastas", placeholder="ex: 035 ou tupla").strip()

    if busca:
        # busca global: percorre todas as subpastas
        pastas, arquivos = buscar(busca)
        total = len(pastas) + len(arquivos)
        st.caption(f"{total} resultado(s) em todas as pastas" if total else "Nenhum resultado.")

        for p in pastas:
            rel = str(p.relative_to(ROOT))
            st.button(f"📁 {p.name}", key=f"bd_{rel}", on_click=ir_para, args=(rel,), use_container_width=True)

        for a in arquivos:
            rel = str(a.relative_to(ROOT))
            rel_pasta = "" if a.parent == ROOT else str(a.parent.relative_to(ROOT))
            local = rel_pasta.replace("\\", "/") or "/"
            st.button(
                f"📄 {a.name}  ·  {local}",
                key=f"bf_{rel}",
                on_click=abrir_resultado,
                args=(rel_pasta, rel),
                use_container_width=True,
                type="primary" if st.session_state.arquivo == rel else "secondary",
            )
    else:
        pastas, arquivos = listar(pasta_atual)

        if not pastas and not arquivos:
            st.info("Nada encontrado aqui.")

        for p in pastas:
            rel = str(p.relative_to(ROOT))
            st.button(f"📁 {p.name}", key=f"d_{rel}", on_click=ir_para, args=(rel,), use_container_width=True)

        for a in arquivos:
            rel = str(a.relative_to(ROOT))
            st.button(
                f"📄 {a.name}",
                key=f"f_{rel}",
                on_click=abrir,
                args=(rel,),
                use_container_width=True,
                type="primary" if st.session_state.arquivo == rel else "secondary",
            )

with col_main:
    rel_arquivo = st.session_state.arquivo
    if not rel_arquivo:
        st.info("Escolha um exercício na lista ao lado para ver o código e executá-lo.")
    else:
        arquivo = caminho_seguro(rel_arquivo)
        if not arquivo.is_file():
            st.error("Arquivo não encontrado.")
        else:
            codigo = arquivo.read_text(encoding="utf-8", errors="replace")
            st.subheader(arquivo.name)

            aba_exec, aba_codigo = st.tabs(["▶️ Iniciar", "📜 Código"])

            with aba_codigo:
                st.code(codigo, language="python", line_numbers=True)

            with aba_exec:
                sessao = st.session_state.sessoes.get(rel_arquivo)
                rotulo = "🔄 Reiniciar" if sessao else "▶️ Iniciar"

                if st.button(rotulo, type="primary", key=f"run_{rel_arquivo}"):
                    sessao = {"entradas": [], "seed": random.randint(1, 10**6)}
                    st.session_state.sessoes[rel_arquivo] = sessao

                if sessao:
                    saida, erro, retorno = executar(
                        str(arquivo), tuple(sessao["entradas"]), sessao["seed"]
                    )

                    st.markdown("**Saída:**")
                    st.code(saida if saida else "(sem saída ainda)", language="text")

                    if retorno == CODIGO_AGUARDANDO:
                        with st.form(key=f"form_{rel_arquivo}", clear_on_submit=True):
                            st.text_input(
                                "Sua resposta (Enter para enviar)",
                                key=f"resp_{rel_arquivo}",
                            )
                            st.form_submit_button(
                                "Enviar", on_click=enviar_resposta, args=(rel_arquivo,)
                            )
                    else:
                        if erro:
                            st.markdown("**Erros:**")
                            st.code(erro, language="text")
                        if retorno == 0:
                            st.success("Programa finalizado.")
                        elif retorno != -1:
                            st.warning(f"Programa terminou com erro (código {retorno}).")

                