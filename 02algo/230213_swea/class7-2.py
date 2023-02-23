# class Dog:
#     @classmethod
#     def bark(self):
#         pass
#
#     def num_of_dogs(cls):
#

def ko_halo(name):
    print(f'안녕하세요, {name}님!')

def ko_halo(name):
    print(f'안녕하세요, {name}님!')

def emoji(name, func):
    func(name)
    print('^^')

def emoji_deco(func):
    def wrapper(name):
        func(name)
        print('^^')

    return wrapper

new_func = emoji_deco(ko_halo)
new_func()

