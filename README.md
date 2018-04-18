Project - Bluetooth App
<br/>
Bluetooth App Implementation using RSA key exchange and AES encryption-decryption.
<br/>
Project Link- https://github.com/vikas2cc/Bluetooth-App
<br/>
BUILD REQUIREMENTS:

  GNU/Linux:<br/>
    - Python 2.7 or more recent version<br/>
     - Python distutils (standard in most Python distros, separate package<br/>
                         python-dev in Debian)<br/>
     - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)<br/>
  Windows XP:<br/>
    - Python 3.4 or more recent version<br/>
     - Python distutils (standard in most Python distros, separate package<br/>
                         python-dev in Debian)<br/>
     - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)<br/>

RUNNING INSTRUCTIONS:<br/>
   
  -Run the python file named "bluetooth_app.py" using python interpreter.<br/>
   python bluetooth_app.py<br/>
  
  -Choose which entity you want to behave<br/>
   choose option to behave like<br/>
   1.As Server<br/>
   2.As Client<br/>
  
  -Performing enquiry start<br/>
        performing inquiry...<br/>
	found 1 devices<br/>
	1. singh-Lenovo-Yoga-500-14IBD - E4:02:9B:3D:7A:6A<br/>
	choose which server to connect<br/>
	1<br/>
  
  -Connection establishment start on choosen device(here choosen device is 1)<br/>
        chosen option = E4:02:9B:3D:7A:6A<br/>
	printing sock=<br/>
	<bluetooth.bluez.BluetoothSocket instance at 0x7f1aaa459950><br/>
	connection successfull<br/>
  -RSA key exchange (generated at server side) to client and AES key exchange using<br/> 
   RSA public key encryption at client side and decryption of received key using RSA <br/>
   private key at server side.<br/>
        waiting for rsa key...<br/>
        public key received<br/>
        sending encrypted aes key...<br/>
  
  -Start conversion using aes key encryption and decryption<br/>
        <You>this is mesg<br/>
	<You>ok then<br/>
	<server>i got it.<br/>

Contact- vikasiitianindia@gmail.com<br/>
