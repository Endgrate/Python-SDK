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

from endgrate.models.configuration_callback_schema_endgrate import ConfigurationCallbackSchemaEndgrate

class TestConfigurationCallbackSchemaEndgrate(unittest.TestCase):
    """ConfigurationCallbackSchemaEndgrate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationCallbackSchemaEndgrate:
        """Test ConfigurationCallbackSchemaEndgrate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationCallbackSchemaEndgrate`
        """
        model = ConfigurationCallbackSchemaEndgrate()
        if include_optional:
            return ConfigurationCallbackSchemaEndgrate(
                provider = '',
                provider_info = endgrate.models.configuration_callback_schema_endgrate_provider_info.ConfigurationCallbackSchema_endgrate_provider_info(
                    name = '', 
                    display_name = '', 
                    url = '', 
                    image = '', 
                    auth_type = 'oauth', 
                    specific = endgrate.models.specific.specific(), 
                    endgrate_provider_type = '', )
            )
        else:
            return ConfigurationCallbackSchemaEndgrate(
        )
        """

    def testConfigurationCallbackSchemaEndgrate(self):
        """Test ConfigurationCallbackSchemaEndgrate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
