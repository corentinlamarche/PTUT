# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestESPController(BaseTestCase):
    """ESPController integration test stubs"""

    def test_control_post(self):
        """Test case for control_post

        Allumer / éteindre la LED de l'ESP
        """
        query_string = [('idESP', 56),
                        ('idCapteur', 56),
                        ('action', true)]
        response = self.client.open(
            '//projet/functions/esp/setLight',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_esp(self):
        """Test case for get_esp

        Récupère l'ESP
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '//projet/functions/esp/getById',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_esp_list(self):
        """Test case for get_esp_list

        Récupère la liste des ESP
        """
        response = self.client.open(
            '//projet/functions/esp/getList',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_json_get(self):
        """Test case for json_get

        Récupère un JSON de l'ESP
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '//projet/functions/esp/getJson',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
