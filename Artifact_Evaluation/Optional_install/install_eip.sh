
#！！！Please install all the projects into ===='./BinPRE/src'==== folder



'''eip'''

cd ../../src

sudo apt-get install doxygen
sudo apt-get install libcap-dev
sudo apt-get install cmake

git clone https://github.com/EIPStackGroup/OpENer.git 
cd OpENer/bin/posix/
#modify: ~OpENer/source/CMakeLists.txt:cmakelist3.18->3.16
./setup_posix.sh
make
cd ../../../

#run server: ./OpENer/bin/posix/src/ports/POSIX/OpENer lo