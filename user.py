import socket
import threading
import time
import sys
import yaml
from process_enum import Process_port


receive_List = []
send_List = []
socket_dict = {}


# Load the YAML file
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)


if __name__ == "__main__":
    # Init name with the process_port
    if len(sys.argv) > 1:
        name = sys.argv[1]
        process_port = Process_port[name].value
    else:
        name = str(input("Please firstly input your username:")).lower()

    IP = data[name]['IP']
    PORT = data[name]['Port']
    connected_edges = data[name]['Edges']['Connected_edge']
    incoming_channels = data[name]['Edges']['Incoming_channel']
    outcoming_channels = data[name]['Edges']['Outcoming_channel']

    self_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self_socket.bind((IP, PORT))

    for node in connected_edges:
        # Node's port
        port = Process_port[node].value
        node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_dict["socket_{}".format(node)] = node_socket
        node_socket.connect(("localhost", port))
        if node in incoming_channels:
            receive_List.append(node_socket)
        if node in outcoming_channels:
            send_List.append(node_socket)
