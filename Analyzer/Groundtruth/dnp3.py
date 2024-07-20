
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

#Groundtruth: user need fill it based on protocol specifications + Wireshark

dnp3_Syntax_Groundtruth = {}

dnp3_Semantic_Functions_Groundtruth = {}


dnp3_Syntax_Groundtruth[0] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[1] = [-1,1,2,3,5,7,9,12,14]
dnp3_Syntax_Groundtruth[2] = [-1,1,2,3,5,7,9,21,23]
dnp3_Syntax_Groundtruth[3] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[4] = [-1,1,2,3,5,7,9,15,17]


dnp3_Syntax_Groundtruth[5] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[6] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[7] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[8] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[9] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[10] = [-1,1,2,3,5,7,9,12,14]

dnp3_Syntax_Groundtruth[11] = [-1,1,2,3,5,7,9,21,23]
dnp3_Syntax_Groundtruth[12] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[13] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[14] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[15] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[16] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[17] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[18] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[19] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[20] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[21] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[22] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[23] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[24] = [-1,1,2,3,5,7,9,12,14]
dnp3_Syntax_Groundtruth[25] = [-1,1,2,3,5,7,9,21,23]
dnp3_Syntax_Groundtruth[26] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[27] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[28] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[29] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[30] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[31] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[32] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[33] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[34] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[35] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[36] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[37] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[38] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[39] = [-1,1,2,3,5,7,9,12,14]
dnp3_Syntax_Groundtruth[40] = [-1,1,2,3,5,7,9,21,23]
dnp3_Syntax_Groundtruth[41] = [-1,1,2,3,5,7,9,24,26]
dnp3_Syntax_Groundtruth[42] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[43] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[44] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[45] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[46] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[47] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[48] = [-1,1,2,3,5,7,9,15,17]
dnp3_Syntax_Groundtruth[49] = [-1,1,2,3,5,7,9,15,17]



#Groundtruth: user need fill it based on protocol specifications + Wireshark

dnp3_Semantic_Groundtruth = {}

dnp3_lengthOffset = '2'

dnp3_commandOffset = '3'

#format1

'''Types'''
dnp3_Semantic_Groundtruth[0] = {
    '0,1':semanticTypes[0],
    '2':semanticTypes[3],
    '3':semanticTypes[3],
    '4,5':semanticTypes[0],
    '6,7':semanticTypes[0],
    '8,9':semanticTypes[3],
    '10,11,12,13,14,15,16,17,18,19,20,21,22,23,24': semanticTypes[4],
    '25,26':semanticTypes[3]
    }
dnp3_Semantic_Groundtruth[1] = {
    '0,1':semanticTypes[0],
    '2':semanticTypes[3],
    '3':semanticTypes[3],
    '4,5':semanticTypes[0],
    '6,7':semanticTypes[0],
    '8,9':semanticTypes[3],
    '10,11,12':semanticTypes[4],
    '13,14':semanticTypes[3],
    }
dnp3_Semantic_Groundtruth[2] = {
    '0,1':semanticTypes[0],
    '2':semanticTypes[3],
    '3':semanticTypes[3],
    '4,5':semanticTypes[0],
    '6,7':semanticTypes[0],
    '8,9':semanticTypes[3],
    '10,11,12,13,14,15,16,17,18,19,20,21': semanticTypes[4],
    '22,23':semanticTypes[3],
    }
    
dnp3_Semantic_Groundtruth[4] = {
    '0,1':semanticTypes[0],
    '2':semanticTypes[3],
    '3':semanticTypes[3],
    '4,5':semanticTypes[0],
    '6,7':semanticTypes[0],
    '8,9':semanticTypes[3],

    '10,11,12,13,14,15': semanticTypes[4],

    '16,17':semanticTypes[3]
    }



'''Function'''
dnp3_Semantic_Functions_Groundtruth[0] = {
    '2':semantic_Functions[1], 
    '8,9':semantic_Functions[3],
    '12': semantic_Functions[0], 
    '25,26':semantic_Functions[3]
    }

dnp3_Semantic_Functions_Groundtruth[4] = {
    '2':semantic_Functions[1], 
    '8,9':semantic_Functions[3],
    '12': semantic_Functions[0], 
    '16,17':semantic_Functions[3]
    }

dnp3_Semantic_Functions_Groundtruth[1] = {
    '2':semantic_Functions[1], 
    '8,9':semantic_Functions[3],
    '12': semantic_Functions[0], 
    '13,14':semantic_Functions[3]
    }

dnp3_Semantic_Functions_Groundtruth[2] = {
    '2':semantic_Functions[1], 
    '8,9':semantic_Functions[3],
    '12': semantic_Functions[0], 
    '22,23':semantic_Functions[3]
    }

for i in [0, 3, 9, 12, 23, 26, 38, 41]:
    dnp3_Semantic_Groundtruth[i] = dnp3_Semantic_Groundtruth[0]
    dnp3_Semantic_Functions_Groundtruth[i] = dnp3_Semantic_Functions_Groundtruth[0]

for i in [1, 10, 24, 39]:
    dnp3_Semantic_Groundtruth[i] = dnp3_Semantic_Groundtruth[1]
    dnp3_Semantic_Functions_Groundtruth[i] = dnp3_Semantic_Functions_Groundtruth[1]

for i in [2, 11, 25, 40]:
    dnp3_Semantic_Groundtruth[i] = dnp3_Semantic_Groundtruth[2]
    dnp3_Semantic_Functions_Groundtruth[i] = dnp3_Semantic_Functions_Groundtruth[2]

for i in list(range(4, 9)) + list(range(13, 23)) + list(range(27, 38)) + list(range(42, 50)):
    dnp3_Semantic_Groundtruth[i] = dnp3_Semantic_Groundtruth[4]
    dnp3_Semantic_Functions_Groundtruth[i] = dnp3_Semantic_Functions_Groundtruth[4]

