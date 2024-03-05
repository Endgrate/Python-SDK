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

from endgrate.models.get_api_integrations200_response_providers_inner_provider import GetApiIntegrations200ResponseProvidersInnerProvider

class TestGetApiIntegrations200ResponseProvidersInnerProvider(unittest.TestCase):
    """GetApiIntegrations200ResponseProvidersInnerProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiIntegrations200ResponseProvidersInnerProvider:
        """Test GetApiIntegrations200ResponseProvidersInnerProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiIntegrations200ResponseProvidersInnerProvider`
        """
        model = GetApiIntegrations200ResponseProvidersInnerProvider()
        if include_optional:
            return GetApiIntegrations200ResponseProvidersInnerProvider(
                name = 'hubspot',
                display_name = 'HubSpot',
                url = 'https://www.hubspot.com/',
                image = 'https://endgrate.nyc3.cdn.digitaloceanspaces.com/integration/hubspot.png',
                auth_type = 'oauth',
                specific = endgrate.models.properties.properties(),
                endgrate_provider_type = 'CRM'
            )
        else:
            return GetApiIntegrations200ResponseProvidersInnerProvider(
        )
        """

    def testGetApiIntegrations200ResponseProvidersInnerProvider(self):
        """Test GetApiIntegrations200ResponseProvidersInnerProvider"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
