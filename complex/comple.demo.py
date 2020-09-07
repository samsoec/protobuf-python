import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()

complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "one dummy"

# FIRST METHOD
first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 234
first_multiple_dummy.name = "first element of multiple dummy"

# SECOND METHOD
complex_message.multiple_dummy.add(id= 345, name="second element of multiple dummy")

# THIRD METHOD
third_dummy = complex_pb2.DummyMessage()
third_dummy.id = 456
third_dummy.name = "third element of multiple dummy"
complex_message.multiple_dummy.extend([third_dummy])

print(complex_message)