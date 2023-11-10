# Assignment 3 - Group 6

To ensure the script runs as intended, please set up the following folder hierarchy (alternatively download the entire *A2: Analysis* folder):

    1. Create a 'Root' folder (if it doesn't exist).
    
    2. Inside the 'Root' folder, create the necessary subfolders in the following structure:
    
    Root
        model
            LLYN - STRU.ifc
        output
        main.py


## Use case:
The BIM tool created for this task is best utilized alongside the one developed in Assignment 2. Its primary objective is to enhance the provided IFC model by incorporating properties typically associated with architectural IFC models, with a specific focus on material types. Furthermore, it introduces structural parameters, such as strength class, to provide a more comprehensive dataset for further processing.  
As a result the primary use case for this joined BIM tool is cost estimation, with a specific focus on structural elements - columns, load bearing walls, beams and slabs. The main objective is to streamline the process of precise quantity takeoffs, provided that an IFC model of an appropriate development level is available. This tool aims to improve the decision making and accuracy in cost estimation for construction projects.

## Tool overview:
In its current version, the tool developed for this task operates as an independent module, focusing on the creation of a new PropertySet to incorporate and store information about material types and structural parameters of the structural elements. An overall outline of the tool's processes is depicted in the BPMN diagram below:
<img src="img/Tool_process.svg" width="1000">

After successfully executing the script and creating a new PropertySet, which is then added to the IFC model, a new file is saved to the output folder. Upon closer inspection using Blender software, we can confirm the implemented changes, as illustrated in the provided example.
<img src="img/PropertySet_new.png" width="300">

While the current tool operates independently, its primary aim was to enhance the functionality of the tool developed in the previous assignment. This improvement would make the original tool more comprehensive, enabling a more thorough and intuitive cost estimation analysis. Presently, due to time constraints, the tool assigns the new PropertySet under the generic name "Pset_MaterialStructural," which does not adhere to ISO 19650 guidelines. To address this, the next steps in the development of this tool should refine the provided script to be more flexible and adapt the PropertySet names according to the provided material type. 
<img src="img/Tool_process_modified.svg" width="1000">



