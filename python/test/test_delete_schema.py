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

from endgrate.models.delete_schema import DeleteSchema

class TestDeleteSchema(unittest.TestCase):
    """DeleteSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteSchema:
        """Test DeleteSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteSchema`
        """
        model = DeleteSchema()
        if include_optional:
            return DeleteSchema(
                session_id = ''
            )
        else:
            return DeleteSchema(
                session_id = '',
        )
        """

    def testDeleteSchema(self):
        """Test DeleteSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
