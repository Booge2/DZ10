class MyMetaClass(type):

    def __new__(cls, name, bases, dct):
        if "do_something" not in dct:
            raise TypeError("Клас повинен мати метод `do_something`")

        dct["do_something"] = decorator(dct["do_something"])

        return super().__new__(cls, name, bases, dct)


def decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Перед викликом `do_something`")

        func(self, *args, **kwargs)

        print("Після виклику `do_something`")

    return wrapper


class MyClass(metaclass=MyMetaClass):

    def do_something(self):
        print("Щось робимо")


my_object = MyClass()

my_object.do_something()

print("-----------------------")


# Завдання 2
class MyMetaClass(type):

    def __new__(cls, name, bases, dct, **kwargs):
        class_name_prefix = kwargs.get("class_name_prefix", None)

        if class_name_prefix:
            name = f"{class_name_prefix}_{name}"

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMetaClass, class_name_prefix="My"):

    def do_something(self):
        print("Щось робимо")


my_object = MyClass()

print(type(my_object).__name__)

print("-----------------------")


# Завдання 3
class MyMetaClass(type):

    def __new__(cls, name, bases, dct):
        dct["author"] = "Your Name"

        dct["version"] = "1.0"

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMetaClass):
    pass


my_object = MyClass()

print(my_object.author)
print(my_object.version)
print("-----------------------")


# Завдання 4
class MyMetaClass(type):

    def __new__(cls, name, bases, dct):
        init_method = dct["__init__"]

        dct["__init__"] = decorator(init_method)

        return super().__new__(cls, name, bases, dct)


def decorator(func):
    def wrapper(self, *args, **kwargs):
        if not args:
            raise TypeError("Необхідно вказати хоча б один аргумент")

        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Аргументи повинні бути типа `int`")

        func(self, *args, **kwargs)

    return wrapper


class MyClass(metaclass=MyMetaClass):

    def __init__(self, *args):
        self.args = args


my_object = MyClass(1, 2, 3)

print(my_object.args)

try:
    my_object = MyClass()
except TypeError as e:
    print(e)
