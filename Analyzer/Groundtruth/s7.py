
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

#Groundtruth: user need fill it based on protocol specifications + Wireshark

s7_Syntax_Groundtruth = {}

#format1
s7_Syntax_Groundtruth[b'\x00'] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27]
s7_Syntax_Groundtruth[b'\x04'] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27]
s7_Syntax_Groundtruth[b'\x05'] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,19,20,21,22,24,26,27,30,31,32,34]
s7_Syntax_Groundtruth[b'\xf0'] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,22]
s7_Syntax_Groundtruth[b'\x1d'] = [-1,0,1,3,4,5,6,7,8,10,12,14,16,17,18,20,24,25,26,28,33]



#Groundtruth: user need fill it based on protocol specifications + Wireshark

s7_Semantic_Groundtruth = {}

s7_Semantic_Functions_Groundtruth = {}

s7_lengthOffset = '2,3'

s7_commandOffset = '17'

#format1
s7_Semantic_Groundtruth[b'\x00'] = {
    '0':semanticTypes[0],
    '1':semanticTypes[0],
    '2,3':semanticTypes[3],
    '4':semanticTypes[3],
    '5':semanticTypes[0],
    '6':semanticTypes[3],

    '7':semanticTypes[0],
    '8':semanticTypes[0],
    '9,10':semanticTypes[0],
    '11,12':semanticTypes[3],
    '13,14':semanticTypes[3],
    '15,16':semanticTypes[3],

    '17':semanticTypes[1],
    '18':semanticTypes[3],
    '19':semanticTypes[0],
    '20':semanticTypes[3],
    '21':semanticTypes[1],
    '22':semanticTypes[0],

    '23':semanticTypes[1],
    '24':semanticTypes[3],
    '25':semanticTypes[0],
    '26':semanticTypes[0],
    '27,28':semanticTypes[3],
    '29,30':semanticTypes[1],
    '31+':semanticTypes[3],
    }
s7_Semantic_Groundtruth[b'\x04'] = {
    '0':semanticTypes[0],
    '1':semanticTypes[0],
    '2,3':semanticTypes[3],
    '4':semanticTypes[3],
    '5':semanticTypes[0],
    '6':semanticTypes[3],

    '7':semanticTypes[0],
    '8':semanticTypes[0],
    '9,10':semanticTypes[0],
    '11,12':semanticTypes[3],
    '13,14':semanticTypes[3],
    '15,16':semanticTypes[3],

    '17':semanticTypes[1],
    '18':semanticTypes[3],
    '19':semanticTypes[0],
    '20':semanticTypes[3],
    '21':semanticTypes[1],
    '22':semanticTypes[3],

    
    '23,24':semanticTypes[3],
    '25,26':semanticTypes[3],
    '27':semanticTypes[0],
    '28,29,30':semanticTypes[0],
    }
s7_Semantic_Groundtruth[b'\x05'] = {
    '0':semanticTypes[0],
    '1':semanticTypes[0],
    '2,3':semanticTypes[3],
    '4':semanticTypes[3],
    '5':semanticTypes[0],
    '6':semanticTypes[3],

    '7':semanticTypes[0],
    '8':semanticTypes[0],
    '9,10':semanticTypes[0],
    '11,12':semanticTypes[3],
    '13,14':semanticTypes[3],
    '15,16':semanticTypes[3],

    '17':semanticTypes[1],
    '18':semanticTypes[3],
    '19':semanticTypes[0],
    '20':semanticTypes[3],
    '21':semanticTypes[1],
    '22':semanticTypes[3],

    
    '23,24':semanticTypes[3],
    '25,26':semanticTypes[3],
    '27':semanticTypes[0],
    '28,29,30':semanticTypes[0],
    
    '31':semanticTypes[0],
    '32':semanticTypes[0],
    '33,34':semanticTypes[3],
    '35+':semanticTypes[4],
    }
s7_Semantic_Groundtruth[b'\xf0'] = {
    '0':semanticTypes[0],
    '1':semanticTypes[0],
    '2,3':semanticTypes[3],
    '4':semanticTypes[3],
    '5':semanticTypes[0],
    '6':semanticTypes[3],

    '7':semanticTypes[0],
    '8':semanticTypes[0],
    '9,10':semanticTypes[0],
    '11,12':semanticTypes[3],
    '13,14':semanticTypes[3],
    '15,16':semanticTypes[3],

    '17':semanticTypes[1],
    '18':semanticTypes[0],
    '19,20':semanticTypes[0],
    '21,22':semanticTypes[0],
    '23,24':semanticTypes[3],
    }
s7_Semantic_Groundtruth[b'\x1d'] = {
    '0':semanticTypes[0],
    '1':semanticTypes[0],
    '2,3':semanticTypes[3],
    '4':semanticTypes[3],
    '5':semanticTypes[0],
    '6':semanticTypes[0],

    '7':semanticTypes[0],
    '8':semanticTypes[1],
    '9,10':semanticTypes[0],
    '11,12':semanticTypes[3],
    '13,14':semanticTypes[3],
    '15,16':semanticTypes[3],

    '17':semanticTypes[1],
    '18':semanticTypes[0],
    '19,20':semanticTypes[0],
    '21,22,23,24':semanticTypes[0],
    '25':semanticTypes[3],
    '26':semanticTypes[0],
    '27,28':semanticTypes[1],
    '29,30,31,32,33':semanticTypes[0],
    '34':semanticTypes[0]
    }


s7_Semantic_Functions_Groundtruth[b'\x00'] = {
    '2,3': semantic_Functions[1],
    '4': semantic_Functions[1],
    '9,10': semantic_Functions[4],
    '13,14': semantic_Functions[1],
    '15,16': semantic_Functions[1],
    '17': semantic_Functions[0],
    '27,28': semantic_Functions[1],
}

s7_Semantic_Functions_Groundtruth[b'\x04'] = {
    '2,3': semantic_Functions[1],
    '4': semantic_Functions[1],
    '9,10': semantic_Functions[4],
    '13,14': semantic_Functions[1],
    '15,16': semantic_Functions[1],
    '17': semantic_Functions[0],
    '23,24': semantic_Functions[1],
}

s7_Semantic_Functions_Groundtruth[b'\x05'] = {
    '2,3': semantic_Functions[1],
    '4': semantic_Functions[1],
    '9,10': semantic_Functions[4],
    '13,14': semantic_Functions[1],
    '15,16': semantic_Functions[1],
    '17': semantic_Functions[0],
    '23,24': semantic_Functions[1],
    '33,34': semantic_Functions[1],
}

s7_Semantic_Functions_Groundtruth[b'\xf0'] = {
    '2,3': semantic_Functions[1],
    '4': semantic_Functions[1],
    '9,10': semantic_Functions[4],
    '13,14': semantic_Functions[1],
    '15,16': semantic_Functions[1],
    '17': semantic_Functions[0],
    '18': semantic_Functions[4],
}

s7_Semantic_Functions_Groundtruth[b'\x1d'] = {
    '2,3': semantic_Functions[1],
    '4': semantic_Functions[1],
    '9,10': semantic_Functions[4],
    '13,14': semantic_Functions[1],
    '15,16': semantic_Functions[1],
    '17': semantic_Functions[0],
    '25': semantic_Functions[1],
    
}