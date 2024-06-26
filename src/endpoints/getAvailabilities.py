from repository.servicesMetadata import ApiServicesStatus

async def getAvailabilities():
    properties = []
    for member in ApiServicesStatus:
        properties.append({   
            'name': member.name, 
            'value': member.value
        });
    
    return properties