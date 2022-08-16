class Store:

    tariff = 1.03

    def __init__(self, address: str) -> None:
        self.__address = address

    def present_address(self) -> None:
        print(self.__address)

    @classmethod
    def sell(cls) -> int:
        return 40 * cls.tariff

    @classmethod
    def change_tariff(cls, new_tariff: int) -> None:
        cls.tariff = new_tariff


store_beach = Store('Beach')
store_center = Store('Center')

store_beach.present_address()

print(store_beach.sell())
print(store_center.sell())

store_center.change_tariff(1.50)

print(store_beach.sell())
print(store_center.sell())
