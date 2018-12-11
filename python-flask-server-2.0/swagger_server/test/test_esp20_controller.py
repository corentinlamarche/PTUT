# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestESP20Controller(BaseTestCase):
    """ESP20Controller integration test stubs"""

    def test_esp_send_data(self):
        """Test case for esp_send_data

        Envoie les données des capteurs en BDD
        """
        response = self.client.open(
            '//projet/functions/esp/sendData',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
