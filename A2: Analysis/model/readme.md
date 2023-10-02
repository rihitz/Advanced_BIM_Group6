As instructed, the DTU Skylab IFC model has not been uploaded to this repository.  
The main.py script has been built and tested on "LLYN - STRU.ifc", which is the structural element model of the Skylab.  

**Note** - the provided IFC model does not contain any quantity properties, therefore it must be processed by BlenderBIM's "Calculate All Quantities" before loading it on the tool. 

For script to run as intended, the following folder hierarchy must be implemented:  

main folder  
├── main.py  
├── model  
│   ├── LLYN - STRU.ifc.ifc  
