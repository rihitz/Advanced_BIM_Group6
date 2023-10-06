# Assignment 2 - Group 6

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

## Use case:
The primary use case for this BIM tool is cost estimation, with a specific focus on structural elements - columns, load bearing walls, beams and slabs. The main objective of this tool is to streamline the process of precise quantity takeoffs, provided that an IFC model of an appropriate development level is available. This tool aims to improve the decision making and accuracy in cost estimation for construction projects.

## Who is the use case for?  
This tool can be used by all stakeholders involved in construction projects, especially those interested in the structural aspects. Designers can quickly compare various design concepts in terms of projected expenses, facilitating quick and informed decision making. Contractors, on the other hand, can efficiently estimate material costs for any given project. Furthermore, this tool has the potential to contribute in Life Cycle Assessment analysis.

## What disciplinary (non BIM) expertise did you use to solve the use case
To develop the proposed BIM tool, a combination of general knowledge in structural elements and materials, as well as proficiency in Python programming, is required.

## What IFC concepts did you use in your script (would you use in your script)
The proposed BIM tool is specifically designed for cost estimation of structural elements, with a primary focus on extracting structural element volumes and surface areas through quantity takeoff. To achieve this, the tool relies on the ifcopenshell Python library and effectively utilizes various IFC concepts, including:

- **IfcElement**: This concept provides access to specific structural elements within the building, such as columns, walls, beams, and slabs.
- **IfcBuildingStorey**: Represents the different stories within a building and provides a quick summary of the total number of stories and their respective "names".
- **IfcRelDefinesProperties**: A relationship concept that defines how properties are associated with elements. It can be used to determine if elements are defined by certain properties of interest.
- **IfcPropertySet**: A collection of properties that can be linked to an element. In this particular case, this concept was utilized to identify load bearing elements.
- **IfcElementQuantity**: Represents quantities associated with elements and was used to extract structural element volumes and surface areas.
- **IfcRelAssociatesMaterial**: While the goal was to incorporate material type extraction into this BIM tool, certain challenges prevented its successful implementation.

## What disciplinary analysis does it require?  
Since the proposed BIM tool is designed exclusively for cost estimation purposes, the only analytical aspect needed is cost analysis.

## What building elements are you interested in?
For this project, the main interest is in common structural elements - columns, load bearing walls, beams, and slabs.

## What (use cases) need to be done before you can start your use case?
Before this BIM tool can be used, a structural IFC model of the building with a specific development level must be provided.

## What is the input data for your use case?
The primary input for this use case is a structural IFC model, along with a price list for materials and labor to perform cost estimation.

## What other use cases are waiting for your use case to complete?
Other use cases within *Build Focus* that are waiting for this case to complete could be construction site planning for improved scheduling and resource allocation as well as life cycle assessment, which could benefit from expedited quantity take off for structural construction materials.
