class MyClass:
    def __init__(self, my_attribute2) -> None:
        self.my_attribute = 'Hello World'
        self.my_attribute2 = my_attribute2

    def my_methody(self):
        print(self.my_attribute)
        print(self.my_attribute2)

    def my_methody2(self, num, mult):
        return num * mult


obj = MyClass(23)
result = obj.my_methody2(3, 2)

print(result)

obj.my_methody()

att = obj.my_attribute
print(att)

att2 = obj.my_attribute2

print(att2)
