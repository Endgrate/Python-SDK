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

from endgrate.api.endgrate_api import EndgrateApi


class TestEndgrateApi(unittest.TestCase):
    """EndgrateApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EndgrateApi()

    def tearDown(self) -> None:
        pass

    def test_get_api_errors(self) -> None:
        """Test case for get_api_errors

        Get Error Logs
        """
        pass

    def test_get_api_integrations(self) -> None:
        """Test case for get_api_integrations

        Get Integrations
        """
        pass

    def test_get_api_pull_data(self) -> None:
        """Test case for get_api_pull_data

        Get Pull Data
        """
        pass

    def test_get_api_session_configuration(self) -> None:
        """Test case for get_api_session_configuration

        Get Session Configuration
        """
        pass

    def test_get_api_session_delete(self) -> None:
        """Test case for get_api_session_delete

        Delete Session
        """
        pass

    def test_get_api_statistics(self) -> None:
        """Test case for get_api_statistics

        Get Statistics
        """
        pass

    def test_get_session(self) -> None:
        """Test case for get_session

        Session Redirect
        """
        pass

    def test_get_session_edit(self) -> None:
        """Test case for get_session_edit

        Edit Session Redirect
        """
        pass

    def test_get_session_reauthenticate(self) -> None:
        """Test case for get_session_reauthenticate

        Reauthenticate Session Redirect
        """
        pass

    def test_post_api_pull_initiate(self) -> None:
        """Test case for post_api_pull_initiate

        Initiate Pull Session
        """
        pass

    def test_post_api_pull_transfer(self) -> None:
        """Test case for post_api_pull_transfer

        Trigger Pull
        """
        pass

    def test_post_api_push_initiate(self) -> None:
        """Test case for post_api_push_initiate

        Initiate Push Session
        """
        pass

    def test_post_api_push_transfer(self) -> None:
        """Test case for post_api_push_transfer

        Trigger Push
        """
        pass

    def test_post_api_schemas(self) -> None:
        """Test case for post_api_schemas

        Set Schemas
        """
        pass

    def test_post_api_session_initiate(self) -> None:
        """Test case for post_api_session_initiate

        Initiate (Push + Pull) Session
        """
        pass


if __name__ == '__main__':
    unittest.main()