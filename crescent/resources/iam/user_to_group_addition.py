from crescent.core import Resource
from .constants import ResourceRequiredProperties


class UserToGroupAddition(Resource):
    __TYPE = "AWS::IAM::UserToGroupAddition"

    def __init__(self, id: str):
        super(UserToGroupAddition, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.GroupName.__name__: 1},
            max_length={self.GroupName.__name__: 128},
            pattern={self.GroupName.__name__: r"[\w+=,.@-]+"},
            required_properties=ResourceRequiredProperties.USER_TO_GROUP_ADDITION
        )

    def GroupName(self, group_name: str):
        return self._set_property(self.GroupName.__name__, group_name)

    def Users(self, *users: str):
        return self._set_property(self.Users.__name__, list(users))
