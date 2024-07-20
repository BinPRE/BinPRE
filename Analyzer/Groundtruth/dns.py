
semanticTypes = ['Static', 'Group', 'String', 'Bit Field', 'Bytes']
semantic_Functions = ['Command', 'Length', 'Delim', 'CheckSum', 'Aligned', 'Filename']

#Groundtruth: user need fill it based on protocol specifications + Wireshark

dns_Syntax_Groundtruth = {}

dns_Semantic_Functions_Groundtruth = {}


dns_Syntax_Groundtruth[0] = [-1,1,3,5,7,9,11,12,17,18,20,21,23,25]
dns_Syntax_Groundtruth[1] = [-1,1,3,5,7,9,11,12,14,15,18,19,21,22,25,26,33,34,38,39,41,43]


dns_Syntax_Groundtruth[4] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 79, 80, 84,
    85, 87, 89]

dns_Syntax_Groundtruth[7] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 16, 17, 26, 27, 30, 31, 33, 35]

dns_Syntax_Groundtruth[22] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 14, 15, 23, 24, 26, 27, 29, 31]

dns_Syntax_Groundtruth[32] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 15, 16, 24, 25, 27, 28, 30, 32]

dns_Syntax_Groundtruth[34] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 20, 21, 23, 24, 
    26, 28, 30, 32, 34, 38, 40, 46, 58, 62, 66, 70, 74, 78]

dns_Syntax_Groundtruth[35] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 20, 21, 23, 
    24, 26, 28, 29, 31, 33, 34, 35, 37, 39]

dns_Syntax_Groundtruth[36] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 20, 21, 23, 24,
    26, 28, 30, 32, 34, 36, 40, 42, 48, 60, 64, 68, 72, 76, 80]

dns_Syntax_Groundtruth[37] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 15, 16, 24, 25, 27,
    28, 30, 32]

dns_Syntax_Groundtruth[38] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 15, 16, 19, 20, 23, 24, 26, 27, 34, 35, 39,
    40, 42, 44]

dns_Syntax_Groundtruth[41] = [-1, 1, 3, 5, 7, 9, 11, 
    12, 15, 16, 24, 25, 27,
    28, 30, 32, 33, 35, 37, 38, 39, 41, 43, 45, 47, 49, 50, 51, 54]

dns_Syntax_Groundtruth[46] = [-1, 1, 3, 5, 7, 9, 11, 13,
    14, 22, 23, 25, 26, 
    28, 30, 31, 33, 35, 36, 37, 39, 41]




#Groundtruth: user need fill it based on protocol specifications + Wireshark

dns_Semantic_Groundtruth = {}

dns_lengthOffset = ''

dns_commandOffset = '2,3'

'''Semantic-Type'''
#format1
dns_Semantic_Groundtruth[0] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],
    '13,14,15,16,17': semanticTypes[2],
    '18': semanticTypes[1],
    '19,20': semanticTypes[2],
    '21': semanticTypes[1],
    '22,23': semanticTypes[1],
    '24,25': semanticTypes[0],
    }

dns_Semantic_Groundtruth[1] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],
    '13,14':semanticTypes[4],
    '15':semanticTypes[1],
    '16,17,18':semanticTypes[4],
    '19':semanticTypes[1],
    '20,21':semanticTypes[4],
    '22':semanticTypes[1],
    '23,24,25':semanticTypes[4],
    '26':semanticTypes[1],
    '27,28,29,30,31,32,33':semanticTypes[4],
    '34':semanticTypes[1],
    '35,36,37,38':semanticTypes[4],
    '39':semanticTypes[1],
    '40,41':semanticTypes[1],
    '42,43':semanticTypes[0],
    }

