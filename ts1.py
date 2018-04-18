from bluetooth import *
import sys
import threading
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import AES 
def sendmesg():
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
    

def receivemesg():
  while True:
    mesg=client_sock.recv(1024)
    print('mes_length',len(mesg))
    plaintext=dec_obj.decrypt(mesg)
    index=plaintext.find('~')
    plfinal=plaintext[:index]
    print('\n' + '<client>' + plfinal+'\n<You>')
    #print('<You>',end='')   

server_sock=BluetoothSocket( RFCOMM )
print (server_sock)
PORT_ANY = 4
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
tsend = threading.Thread(target=sendmesg,args=())
treceive = threading.Thread(target=receivemesg,args=())

tsend.start()
treceive.start()

tsend.join()
treceive.join()
print('connection closed')
