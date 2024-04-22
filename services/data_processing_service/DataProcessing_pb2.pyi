from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Replyresult(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: int
    def __init__(self, msg: _Optional[int] = ...) -> None: ...

class RequestFace(_message.Message):
    __slots__ = ("images", "action", "name")
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    images: bytes
    action: str
    name: str
    def __init__(self, images: _Optional[bytes] = ..., action: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
