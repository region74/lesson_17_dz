import random


class Cart:
    def __init__(self):
        self.cart = None
        self.create()

    def create(self):
        self.cart = list(sorted(random.sample(range(1, 100), k=15)))
        for i in range(14):
            self.cart.append('#')
        random.shuffle(self.cart)

    def dec(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            remade = ('*' * 42 + '\n' + str(result[0:9]) + '\n' + str(result[9:18]) + '\n' + str(
                result[18:27]) + '\n' + '*' * 42)
            return remade

        return inner

    @dec
    def __str__(self):
        return self.cart

    def __len__(self):
        return len(self.cart)

    def __contains__(self, item):
        return self.cart[item]

    def is_empty(self):
        # return False if (lambda x:(str(i).isdigit() for i in self.cart)) else True
        count = 0
        for item in self.cart:
            if str(item).isdigit():
                count += 1
                return False

    def is_num_to_cart(self, num):
        return True if num in list(self.cart) else False

    def cross_out(self, num):
        for item in self.cart:
            if num == item:
                idx = list(self.cart).index(item)
                self.cart[idx] = '❌'


class Person:

    def __init__(self):
        self.cart = Cart()
        self.name = input('Введите имя игрока: ')
        print(f'Имя игрока: {self.name}')

    def step(self, num):
        print(self.cart)
        answer = input('Зачеркнуть цифру (Y/N)? ')
        while answer not in 'yYNn':
            answer = input('Некорректный ввод. Зачеркнуть цифру (Y/N)? ')
        if answer in 'Yy':
            if self.cart.is_num_to_cart(num):
                self.cart.cross_out(num)
                return True
            else:
                return False
        else:
            if self.cart.is_num_to_cart(num):
                return False
            else:
                return True


class Npc:

    def __init__(self):
        self.cart = Cart()
        self.name = f'Compucter {random.randint(1, 10)}'

    def step(self, num):
        print(self.cart)
        if self.cart.is_num_to_cart(num):
            self.cart.cross_out(num)
            print('Номер есть')
        else:
            print('Номера нет')
        return True


class Game:
    bag = list(range(1, 100))

    def __init__(self):
        self.player = None
        self.npc = None
        self.default = self.menu()
        self.loser = None
        self.winner = None

    def menu(self):
        menu = '1. Один игрок с компьютером\n2. 2 игрока\n3. 2 Компьютера\n4. Выход'
        print(menu)
        choise = input('Выберите пункт меню: ')
        while choise not in '1234':
            choise = input('Некорректный ввод. Введите номер пункта: ')
        if choise == '1':
            self.player = Person()
            self.npc = Npc()
        elif choise == '2':
            self.player = Person()
            self.npc = Person()
        elif choise == '3':
            self.player = Npc()
            self.npc = Npc()
        else:
            return True
        return False

    def play(self):
        step1, step2 = False, False
        num = random.sample(self.bag, k=1)
        print(f'Выпал бочонок: {num[0]}')
        self.bag.remove(num[0])
        print(f'Карточка {self.npc.name}:\n')
        self.npc.step(num[0])
        print(f'\nКарточка {self.player.name}:\n')
        self.player.step(num[0])
        while (self.player.cart.is_empty or self.npc.cart.is_empty):
            num = random.sample(self.bag, k=1)
            print(f'Выпал бочонок: {num[0]}')
            self.bag.remove(num[0])
            print(f'Карточка {self.npc.name}:\n')
            step1 = self.npc.step(num[0])
            print(f'\nКарточка {self.player.name}:\n')
            step2 = self.player.step(num[0])
            if not (step1 and step2 and len(self.bag)):
                break
        if self.player.cart.is_empty or not step1:
            self.winner = self.npc.name
            self.loser = self.player.name
        elif self.npc.cart.is_empty or not step2:
            self.loser = self.npc.name
            self.winner = self.player.name
        else:
            print('Игра закончена!')
            return
        print("🟢" * 11)
        print(f'Победитель: {self.winner}')
        print("🟢" * 11)
        print(f'{self.loser} сегодня не выиграл')


if __name__ == '__main__':
    game = Game()
    if not game.default:
        game.play()
