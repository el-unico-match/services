from repository.servicesMetadata import ApiServicesTypes

async def getTypes():
    properties = []
    for member in ApiServicesTypes:
        properties.append({   
            'name': member.name, 
            'value': member.value
        });
    
    return properties