dns_Semantic_Groundtruth[4] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],
    '13':semanticTypes[4],
    '14':semanticTypes[1],
    '15':semanticTypes[4],
    '16':semanticTypes[1],
    '17':semanticTypes[4],
    '18':semanticTypes[1],
    '19':semanticTypes[4],
    '20':semanticTypes[1],
    '21':semanticTypes[4],
    '22':semanticTypes[1],
    '23':semanticTypes[4],
    '24':semanticTypes[1],
    '25':semanticTypes[4],
    '26':semanticTypes[1],
    '27':semanticTypes[4],
    '28':semanticTypes[1],
    '29':semanticTypes[4],
    '30':semanticTypes[1],
    '31':semanticTypes[4],
    '32':semanticTypes[1],
    '33':semanticTypes[4],
    '34':semanticTypes[1],
    '35':semanticTypes[4],
    '36':semanticTypes[1],
    '37':semanticTypes[4],
    '38':semanticTypes[1],
    '39':semanticTypes[4],
    '40':semanticTypes[1],
    '41':semanticTypes[4],
    '42':semanticTypes[1],
    '43':semanticTypes[4],
    '44':semanticTypes[1],
    '45':semanticTypes[4],
    '46':semanticTypes[1],
    '47':semanticTypes[4],
    '48':semanticTypes[1],
    '49':semanticTypes[4],
    '50':semanticTypes[1],
    '51':semanticTypes[4],
    '52':semanticTypes[1],
    '53':semanticTypes[4],
    '54':semanticTypes[1],
    '55':semanticTypes[4],
    '56':semanticTypes[1],
    '57':semanticTypes[4],
    '58':semanticTypes[1],
    '59':semanticTypes[4],
    '60':semanticTypes[1],
    '61':semanticTypes[4],
    '62':semanticTypes[1],
    '63':semanticTypes[4],
    '64':semanticTypes[1],
    '65':semanticTypes[4],
    '66':semanticTypes[1],
    '67':semanticTypes[4],
    '68':semanticTypes[1],
    '69':semanticTypes[4],
    '70':semanticTypes[1],
    '71':semanticTypes[4],
    '72':semanticTypes[1],
    '73':semanticTypes[4],
    '74':semanticTypes[1],
    '75':semanticTypes[4],
    '76':semanticTypes[1],
    '77,78,79':semanticTypes[4],
    '80':semanticTypes[1],
    '81,82,83,84':semanticTypes[4],
    '85':semanticTypes[1],
    '86,87':semanticTypes[1],
    '88,89':semanticTypes[0],
    }

dns_Semantic_Groundtruth[7] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],
    '13,14,15,16':semanticTypes[4],
    '17':semanticTypes[1],
    '18,19,20,21,22,23,24,25,26':semanticTypes[4],
    '27':semanticTypes[1],
    '28,29,30':semanticTypes[4],
    '31':semanticTypes[1],
    '32,33':semanticTypes[1],
    '34,35':semanticTypes[0],
    }

dns_Semantic_Groundtruth[22] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14':semanticTypes[4],
    '15':semanticTypes[1],
    '16,17,18,19,20,21,22,23':semanticTypes[4],
    '25':semanticTypes[1],
    '28,29,30':semanticTypes[4],
    '31':semanticTypes[1],
    '32,33':semanticTypes[1],
    '34,35':semanticTypes[0],
    }

dns_Semantic_Groundtruth[32] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15':semanticTypes[4],
    '16':semanticTypes[1],
    '17,18,19,20,21,22,23,24':semanticTypes[4],
    '25':semanticTypes[1],
    '26,27':semanticTypes[4],
    '28':semanticTypes[1],
    '29,30':semanticTypes[1],
    '31,32':semanticTypes[0],
    }

dns_Semantic_Groundtruth[34] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15,16,17,18,19,20':semanticTypes[4],
    '21':semanticTypes[1],
    '22,23':semanticTypes[4],
    '24':semanticTypes[1],

    '25,26':semanticTypes[1],
    '27,28':semanticTypes[0],

    '29,30':semanticTypes[1],
    '31,32':semanticTypes[1],
    '33,34':semanticTypes[0],
    '35,36,37,38':semanticTypes[0],
    '39,40':semanticTypes[3],

    '41,42,43,44,45,46':semanticTypes[2],
    '47,48,49,50,51,52,53,54,55,56,57,58':semanticTypes[2],
    '59,60,61,62':semanticTypes[3],
    '63,64,65,66':semanticTypes[3],
    '67,68,69,70':semanticTypes[3],
    '71,72,73,74':semanticTypes[3],
    '75,76,77,78':semanticTypes[3],
    }

