from pathlib import Path
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.api

def loadFile():
    # Specify the name of the IFC model
    modelname = input("Enter the IFC model name (or press Enter for default 'LLYN - STRU'): ")
    
    # Set a default value if the user didn't provide input
    if not modelname:
        modelname = 'LLYN - STRU'
    
    try:
        dir_path = Path(__file__).parent
        model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        try:
            # If file not found, bpy import will produce an error, if script is run outside of Blender
            import bpy
            model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
            model = ifcopenshell.open(model_url)
        except OSError:
            print(f'ERROR: please check your model folder : {model_url} does not exist')
    
    # Load the IFC model
    model = ifcopenshell.open(model_url)
    
    return model, modelname

def createMaterialProp():
    # Initialize a property list
    prop = []

    while len(prop) < 2:
        if len(prop) == 0:
            user_input = input("\nEnter Material: ")
        else:
            user_input = input("\nEnter Strength class: ")

        prop.append(user_input)
    
    return prop

def assignProperty(ifc_file, element, propName):
    
    propValue = createMaterialProp()
    
    # Retrieve IFC elements of the specified type
    str_elements = model.by_type(str(element))
    
    # Check if the IFC model contains specified structural elements
    if len(str_elements) != 0:
       # Iterate through elements of the specified type
        for str_element in str_elements:
            pset = ifcopenshell.api.run("pset.add_pset", ifc_file, product=str_element, name=propName)
            ifcopenshell.api.run("pset.edit_pset", ifc_file, pset=pset, properties={"Material": propValue[0], "Strength class": propValue[1]})
    
    print('Material property -', propValue[0], ":", propValue[1], "has been added to all ", element, "elements.")
    

def saveFile(model, modelname):
    path = './output/' + "modified_" + modelname + '.ifc'
    model.write(path)
    print("\nSaving changes to ", path, "and exiting the menu.")
       
# Load the IFC model
model, modelname = loadFile()  

while True:
    # Display the menu
    print("\nSelect an option:")
    print("1. IfcColumn")
    print("2. IfcWall")
    print("3. IfcBeam")
    print("4. IfcSlab")
    print("5. Exit")

    # Get user input
    choice = input("\nEnter your choice: ")

    if choice == "1":
        
        element = "IfcColumn"
        print("You selected ", element)
        assignProperty(model, element, "Pset_MaterialStructural")
            
    elif choice == "2":
        
        element = "IfcWall"
        print("You selected ", element)
        assignProperty(model, element, "Pset_MaterialStructural")
        
    elif choice == "3":
        
        element = "IfcBeam"
        print("You selected ", element)
        assignProperty(model, element, "Pset_MaterialStructural")
        
    elif choice == "4":
        
        element = "IfcSlab"
        print("You selected ", element)
        assignProperty(model, element, "Pset_MaterialStructural")
        
    elif choice == "5":
         saveFile(model, modelname)
         break
    else:
        print("\nInvalid choice. Please select a valid option.")
 
    repeat = input("\nDo you want to repeat the menu? (yes/no): ")
    if repeat.lower() != "yes":
        saveFile(model, modelname)
        break
