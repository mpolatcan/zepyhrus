from crescent.core import Resource, Tag
from .constants import ResourceRequiredProperties


class DBSubnetGroup(Resource):
    __TYPE = "AWS::RDS::DBSubnetGroup"

    def __init__(self, id: str):
        super(DBSubnetGroup, self).__init__(
            id=id,
            type=self.__TYPE,
            max_length={self.DBSubnetGroupName.__name__: 255},
            required_properties=ResourceRequiredProperties.DB_SUBNET_GROUP
        )

    def DBSubnetGroupDescription(self, db_subnet_group_description: str):
        return self._set_property(self.DBSubnetGroupDescription.__name__, db_subnet_group_description)

    def DBSubnetGroupName(self, db_subnet_group_name: str):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    def SubnetIds(self, *subnet_ids: str):
        return self._set_property(self.SubnetIds.__name__, list(subnet_ids))

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
