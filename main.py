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
	website = web_input.get().lower()
	email = email_input.get().lower()
	password = password_input.get()

	new_data = {website: { "email": email , "password": password}}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
	else:
		try:
			
			with open("json_data.json", "r") as data_file:
				#Reading old data
					contents = json.load(data_file)
		
		except FileNotFoundError:
			with open("json_data.json", "w") as data_file:
				json.dump(new_data, data_file, indent=4)
				
		else:
			#Updating old data with new data
			 contents.update(new_data)

			 with open("json_data.json", "w") as data_file:
			 	#Saving updated data to data_file
			 	json.dump(contents, data_file, indent=4)
		finally:
			web_input.delete(0, END)
			password_input.delete(0, END)

# ---------------------------- fIND PASSWORD ------------------------------- #

def find_password():

	website_name = web_input.get().lower() 
	try:
		with open("json_data.json", "r") as data_file:
			contents = json.load(data_file)
		
	except FileNotFoundError:
		messagebox.showinfo(title="Error", message="No Data File Found")

	else:
		if website_name in contents:
			email = contents[website_name]["email"]
			password = contents[website_name]["password"]
			messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
		else:
			messagebox.showinfo(title="Error", message=f"No details for {website_name} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


############ Labels ###############
website_label = Label(text="Website:", font=("courier", 12, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("courier", 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("courier", 12, "bold"))
password_label.grid(row=3, column=0)


############# Inputs ############b
web_input = Entry(width=35)
web_input.grid(row=1, column=1)
web_input.focus()

email_input = Entry(width=54)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "haraebm@gmail.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1)


############# Buttons ###########
generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)




window.mainloop()