# coding: utf-8

"""
    Endgrate API

    Endgrate API Reference

    The version of the OpenAPI document: 1.0.0
    Contact: team@endgrate.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endgrate.models.configuration_callback_schema_schemas_value_schema_properties_value import ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue

class TestConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue(unittest.TestCase):
    """ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue:
        """Test ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue`
        """
        model = ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue()
        if include_optional:
            return ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue(
                format = '',
                type = '',
                title = ''
            )
        else:
            return ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue(
        )
        """

    def testConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue(self):
        """Test ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
