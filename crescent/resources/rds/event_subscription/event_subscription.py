from crescent.core import Resource
from .constants import AllowedValues, Conditions, ResourceRequiredProperties


class EventSubscription(Resource):
    __TYPE = "AWS::RDS::EventSubscription"

    def __init__(self, id: str):
        super(EventSubscription, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.SourceType.__name__: AllowedValues.SOURCE_TYPE},
            conditions={self.EventCategories.__name__: Conditions.EVENT_CATEGORIES,
                        self.SourceIds.__name__: Conditions.SOURCE_IDS},
            required_properties=ResourceRequiredProperties.EVENT_SUBSCRIPTION
        )

    def Enabled(self, enabled: bool):
        return self._set_property(self.Enabled.__name__, enabled)

    def EventCategories(self, *event_categories: str):
        return self._set_property(self.EventCategories.__name__, list(event_categories))

    def SnsTopicArn(self, sns_topic_arn: str):
        return self._set_property(self.SnsTopicArn.__name__, sns_topic_arn)

    def SourceIds(self, *source_ids: str):
        return self._set_property(self.SourceIds.__name__, list(source_ids))

    def SourceType(self, source_type: str):
        return self._set_property(self.SourceType.__name__, source_type)
