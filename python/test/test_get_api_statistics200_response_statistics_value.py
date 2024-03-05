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

from endgrate.models.get_api_statistics200_response_statistics_value import GetApiStatistics200ResponseStatisticsValue

class TestGetApiStatistics200ResponseStatisticsValue(unittest.TestCase):
    """GetApiStatistics200ResponseStatisticsValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApiStatistics200ResponseStatisticsValue:
        """Test GetApiStatistics200ResponseStatisticsValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApiStatistics200ResponseStatisticsValue`
        """
        model = GetApiStatistics200ResponseStatisticsValue()
        if include_optional:
            return GetApiStatistics200ResponseStatisticsValue(
                batch_size = 56,
                records = 56,
                batches = 56,
                batches_queued = 56,
                batches_success = 56,
                batches_fail = 56,
                records_transferred = 56,
                completed = True,
                provider = '',
                integration = ''
            )
        else:
            return GetApiStatistics200ResponseStatisticsValue(
        )
        """

    def testGetApiStatistics200ResponseStatisticsValue(self):
        """Test GetApiStatistics200ResponseStatisticsValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
