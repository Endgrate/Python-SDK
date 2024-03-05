# coding: utf-8

"""
    Endgrate API

    Endgrate API Reference

    The version of the OpenAPI document: 1.0.0
    Contact: team@endgrate.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_api_pull_data200_response_meta_previous import GetApiPullData200ResponseMetaPrevious
from typing import Optional, Set
from typing_extensions import Self

class GetApiPullData200ResponseMeta(BaseModel):
    """
    Paging metadata.
    """ # noqa: E501
    count: Optional[StrictInt] = None
    previous: Optional[GetApiPullData200ResponseMetaPrevious] = None
    next: Optional[GetApiPullData200ResponseMetaPrevious] = None
    __properties: ClassVar[List[str]] = ["count", "previous", "next"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetApiPullData200ResponseMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of previous
        if self.previous:
            _dict['previous'] = self.previous.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next
        if self.next:
            _dict['next'] = self.next.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetApiPullData200ResponseMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "previous": GetApiPullData200ResponseMetaPrevious.from_dict(obj["previous"]) if obj.get("previous") is not None else None,
            "next": GetApiPullData200ResponseMetaPrevious.from_dict(obj["next"]) if obj.get("next") is not None else None
        })
        return _obj


