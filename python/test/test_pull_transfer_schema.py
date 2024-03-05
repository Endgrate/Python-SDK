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

from endgrate.models.pull_transfer_schema import PullTransferSchema

class TestPullTransferSchema(unittest.TestCase):
    """PullTransferSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PullTransferSchema:
        """Test PullTransferSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PullTransferSchema`
        """
        model = PullTransferSchema()
        if include_optional:
            return PullTransferSchema(
                bypass_rate_limit = None,
                endgrate_type = '',
                params = endgrate.models.properties.properties(),
                session_id = '',
                synchronous = None
            )
        else:
            return PullTransferSchema(
                endgrate_type = '',
                session_id = '',
        )
        """

    def testPullTransferSchema(self):
        """Test PullTransferSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
