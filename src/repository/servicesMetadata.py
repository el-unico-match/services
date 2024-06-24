from enum import Enum
from datetime import datetime
from dataclasses import dataclass

class ApiServicesTypes(str, Enum):
    USER = 'user',
    PROFILE = 'profile',
    GATEWAY = 'gateway',
    SERVICE = 'service',
    MATCH = 'match',

class ApiServicesStatus(str, Enum):
    ENABLED  = 'enabled',
    DISABLED = 'disabled',
    BLOCKED  = 'blocked',

@dataclass
class ApiService():
   id: str
   type: ApiServicesTypes
   key: str
   apiKey: str
   baseUrl: str
   version: str
   created: datetime
   updated: datetime
   availability: ApiServicesStatus

