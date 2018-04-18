Project - Bluetooth App
<br/>
Bluetooth App Implementation using RSA key exchange and AES encryption-decryption.
<br/>
Project Link- https://github.com/vikas2cc/Bluetooth-App
<br/>
BUILD REQUIREMENTS:

  GNU/Linux:<br/>
   &nbsp; &nbsp; &nbsp;- Python 2.7 or more recent version<br/>
   &nbsp; &nbsp; &nbsp;  - Python distutils (standard in most Python distros, separate package<br/>
                         python-dev in Debian)<br/>
   &nbsp; &nbsp; &nbsp;  - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)<br/>
  Windows XP:<br/>
   &nbsp; &nbsp; &nbsp; - Python 3.4 or more recent version<br/>
   &nbsp; &nbsp; &nbsp;  - Python distutils (standard in most Python distros, separate package<br/>
                         python-dev in Debian)<br/>
   &nbsp; &nbsp; &nbsp;  - PyBlueZ libraries and header files (package libbluetooth-dev in Debian)<br/>

RUNNING INSTRUCTIONS:<br/>
   
  -Run the python file named "bluetooth_app.py" using python interpreter.<br/>
  &nbsp; &nbsp; &nbsp; python bluetooth_app.py<br/>
  
  -Choose which entity you want to behave<br/>
   &nbsp; &nbsp; &nbsp;choose option to behave like<br/>
  &nbsp; &nbsp; &nbsp; 1.As Server<br/>
  &nbsp; &nbsp; &nbsp; 2.As Client<br/>
  
  -Performing enquiry start<br/>
  &nbsp; &nbsp; &nbsp;      performing inquiry...<br/>
&nbsp; &nbsp; &nbsp;	found 1 devices<br/>
&nbsp; &nbsp; &nbsp;	1. singh-Lenovo-Yoga-500-14IBD - E4:02:9B:3D:7A:6A<br/>
&nbsp; &nbsp; &nbsp;	choose which server to connect<br/>
&nbsp; &nbsp; &nbsp;	1<br/>
  
  -Connection establishment start on choosen device(here choosen device is 1)<br/>
  &nbsp; &nbsp; &nbsp;      chosen option = E4:02:9B:3D:7A:6A<br/>
&nbsp; &nbsp; &nbsp;	printing sock=<br/>
&nbsp; &nbsp; &nbsp;	<bluetooth.bluez.BluetoothSocket instance at 0x7f1aaa459950><br/>
&nbsp; &nbsp; &nbsp;	connection successfull<br/>
  -RSA key exchange (generated at server side) to client and AES key exchange using<br/> 
   RSA public key encryption at client side and decryption of received key using RSA <br/>
   private key at server side.<br/>
  &nbsp; &nbsp; &nbsp;      waiting for rsa key...<br/>
  &nbsp; &nbsp; &nbsp;      public key received<br/>
  &nbsp; &nbsp; &nbsp;      sending encrypted aes key...<br/>
  
  -Start conversion using aes key encryption and decryption<br/>
  &nbsp; &nbsp; &nbsp;      &lt;You&gt;this is mesg<br/>
&nbsp; &nbsp; &nbsp;	&lt;You&gt;ok then<br/>
&nbsp; &nbsp; &nbsp;	&lt;server&gt;i got it.<br/>

Contact- vikasiitianindia@gmail.com<br/>
