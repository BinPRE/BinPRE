FROM homebrew/ubuntu20.04


# install BinPRE

RUN cd ~ && \
    git clone https://github.com/BinPRE/BinPRE && \
    cd BinPRE && \
    git checkout Artifact_Evaluation && \
    sudo chmod 777 -R ./ && \
    ./install_preliminary.sh

# install pin (./install_pin.sh)

RUN cd ~/BinPRE && \
    wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz && \
    tar -xzf pin-3.28-98749-g6643ecee5-gcc-linux.tar.gz && \
    chmod 777 -R ./ && \
    cd pin-3.28-98749-g6643ecee5-gcc-linux && \
    sudo ln -s ${PWD}/pin /usr/local/bin 


# example: modbus has been installed

# (optional) install the other  servers

#eip 
RUN cd ~/BinPRE/src && \
    sudo apt-get install -y doxygen && \
    sudo apt-get install -y libcap-dev && \
    sudo apt-get install -y cmake && \
    git clone https://github.com/EIPStackGroup/OpENer.git && \
    cd OpENer/source/ && \
    sed -i 's/VERSION 3.18/VERSION 3.16/g' CMakeLists.txt && \
    cd ../bin/posix/ && \
    ./setup_posix.sh && \
    make  && \
    cd ../../../

#dns 
RUN cd ~/BinPRE/src && \
    git clone https://github.com/infinet/dnsmasq && \
    cd dnsmasq && \
    make && \
    cd src 

# #dnp3.0 
RUN cd ~/BinPRE/src && \
    git clone --recursive https://github.com/automatak/dnp3.git && \
    mv dnp3 automatak && cd automatak && \
    mkdir build && cd build && \
    cmake .. && sudo make install && \
    cd ../cpp/examples/outstation/ && \
    sed -i 's/"0.0.0.0", 20000/"127.0.0.1", 4999/g' main.cpp && \
    cmake . && \
    make && \
    LD_LIBRARY_PATH=/usr/lib/libopendnp3.so && \
    LD_LIBRARY_PATH=/usr/lib/libopendnp3.so:$LD_LIBRARY_PATH && \
    sudo chmod 777 /etc/ld.so.conf && \
    sudo echo "/usr/lib/libopendnp3.so" >> /etc/ld.so.conf && \
    sudo ldconfig


#ftp
RUN cd ~/BinPRE/src && \
    sudo apt install -y build-essential && \
    sudo apt install -y gnutls-dev && \
    git clone https://github.com/hfiref0x/LightFTP.git && \
    cd LightFTP/Source/Release && \
    cp ~/BinPRE/Artifact_Evaluation/Optional_install/fftp.conf ./ && \
    make && \
    cp ~/BinPRE/Artifact_Evaluation/Optional_install/fftp ./


#tftp
RUN sudo apt-get install -y autoconf && \
    sudo apt-get install -y vim && \
    sudo apt-get install -y tftpd-hpa && \
    sudo cp ~/BinPRE/Artifact_Evaluation/Optional_install/in.tftpd /usr/sbin/ && \
    sudo mkdir /var/lib/tftpboot && \
    sudo chmod 777 -R /var/lib/tftpboot && \
    sudo chmod 777 -R /usr/sbin/in.tftpd && \
    sudo pip3 install -r ~/BinPRE/requirements.txt

#s7 

RUN cd ~/BinPRE/src && \
    wget http://sourceforge.net/projects/snap7/files/1.2.1/snap7-full-1.2.1.tar.gz && \
    tar -zxvf snap7-full-1.2.1.tar.gz && cd snap7-full-1.2.1 && \
    cd build/unix && make -f x86_64_linux.mk all && \
    sudo cp ~/BinPRE/Artifact_Evaluation/Optional_install/snap7-full-1.2.1/server /home/linuxbrew/BinPRE/src/snap7-full-1.2.1/examples/cpp/x86_64-linux/server && \
    sudo cp ~/BinPRE/Artifact_Evaluation/Optional_install/snap7-full-1.2.1/libsnap7.so /usr/lib/libsnap7.so && \
    sudo chmod 777 -R /usr/lib/libsnap7.so && \
    sudo chmod 777 -R ~/BinPRE/src/snap7-full-1.2.1
    


RUN sudo chmod 777 -R ~/BinPRE/



