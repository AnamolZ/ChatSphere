## CodeX-Chat

### Requirements
    tkinter library
    customtkinter library (provided)

### Usage
    Run the Server.py script on the machine that will act as the server.
    Run the Client.py script on the machine that will act as the client.
    Enter your name when prompted in the client application.
    The client window will appear. Type a message in the entry box and press Enter to send it to the server.
    Messages from other clients connected to the server will be displayed in the message display.

### Features
   User-friendly graphical user interface using tkinter.
   Messages are displayed in a scrollable label.
   The client stores a history of sent and received messages, which is limited to the last 8 messages.
   The client sends messages to the server using a separate thread, allowing the user to continue interacting with the GUI while messages are being sent.
   The client receives messages from the server using a separate thread, allowing the user to continue interacting with the GUI while messages are being received.

## Installation

Clone the repository.

```bash
git clone https://github.com/AnamolZ/CodeX.git
```

Navigate to the project directory.

```bash
cd codex
```
Install the required libraries.

```bash
pip install -r requirements.txt
```
Usage
Start the server. (Only for testing, Server will be always open after production)
```bash
python server.py
```
Start two clients, one for each player.
```bash
python client.py
```

## Class documentation
      Client
        A class representing a chat client.
         ### Attributes
            root (CTk): The main window of the client.
            entry (CTkEntry): The entry box for user input.
            display (tk.StringVar): The string variable to display messages.
            msg_display (CTkLabel): The label to display messages.
            Your_Name (str): The name of the client.
            history (list): A list of messages sent and received by the client.
            
         ### Methods
            __init__(): Initializes the Client object and its attributes.
            receive_message(client_socket): Receives messages from the server and updates the message display.
            send_input(client_socket): Sends user input to the server.
            Enter(event=None): Sends user input when the Enter key is pressed.
            update_display(): Updates the message display with the latest messages.
            run(): Runs the main event loop of the tkinter application.
