import socket
import sys
import errno
import math
from multiprocessing import Process

def server_start(cal_client):
 # cal_client(str.encode('Welcome to the server :] \n'))
  while True:
     choice =cal_client.recv(2048).decode()

     if choice == 'A':
       #log calculation
       no, bas = [float(i) for i in cal_client.recv(2048).decode('utf-8').split('\n')]
       kira= math.log(float(no), float(bas))

     elif choice == 'B':
       #Square root calculation
       no= cal_client.recv(2048).decode()
       kira= math.sqrt(float(no))

     elif choice == 'C':
       #Exponent calcualtion
       no=cal_client.recv(2048).decode()
       kira= math.exp(float(no))

     elif choice == 'D':
       #Powerof calculation
       no, pwr=[float(i) for i in cal_client.recv(2048).decode('utf-8').split('\n')]
       kira= math.pow(no,pwr)

     elif choice == 'E':
       #System End
       cal_client.close()
       break

     cal_client.sendall(str(kira).encode())

if __name__=='__main__':

   client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host=''
   port=8888

   try:
     client.bind((host,port))
   except socket.error as e:
     print(str(e))
     sys.exit()

   client.listen(5)
   while True:
     try:
         cal_client,cal_addr=client.accept()
         print('Berjaya buat connection')
         p_client=Process(target=server_start, args=(cal_client,))
         p_client.start()
     except socket.error:
         print('ada error pulak!!')

client.close()


