
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

#Groundtruth: user need fill it based on protocol specifications + Wireshark

ftp_Syntax_Groundtruth = {}

#Groundtruth: user need fill it based on protocol specifications + Wireshark

ftp_Semantic_Groundtruth = {}

ftp_Semantic_Functions_Groundtruth = {}

# no length field
ftp_lengthOffset = '' 

ftp_commandOffset = '0,1,2,3'

'''Semantic-Type'''

ftp_Semantic_Groundtruth[0] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5,6,7,8,9,10,11,12,13':semanticTypes[2],
    '14,15':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[1] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5,6,7,8,9,10,11,12,13,14':semanticTypes[2],
    '15,16':semanticTypes[0],
    }

ftp_Semantic_Groundtruth[4] = {
    '0,1,2,3':semanticTypes[2],
    '4,5':semanticTypes[0],
    }

ftp_Semantic_Groundtruth[5] = {
    '0,1,2':semanticTypes[2],
    '3':semanticTypes[1],
    '4,5,6,7,8,9,10,11,12,13,14':semanticTypes[2],
    '15,16':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[8] = {
    '0,1,2':semanticTypes[2],
    '3':semanticTypes[1],
    '4,5,6,7,8,9':semanticTypes[2],
    '10,11':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[11] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5':semanticTypes[2],
    '6,7':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[13] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5,6,7,8,9,10,11,12,13,14,15,16,17':semanticTypes[2],
    '18,19':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[16] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5':semanticTypes[2],
    '6,7':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[18] = {
    '0,1,2':semanticTypes[2],
    '3':semanticTypes[1],
    '4':semanticTypes[2],
    '5,6':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[20] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5,6,7,8,9':semanticTypes[2],
    '10,11':semanticTypes[0],
    }
ftp_Semantic_Groundtruth[35] = {
    '0,1,2,3':semanticTypes[2],
    '4':semanticTypes[1],
    '5':semanticTypes[2],
    '6,7':semanticTypes[0],
    }

'''Semantic-Func'''

ftp_Semantic_Functions_Groundtruth[0] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '14,15':semantic_Functions[2],
    }
ftp_Semantic_Functions_Groundtruth[1] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '15,16':semantic_Functions[2],
    }
ftp_Semantic_Functions_Groundtruth[4] = {
    '0,1,2,3':semantic_Functions[0],
    '4,5':semantic_Functions[2],
    }
ftp_Semantic_Functions_Groundtruth[5] = {
    '0,1,2':semantic_Functions[0],
    '3':semantic_Functions[2],
    '15,16':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[8] = {
    '0,1,2':semantic_Functions[0],
    '3':semantic_Functions[2],
    '10,11':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[11] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '6,7':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[13] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '18,19':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[16] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '6,7':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[18] = {
    '0,1,2':semantic_Functions[0],
    '3':semantic_Functions[2],
    '5,6':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[20] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '10,11':semantic_Functions[2],
}
ftp_Semantic_Functions_Groundtruth[35] = {
    '0,1,2,3':semantic_Functions[0],
    '4':semantic_Functions[2],
    '6,7':semantic_Functions[2],
}


for i in [0, 2, 14, 23, 27, 31, 38, 39]: # USER anonymous
    ftp_Syntax_Groundtruth[i] = [-1,3,4,13,15]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[0]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[0]


for i in [1, 3, 15, 24, 28, 32, 40, 41]: # PASS <password>
    ftp_Syntax_Groundtruth[i] = [-1,3,4,14,16]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[1]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[1]
    
for i in [5]: # CWD pub/xnwang/
    ftp_Syntax_Groundtruth[i] = [-1,2,3,14,16]
    
for i in [4, 6, 9, 12, 7, 10, 22, 25, 26, 29, 30, 33, 37, 42, 43, 48, 49]: # PASV / LIST / QUIT / STAT / SYST
    ftp_Syntax_Groundtruth[i] = [-1,3,5]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[4]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[4]
    
for i in [8]: # CWD hijing
    ftp_Syntax_Groundtruth[i] = [-1,2,3,9,11]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[8]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[8]
    
for i in [11, 17, 19, 21, 34, 44, 46]: # TYPE I / TYPE A
    ftp_Syntax_Groundtruth[i] = [-1,3,4,5,7]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[11]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[11]

for i in [13]: # RETR hijing1.382.f
    ftp_Syntax_Groundtruth[i] = [-1,3,4,17,19]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[13]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[13]
    
for i in [16]: # REST 0
    ftp_Syntax_Groundtruth[i] = [-1,3,4,5,7]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[16]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[16]
    
for i in [18, 36]: # CWD /
    ftp_Syntax_Groundtruth[i] = [-1,2,3,4,6]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[18]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[18]

for i in [20]: # LIST -lRat
    ftp_Syntax_Groundtruth[i] = [-1,3,4,9,11]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[20]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[20]
    
for i in [35, 45, 47]: # RETR /
    ftp_Syntax_Groundtruth[i] = [-1,3,4,5,7]
    ftp_Semantic_Groundtruth[i] = ftp_Semantic_Groundtruth[35]
    ftp_Semantic_Functions_Groundtruth[i] = ftp_Semantic_Functions_Groundtruth[35]