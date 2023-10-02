from pathlib import Path
import ifcopenshell  
import pandas as pd  

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
    
    return model

def quantityTakeOff(element):
    # Retrieve IFC elements of the specified type
    str_elements = model.by_type(str(element))
    tot_elements = len(str_elements)
    
    # Create an empty pandas DataFrame with column titles
    columns = ['Floor', 'Volume, m3', 'Area, m2', 'Material']
    df = pd.DataFrame(columns=columns)

    # Check if the IFC model contains specified structural elements
    if len(str_elements) != 0:
       # Iterate through elements of the specified type
        for str_element in str_elements:
            if str_element.IsDefinedBy:
                definitions = str_element.IsDefinedBy
    
                is_load_bearing = False  # Initialize the load-bearing flag
    
                for definition in definitions:
                    # Check if the relationship is of type 'IfcRelDefinesByProperties'
                    if definition.is_a('IfcRelDefinesByProperties'):
                        property_definition = definition.RelatingPropertyDefinition
    
                        # Check if the element is load-bearing (assuming 'LoadBearing' property)
                        if property_definition.is_a('IfcPropertySet'):
                            for property in property_definition.HasProperties:
                                if property.Name == 'LoadBearing':
                                    # Check if the property value is True
                                    if property.NominalValue.wrappedValue == True:
                                        is_load_bearing = True  # Set the flag to True and break
                                        break  # Exit the property loop once load-bearing is confirmed
    
                # If the element is load-bearing, proceed to calculate quantities
                if is_load_bearing:
                    floor_name = str_element.ContainedInStructure[0].RelatingStructure.Name
                    
                    # Create a dictionary to store data for a DataFrame entry
                    element_properties = {
                        'Floor': floor_name,
                        'Volume': None,
                        'Area': None,
                        'Material': None
                    }
    
                    for definition in definitions:
                        # Check if the relationship is of type 'IfcRelDefinesByProperties'
                        if definition.is_a('IfcRelDefinesByProperties'):
                            property_definition = definition.RelatingPropertyDefinition
    
                            if property_definition.is_a('IfcElementQuantity'):
                                for quantity in property_definition.Quantities:
                                    
                                    # Check if the quantity is of type 'IfcQuantityArea'
                                    if quantity.is_a('IfcQuantityArea'):
                                        
                                        # Slab area, m2
                                        if quantity.Name == 'NetArea':
                                            element_properties['Area, m2'] = quantity.AreaValue
                                            
                                        # Wall surface area, m2
                                        elif quantity.Name == 'NetSideArea':
                                            element_properties['Area, m2'] = quantity.AreaValue
                                            
                                        # Beam surface area, m2
                                        elif quantity.Name == 'NetSurfaceArea':
                                            element_properties['Area, m2'] = quantity.AreaValue
                                            
                                    # Check if the quantity is of type 'IfcQuantityVolume' 
                                    elif quantity.is_a('IfcQuantityVolume'):
                                        
                                        # Element volume, m3
                                        if quantity.Name == 'NetVolume':
                                            element_properties['Volume, m3'] = quantity.VolumeValue
    
                    for definition in definitions:
                        # Check if the relationship is of type 'IfcRelAssociatesMaterial'
                        if definition.is_a('IfcRelAssociatesMaterial'):
                            # This relationship associates materials with the element
                            # Iterate through related materials
                            for related_material in definition.RelatedObjects:
                                if related_material.is_a('IfcMaterial'):
                                    # Extract material name and add it to the list
                                    element_properties['Material'] = related_material.Name
    
                    # Append the data as a new row to the pandas DataFrame
                    df = pd.concat([df, pd.DataFrame([element_properties], columns=columns)], ignore_index=True)
                    
                    # Create a floorwise summary:
                    floorwise_sum = df.groupby('Floor')[['Volume, m3', 'Area, m2']].sum()
                    
                    # Calculate total quantities for the specified element type
                    total_volume = df['Volume, m3'].sum()
                    total_area = df['Area, m2'].sum()
                

    return df, tot_elements, floorwise_sum, total_volume, total_area, element

# Load the IFC model
model = loadFile()  

# Output a written report within Python's console:  

# Collect floor names from the IFC model
floorNames = []

for entity in model.by_type('IfcBuildingStorey'):
    floorNames.append(entity.Name)

print('\nThere are', len(floorNames), 'floors in the model: \n')

# Print the names of each floor
for floor in floorNames:
    print(floor)

# List of structural element types to be reported
elements = ['IfcColumn', 'IfcWall', 'IfcBeam', 'IfcSlab']

# Initialize a list for a full DataFrame storage per specified element type
element_summary = []

# Process and report each type of element
for element in elements:
    element_quantities, tot_elements, floorwise_sum, total_volume, total_area , element = quantityTakeOff(element)
    element_summary.append(element_quantities)
    print('________________________________________________________________')
    print('\nOut of', tot_elements, element, 'elements', len(element_quantities), 'are load bearing (structural).')
    print('\nFloorwise summary for', element,' elements: \n')
    print(floorwise_sum, '\n')
    print('Total material quantities for', element, 'elements:')
    print('Volume: ', round(total_volume,2), 'm3')
    print('Area: ', round(total_area,2), 'm2')
    
# To access the full DataFrame of an element:
    # element_summary[0] - Columns
    # element_summary[1] - Walls
    # element_summary[2] - Beams
    # element_summary[3] - Slabs
    
    # (to be used in further processing for price calculations)
