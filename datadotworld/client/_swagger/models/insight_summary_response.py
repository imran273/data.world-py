# coding: utf-8

"""
    data.world API

    data.world is designed for data and the people who work with data.  From professional projects to open data, data.world helps you host and share your data, collaborate with your team, and capture context and conclusions as you work.   Using this API users are able to easily access data and manage their data projects regardless of language or tool of preference.  Check out our [documentation](https://dwapi.apidocs.io) for tips on how to get started, tutorials and to interact with the API right within your browser.

    OpenAPI spec version: 0.14.1
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InsightSummaryResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'title': 'str',
        'description': 'str',
        'body': 'InsightBody',
        'source_link': 'str',
        'data_source_links': 'list[str]',
        'author': 'str',
        'created': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'body': 'body',
        'source_link': 'sourceLink',
        'data_source_links': 'dataSourceLinks',
        'author': 'author',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, title=None, description=None, body=None, source_link=None, data_source_links=None, author=None, created=None, updated=None):
        """
        InsightSummaryResponse - a model defined in Swagger
        """

        self._id = None
        self._title = None
        self._description = None
        self._body = None
        self._source_link = None
        self._data_source_links = None
        self._author = None
        self._created = None
        self._updated = None

        self.id = id
        self.title = title
        if description is not None:
          self.description = description
        self.body = body
        if source_link is not None:
          self.source_link = source_link
        if data_source_links is not None:
          self.data_source_links = data_source_links
        self.author = author
        self.created = created
        self.updated = updated

    @property
    def id(self):
        """
        Gets the id of this InsightSummaryResponse.
        Unique Insight id.

        :return: The id of this InsightSummaryResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InsightSummaryResponse.
        Unique Insight id.

        :param id: The id of this InsightSummaryResponse.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this InsightSummaryResponse.
        Insight title.

        :return: The title of this InsightSummaryResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this InsightSummaryResponse.
        Insight title.

        :param title: The title of this InsightSummaryResponse.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this InsightSummaryResponse.
        Insight description.

        :return: The description of this InsightSummaryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InsightSummaryResponse.
        Insight description.

        :param description: The description of this InsightSummaryResponse.
        :type: str
        """

        self._description = description

    @property
    def body(self):
        """
        Gets the body of this InsightSummaryResponse.

        :return: The body of this InsightSummaryResponse.
        :rtype: InsightBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this InsightSummaryResponse.

        :param body: The body of this InsightSummaryResponse.
        :type: InsightBody
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")

        self._body = body

    @property
    def source_link(self):
        """
        Gets the source_link of this InsightSummaryResponse.
        Permalink to source code or platform this insight was generated with. Allows others to replicate the steps originally used to produce the insight.

        :return: The source_link of this InsightSummaryResponse.
        :rtype: str
        """
        return self._source_link

    @source_link.setter
    def source_link(self, source_link):
        """
        Sets the source_link of this InsightSummaryResponse.
        Permalink to source code or platform this insight was generated with. Allows others to replicate the steps originally used to produce the insight.

        :param source_link: The source_link of this InsightSummaryResponse.
        :type: str
        """

        self._source_link = source_link

    @property
    def data_source_links(self):
        """
        Gets the data_source_links of this InsightSummaryResponse.
        One or more permalinks to the data sources used to generate this insight. Allows others to access the data originally used to produce the insight.

        :return: The data_source_links of this InsightSummaryResponse.
        :rtype: list[str]
        """
        return self._data_source_links

    @data_source_links.setter
    def data_source_links(self, data_source_links):
        """
        Sets the data_source_links of this InsightSummaryResponse.
        One or more permalinks to the data sources used to generate this insight. Allows others to access the data originally used to produce the insight.

        :param data_source_links: The data_source_links of this InsightSummaryResponse.
        :type: list[str]
        """

        self._data_source_links = data_source_links

    @property
    def author(self):
        """
        Gets the author of this InsightSummaryResponse.
        User name of the author of the insight.

        :return: The author of this InsightSummaryResponse.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this InsightSummaryResponse.
        User name of the author of the insight.

        :param author: The author of this InsightSummaryResponse.
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")

        self._author = author

    @property
    def created(self):
        """
        Gets the created of this InsightSummaryResponse.
        Date and time when insight was created.

        :return: The created of this InsightSummaryResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this InsightSummaryResponse.
        Date and time when insight was created.

        :param created: The created of this InsightSummaryResponse.
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def updated(self):
        """
        Gets the updated of this InsightSummaryResponse.
        Date and time when insight was last updated.

        :return: The updated of this InsightSummaryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this InsightSummaryResponse.
        Date and time when insight was last updated.

        :param updated: The updated of this InsightSummaryResponse.
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")

        self._updated = updated

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InsightSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
