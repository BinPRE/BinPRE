
cd ../../src

while true; do
    ./run run taint ./snap7-full-1.2.1/examples/cpp/x86_64-linux/server
    server_pid=$!
    
    kill $server_pid
    echo "Server process killed. Restarting..."
done

