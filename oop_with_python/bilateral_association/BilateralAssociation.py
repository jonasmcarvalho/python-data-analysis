from modules import House, Person

house_of_jonas = House()
jonas = Person('Jonas')

jonas.local_set(house_of_jonas)
house_of_jonas.set_owner(jonas)

proprietario = house_of_jonas.get_owner()
proprietario.introduce_yourself()

jonas.present_location()
