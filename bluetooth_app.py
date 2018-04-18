
import sys
import threading
from bluetooth import *
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import AES

#server functions
def sendmesgs():
  while True:
    mesg = raw_input('<You>')
    
    if(mesg=="close"):
      client_sock.close()
      server_sock.close()
    mesg_len = len(mesg)
    qt=mesg_len%16
    if(qt==0):
      ciphertext=enc_obj.encrypt(mesg)
      client_sock.send(ciphertext)
    else:
      lenreq=16-qt
      st='~'
      st=st*lenreq
      mesg=mesg+st
      ciphertext=enc_obj.encrypt(mesg)
      client_sock.send(ciphertext)
    

def receivemesgs():
  while True:
    mesg=client_sock.recv(1024)
    print('mes_length',len(mesg))
    plaintext=dec_obj.decrypt(mesg)
    index=plaintext.find('~')
    plfinal=plaintext[:index]
    print('\n' + '<client>' + plfinal+'\n<You>')
    #print('<You>',end='')  

 #client functions

def sendmesgc():
  while True:
    mesg = raw_input('<You>')

    if(mesg=="close"):
      sock.close()
    mesg_len=len(mesg)
    qt=mesg_len%16
    if(qt==0):
      ciphertext=enc_obj.encrypt(mesg)
      sock.send(ciphertext)
    else:
      lenreq=16-qt
      st='~'
      st=st*lenreq
      mesg=mesg+st
      #print("mesg_len=",len(mesg))
      ciphertext=enc_obj.encrypt(mesg)
      sock.send(ciphertext)

def receivemesgc():
  while True:
    mesg=sock.recv(1024)
    plaintext=dec_obj.decrypt(mesg)
    index=plaintext.find('~')
    plfinal=plaintext[:index]
    print('\n' + '<server>' + plfinal +'\n<You>')   

print("choose option to behave like\n1.As Server\n2.As Client")
option = input()
if(option==1):
  #server code
  server_sock=BluetoothSocket( RFCOMM )
  print(server_sock)
  PORT_ANY = 5
  server_sock.bind(("",PORT_ANY))
  server_sock.listen(1)
  #UUID = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"

  #advertise_service( server_sock,"Bluetooth_service",service_classes = [SERIAL_PORT_CLASS],profiles = [SERIAL_PORT_PROFILE])

  print("waiting..")
  client_sock, client_info = server_sock.accept()
  print("Accepted connection from ",client_info)

  #rsa generation
  random_generator = Random.new().read
  key = RSA.generate(1024, random_generator) #generate pub and priv key
  publickey = key.publickey() # pub key export for exchange

  public_key_string = publickey.exportKey()
  print("sending rsa publickey")
  client_sock.send(public_key_string)
  print("waiting for aes key..")
  aes_key_client=client_sock.recv(1024)
  #print("aeskey received = "+aes_key_client)

  decrypted = key.decrypt(ast.literal_eval(aes_key_client))
  print 'decrypted', decrypted

  dec_obj= AES.new(decrypted,AES.MODE_CBC,'This is an IV456')

  enc_obj= AES.new(decrypted,AES.MODE_CBC,'This is an IV456')

  #chat start
  tsend = threading.Thread(target=sendmesgs,args=())
  treceive = threading.Thread(target=receivemesgs,args=())

  tsend.start()
  treceive.start()

  tsend.join()
  treceive.join()
  print('connection closed')
elif(option==2):
  #client code
  
  print "performing inquiry..."

  nearby_devices = discover_devices(lookup_names = True)

  print "found %d devices" % len(nearby_devices)

  i=1;

  for name, addr in nearby_devices:
       print "%s. %s - %s" % (i,addr, name)
       i=i+1

  print "choose which server to connect"

  chosen_option = input();
  server_address = nearby_devices[chosen_option-1][0]

  print("chosen option = "+server_address)
  PORT_ANY = 5
  sock=BluetoothSocket( RFCOMM )
  print("printing sock=")
  print(sock)
  sock.connect((server_address, PORT_ANY))
  print("connection successfull")
  tsend1 = threading.Thread(target=sendmesgc,args=())
  trecieve1 = threading.Thread(target=receivemesgc,args=())
  #rsa key receiving
  print("waiting for rsa key...")
  public_key_string = sock.recv(1024)

  public_key = RSA.importKey(public_key_string)
  print("public key received")
  #aes generation
  aes_key = 'This is a key123'
  encrypted = public_key.encrypt(aes_key, 16)
  print("sending encrypted aes key...")
  sock.send(str(encrypted))

  dec_obj= AES.new(aes_key,AES.MODE_CBC,'This is an IV456')

  enc_obj= AES.new(aes_key,AES.MODE_CBC,'This is an IV456')


	#chat start
  tsend1.start()
  trecieve1.start()

tsend1.join()
  trecieve1.join() 
else:
print("wrong option opted..")
