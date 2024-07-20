cd ../../Analyzer

#wait server start: 1min
sleep 10

python3 fsend_split.py s7 0 0 bo xx big 1

#wait and enter threadId: 2