cd ../../src

sudo ./run run taint /usr/sbin/in.tftpd --user tftp --address 0.0.0.0:69 -L -s -c /var/lib/tftpboot
