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

from endgrate.models.get_api_errors200_response import GetApiErrors200Response

class TestGetApiErrors200Response(unittest.TestCase):
    """GetApiErrors200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiErrors200Response:
        """Test GetApiErrors200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiErrors200Response`
        """
        model = GetApiErrors200Response()
        if include_optional:
            return GetApiErrors200Response(
                success = True,
                meta = endgrate.models.get_api_errors_200_response_meta.get_api_errors_200_response_meta(
                    count = 56, 
                    previous = endgrate.models.get_api_errors_200_response_meta_previous.get_api_errors_200_response_meta_previous(
                        offset = 56, ), 
                    next = endgrate.models.get_api_errors_200_response_meta_previous.get_api_errors_200_response_meta_previous(
                        offset = 56, ), ),
                errors = [
                    endgrate.models.error_list_schema.ErrorListSchema(
                        pk = '', 
                        transfer_id = '', 
                        session_id = '', 
                        timestamp = '', 
                        error_resolve_text = '', 
                        error_type = 'internal', 
                        resolved = True, 
                        endgrate = endgrate.models.error_list_schema_endgrate.ErrorListSchema_endgrate(
                            provider_info = endgrate.models.configuration_callback_schema_endgrate_provider_info.ConfigurationCallbackSchema_endgrate_provider_info(
                                name = '', 
                                display_name = '', 
                                url = '', 
                                image = '', 
                                auth_type = 'oauth', 
                                specific = endgrate.models.specific.specific(), 
                                endgrate_provider_type = '', ), 
                            integration_info = endgrate.models.error_list_schema_endgrate_integration_info.ErrorListSchema_endgrate_integration_info(
                                name = '', 
                                display_name = '', 
                                method = 'IMPORT', 
                                endgrate_type = '', 
                                supports_associations = True, ), ), )
                    ]
            )
        else:
            return GetApiErrors200Response(
        )
        """

    def testGetApiErrors200Response(self):
        """Test GetApiErrors200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()