

cd ../../Analyzer
#wait server start: 1min
sleep 60

python3 fsend_split.py dnp3 0 0 oa index big 0
#wait and enter threadId: 1
#Total Analyze Time:564.5407269001007