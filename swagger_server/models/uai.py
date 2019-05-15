# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UAI(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uai_name: str=None, username: str=None, publickey: str=None, uai_img: str=None, uai_ip: str=None, uai_status: str=None, uai_msg: str=None, uai_port: str=None, uai_connect_string: str=None, uai_portmap: dict={}):  # noqa: E501
        """UAI - a model defined in Swagger

        :param uai_name: The uai_name of this UAI.  # noqa: E501
        :type uai_name: str
        :param username: The username of this UAI.  # noqa: E501
        :type username: str
        :param publickey: The publickey of this UAI.  # noqa: E501
        :type publickey: str
        :param uai_img: The uai_img of this UAI.  # noqa: E501
        :type uai_img: str
        :param uai_ip: The uai_ip of this UAI.  # noqa: E501
        :type uai_ip: str
        :param uai_status: The uai_status of this UAI.  # noqa: E501
        :type uai_status: str
        :param uai_msg: The uai_msg of this UAI.  # noqa: E501
        :type uai_msg: str
        :param uai_port: The uai_port of this UAI.  # noqa: E501
        :type uai_port: str
        :param uai_connect_string: The uai_connect_string of this UAI.  # noqa: E501
        :type uai_connect_string: str
        :param uai_portmap: The uai_portmap of this UAI.  # noqa: E501
        :type uai_portmap: dict
        """
        self.swagger_types = {
            'uai_name': str,
            'username': str,
            'publickey': str,
            'uai_img': str,
            'uai_ip': str,
            'uai_status': str,
            'uai_msg': str,
            'uai_port': str,
            'uai_connect_string': str,
            'uai_portmap': dict
        }

        self.attribute_map = {
            'uai_name': 'uai_name',
            'username': 'username',
            'publickey': 'publickey',
            'uai_img': 'uai_img',
            'uai_ip': 'uai_ip',
            'uai_status': 'uai_status',
            'uai_msg': 'uai_msg',
            'uai_port': 'uai_port',
            'uai_connect_string': 'uai_connect_string',
            'uai_portmap': 'uai_portmap'
        }

        self._uai_name = uai_name
        self._username = username
        self._publickey = publickey
        self._uai_img = uai_img
        self._uai_ip = uai_ip
        self._uai_status = uai_status
        self._uai_msg = uai_msg
        self._uai_port = uai_port
        self._uai_connect_string = uai_connect_string
        self._uai_portmap = uai_portmap

    @classmethod
    def from_dict(cls, dikt) -> 'UAI':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UAI of this UAI.  # noqa: E501
        :rtype: UAI
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uai_name(self) -> str:
        """Gets the uai_name of this UAI.


        :return: The uai_name of this UAI.
        :rtype: str
        """
        return self._uai_name

    @uai_name.setter
    def uai_name(self, uai_name: str):
        """Sets the uai_name of this UAI.


        :param uai_name: The uai_name of this UAI.
        :type uai_name: str
        """

        self._uai_name = uai_name

    @property
    def username(self) -> str:
        """Gets the username of this UAI.


        :return: The username of this UAI.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UAI.


        :param username: The username of this UAI.
        :type username: str
        """

        self._username = username

    @property
    def publickey(self) -> str:
        """Gets the publickey of this UAI.


        :return: The publickey of this UAI.
        :rtype: str
        """
        return self._publickey

    @publickey.setter
    def publickey(self, publickey: str):
        """Sets the publickey of this UAI.


        :param publickey: The publickey of this UAI.
        :type publickey: str
        """

        self._publickey = publickey

    @property
    def uai_img(self) -> str:
        """Gets the uai_img of this UAI.


        :return: The uai_img of this UAI.
        :rtype: str
        """
        return self._uai_img

    @uai_img.setter
    def uai_img(self, uai_img: str):
        """Sets the uai_img of this UAI.


        :param uai_img: The uai_img of this UAI.
        :type uai_img: str
        """

        self._uai_img = uai_img

    @property
    def uai_ip(self) -> str:
        """Gets the uai_ip of this UAI.


        :return: The uai_ip of this UAI.
        :rtype: str
        """
        return self._uai_ip

    @uai_ip.setter
    def uai_ip(self, uai_ip: str):
        """Sets the uai_ip of this UAI.


        :param uai_ip: The uai_ip of this UAI.
        :type uai_ip: str
        """

        self._uai_ip = uai_ip

    @property
    def uai_status(self) -> str:
        """Gets the uai_status of this UAI.


        :return: The uai_status of this UAI.
        :rtype: str
        """
        return self._uai_status

    @uai_status.setter
    def uai_status(self, uai_status: str):
        """Sets the uai_status of this UAI.


        :param uai_status: The uai_status of this UAI.
        :type uai_status: str
        """

        self._uai_status = uai_status

    @property
    def uai_msg(self) -> str:
        """Gets the uai_msg of this UAI.


        :return: The uai_msg of this UAI.
        :rtype: str
        """
        return self._uai_msg

    @uai_msg.setter
    def uai_msg(self, uai_msg: str):
        """Sets the uai_msg of this UAI.


        :param uai_msg: The uai_msg of this UAI.
        :type uai_msg: str
        """

        self._uai_msg = uai_msg

    @property
    def uai_port(self) -> str:
        """Gets the uai_port of this UAI.


        :return: The uai_port of this UAI.
        :rtype: str
        """
        return self._uai_port

    @uai_port.setter
    def uai_port(self, uai_port: str):
        """Sets the uai_port of this UAI.


        :param uai_port: The uai_port of this UAI.
        :type uai_port: str
        """

        self._uai_port = uai_port

    @property
    def uai_connect_string(self) -> str:
        """Gets the uai_connect_string of this UAI.


        :return: The uai_connect_string of this UAI.
        :rtype: str
        """
        return self._uai_connect_string

    @uai_connect_string.setter
    def uai_connect_string(self, uai_connect_string: str):
        """Sets the uai_connect_string of this UAI.


        :param uai_connect_string: The uai_connect_string of this UAI.
        :type uai_connect_string: str
        """

        self._uai_connect_string = uai_connect_string

    @property
    def uai_portmap(self) -> dict:
        """Gets the uai_portmap of this UAI.


        :return: The uai_portmap of this UAI.
        :rtype: dict
        """
        return self._uai_portmap

    @uai_portmap.setter
    def uai_portmap(self, uai_portmap: dict):
        """Sets the uai_portmap of this UAI.


        :param uai_portmap: The uai_portmap of this UAI.
        :type uai_portmap: dict
        """

        self._uai_portmap = uai_portmap