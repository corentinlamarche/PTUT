import connexion
import six

from swagger_server import util


def bdd_get_data():  # noqa: E501
    """Récupère la valeur de tous les capteurs en BDD

    Récupère la valeur de tous les capteurs en BDD # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def bdd_get_data_by_building(Batiment):  # noqa: E501
    """Récupère toutes les données des capteurs d&#39;un bâtiment

    Récupère toutes les données des capteurs d&#39;un bâtiment # noqa: E501

    :param Batiment: Nom du bâtiment
    :type Batiment: str

    :rtype: None
    """
    return 'do some magic!'


def bdd_get_data_by_date(Batiment, Date1, Date2):  # noqa: E501
    """Recupère toutes les données entre deux dates

    Récupère toutes les données des capteurs d&#39;un bâtiment entre deux dates # noqa: E501

    :param Batiment: Nom du bâtiment
    :type Batiment: str
    :param Date1: Date et heure de début
    :type Date1: str
    :param Date2: Date et heure de fin
    :type Date2: str

    :rtype: None
    """
    return 'do some magic!'


def delete_esp(ID):  # noqa: E501
    """Supprime l&#39;ESP dans la BDD

    Supprime l&#39;ESP dans la BDD # noqa: E501

    :param ID: ID de l&#39;ESP
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'


def insert_esp(ID, IP):  # noqa: E501
    """Ajoute une ESP dans la BDD

    Insert une ESP dans la BDD # noqa: E501

    :param ID: ID de l&#39;ESP
    :type ID: int
    :param IP: IP de l&#39;ESP
    :type IP: str

    :rtype: None
    """
    return 'do some magic!'


def update_esp(ID, IP):  # noqa: E501
    """Met à jour l&#39;ESP dans la BDD

    Met à jour l&#39;ESP dans la BDD # noqa: E501

    :param ID: ID de l&#39;ESP
    :type ID: int
    :param IP: Nouvelle IP
    :type IP: str

    :rtype: None
    """
    return 'do some magic!'
