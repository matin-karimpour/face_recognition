from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplyData(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: int
    def __init__(self, msg: _Optional[int] = ...) -> None: ...

class RequestData(_message.Message):
    __slots__ = ("images",)
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    images: bytes
    def __init__(self, images: _Optional[bytes] = ...) -> None: ...
