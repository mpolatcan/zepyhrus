from .model import Model
from .resource import Resource
from .parameter import Parameter
from .mapping import Mapping
import json
import yaml


class TemplateErrorException(Exception):
    pass

# ------------------------------------------


class Template(Model):
    def __init__(self, version: str):
        super(Template, self).__init__()
        self._set_field("AWSTemplateFormatVersion", version)

    def Description(self, description: str):
        return self._set_field(self.Description.__name__, description)

    def Parameters(self, *parameters: Parameter):
        return self._set_field(self.Parameters.__name__, list(parameters))

    def Mappings(self, *mappings: Mapping):
        return self._set_field(self.Mappings.__name__, list(mappings))

    def Resources(self, *resources: Resource):
        return self._set_field(self.Resources.__name__, list(resources))

    def Json(self, filename: str):
        converted_template = self.__to_dict__()

        if converted_template:
            json.dump(converted_template, open("{}.json".format(filename), "w"))

    def Yaml(self, filename: str):
        converted_template = self.__to_dict__()

        if converted_template:
            yaml.dump(json.loads(json.dumps(converted_template)), open("{}.yml".format(filename), "w"), sort_keys=False)

    def __rearrange_multiple_valued_field(self, field):
        fields_dict = {}

        if self.__get_field__(field):
            for field_dict in self.__get_field__(field):
                fields_dict.update(field_dict)

            self._set_field(field, fields_dict)

    def __to_dict__(self):
        conversion_success, conversion_result = super().__to_dict__()

        if conversion_success:
            self.__rearrange_multiple_valued_field(self.Resources.__name__)
            self.__rearrange_multiple_valued_field(self.Mappings.__name__)
            self.__rearrange_multiple_valued_field(self.Parameters.__name__)

            return conversion_result
        else:
            raise TemplateErrorException("Template has errors: \n\t- {errors}".format(
                errors="\n\t- ".join(conversion_result)
            ))
