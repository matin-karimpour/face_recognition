# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FaceDetection.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x46\x61\x63\x65\x44\x65tection.proto\"\'\n\tReplyData\x12\r\n\x05\x66\x61\x63\x65s\x18\x01 \x01(\x0c\x12\x0b\n\x03ids\x18\x02 \x01(\x0c\"\x1c\n\x0bRequestData\x12\r\n\x05\x66rame\x18\x01 \x01(\x0c\x32\x38\n\rFaceDetection\x12\'\n\tgetStream\x12\x0c.RequestData\x1a\n.ReplyData\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FaceDetection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REPLYDATA']._serialized_start=23
  _globals['_REPLYDATA']._serialized_end=62
  _globals['_REQUESTDATA']._serialized_start=64
  _globals['_REQUESTDATA']._serialized_end=92
  _globals['_FACEDETECTION']._serialized_start=94
  _globals['_FACEDETECTION']._serialized_end=150
# @@protoc_insertion_point(module_scope)