from enum import Enum
from primitive_data_type import PrimitiveDataType
from struct_data_type import StructDataType

class DataTypeKind(Enum):
    PRIMITIVE_DATA_TYPE = 1
    STRUCT_DATA_TYPE = 2




class Factory(object):
    def __init__(self, service):
        self.service = service
        self.data_type = service.dereferenced_type

    def get_path_due_to_namespace(self):
        return self.service.namesapce

    def create_data_type(self):
        path = self.get_path_due_to_namespace()

        if self.data_type.category == "VALUE":
            kind = DataTypeKind.PRIMITIVE_DATA_TYPE
            return PrimitiveDataType(self.data_type, kind, path)
        elif self.data_type.category == "STRUCT":
            kind = DataTypeKind.STRUCT_DATA_TYPE
            return StructDataType(self.data_type, kind, path)
        else:
            return None



