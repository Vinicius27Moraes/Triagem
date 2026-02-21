import tkinter as tk
import pyautogui
import pyperclip
import time
from time import sleep

# Função que será chamada quando uma opção for selecionada
def executar_script(opcao, periodo):
    condicao = condicao_periodo(periodo)
    script_done(opcao, condicao)

    if opcao == "Vinicius Moraes Contini":
        script1(periodo)
    elif opcao == "Alexandre Maximo de Souza":
        script2(periodo)
    elif opcao == "Jose Miguel Silva":
        script3(periodo)
    # elif opcao == "":
    #     script4(periodo)
    elif opcao == "Aler Julion Rocha Veronezi":
        script5(periodo)
    # elif opcao == "":
    #     script6(periodo)

# Função para definir a saudação conforme o período
def condicao_periodo(condicao):
    return {
        "Manhã": "Bom dia!",
        "Tarde": "Boa tarde!"
    }.get(condicao, "Bom dia!")

# Substitui a digitação por colagem com acento
def escrever_com_acentos(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")

# Função que representa o script genérico
def script_done(opcao, condicao):
    pyautogui.click(498, 996, duration=1)   # Abrir a resposta
    pyautogui.click(722, 387, duration=1)   # Selecionar campo para preencher a resposta
    pyautogui.write(f"{condicao}\nEstamos cientes e iremos verificar.\nAt.te".encode('utf-8').decode('utf-8'))  # Resposta 
    pyautogui.click(629, 669, duration=1)   # Salvar a resposta 

    pyautogui.click(1670, 409, duration=1)  # Abrir menu para selecionar status do chamado
    pyautogui.click(1634, 502, duration=1)  # Selecionar status para aguardar na fila

    pyautogui.click(1707, 865, duration=1)  #  Inserir para qual analista
    pyperclip.copy(opcao)          # 1️⃣ Copia o conteúdo para o clipboard
    pyautogui.hotkey('ctrl', 'v')  # 2️⃣ Cola o conteúdo via hotkey Ctrl + V
    sleep(1)                       # Pequena pausa antes de pressionar ENTER
    pyautogui.hotkey("enter") 
    pyautogui.click(1831, 1002, duration=1) # Salvando 

# Funções de notificação específicas
def script1(periodo): criar_notificacao(f"Você encaminhou para o Contini de {periodo}")
def script2(periodo): criar_notificacao(f"Você encaminhou para o Alexandre de {periodo}")
def script3(periodo): criar_notificacao(f"Você encaminhou para o Jose de {periodo}")
# def script4(periodo): criar_notificacao(f"Você encaminhou para o  de {periodo}")
def script5(periodo): criar_notificacao(f"Você encaminhou para o Aler de {periodo}")
# def script6(periodo): criar_notificacao(f"Você encaminhou para o  de {periodo}")

# Janela de notificação flutuante
def criar_notificacao(mensagem):
    notificacao = tk.Toplevel()
    notificacao.title("Notificação")
    notificacao.configure(bg='white')
    notificacao.geometry("400x100")

    label_notif = tk.Label(notificacao, text=mensagem, bg='white', fg='black', font=("Arial", 12))
    label_notif.pack(pady=20)

    botao_ok = tk.Button(notificacao, text="OK", command=notificacao.destroy, bg='blue', fg='white', width=10, height=2)
    botao_ok.pack(pady=10)

    notificacao.after(2500, notificacao.destroy)

# Criação da janela principal
janela = tk.Tk()
janela.title("Painel de Encaminhamento")

largura = 320
altura = 300
tela_largura = janela.winfo_screenwidth()
tela_altura = janela.winfo_screenheight()
pos_x = int((tela_largura / 2) - (largura / 2))
pos_y = int((tela_altura / 2) - (altura / 2))
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.configure(bg='#1e1e1e')

# Título
titulo = tk.Label(janela, text="Encaminhamento Técnico", font=("Helvetica", 14, "bold"),
                  bg='#1e1e1e', fg='white')
titulo.pack(pady=15)

# Menu suspenso de opções
label_opcao = tk.Label(janela, text="Selecione o técnico:", bg='#1e1e1e', fg='white', font=("Arial", 10))
label_opcao.pack()

opcoes = [
    "Vinicius Moraes Contini",
    "Alexandre Maximo de Souza",
    "Jose Miguel Silva",
    "Aler Julion Rocha Veronezi",
]
opcao_selecionada = tk.StringVar(janela)
opcao_selecionada.set(opcoes[0])
menu_opcoes = tk.OptionMenu(janela, opcao_selecionada, *opcoes)
menu_opcoes.config(bg='#333', fg='white', width=20)
menu_opcoes.pack(pady=5)

# Período
label_periodo = tk.Label(janela, text="Selecione o período:", bg='#1e1e1e', fg='white', font=("Arial", 10))
label_periodo.pack(pady=(10, 0))

periodo_selecionado = tk.StringVar(janela)
periodo_selecionado.set("Manhã")

radio_manha = tk.Radiobutton(janela, text="Manhã", variable=periodo_selecionado, value="Manhã",
                             bg='#1e1e1e', fg='white', selectcolor='gray')
radio_tarde = tk.Radiobutton(janela, text="Tarde", variable=periodo_selecionado, value="Tarde",
                             bg='#1e1e1e', fg='white', selectcolor='gray')
radio_manha.pack()
radio_tarde.pack()

# Botão de execução
botao_executar = tk.Button(
    janela,
    text="Executar",
    command=lambda: executar_script(opcao_selecionada.get(), periodo_selecionado.get()),
    bg='green', fg='white',
    font=('Arial', 10, 'bold'),
    width=20, height=2
)
botao_executar.pack(pady=20)

# Iniciar interface
janela.mainloop()
