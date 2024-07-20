
#！！！Please install all the projects into ===='./BinPRE/src'==== folder



'''ftp'''

cd ../../src

sudo apt install build-essential
sudo apt install gnutls-dev
git clone https://github.com/hfilef0x/lightftp
cd lightftp/Source/Release
make
#Please remember to put './fftp.conf' into './BinPRE/src/LightFTP/Source/Release/' folder


#run server: ./fftp