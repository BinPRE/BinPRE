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


RUN cd ~/BinPRE/ && \
    chmod 777 -R ./

