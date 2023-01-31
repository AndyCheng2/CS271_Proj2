# Chandy-Lamport Algorithm

Network Connectivity Directed Graph: 

![graph](./photo/graph.png)



### Project structure

1.  We have 5 clients in total,  each these clients handle by a main process window

2. Main process: 

   1. Initial the Socket connections:
      + `A: 10011, B: 10012, C:10013, D:10014, E:10015` (Port number)
      + Input a agrv detect the user ---Auto Script
      + Depend the Graph to connect with Sockets
      + Bind Socket success, put in `receive_List[]` & `send_List[]`  -------> create `receive_handler()` Thread for each socket in `receiver_list[]`
      + Create a `user_input()` thread --> (while true)
   2. `receive_handler()` while true `recv()`,  if message exist ------> create new `receive_process()` thread and with lock to handle the token
   3. User interface:
      + Initial a token
      + Start a snapshot
      + start message passing perturbation: `perturb_tag`
   4. Local state:  local token states
   5. Channel States:  (A, B) tuple
   

   

   
