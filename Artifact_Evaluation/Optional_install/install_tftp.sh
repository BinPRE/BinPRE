
#！！！Please install all the projects into ===='./BinPRE/src'==== folder



'''tftp'''

cd ../../src

sudo apt-get install autoconf
sudo apt-get install vim
git clone https://github.com/Distrotech/tftp-hpa.git
cd tftp-hpa
sudo ./autogen.sh 
sudo ./configure CFLAGS=-O0
sudo make
sudo make install

#modify configuration...
sudo vim /etc/default/tftpd-hpa
```
	TFTP_USERNAME="tftp"
	TFTP_DIRECTORY="/var/lib/tftpboot"
	TFTP_ADDRESS="0.0.0.0:69"
	TFTP_OPTIONS="-l -c -s"
```


sudo mkdir /var/lib/tftpboot
sudo chmod 777 /var/lib/tftpboot
sudo chmod 777 /usr/sbin/in.tftpd




#run server: sudo /usr/sbin/in.tftpd --user tftp --address 0.0.0.0:69 -L -c -s /var/lib/tftpboot