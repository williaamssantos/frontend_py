# FrontEnd
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="AutoEscola Yahoo")
texto.pack(padx=10, pady=10)

matricula = customtkinter.CTkEntry(janela, placeholder_text="Sua Matricula")
matricula.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua Senha", show="*")
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
