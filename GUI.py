import customtkinter
import tkinter as tk
import multiprocessing

class Client:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("XZNOM - CodeX")
        self.root.geometry("800x500")
        self.root.resizable(0, 0)

        self.old_msg = []
        
        self.entry = customtkinter.CTkEntry(self.root, width=800, height=50, border_width=2, corner_radius=2)
        self.entry.place(relx=0, rely=0.9)

        self.my_msg = tk.StringVar(value="")
        self.msg_display = customtkinter.CTkLabel(self.root, textvariable=self.my_msg)
        self.msg_display.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.6, anchor = tk.CENTER)

        self.entry.bind('<Return>', self.on_enter_pressed)

    def on_enter_pressed(self, event):
        if self.entry.get() == "":
            pass
        else:
            if len(self.old_msg) > 8:
                del self.old_msg[:7]
            self.old_msg.append(self.entry.get()+"\n\n")
            self.my_msg.set("".join(self.old_msg))
            self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    client = Client()
    client.run()
