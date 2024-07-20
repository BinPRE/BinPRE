#！！！Please install all the projects into ===='./BinPRE/src'==== folder


'''dnp3'''

cd ../../src

git clone --recursive https://github.com/automatak/dnp3.git
mv dnp3 automatak && cd automatak
mkdir build && cd build
cmake .. && sudo make install 
cd ../cpp/examples/outstation/
#modify:/automatak/cpp/examples/outstation/main.cpp->IPEndPoint("127.0.0.1", 4999)
cmake .
make

export LD_LIBRARY_PATH=/usr/lib/libopendnp3.so
export LD_LIBRARY_PATH=/usr/lib/libopendnp3.so:$LD_LIBRARY_PATH
sudo chmod 777 /etc/ld.so.conf
sudo echo "/usr/lib/libopendnp3.so" >> /etc/ld.so.conf
sudo  ldconfig
ldd ./outstation-demo

#run server: ./outstation-demo