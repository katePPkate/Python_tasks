class Family:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name} Age: {self.age}")

sister = Family("Anya","Valova", 16)
mother = Family("Zhenya", "Valova", 40)
brother = Family("Vanya", "Valov", 3)
sister.display_info()

