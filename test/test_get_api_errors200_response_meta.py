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

from endgrate.models.get_api_errors200_response_meta import GetApiErrors200ResponseMeta

class TestGetApiErrors200ResponseMeta(unittest.TestCase):
    """GetApiErrors200ResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiErrors200ResponseMeta:
        """Test GetApiErrors200ResponseMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiErrors200ResponseMeta`
        """
        model = GetApiErrors200ResponseMeta()
        if include_optional:
            return GetApiErrors200ResponseMeta(
                count = 56,
                previous = endgrate.models.get_api_errors_200_response_meta_previous.get_api_errors_200_response_meta_previous(
                    offset = 56, ),
                next = endgrate.models.get_api_errors_200_response_meta_previous.get_api_errors_200_response_meta_previous(
                    offset = 56, )
            )
        else:
            return GetApiErrors200ResponseMeta(
        )
        """

    def testGetApiErrors200ResponseMeta(self):
        """Test GetApiErrors200ResponseMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()