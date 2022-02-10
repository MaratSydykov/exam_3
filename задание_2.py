class Lemonade:
    def __init__(self, add='oбычная газировка'):
        self.add = add

    def drink_info(self):
        if self.add == 'Обычная газировка' or self.add == '':
            return ('oбычная газировка')
        else:
            return(f'Газировка и {self.add}')

lemonade = Lemonade('апельсин')
print(lemonade.drink_info())