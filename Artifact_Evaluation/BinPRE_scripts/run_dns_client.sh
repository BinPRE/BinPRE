cd ../../Analyzer
#wait server start: 1min
sleep 120

python3 fsend_split.py dns 0 1 oa index big 0
#wait and enter threadId: 0
#Total Analyze Time:574.6657240390778