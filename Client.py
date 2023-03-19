import tkinter as tk
import multiprocessing
import threading
import socket
from customtkinter import CTk, CTkEntry, CTkLabel

HOST = '172.23.128.1'
PORT = 1379

class Client:
    """
    A class representing a chat client.

    Attributes:
    -----------
    root : CTk
        The main window of the client.
    entry : CTkEntry
        The entry box for user input.
    display : tk.StringVar
        The string variable to display messages.
    msg_display : CTkLabel
        The label to display messages.
    Your_Name : str
        The name of the client.
    history : list
        A list of messages sent and received by the client.
    """
    def __init__(self):
        """
        Initializes the Client object and its attributes.
        """
        self.root = CTk()
        self.root.title("XZNOM - CodeX")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # create the entry box for user input
        self.entry = CTkEntry(self.root, width=800, height=50, border_width=2, corner_radius=2)
        self.entry.place(relx=0, rely=0.9)

        # create the label to display messages
        self.display = tk.StringVar()
        self.msg_display = CTkLabel(self.root, textvariable=self.display)
        self.msg_display.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.6, anchor=tk.CENTER)

        # bind the Enter key to the entry box
        self.entry.bind('<Return>', self.Enter)

        # set the name of the client
        self.Your_Name = input("Your Name: ") + ": "
        
        # create a history list to store messages
        self.history = []

    def receive_message(self, client_socket):
        """
        Receives messages from the server and updates the message display.
        
        Parameters:
        -----------
        client_socket : socket.socket
            The socket object representing the client connection.
        """
        while True:
            response = client_socket.recv(1024).decode()
            if not response:
                break
            print(f"{response}")
            self.history.append(response)
            self.update_display()

    def send_input(self, client_socket):
        """
        Sends user input to the server.
        
        Parameters:
        -----------
        client_socket : socket.socket
            The socket object representing the client connection.
        """
        while True:
            msg = input()
            if msg == "":
                continue
            message = self.Your_Name + msg
            client_socket.sendall(message.encode())
            self.history.append(message)
            self.update_display()

    def Enter(self, event=None):
        """
        Sends user input when the Enter key is pressed.
        """
        # limit the history list to the last 8 messages
        if len(self.history) > 8:
            del self.history[:7]
        if self.entry.get() != "":
            self.history.append(self.Your_Name + self.entry.get())
            message = self.Your_Name + self.entry.get()
            client_socket.sendall(message.encode())
            self.update_display()
            self.entry.delete(0, tk.END)

    def update_display(self):
        """
        Updates the message display with the latest messages.
        """
        # limit the history list to the last 8 messages
        if len(self.history) > 8:
            del self.history[:7]
        self.display.set("\n".join([str(i) for i in self.history]))

    def run(self):
        """
        Runs the main event loop of the tkinter application.

        The main window of the client is displayed and the program waits for user input.
        """
        self.root.mainloop()


if __name__ == '__main__':
    # Create and freeze the client object
    multiprocessing.freeze_support()
    client = Client()

    # Create a socket object for the client
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")

        # Create two threads, one for receiving messages and one for sending messages
        receive_thread = threading.Thread(target=client.receive_message, args=(client_socket,))
        receive_thread.start()

        send_thread = threading.Thread(target=client.send_input, args=(client_socket,))
        send_thread.start()

        # Run the main event loop of the tkinter application
        client.run()

        # Wait for the threads to finish
        receive_thread.join()
        send_thread.join()

        print("Disconnected from server")