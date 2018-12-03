# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestBDDController(BaseTestCase):
    """BDDController integration test stubs"""

    def test_delete_esp(self):
        """Test case for delete_esp

        Supprime l'ESP dans la BDD
        """
        query_string = [('ID', 56)]
        response = self.client.open(
            '//projet/functions/bdd/delete',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_esp(self):
        """Test case for insert_esp

        Ajoute une ESP dans la BDD
        """
        query_string = [('ID', 56),
                        ('IP', 'IP_example')]
        response = self.client.open(
            '//projet/functions/bdd/insert',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_esp(self):
        """Test case for update_esp

        Met à jour l'ESP dans la BDD
        """
        query_string = [('ID', 56),
                        ('IP', 'IP_example')]
        response = self.client.open(
            '//projet/functions/bdd/update',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
