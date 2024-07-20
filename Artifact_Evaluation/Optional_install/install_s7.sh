
#！！！Please install all the projects into ===='./BinPRE/src'==== folder



'''snap7'''

cd ../../src

wget http://sourceforge.net/projects/snap7/files/1.2.1/snap7-full-1.2.1.tar.gz
tar -zxvf snap7-full-1.2.1.tar.gz && cd snap7-full-1.2.1
cd build/unix && make -f x86_64_linux.mk all
sudo cp ../bin/x86_64-linux/libsnap7.so /usr/lib/libsnap7.so
cd ../../examples/cpp/x86_64-linux/ && make
cd ../../../../

#run server: ./snap7-full-1.2.1/examples/cpp/x86_64-linux/server