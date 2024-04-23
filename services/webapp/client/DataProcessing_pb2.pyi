from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Replyresult(_message.Message):
    __slots__ = ("image", "track_id", "msg")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    image: bytes
    track_id: int
    msg: int
    def __init__(self, image: _Optional[bytes] = ..., track_id: _Optional[int] = ..., msg: _Optional[int] = ...) -> None: ...

class RequestFace(_message.Message):
    __slots__ = ("images", "action", "name", "track_ids", "frame_index")
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRACK_IDS_FIELD_NUMBER: _ClassVar[int]
    FRAME_INDEX_FIELD_NUMBER: _ClassVar[int]
    images: bytes
    action: str
    name: str
    track_ids: bytes
    frame_index: int
    def __init__(self, images: _Optional[bytes] = ..., action: _Optional[str] = ..., name: _Optional[str] = ..., track_ids: _Optional[bytes] = ..., frame_index: _Optional[int] = ...) -> None: ...
