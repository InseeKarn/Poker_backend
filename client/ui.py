import tkinter as tk
from tkinter import messagebox
import socket
import threading

# ตั้งค่าการเชื่อมต่อ
HOST = '127.0.0.1'  # เปลี่ยนเป็น IP ของเซิร์ฟเวอร์เมื่อเชื่อมต่อกับเพื่อน
PORT = 12345

class PokerClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Poker Game")
        self.master.geometry("400x300")

        self.username_label = tk.Label(master, text="Enter your username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.join_button = tk.Button(master, text="Join Game", command=self.join_game)
        self.join_button.pack()

        self.messages_text = tk.Text(master)
        self.messages_text.pack()

        self.bet_label = tk.Label(master, text="Enter your bet:")
        self.bet_label.pack()

        self.bet_entry = tk.Entry(master)
        self.bet_entry.pack()

        self.bet_button = tk.Button(master, text="Place Bet", command=self.place_bet)
        self.bet_button.pack()

        self.client_socket = None
        self.receive_thread = None

    def join_game(self):
        username = self.username_entry.get()
        if username:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
            self.client_socket.send(username.encode('utf-8'))
            self.messages_text.insert(tk.END, f"You joined as {username}\n")
            self.receive_thread = threading.Thread(target=self.receive_messages)
            self.receive_thread.start()
        else:
            messagebox.showerror("Error", "Please enter a username.")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.messages_text.insert(tk.END, message + "\n")
            except:
                self.client_socket.close()
                break

    def place_bet(self):
        bet_amount = self.bet_entry.get()
        if bet_amount.isdigit():
            self.client_socket.send(f"BET {bet_amount}".encode('utf-8'))
            self.bet_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid bet.")

if __name__ == "__main__":
    root = tk.Tk()
    poker_client = PokerClient(root)
    root.mainloop()