dns_Semantic_Groundtruth[35] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15,16,17,18,19,20':semanticTypes[4],
    '21':semanticTypes[1],
    '22,23':semanticTypes[4],
    '24':semanticTypes[1],
    '25,26':semanticTypes[1],
    '27,28':semanticTypes[0],
    '29':semanticTypes[0],
    '30,31':semanticTypes[1],

    '32,33':semanticTypes[3],
    '34':semanticTypes[0],
    '35':semanticTypes[0],
    '36,37':semanticTypes[0],
    '38,39':semanticTypes[3],
    }

dns_Semantic_Groundtruth[36] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15,16,17,18,19,20':semanticTypes[4],
    '21':semanticTypes[1],
    '22,23':semanticTypes[4],
    '24':semanticTypes[1],

    '25,26':semanticTypes[1],
    '27,28':semanticTypes[0],

    '29,30':semanticTypes[0],
    '31,32':semanticTypes[1],
    '33,34':semanticTypes[0],
    '35,36':semanticTypes[0],
    '37,38,39,40':semanticTypes[0],

    '41,42':semanticTypes[3],
    '43,44,45,46,47,48':semanticTypes[2],
    '49,50,51,52,53,54,55,56,57,58,59,60':semanticTypes[2],
    '61,62,63,64':semanticTypes[3],
    '65,66,67,68':semanticTypes[3],
    '69,70,71,72':semanticTypes[3],
    '73,74,75,76':semanticTypes[3],
    '77,78,79,80':semanticTypes[3],
    }

dns_Semantic_Groundtruth[37] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15':semanticTypes[4],
    '16':semanticTypes[1],
    '17,18,19,20,21,22,23,24':semanticTypes[4],
    '25':semanticTypes[1],

    '26,27':semanticTypes[4],
    '28':semanticTypes[1],
    '29,30':semanticTypes[1],
    '31,32':semanticTypes[0],
    }

dns_Semantic_Groundtruth[38] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15':semanticTypes[4],
    '16':semanticTypes[1],
    '17,18,19':semanticTypes[4],
    '20':semanticTypes[1],
    '21,22,23':semanticTypes[4],
    '24':semanticTypes[1],
    '25,26':semanticTypes[4],
    '27':semanticTypes[1],
    '28,29,30,31,32,33,34':semanticTypes[4],
    '35':semanticTypes[1],
    '36,37,38,39':semanticTypes[4],
    '40':semanticTypes[1],
    '41,42':semanticTypes[1],
    '43,44':semanticTypes[0],
    }

dns_Semantic_Groundtruth[41] = {
    '0,1':semanticTypes[4],
    '2,3':semanticTypes[1],
    '4,5':semanticTypes[3],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12':semanticTypes[1],

    '13,14,15':semanticTypes[4],
    '16':semanticTypes[1],
    '17,18,19,20,21,22,23,24':semanticTypes[4],
    '25':semanticTypes[1],

    '26,27':semanticTypes[4],
    '28':semanticTypes[1],
    '29,30':semanticTypes[1],
    '31,32':semanticTypes[0],
    '33':semanticTypes[0],
    '34,35':semanticTypes[1],
    '36,37':semanticTypes[3],

    '38':semanticTypes[0],
    '39':semanticTypes[0],
    '40,41':semanticTypes[0],
    '42,43':semanticTypes[3],
    '44,45':semanticTypes[1],
    '46,47':semanticTypes[3],
    '48,49':semanticTypes[1],
    '50':semanticTypes[0],
    '51':semanticTypes[0],
    '52,53,54':semanticTypes[0],
    }

