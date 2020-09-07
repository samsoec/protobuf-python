import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()

simple_message.id = 123
simple_message.is_simple = True
simple_message.name = "name"
simple_list = simple_message.simple_list

simple_list.append(3)
simple_list.append(4)
simple_list.append(5)

print(simple_message)

with open("simple.bin", "wb") as f:
    print("write to bin")
    byteAsString = simple_message.SerializeToString()
    f.write(byteAsString)

with open("simple.bin", "rb") as f:
    print("read from bin")
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())
    print(simple_message_read)

print("check name : ", simple_message_read.name)