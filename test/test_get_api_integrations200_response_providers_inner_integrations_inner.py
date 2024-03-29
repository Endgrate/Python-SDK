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

from endgrate.models.get_api_integrations200_response_providers_inner_integrations_inner import GetApiIntegrations200ResponseProvidersInnerIntegrationsInner

class TestGetApiIntegrations200ResponseProvidersInnerIntegrationsInner(unittest.TestCase):
    """GetApiIntegrations200ResponseProvidersInnerIntegrationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiIntegrations200ResponseProvidersInnerIntegrationsInner:
        """Test GetApiIntegrations200ResponseProvidersInnerIntegrationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiIntegrations200ResponseProvidersInnerIntegrationsInner`
        """
        model = GetApiIntegrations200ResponseProvidersInnerIntegrationsInner()
        if include_optional:
            return GetApiIntegrations200ResponseProvidersInnerIntegrationsInner(
                display_name = 'Contact',
                endgrate_type = 'crm-contact',
                supports_push = True,
                supports_pull = True,
                is_custom_object = False,
                supports_associations = True
            )
        else:
            return GetApiIntegrations200ResponseProvidersInnerIntegrationsInner(
        )
        """

    def testGetApiIntegrations200ResponseProvidersInnerIntegrationsInner(self):
        """Test GetApiIntegrations200ResponseProvidersInnerIntegrationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
