# coding: utf-8

"""
    Finnhub Stock API

    OpenAPI spec for real-time stock quotes using Finnhub’s `/quote` endpoint. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class QuoteResponse(BaseModel):
    """
    QuoteResponse
    """ # noqa: E501
    c: Union[StrictFloat, StrictInt] = Field(description="Current price")
    d: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Absolute change from previous close")
    dp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percent change from previous close")
    h: Union[StrictFloat, StrictInt] = Field(description="High price of the day")
    l: Union[StrictFloat, StrictInt] = Field(description="Low price of the day")
    o: Union[StrictFloat, StrictInt] = Field(description="Open price of the day")
    pc: Union[StrictFloat, StrictInt] = Field(description="Previous close price")
    t: StrictInt = Field(description="Timestamp (Unix)")
    __properties: ClassVar[List[str]] = ["c", "d", "dp", "h", "l", "o", "pc", "t"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QuoteResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "c": obj.get("c"),
            "d": obj.get("d"),
            "dp": obj.get("dp"),
            "h": obj.get("h"),
            "l": obj.get("l"),
            "o": obj.get("o"),
            "pc": obj.get("pc"),
            "t": obj.get("t")
        })
        return _obj


