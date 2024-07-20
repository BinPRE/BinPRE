cd ../../src

while true; do
    ./run run taint ./LightFTP/Source/Release/fftp ./LightFTP/Source/Release/fftp.conf
    server_pid=$!
    
    kill $server_pid
    echo "Server process killed. Restarting..."
done
