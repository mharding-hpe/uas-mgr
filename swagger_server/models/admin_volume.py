#
# Copyright 2020, Cray Inc.  All Rights Reserved.
#
# coding: utf-8
"""Auto generated models for swagger schema

"""

from __future__ import absolute_import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AdminVolume(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(
            self,
            volumename: str = None,
            mount_path: str = None,
            volume_description: str = None
    ):  # noqa: E501
        """AdminVolume - a model defined in Swagger

        :param volumename: The volumename of this AdminVolume.  # noqa: E501
        :type volumename: str
        :param mount_path: The mount_path of this AdminVolume.  # noqa: E501
        :type mount_path: str
        :param volume_description: The volume_description of this
                                   AdminVolume.  # noqa: E501
        :type volume_description: str
        """
        self.swagger_types = {
            'volumename': str,
            'mount_path': str,
            'volume_description': str
        }

        self.attribute_map = {
            'volumename': 'volumename',
            'mount_path': 'mount_path',
            'volume_description': 'volume_description'
        }
        self._volumename = volumename
        self._mount_path = mount_path
        self._volume_description = volume_description

    @classmethod
    def from_dict(cls, dikt) -> 'AdminVolume':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdminVolume of this AdminVolume.  # noqa: E501
        :rtype: AdminVolume
        """
        return util.deserialize_model(dikt, cls)

    @property
    def volumename(self) -> str:
        """Gets the volumename of this AdminVolume.


        :return: The volumename of this AdminVolume.
        :rtype: str
        """
        return self._volumename

    @volumename.setter
    def volumename(self, volumename: str):
        """Sets the volumename of this AdminVolume.


        :param volumename: The volumename of this AdminVolume.
        :type volumename: str
        """

        self._volumename = volumename

    @property
    def mount_path(self) -> str:
        """Gets the mount_path of this AdminVolume.


        :return: The mount_path of this AdminVolume.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path: str):
        """Sets the mount_path of this AdminVolume.


        :param mount_path: The mount_path of this AdminVolume.
        :type mount_path: str
        """

        self._mount_path = mount_path

    @property
    def volume_description(self) -> str:
        """Gets the volume_description of this AdminVolume.


        :return: The volume_description of this AdminVolume.
        :rtype: str
        """
        return self._volume_description

    @volume_description.setter
    def volume_description(self, volume_description: str):
        """Sets the volume_description of this AdminVolume.


        :param volume_description: The volume_description of this AdminVolume.
        :type volume_description: str
        """

        self._volume_description = volume_description
