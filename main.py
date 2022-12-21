"""A função acima serve para criar uma senha aleatória para o usuário usando uma quantidade
de 8 a 10 letras, 2 a 4 símbolos e 2 a 4 números. Para isso, primeiro é criada uma lista de cada
item, depois, através do list comprehension é selecionado o númeto de itens de cada lista, através
do método choice. Reparar que esse código substitui o um for _ in pelo list_comprehension, a forma
mais longa de escrever o código seria:
for char in range(letters):
    password_list.append(random.choice(letters))
Depois, os itens selecionados são somados e a função shuffle os embaralha. Já a função join serve
para juntar elementos, separando-os por um símbolo como #, %,,, ou qualquer outro selecionada
ou por símbolo nenhum, como é o caso. Já a função passeord_entry.insert, mostra o password criado
dentro do box. Por fim, a função pyperclip.copy copia automaticamente o texto selecionado"""



from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
"""Primeiro, a função pega, através do get, a informação que é inserida através de cada box. Então é criado
como atributo um novo dicionário new_data, com o dado do website e dentro dele o e-mail e senha. Depois, o 
if determina que se nada for escrito no campo, aparece uma caixa de mensagem, do contrário, else, a função
deve tentar abrir e ler (para isso o r) um arquivo json, caso ocorra a exceção de arquivo não encontrado, ele
 deve criá-lo (por isso o w). Caso o arquivo exista, ele vai ser atualizado . Por fim, finally,
 a tela vai ser limpa. Sempre reparar na identação """

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

"""a função acima serve para dar a função ao botão Search, que vai pesquisar se o site a a respectiva
senha já existem no banco de dados. Primeiro ele considera o website digitado no box, então, ele vai tentar
abrir data.json como data_file, caso não encontre, except, aparece uma mensagem, do contrário, else, ele vai 
mostrar uma outra mensagem com o nome do site e o e-mail. Reparar que aqui ocorreu um dicionário aninhado,
por isso, [] [], o último else é necessário pois caso o arquivo data exista, mas o website não, o 
programa não vai funcionar, mas também não vai dar erro."""
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
"""O método focus serve para que o curso esteja naquela entrada quando o programa iniciar, já
o método insert determina onde no box o texto vai ser inserido e, se quiser, adiciona algum
texto inicial"""
# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
"""reparar que a função é chamada através do método command e o nome da função, sem o ()"""
window.mainloop()