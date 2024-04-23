from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplyForward(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: int
    def __init__(self, msg: _Optional[int] = ...) -> None: ...

class RequestForward(_message.Message):
    __slots__ = ("images", "track_ids", "frame_index")
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    TRACK_IDS_FIELD_NUMBER: _ClassVar[int]
    FRAME_INDEX_FIELD_NUMBER: _ClassVar[int]
    images: bytes
    track_ids: int
    frame_index: int
    def __init__(self, images: _Optional[bytes] = ..., track_ids: _Optional[int] = ..., frame_index: _Optional[int] = ...) -> None: ...
