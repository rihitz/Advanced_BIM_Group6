As instructed, the DTU Skylab IFC model has not been uploaded to this repository.  
The main.py script has been built and tested on "LLYN - STRU.ifc", which is the structural element model of the Skylab.  

**Note** - the provided IFC model does not contain any quantity properties, therefore it must be processed by BlenderBIM's "Calculate All Quantities" before loading it on the tool. 

To ensure the script runs as intended, please set up the following folder hierarchy (alternatively download the entire *A2: Analysis* folder):

    1. Create a 'Root' folder (if it doesn't exist).
    
    2. Inside the 'Root' folder, create the necessary subfolders in the following structure:
    
    Root
        input
            rep_template.xlsx
        model
            LLYN - STRU.ifc.ifc
        output
            report_LLYN - STRU.xlsx
        main.py
