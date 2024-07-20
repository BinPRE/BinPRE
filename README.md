# BinPRE
A protocol reverse engineering(PRE) tool that accurately and finely accomplished field inference for protocol messages.

## Directory Structure

```
BinPRE
   |
   |--- Analyzer:                       The source code of BinPRE
       |
       |--- fsend_split.py:                   The entry of BinPRE, which accepts the tool parameters
       |--- Separator.py:                     The main module of our Format Extraction
       |--- Speculator.py:                    The main module of our Semanic Inference
       |--- Corrector.py:                     The main module of our Semantic Refinement
       |
       |--- Baseline:                   The re-implementations of the other three ExeT-based baselines.
          |
          |--- Polyglot     The modules of Polyglot
          |--- AutoFormat   The modules of AutoFormat
          |--- Tupni        The modules of Tupni

   |--- src:                            The Taint Tracker for monitoring server execution.
   |
   |--- BinPRE_Res:                     The folder of outputs.
       |
       |--- {protocol}_{msgnum} 
          |
          |--- {protocol}_{msgnum}_eval.txt      The results of BinPRE
          |--- {protocol}_{msgnum}_bo_eval.txt   The results of the other three ExeT-based baselines. 
```


## Installation Steps.

### preliminary request
Ubuntu 20.04

python3.8

#### install **BinPRE & requirements & pin-3.28,**：

```
cd ~
git clone https://github.com/BinPRE/BinPRE
cd BinPRE
git checkout Artifact_Evaluation
./install_preliminary.sh
./install_pin.sh
cd ..
```


#### (optional) download and install the object to be tested:
```
cd BinPRE/src
# install the server to be tested
```


## How to use BinPRE & re-implementations(Baselines: Polyglot, AutoFormat, Tupni)
(An example: freemodbus: https://github.com/cwalter-at/freemodbus)

The binary file of freemodbus is stored in ```./BinPRE/src/freemodbus/tcpmodbus``` 

**Note that**, by replacing packet captures (pcaps) and protocol implementations(binary files), you can easily start analyzing other protocols!

You can quickly try BinPRE with following steps:

step 1: instrument and start the server
```
# ==== Execution Monitor
cd ./BinPRE/src
./run run taint ./freemodbus/tcpmodbus
#type 'e' to enable the protocol stack

```
step2a <u>(BinPRE)</u>: Simulate client sending messages and Reverse Engineering (BinPRE mode: 'oa')
```
# ==== Field Inference(Format & Semantic) & Evaluation

cd ./BinPRE/Analyzer
python3 fsend_split.py modbus 0 0 oa xx big 0 

<Please enter the value of threadId: 1> #For this example is '1'

```

step2b <u>(Baselines)</u>: Simulate client sending messages and Reverse Engineering (baselines mode: 'bo' )
```
# ==== Field Inference(Format & Semantic) & Evaluation

cd ./BinPRE/Analyzer
python3 fsend_split.py modbus 0 0 bo xx big 0 

<Please enter the value of threadId: 1> #For this example is '1'

```

## =====A road map for evaluation=====

(Important Tips: When an error is reported, please check the hints in the scripts.)

```
BinPRE
   |
   |--- Artifact_Evaluation:                  Enter into this folder for Artifact Evaluation
       |
       |--- BinPRE_scripts             A series of scripts used to run BinPRE.
       |--- ExeT-based_scripts         A series of scripts used to run Polyglot, AutoFormat, and Tupni.
       |--- Optional_install          (Optional) A series of scripts used to install all the server used in our experiments.
       |
   |
   |--- BinPRE_Res:                     The folder of outputs.
       |
       |--- {protocol}_{msgnum} 
          |
          |--- {protocol}_{msgnum}_eval.txt      The results of BinPRE
          |--- {protocol}_{msgnum}_bo_eval.txt   The results of the other three ExeT-based baselines. 
```
**Quick Start: Use modbus as an Example**

step1: start server
```
cd ./BinPRE/Artifact_Evaluation/BinPRE_scripts
./run_modbus_server.sh
```

step2: run BinPRE
```
cd ./BinPRE/Artifact_Evaluation/BinPRE_scripts
./run_modbus_client.sh
```

step3: check results in './BinPRE/BinPRE_Res/modbus_50'


**(Optinal)Please pay attention to the tips in the script. **

step0: install other server

```
cd ./BinPRE/Artifact_Evaluation/Optional_install
./install_<protocol>.sh
```


step1: start server
```
cd ./BinPRE/Artifact_Evaluation/BinPRE_scripts
./run_<protocol>_server.sh
```

step2: run BinPRE
```
cd ./BinPRE/Artifact_Evaluation/BinPRE_scripts
./run_<protocol>_client.sh
```

step3: check results in './BinPRE/BinPRE_Res/(protocol)_50'




