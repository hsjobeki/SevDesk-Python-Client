from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VoucherPosResponseModelSevClient")


@attr.s(auto_attribs=True)
class VoucherPosResponseModelSevClient:
    """Client to which voucher position belongs. Will be filled automatically

    Attributes:
        id (str): Unique identifier of the client Example: 0.
        object_name (str): Model name, which is 'SevClient' Example: SevClient.
    """

    id: str
    object_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_name = self.object_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "objectName": object_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_name = d.pop("objectName")

        voucher_pos_response_model_sev_client = cls(
            id=id,
            object_name=object_name,
        )

        voucher_pos_response_model_sev_client.additional_properties = d
        return voucher_pos_response_model_sev_client

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
