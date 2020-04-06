from crescent.core import Model
from .option_setting import OptionSetting
from .constants import ModelRequiredProperties


class OptionConfiguration(Model):
    def __init__(self):
        super(OptionConfiguration, self).__init__(required_properties=ModelRequiredProperties.OPTION_CONFIGURATION)

    def DBSecurityGroupMemberships(self, *db_security_group_memberships: str):
        return self._set_field(self.DBSecurityGroupMemberships.__name__, list(db_security_group_memberships))

    def OptionName(self, option_name: str):
        return self._set_field(self.OptionName.__name__, option_name)

    def OptionSettings(self, *option_settings: OptionSetting):
        return self._set_field(self.OptionSettings.__name__, list(option_settings))

    def OptionVersion(self, option_version: str):
        return self._set_field(self.OptionVersion.__name__, option_version)

    def Port(self, port: int):
        return self._set_field(self.Port.__name__, port)

    def VpcSecurityGroupMemberships(self, *vpc_security_group_memberships: str):
        return self._set_field(self.VpcSecurityGroupMemberships.__name__, list(vpc_security_group_memberships))
