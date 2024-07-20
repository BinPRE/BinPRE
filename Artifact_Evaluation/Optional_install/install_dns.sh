
#！！！Please install all the projects into ===='./BinPRE/src'==== folder


'''dns'''

cd ../../src

git clone https://github.com/infinet/dnsmasq
cd dnsmasq
make
cd src
./dnsmasq --no-daemon --log-queries --address=/example.com/1.1.1.1