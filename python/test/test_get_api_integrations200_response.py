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

from endgrate.models.get_api_integrations200_response import GetApiIntegrations200Response

class TestGetApiIntegrations200Response(unittest.TestCase):
    """GetApiIntegrations200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiIntegrations200Response:
        """Test GetApiIntegrations200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiIntegrations200Response`
        """
        model = GetApiIntegrations200Response()
        if include_optional:
            return GetApiIntegrations200Response(
                providers = [
                    endgrate.models.get_api_integrations_200_response_providers_inner.get_api_integrations_200_response_providers_inner(
                        provider = endgrate.models.get_api_integrations_200_response_providers_inner_provider.get_api_integrations_200_response_providers_inner_provider(
                            name = 'hubspot', 
                            display_name = 'HubSpot', 
                            url = 'https://www.hubspot.com/', 
                            image = 'https://endgrate.nyc3.cdn.digitaloceanspaces.com/integration/hubspot.png', 
                            auth_type = 'oauth', 
                            specific = endgrate.models.properties.properties(), 
                            endgrate_provider_type = 'CRM', ), 
                        integrations = [
                            endgrate.models.get_api_integrations_200_response_providers_inner_integrations_inner.get_api_integrations_200_response_providers_inner_integrations_inner(
                                display_name = 'Contact', 
                                endgrate_type = 'crm-contact', 
                                supports_push = True, 
                                supports_pull = True, 
                                is_custom_object = False, 
                                supports_associations = True, )
                            ], )
                    ]
            )
        else:
            return GetApiIntegrations200Response(
        )
        """

    def testGetApiIntegrations200Response(self):
        """Test GetApiIntegrations200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
