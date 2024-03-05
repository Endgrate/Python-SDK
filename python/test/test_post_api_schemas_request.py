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

from endgrate.models.post_api_schemas_request import PostApiSchemasRequest

class TestPostApiSchemasRequest(unittest.TestCase):
    """PostApiSchemasRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostApiSchemasRequest:
        """Test PostApiSchemasRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostApiSchemasRequest`
        """
        model = PostApiSchemasRequest()
        if include_optional:
            return PostApiSchemasRequest(
                session_id = '6566e85e7cf20dca9cef0c0a',
                data = [
                    endgrate.models.post_api_schemas_request_data_inner.post_api_schemas_request_data_inner(
                        endgrate_type = 'crm-contact', 
                        associations = True, )
                    ]
            )
        else:
            return PostApiSchemasRequest(
        )
        """

    def testPostApiSchemasRequest(self):
        """Test PostApiSchemasRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
