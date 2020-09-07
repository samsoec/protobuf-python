import enums.enum_pb2 as enum_pb2

enum_message = enum_pb2.EnumMessage()
enum_message.id = 345
enum_message.day_name = enum_pb2.MONDAY

print(enum_message)

print(enum_message.day_name)

with open("enums.bin", "wb") as f:
    print("write to bin")
    byteAsString = enum_message.SerializeToString()
    f.write(byteAsString)

with open("enums.bin", "rb") as f:
    print("read from bin")
    enums_message_read = enum_pb2.EnumMessage().FromString(f.read())
    print(enums_message_read)