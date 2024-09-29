import socket
import threading
from logics.poker_game import PokerGame

# ตั้งค่าเซิร์ฟเวอร์
HOST = '0.0.0.0'
PORT = 12345

# สร้าง socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server started and listening on {HOST}:{PORT}")

clients = []
usernames = {}

def handle_client(client_socket):
    while True:
        try:
            username = client_socket.recv(1024).decode('utf-8')
            if username:
                usernames[client_socket] = username
                clients.append(client_socket)
                broadcast(f"{username} has joined the game.".encode('utf-8'))
                break
        except:
            client_socket.close()
            break

    cards, deck = deal_cards()  # เรียกใช้ฟังก์ชันแจกไพ่จากโมดูล
    message = f"Your cards: {', '.join(cards)}"
    client_socket.send(message.encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            username = usernames[client_socket]
            del usernames[client_socket]
            broadcast(f"{username} has left the game.".encode('utf-8'))
            break

def broadcast(message, client_socket=None):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def start_server():
    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

start_server()
