import socket
import threading
import time
import sys
import yaml
from process_enum import Process_port
from connect_port_enum import Connect_port

# both of them are socket list
receive_List = []
send_List = []

# translate the string name to socket object
socket_dict = {}

# string list
outgoing_channels = []
incoming_channels = []




# Load the YAML file
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)


def receive_handler(receive_socket, data):
    print("\nReceive the message: " + data)
    return


def receive_message(receive_socket):
    while True:
        data = receive_socket.recv(1024).decode()
        # print("new thread created, message is: " + data)
        receive_msg_thread = threading.Thread(target=receive_handler, args=(receive_socket, data))
        receive_msg_thread.start()
        # receive_thread.join()
        # print("one thread close")


def user_input():
    print("user get into user_input thread")
    while True:
        print("Hi, " + name + ", please input what do you want to do")
        print(f"1:Init a token from here-{name}")
        print("2:Start a snapshot")
        print("3.Start message passing perturbation")
        print("4.Send a message to someone")
        print("0.Exit")
        op = input("Input a number here:")
        while not op.isdigit():
            op = input("Input here:")
        op = int(op)
        if op == 1:
            print("Init a token from here")
            print("waiting for future development\n")
        elif op == 2:
            print("Start a snapshot")
            print("waiting for future development\n")
        elif op == 3:
            print("Start message passing perturbation")
            print("waiting for future development\n")
        elif op == 4:
            print("Here is your outgoing channels:")
            print(outgoing_channels)
            receiver = str(input("Please input the username that you want to send: "))
            while receiver not in outgoing_channels:
                receiver = input("Please input the correct name:  ")
            message = input("Please input the message that you want to send: ")
            receiver_socket_name = "socket_" + receiver
            socket_dict[receiver_socket_name].send(message.encode())
        elif op == 0:
            sys.exit()
        else:
            print("Bad request, re-input again!")
            input("Press enter to continue")
            continue


def connect_trans(client_port, my_name):
    my_number = Connect_port[my_name].value
    client_port -= 20000
    other_number = client_port - my_number
    for name_id, port_number in Connect_port.__members__.items():
        if port_number == other_number:
            return name_id


def connect_edge(connected_edges):
    for c_tuple in connected_edges:
        # Node's port
        c_tuple = tuple(c_tuple.strip().split(","))
        print(c_tuple)
        node = c_tuple[0]
        port = int(c_tuple[-1])
        node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_socket.bind(("localhost", port))
        aim_port = Process_port[node].value
        print(f"My aim_port is {aim_port}")
        socket_dict["socket_{}".format(node)] = node_socket
        node_socket.connect(("localhost", aim_port))
        print(f"Connect user {node} success at {port}")
        if node in incoming_channels:
            receive_List.append(node_socket)
        if node in outgoing_channels:
            send_List.append(node_socket)


def listen_add_socket(client_socket, client_address, my_name):
    print("enter listen_add_socket")
    client_port = client_address[-1]
    name = connect_trans(client_port, my_name)
    socket_dict["socket_{}".format(name)] = client_socket
    if name in incoming_channels:
        receive_List.append(client_socket)
    if name in outgoing_channels:
        send_List.append(client_socket)
    print(f"Connect user {name} success at {client_port}")


if __name__ == "__main__":
    # Init name with the process_port
    if len(sys.argv) > 1:
        name = sys.argv[1]
        process_port = Process_port[name].value
    else:
        name = str(input("Please firstly input your username:"))

    IP = data[name]['IP']
    PORT = data[name]['Port']
    connected_edges = data[name]['Edges']['Connected_edge']
    incoming_channels = data[name]['Edges']['Incoming_channel']
    outgoing_channels = data[name]['Edges']['Outgoing_channel']

    print(f"{IP} _ {PORT} _ {name}")

    self_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self_socket.bind((IP, PORT))

    if name == "B":
        self_socket.listen(4)
        print(f"Server {name} is starting, listening for incoming connections...")
        # i means connected socket number
        i = 0
        while True:
            # Accept an incoming connection
            if i >= 4:
                break
            print(f"Waiting at {i}")
            client_socket, client_address = self_socket.accept()
            print(client_address)
            # socket_List.append(client_socket)
            listen_add_socket(client_socket, client_address, name)
            i += 1
            # client_recev = threading.Thread(target=receive_client, args=(client_socket, client_address))
            # client_recev.start()
    elif name == "D":
        node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        node_socket.bind(("localhost", 21010))
        node_socket.connect(("localhost", 10012))
        receive_List.append(node_socket)
        send_List.append(node_socket)
        self_socket.listen(3)
        i = 0
        print(f"Server {name} is starting, listening for incoming connections...")
        # i means connected socket number
        while True:
            # Accept an incoming connection
            if i >= 3:
                break
            client_socket, client_address = self_socket.accept()
            # socket_List.append(client_socket)
            listen_add_socket(client_socket, client_address, name)
            i += 1
    elif name == "A" or name == "C" or name == "E":
        connect_edge(connected_edges)
    else:
        print("name error, input again!")

    # start receive thread
    for r_socket in receive_List:
        receive_thread = threading.Thread(target=receive_message, args=(r_socket,))
        receive_thread.start()
    # start user input thread
    input_thread = threading.Thread(target=user_input, args=())
    input_thread.start()
    # if you want to present the receive_List or send_List
    # print("recive_List:")
    # print(receive_List)
    # print("send_LIst:")
    # print(send_List)
    print("all connect success, now exit the main process!")
