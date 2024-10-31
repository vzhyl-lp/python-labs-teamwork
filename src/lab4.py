# Лабораторна робота №4
# Жилочкін Вадим, варіянт 8


class Helicopter():

    def __init__(self,
                 name = "Sikorsky R-4", person_capacity = 4, max_speed = 132, 
                 my_public_num = 7654, my_public_str = "fff", resource = 10000):
        
        # Приватні:
        self.__person_capacity = person_capacity
        self.__name = name
        self.__max_speed = max_speed
        self.__resource = resource

        # Публічні:
        self.my_public_num = my_public_num
        self.my_public_str = my_public_str

    def get_resource(self):
        return self.__resource
    
    def set_resource(self, hours):
        self.__resource -= hours

    def main(self):
        obj1 = Helicopter("Mi-6", 5, 100, 123, "jsasd")
        obj2 = Helicopter("Mi-7", 10, 125, 321, "kjgdss")
        obj3 = Helicopter("Mi-8", 15, 150, 654, "lkjhgf")

        def get_max_resource(self, *args):
            max = obj1.get_resource()
            for object in args:
                if object.get_resource() > max:
                    max = object.get_resource()
            print(max)

        obj1.set_resource(500)
        obj2.set_resource(1000)
        obj3.set_resource(1500)
        get_max_resource(obj1, obj2, obj3)
        

        def output_data(obj):
            object_keys = obj.__dict__.keys()
            for key in object_keys:
                print(f"{key} = {obj.__dict__[key]}")
            
        output_data(obj1)
        output_data(obj2)
        output_data(obj3)


    # Доступ до приватних змінних
    def get_person_capacity(self):
        return self.__person_capacity 
    def get_name(self):
        return self.__name
    def get_max_speed(self):
        return self.__max_speed
    

    # Перевизначення методів
    def __str__():
        return "Тут виконується перевизначений метод __str__"
    def __repr__():
        return "Тут виконується перевизначений метод __repr__"
    

    # Деструктор
    def __del__(self):
        print(f"Об'єкт {self.__name} видалено")
    

new_helicopter = Helicopter()

new_helicopter.main()