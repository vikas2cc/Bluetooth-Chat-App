import sys
import threading
from bluetooth import *
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import AES


def sendmesg():
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

def receivemesg():
  while True:
    mesg=sock.recv(1024)
    plaintext=dec_obj.decrypt(mesg)
    index=plaintext.find('~')
    plfinal=plaintext[:index]
    print('\n' + '<server>' + plfinal +'\n<You>')   


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
port = 4
sock=BluetoothSocket( RFCOMM )
print("printing sock=")
print(sock)
sock.connect((server_address, port))
print("connection successfull")
tsend1 = threading.Thread(target=sendmesg,args=())
trecieve1 = threading.Thread(target=receivemesg,args=())
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

