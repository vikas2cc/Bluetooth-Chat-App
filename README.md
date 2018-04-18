Project - Bluetooth App

Bluetooth App Implementation using RSA key exchange and AES encryption-decryption.

Project Link- https://github.com/vikas2cc/Bluetooth-App

BUILD REQUIREMENTS:

  GNU/Linux:
    - Python 2.7 or more recent version
     - Python distutils (standard in most Python distros, separate package
                         python-dev in Debian)
     - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)
  Windows XP:
    - Python 3.4 or more recent version
     - Python distutils (standard in most Python distros, separate package
                         python-dev in Debian)
     - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)

RUNNING INSTRUCTIONS:
   
  -Run the python file named "bluetooth_app.py" using python interpreter.
   # python bluetooth_app.py
  
  -Choose which entity you want to behave
   choose option to behave like
   1.As Server
   2.As Client
  
  -Performing enquiry start
        performing inquiry...
	found 1 devices
	1. singh-Lenovo-Yoga-500-14IBD - E4:02:9B:3D:7A:6A
	choose which server to connect
	1
  
  -Connection establishment start on choosen device(here choosen device is 1)
        chosen option = E4:02:9B:3D:7A:6A
	printing sock=
	<bluetooth.bluez.BluetoothSocket instance at 0x7f1aaa459950>
	connection successfull
  -RSA key exchange (generated at server side) to client and AES key exchange using 
   RSA public key encryption at client side and decryption of received key using RSA 
   private key at server side.
        waiting for rsa key...
        public key received
        sending encrypted aes key...
  
  -Start conversion using aes key encryption and decryption
        <You>this is mesg
	<You>ok then
	<server>i got it.

Contact- vikasiitianindia@gmail.com




