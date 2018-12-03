# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCapteursController(BaseTestCase):
    """CapteursController integration test stubs"""

    def test_get_captor_data(self):
        """Test case for get_captor_data

        Récupère la valeur du capteur
        """
        query_string = [('ID', 56),
                        ('Type', 'Type_example')]
        response = self.client.open(
            '//projet/functions/capteurs/getData',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_captors_list(self):
        """Test case for get_captors_list

        Récupère la liste des capteurs liés à l'ESP
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '//projet/functions/capteurs/getList',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
