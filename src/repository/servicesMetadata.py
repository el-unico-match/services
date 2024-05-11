from enum import Enum
from datetime import datetime
from typing import Union
from bson import ObjectId
from dataclasses import dataclass

class ApiServicesTypes(str, Enum):
    USERS = 'users',
    PROFILES = 'profiles',
    GATEWAY = 'gateway',
    SERVICES = 'services',
    MATCH = 'match',

class ApiServicesStatus(str, Enum):
    ENABLED = 'enabled',
    BLOCKED = 'blocked',

@dataclass
class ApiService():
   id: str
   type: ApiServicesTypes
   key: str
   baseUrl: str
   version: str
   created: datetime
   availability: ApiServicesStatus

