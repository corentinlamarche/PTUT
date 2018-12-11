import connexion
import six

from swagger_server import util


def control_post(idESP, idCapteur, action):  # noqa: E501
    """Allumer / éteindre la LED de l&#39;ESP

    Allume ou éteint la LED de l&#39;ESP # noqa: E501

    :param idESP: L&#39;ID de l&#39;ESP
    :type idESP: int
    :param idCapteur: L&#39;ID du capteur
    :type idCapteur: int
    :param action: Allume ou éteint
    :type action: bool

    :rtype: None
    """
    return 'do some magic!'


def get_esp(ID):  # noqa: E501
    """Récupère l&#39;ESP

    Récupère l&#39;ESP grâce à son ID # noqa: E501

    :param ID: ID de l&#39;ESP
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'


def get_esp_list():  # noqa: E501
    """Récupère la liste des ESP

    Récupère la liste des ESP # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def json_get(ID):  # noqa: E501
    """Récupère un JSON de l&#39;ESP

    Récupère le JSON de l&#39;ESP # noqa: E501

    :param ID: ID de l&#39;ESP
    :type ID: int

    :rtype: None
    """
    return 'do some magic!'
