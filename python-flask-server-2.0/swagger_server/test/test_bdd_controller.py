# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestBDDController(BaseTestCase):
    """BDDController integration test stubs"""

    def test_bdd_get_data(self):
        """Test case for bdd_get_data

        Récupère la valeur de tous les capteurs en BDD
        """
        response = self.client.open(
            '//projet/functions/bdd/getData',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bdd_get_data_by_building(self):
        """Test case for bdd_get_data_by_building

        Récupère toutes les données des capteurs d'un bâtiment
        """
        query_string = [('Batiment', 'Batiment_example')]
        response = self.client.open(
            '//projet/functions/bdd/getDataByBuilding',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bdd_get_data_by_date(self):
        """Test case for bdd_get_data_by_date

        Recupère toutes les données entre deux dates
        """
        query_string = [('Batiment', 'Batiment_example'),
                        ('Date1', '01/01/1970 00:00'),
                        ('Date2', '01/01/1970 00:00')]
        response = self.client.open(
            '//projet/functions/bdd/getDataByDate',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
