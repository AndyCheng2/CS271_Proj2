# Chandy-Lamport Algorithm

Network Connectivity Directed Graph: 

![graph](./photo/graph.png)

### How to run the project
1. Run auto.py
2. In user-interface input what you want

### Project structure

1.  We have 5 clients in total,  each these clients handle by a main process window

2. Main process: 

   1. Initial the Socket connections:
      + Self_port:`A: 10011, B: 10012, C:10013, D:10014, E:10015`
      + Connect_port: `{A: 1, B: 10, C: 100, D:1000, E:10000} + 20000` eg: AB_Port = 1 + 10 + 20000 = 20011
      + Input a agrv detect the user ---Auto Script
      + Depend the Graph to connect with Sockets
      + When we connected, we use socket_dict to trace socket_name, like `socket_dict["socket_A]`, it will return the socket you want to communicate
      + Bind Socket success, put in `receive_List[]` & `send_List[]`  -------> create `receive_handler()` Thread for each socket in `receiver_list[]`
      + Create a `user_input()` thread --> (while true)
   2. `receive_handler()` while true `recv()`,  if message exist ------> create new `receive_process()` thread and with lock to handle the token
   3. User interface:
      + Initial a token
      + Start a snapshot
      + start message passing perturbation: `perturb_tag`
      + Send a message to someone (used for test and debug)
   4. Local state:  local token states
   5. Channel States:  (A, B) tuple
   

   

   
