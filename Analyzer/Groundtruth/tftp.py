
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

tftp_Syntax_Groundtruth = {}
 

#Groundtruth: user need fill it based on protocol specifications + Wireshark

tftp_Semantic_Groundtruth = {}

tftp_Semantic_Functions_Groundtruth = {}



# no length field
tftp_lengthOffset = '' 

tftp_commandOffset = '0,1'

'''Semantic-Type'''

tftp_Semantic_Groundtruth[0] = {
    '0,1':semanticTypes[1],
    '2,3,4,5,6,7,8,9,10,11':semanticTypes[2],
    '12,13,14,15,16,17':semanticTypes[0],
    }
tftp_Semantic_Groundtruth[40] = {
    '0,1':semanticTypes[1],
    '2,3,4,5,6,7,8,9,10,11,12,13':semanticTypes[2],
    '14,15,16,17,18,19':semanticTypes[0],
    '20,21,22,23,24,25':semanticTypes[2],
    '26,27':semanticTypes[3],
    '28,29,30,31,32,33,34,35':semanticTypes[2],
    '36,37,38,39,40':semanticTypes[3],
    }

'''Semantic-Func'''

tftp_Semantic_Functions_Groundtruth[0] = {
    '0,1':semantic_Functions[0],
    '2,3,4,5,6,7,8,9,10,11':semantic_Functions[5],
}

tftp_Semantic_Functions_Groundtruth[40] = {
    '0,1':semantic_Functions[0],
    '2,3,4,5,6,7,8,9,10,11,12,13':semantic_Functions[5],
}

for i in list(range(40)): 
    tftp_Syntax_Groundtruth[i] = [-1,1,11,17]
    tftp_Semantic_Groundtruth[i] = tftp_Semantic_Groundtruth[0]
    tftp_Semantic_Functions_Groundtruth[i] = tftp_Semantic_Functions_Groundtruth[0]

for i in list(range(40, 50)): 
    tftp_Syntax_Groundtruth[i] = [-1,1,13,19,25,27,35,40]
    tftp_Semantic_Groundtruth[i] = tftp_Semantic_Groundtruth[40]
    tftp_Semantic_Functions_Groundtruth[i] = tftp_Semantic_Functions_Groundtruth[40]


