from enum import Enum
from datetime import datetime
from dataclasses import dataclass

class ApiServicesTypes(str, Enum):
    USERS = 'users',
    PROFILES = 'profiles',
    GATEWAY = 'gateway',
    SERVICES = 'services',
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
   baseUrl: str
   version: str
   created: datetime
   availability: ApiServicesStatus

