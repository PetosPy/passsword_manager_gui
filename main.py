from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '*', '+']

	letter_list = [choice(letters) for _ in range(randint(8, 10))]
	symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
	number_list = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = letter_list + symbol_list + number_list
	shuffle(password_list)

	password = "".join(password_list)

	print(f"Your password is: {password}")
	password_input.insert(0, password)
	pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
	website = web_input.get()
	email = email_input.get()
	password = password_input.get()

	new_data = {website: { "email": email , "password": password}}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
	else:
	
		with open("data.json", "r") as data_file:
			#reading old data
			data_1 = json.load(data_file)
			#Update old data with new data
			data_1.update(new_data)

		with open("data.json", "w") as data_file:
			#write new data to data_file
			json.dump(data_1, data_file, indent=4)
			
			web_input.delete(0, END)
			password_input.delete(0, END)  

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

############ Labels ###############
website_label = Label(text="Website:", font=("courier", 10, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("courier", 10, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("courier", 10, "bold"))
password_label.grid(row=3, column=0)

create_password = Label(text= "Please Provide details", font=("courier", 10, "bold"))


############# Inputs ############b
web_input = Entry(width=35)
web_input.grid(row=1, column=1)
web_input.focus()


email_input = Entry(width=35)
email_input.grid(row=2, column=1)
email_input.insert(0, "haraebm@gmail.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1)

############# Buttons ###########
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()