import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("400x200")
root.resizable(0,0)

def get_data():
    label = customtkinter.CTkLabel(root, text=entry.get())
    label.place(relx=0.7, rely=0.2)
    
entry = customtkinter.CTkEntry(root, width=150, height=50, border_width=2, corner_radius=2)
entry.place(relx=0.2, rely=0.2)

button = customtkinter.CTkButton(root, text="Send", command=get_data)
button.place(relx=0.2, rely=0.6)

root.mainloop()
