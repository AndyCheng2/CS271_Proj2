import yaml
import socket
from process_enum import Process_port

receive_List = []
send_List = []

# Load the YAML file
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Access the data stored in the YAML file
IP = data['A']['IP']
PORT = data['A']['Port']
connected_edges = data['A']['Edges']['Connected_edge']
incoming_channels = data['A']['Edges']['Incoming_channel']
outcoming_channels = data['A']['Edges']['Outcoming_channel']

for node in connected_edges:
    port = Process_port[node].value
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_name = "socket_{}".format(node)
    locals()[socket_name] = socket_
    if node in incoming_channels:
        receive_List.append(socket_name)
    if node in outcoming_channels:
        send_List.append(socket_name)

# Print the loaded data
print(f'IP: {IP}')
print(f'PORT: {PORT}')
print(f'Connected Edges: {connected_edges}')
print(f'Incoming Channels: {incoming_channels}')
print(f'Outcoming Channels: {outcoming_channels}')
print(f'receive_List: {receive_List}')
print(f'send_List: {send_List}')