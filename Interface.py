import tkinter as tk
import pyautogui
import time

# Função que será chamada quando uma opção for selecionada
def executar_script(opcao, periodo):
    condicao = condicao_periodo(periodo)  # Obtem a condição com base no período
    script_done(opcao, condicao)  # Chama a função que irá executar o script genérico

    # Chama o script específico correspondente à opção selecionada
    if opcao == "Contini":
        time.sleep(1)  # Espera 2 segundos
        script1(periodo)
    elif opcao == "Alexandre Maximo":
        time.sleep(1)
        script2(periodo)
    elif opcao == "Jose Miguel":
        time.sleep(1)
        script3(periodo)
    elif opcao == "Cassio":
        time.sleep(1)
        script4(periodo)
    elif opcao == "Aler":
        time.sleep(1)
        script5(periodo)
    elif opcao == "Antonio":
        time.sleep(1)
        script6(periodo)

# Condição para escrever o periodo
def condicao_periodo(condicao):
    if condicao == "Manhã":
        return "Bom dia!"
    elif condicao == "Tarde":
        return "Boa tarde!"
    else:
        return "Bom dia!"  # Adiciona um retorno padrão caso nenhum período seja reconhecido

# Função que representa o script genérico
def script_done(opcao, condicao):
    pyautogui.click(374, 1004, duration=1)   # Abrir a resposta
    pyautogui.click(934, 392, duration=1)  # Selecionar campo para preencher a resposta
    pyautogui.write(f"{condicao}\nEstamos cientes e ja iremos verificar.\nAt.te".encode('utf-8').decode('utf-8'))  # Resposta 
    pyautogui.click(510, 726, duration=1)  # Salvar a resposta 

    pyautogui.click(1700, 444, duration=1)  # Abrir menu para selecionar status do chamado
    pyautogui.click(1700, 540, duration=1)  # Selecionar status para aguardar na fila

    pyautogui.click(1680, 933, duration=1)  #  Inserir para qual 
    pyautogui.write(opcao)                   # Preencher com o nome do técnico
    pyautogui.click(1692, 965, duration=1)  # selecionar o tecnico  
    
    pyautogui.click(1836, 1006, duration=1)   # Salvando 

# Funções que representam os diferentes scripts
def script1(periodo):
    criar_notificacao(f"Você encaminhou para o Contini de {periodo}")

def script2(periodo):
    criar_notificacao(f"Você encaminhou para o Alexandre Maximo de {periodo}")

def script3(periodo):
    criar_notificacao(f"Você encaminhou para o Jose Miguel de {periodo}")

def script4(periodo):
    criar_notificacao(f"Você encaminhou para o Cassio de {periodo}")

def script5(periodo):
    criar_notificacao(f"Você encaminhou para o Aler de {periodo}")

def script6(periodo):
    criar_notificacao(f"Você encaminhou para o Antonio de {periodo}")

# Função para criar uma janela de notificação personalizada
def criar_notificacao(mensagem):
    notificacao = tk.Toplevel()
    notificacao.title("Notificação")
    notificacao.configure(bg='black')
    notificacao.geometry("400x100")

    # Define a janela como "sempre no topo"
    notificacao.attributes("-topmost", True)

    label_notif = tk.Label(notificacao, text=mensagem, bg='black', fg='white', font=("Arial", 12))
    label_notif.pack(pady=20)

    botao_ok = tk.Button(notificacao, text="OK", command=notificacao.destroy, bg='gray', fg='white', width=10, height=2)
    botao_ok.pack(pady=10)

    # Fechar a notificação automaticamente após 2 segundos
    notificacao.after(2000, notificacao.destroy)

# Criação da janela principal
janela = tk.Tk()
janela.title("ENCAMINHAMENTO")
janela.geometry("200x205")
janela.configure(bg='black')

# Label para instrução
label = tk.Label(janela, text="Selecione uma opção:", bg='black', fg='white', font=("Arial", 12))
label.pack(pady=10)

# Criação do menu suspenso
opcoes = ["Contini", "Alexandre Maximo", "Jose Miguel", "Cassio", "Aler", "Antonio"]
opcao_selecionada = tk.StringVar(janela)
opcao_selecionada.set(opcoes[0])  # Define a opção inicial

# Personalizar o OptionMenu com fundo preto e texto branco
menu_opcoes = tk.OptionMenu(janela, opcao_selecionada, *opcoes)
menu_opcoes.config(bg='black', fg='white', activebackground='gray', activeforeground='white')
menu_opcoes["menu"].config(bg='black', fg='white')
menu_opcoes.pack(pady=10)

# Variável para armazenar a seleção do período
periodo_selecionado = tk.StringVar(janela)
periodo_selecionado.set("Manhã")  # Define a opção padrão

# Criação de Radiobuttons para escolher entre "manhã" e "tarde"
radio_manha = tk.Radiobutton(janela, text="Manhã", variable=periodo_selecionado, value="Manhã", bg='black', fg='white')
radio_tarde = tk.Radiobutton(janela, text="Tarde", variable=periodo_selecionado, value="Tarde", bg='black', fg='white')
radio_manha.pack(pady=5)
radio_tarde.pack(pady=5)

# Botão para executar o script com base na opção selecionada
botao_executar = tk.Button(janela, text="Executar", command=lambda: executar_script(opcao_selecionada.get(), periodo_selecionado.get()),
                           bg='gray', fg='white', activebackground='white', activeforeground='black')
botao_executar.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()
