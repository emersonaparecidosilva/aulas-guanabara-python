# 🐍 Navegador de Exercícios - Curso de Python

Bem-vindo ao repositório de exercícios práticos! Para facilitar a navegação e a execução de cada um dos desafios de código, desenvolvemos dois gerenciadores de acesso: um **Modo Terminal** e um **Modo Interface Gráfica**.

Escolha a opção que melhor se adapta ao seu fluxo de trabalho e bons estudos! 🚀

---

## 💻 Opção 1: Menu via Terminal (`menu.py`)

Ideal para quem gosta da raiz da programação e prefere interagir diretamente via linha de comando (CLI).

### Como utilizar:
1. Abra o seu terminal (Prompt de Comando, PowerShell ou terminal da sua IDE).
2. Navegue até a pasta raiz deste projeto.
3. Execute o comando abaixo:
   ```bash
   python menu.py
   ```
4. O menu exibirá as pastas e arquivos disponíveis, cada um associado a um número.
5. **Comandos de Navegação:**
   * Digite o **número** correspondente e aperte Enter para entrar em uma pasta ou executar um script `.py`.
   * Digite `0` para voltar um nível (retornar à pasta anterior).
   * Digite `q` para encerrar e sair do menu.

---

## 🖥️ Opção 2: Interface Gráfica (`menu_gui.py`)

Uma interface visual (GUI) interativa para quem busca praticidade, contando com sistema de busca em tempo real e janelas isoladas de execução.

### Como utilizar:
1. Abra o seu terminal e certifique-se de estar na pasta do projeto.
2. Execute o comando abaixo:
   ```bash
   python menu_gui.py
   ```
   *(Dica: No Windows, você pode simplesmente dar dois cliques no arquivo `menu_gui.py` pelo explorador de arquivos).*

### Recursos Exclusivos:
* 🖱️ **Navegação por Cliques:** Dê um **clique duplo** sobre uma pasta para acessá-la ou sobre um arquivo `.py` para executá-lo.
* 🔍 **Busca Inteligente:** Digite o nome ou o número do exercício (ex: `035`) na barra de pesquisa superior. A lista será filtrada instantaneamente conforme você digita.
* 🪟 **Execução Isolada:** Ao rodar um exercício, o sistema abrirá uma **nova janela de terminal** limpa exclusivamente para aquele código, pausando no final. Sua interface principal continuará rodando livremente e sem travamentos.
* 🛡️ **Navegação Segura:** O botão "Voltar Diretório" possui uma trava que impede que você navegue acidentalmente para fora das pastas principais do projeto.

---

## 🛠️ Requisitos

* **Python 3.x** instalado em seu sistema.
* **Nenhuma biblioteca externa necessária!** A interface gráfica utiliza o `tkinter`, que já vem nativamente embutido nas instalações padrão do Python.
