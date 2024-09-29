import tkinter as tk
from tkinter import messagebox
import socket
import threading

# ฟังก์ชันเพื่อรับข้อความจากเซิร์ฟเวอร์
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                messages_text.insert(tk.END, message + '\n')
                messages_text.see(tk.END)
        except:
            break

# ฟังก์ชันเพื่อส่งข้อความ
def send_message():
    message = message_entry.get()
    client_socket.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Poker Game")
root.geometry("400x500")
root.configure(bg="#2C3E50")

# ข้อความสำหรับการแสดงผล
messages_text = tk.Text(root, bg="#34495E", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
messages_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# กล่องข้อความสำหรับการป้อนข้อความ
message_entry = tk.Entry(root, bg="#BDC3C7", fg="black", font=("Helvetica", 12))
message_entry.pack(padx=10, pady=10, fill=tk.X)

# ปุ่มส่งข้อความ
send_button = tk.Button(root, text="ส่ง", bg="#2980B9", fg="white", font=("Helvetica", 12), command=send_message)
send_button.pack(padx=10, pady=10)

# เชื่อมต่อกับเซิร์ฟเวอร์
HOST = '127.0.0.1'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# เริ่มเธรดเพื่อรับข้อความ
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# เริ่มโปรแกรม
root.mainloop()
