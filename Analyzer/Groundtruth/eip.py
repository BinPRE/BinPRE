
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

#Groundtruth: user need fill it based on protocol specifications + Wireshark

eip_Syntax_Groundtruth = {}

eip_Semantic_Functions_Groundtruth = {}

#format1
eip_Syntax_Groundtruth[b'\x65\x00'] = [-1,1,3,7,11,19,23,25]
eip_Syntax_Groundtruth[b'\x63\x00'] = [-1,1,3,7,11,13,19]
eip_Syntax_Groundtruth[b'\x6f\x00'] = [-1,1,3,7,11,19,23,27,29,31,33]
eip_Syntax_Groundtruth[b'\x04\x00'] = [-1,1,3,7,11,19]



#Groundtruth: user need fill it based on protocol specifications + Wireshark

eip_Semantic_Groundtruth = {}

eip_lengthOffset = '2,3'

eip_commandOffset = '0,1'

#format1
eip_Semantic_Groundtruth[b'\x65\x00'] = {
    '0,1':semanticTypes[1],
    '2,3':semanticTypes[3],
    '4,5,6,7':semanticTypes[0],
    '8,9,10,11':semanticTypes[0],
    '12,13,14,15,16,17,18,19':semanticTypes[4],
    '20,21,22,23':semanticTypes[0],
    '24,25':semanticTypes[1],
    '26,27': semanticTypes[0]
    }
eip_Semantic_Groundtruth[b'\x63\x00'] = {
    '0,1':semanticTypes[1],
    '2,3':semanticTypes[3],
    '4,5,6,7':semanticTypes[0],
    '8,9,10,11':semanticTypes[0],
    '12,13': semanticTypes[4],
    '14,15,16,17,18,19':semanticTypes[4],
    '20,21,22,23':semanticTypes[0]
    }
eip_Semantic_Groundtruth[b'\x6f\x00'] = {
    '0,1':semanticTypes[1],
    '2,3':semanticTypes[3],
    '4,5,6,7':semanticTypes[0],
    '8,9,10,11':semanticTypes[0],
    '12,13,14,15,16,17,18,19':semanticTypes[4],
    '20,21,22,23':semanticTypes[0],

    '24,25,26,27':semanticTypes[0],
    '28,29':semanticTypes[0],
    '30,31':semanticTypes[3],
    '32,33':semanticTypes[0],
    '34,35':semanticTypes[3],
    }
eip_Semantic_Groundtruth[b'\x04\x00'] = {
    '0,1':semanticTypes[1],
    '2,3':semanticTypes[3],
    '4,5,6,7':semanticTypes[0],
    '8,9,10,11':semanticTypes[0],
    '12,13,14,15,16,17,18,19':semanticTypes[4],
    '20,21,22,23':semanticTypes[0],

    }

eip_Semantic_Functions_Groundtruth[b'\x65\x00'] = {
    '0,1': semantic_Functions[0],
    '2,3': semantic_Functions[1],
}

eip_Semantic_Functions_Groundtruth[b'\x63\x00'] = {
    '0,1': semantic_Functions[0],
    '2,3': semantic_Functions[1],
}

eip_Semantic_Functions_Groundtruth[b'\x6f\x00'] = {
    '0,1': semantic_Functions[0],
    '2,3': semantic_Functions[1],
}

eip_Semantic_Functions_Groundtruth[b'\x04\x00'] = {
    '0,1': semantic_Functions[0],
    '2,3': semantic_Functions[1],
}
