from crescent.core import Model
from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration
from .constants import AllowedValues, ModelRequiredProperties


class ReplicationDestination(Model):
    def __init__(self):
        super(ReplicationDestination, self).__init__(
            allowed_values={self.StorageClass.__name__: AllowedValues.REPLICATION_DESTINATION_SC},
            required_properties=ModelRequiredProperties.REPLICATION_DESTINATION
        )

    def AccessControlTranslation(self, access_control_translation: AccessControlTranslation):
        return self._set_field(self.AccessControlTranslation.__name__, access_control_translation)

    def Account(self, account: str):
        return self._set_field(self.Account.__name__, account)

    def Bucket(self, bucket: str):
        return self._set_field(self.Bucket.__name__, bucket)

    def EncryptionConfiguration(self, encryption_conf: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, encryption_conf)

    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)
