# import socket
# def client_program():
#     host = '192.168.0.3'  
#     port = 5000 

#     client_socket = socket.socket()  
#     client_socket.connect((host, port))  

#     message = input(" -> ") 

#     while message.lower().strip() != 'bye':
#         client_socket.send(message.encode())  
#         data = client_socket.recv(1024).decode() 
#         print('Received from server: ' + data)  

#         message = input(" -> ")  

#     client_socket.close()  


# if __name__ == '__main__':
#     client_program()


arr = []
n = int(input('Enter Array Size: '))

for i in range(n): 
    i = int(input('Enter Elements: ')) 
    arr.append(i)

for b in range(n-1): 
    for k in range(n-1): 
       if arr[k] > arr[k+1]:
           arr[k],arr[k+1] = arr[k+1],arr[k]


for j in range(n): print('\t',arr[j])

arr.reverse()

print("Reversed Order: ",arr)











