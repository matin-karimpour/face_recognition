from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ("datas",)
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: bytes
    def __init__(self, datas: _Optional[bytes] = ...) -> None: ...
