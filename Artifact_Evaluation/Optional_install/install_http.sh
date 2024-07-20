
#！！！Please install all the projects into ===='./BinPRE/src'==== folder



'''http'''

cd ../../src

git clone https://github.com/avih/miniweb.git
cd miniweb
#modify makefile: add 'CFLAGS += -DENABLE_DTSP' after line25
make
cd ..

#run server: sudo ./miniweb/miniweb -r ./miniweb/bin/htdocs/