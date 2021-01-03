import sys
import socket

cal_serv=socket.socket()
host='192.168.43.44'
port=8888

print('waiting for connetion from server')
try:
  cal_serv.connect((host,port))
except socket.error as e:
  print(str(e))

while True:
  print('------------------Welcome to Python Calculator----------------\n')
  print('---This calculator only calculate log,square root,pow and exponantial---\n')
  print('----------------You need to choose from A to B----------------\n')
  print('----------------A for Logarithmic Expression------------------\n')
  print('----------------B for Square Root Operation-------------------\n')
  print('----------------C for Exponential Expression------------------\n')
  print('----------------D for Power Of Operation----------------------\n')
  print('----------------E for Exit from the system--------------------\n')
  print('----------------Maual end for the system----------------------\n')

  choice=input('\n Enter you input from (A to E):')
  cal_serv.send(choice.encode())

  if choice == 'A':
   #log expression
   print('Logarithmic Expression')
   nom=input('\n Masukkan Nombor:')
   bas=input('\n Masukkan Nombor Base:')
   cal_serv.sendall(str.encode('\n'.join([str(no), str(bas)])))
   resp=calc_serv(2048)
   print('Pengiraan'+no+ 'untuk nombor Base' +bas+ ':' +str(resp.decode()))

  elif choice == 'B':
   #Square Root Operation
   print('Square Root Operation')
   nom=input('\n Masukkan Nombor:')
   while True:
          if (nom) < 0:
             print('Your number is less than one please try again\n')
          else:
             cal_serv.send(nom.encode())
             resp=cal_serv.recv(2048)
             print('Pengiraan untuk Punca Kuasa:' +nom+ str(resp.decode()))

  elif choice == 'C':
   #Exponential Expression
   print('Exponential Expression')
   nom=input('Masukkan Nombor:')
   cal_serv.send(nom.encode())
   resp=cal_serv.recv(2048)
   print('Pengiraan untuk Exponent:' +nom+ str(resp.decode()))

  elif choice == 'D':
   #Power Of
   print('Power Of Expresion')
   nom=input('Masukkan Nombor:')
   kuasa=input('Masukkan Nombor Kuasa:')
   cal_serv.sendall(str.encode('\n'.join([str(nom), str(kuasa)])))
   resp=cal_serv(2048)
   print('Pengiraan untuk Kuasa' +kuasa+ ':' +nom+ str(resp.decode()))

  elif choice == 'E':
   #keluar System
   cal_serv.close()
   print('Terima Kasih! Bye :]')
   sys.exit()
  else:
     print('Input yang anda masukan tiada dalam pilihan, sila cuba lagi\n')
  input('\n Sila Tekan ener untuk sambungan........')

