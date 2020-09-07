import practice.practice_pb2 as practice_pb2

address_book = practice_pb2.AddressBook()

first_people = practice_pb2.Person()
first_people.id = 123
first_people.name = "Rizal"
first_people.email = "sam@gmail.com"
first_people.phones.add(number="021111", type=practice_pb2.Person.PhoneType.WORK)
first_people.phones.add(number="081111", type=practice_pb2.Person.PhoneType.WORK)

second_people = practice_pb2.Person()
second_people.id = 234
second_people.name = "Samsul"
second_people.email = "samsul@gmail.com"
second_people.phones.add(number="0211112", type=practice_pb2.Person.PhoneType.WORK)
second_people.phones.add(number="0811112", type=practice_pb2.Person.PhoneType.WORK)

address_book.people.extend([first_people, second_people])

print(address_book)