dns_Semantic_Groundtruth[46] = {
    '0,1':semanticTypes[3],
    '2,3':semanticTypes[4],
    '4,5':semanticTypes[1],
    '6,7':semanticTypes[3],
    '8,9':semanticTypes[3],
    '10,11':semanticTypes[3],
    '12,13':semanticTypes[3],
    '14':semanticTypes[1],

    '15,16,17,18,19,20,21,22':semanticTypes[4],
    '23':semanticTypes[1],
    '24,25':semanticTypes[4],
    '26':semanticTypes[1],

    '27,28':semanticTypes[1],
    '29,30':semanticTypes[0],
    '31':semanticTypes[0],
    '32,33':semanticTypes[1],

    '34,35':semanticTypes[3],
    '36':semanticTypes[0],
    '37':semanticTypes[0],
    '38,39':semanticTypes[0],
    '40,41':semanticTypes[3],
    }


'''Semantic-Func'''

dns_Semantic_Functions_Groundtruth[0] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '18':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[1] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '15':semantic_Functions[2], 
    '19':semantic_Functions[2], 
    '22':semantic_Functions[2], 
    '26':semantic_Functions[2], 
    '34':semantic_Functions[2], 
    '39':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[2] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '18':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[4] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '19':semantic_Functions[2], 
    '28':semantic_Functions[2], 
    '31':semantic_Functions[2], 
    '43,44':semantic_Functions[4], 
    }

dns_Semantic_Functions_Groundtruth[4] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    # '18':semantic_Functions[2], 
    # '21':semantic_Functions[2], 
    }
dns_Semantic_Functions_Groundtruth[7] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '18':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    }
dns_Semantic_Functions_Groundtruth[22] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '15':semantic_Functions[2], 
    '25':semantic_Functions[2], 
    '31':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[32] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '25':semantic_Functions[2], 
    '28':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[34] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    '24':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[35] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    '24':semantic_Functions[2], 
    }
dns_Semantic_Functions_Groundtruth[36] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '21':semantic_Functions[2], 
    '24':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[37] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '16':semantic_Functions[2], 
    '25':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[38] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '16':semantic_Functions[2], 
    '20':semantic_Functions[2],
    '24':semantic_Functions[2], 
    '27':semantic_Functions[2], 
    '35':semantic_Functions[2],
    '40':semantic_Functions[2], 
    }

dns_Semantic_Functions_Groundtruth[41] = {
    '2,3':semantic_Functions[0], 
    '12':semantic_Functions[2], 
    '16':semantic_Functions[2], 
    '25':semantic_Functions[2],
    }

dns_Semantic_Functions_Groundtruth[46] = {
    '2,3':semantic_Functions[0], 
    '14':semantic_Functions[2], 
    '23':semantic_Functions[2], 
    '26':semantic_Functions[2],
    }





for i in [0, 3]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 21, 23, 25]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[0]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[0]

for i in [1, 2]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 39, 41, 43]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[1]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[1]

for i in [4, 5, 6]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 85, 87, 89]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[4]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[4]

for i in list(range(7, 22)): 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 31, 33, 35]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[7]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[7]

for i in list(range(22, 32)): 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 27, 29, 31]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[22]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[22]
    
for i in [32, 33]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 28, 30, 32]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[32]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[32]
    
for i in [34]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 24, 26, 28, 30, 32, 34, 38, 40, 46, 58, 62, 66, 70, 74, 78]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[34]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[34]
    
for i in [35, 45, 47, 48, 49]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 24, 26, 28, 29, 31, 33, 34, 35, 37, 39]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[35]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[35]
    
for i in [36]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 13, 26, 28, 30, 32, 34, 36, 40, 42, 48, 60, 64, 68, 72, 76, 80]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[36]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[36]
    
for i in [37, 39, 40, 42, 44]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 28, 30, 32]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[37]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[37]
    
for i in [38]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 40, 42, 44]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[38]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[38]
    
for i in [41, 43]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 28, 30, 32, 33, 35, 37, 38, 39, 41, 43, 45, 47, 49, 50, 51, 54]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[41]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[41]

    
for i in [46]: 
    dns_Syntax_Groundtruth[i] = [-1, 1, 3, 5, 7, 9, 11, 13, 26, 28, 30, 31, 33, 35, 36, 37, 39, 41]
    dns_Semantic_Groundtruth[i] = dns_Semantic_Groundtruth[46]
    dns_Semantic_Functions_Groundtruth[i] = dns_Semantic_Functions_Groundtruth[46]

