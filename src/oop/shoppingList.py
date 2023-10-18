from enum import Enum


class Cart:
    def __init__(self) -> None:
        self.items = dict()

    def add(self, item: str, amount: int):
        val = self.items.get(item)
        if val == None:
            self.items[item] = amount
        else:
            self.items[item] = val + amount

    def remove(self, item: str, amount: int):
        val = self.items.get(item)
        if val != None:
            if amount <= val:
                del self.items[item]
            else:
                self.items[item] = val - amount

    def remove_all(self) -> None:
        self.items = dict()


def main():
    cart: Cart = Cart()
    cart.add("Apple", 1)
    cart.add("Apple", 11)
    for k, v in cart.items.items():
        print(f"{k} : {v}")
    cart.remove("Apple", 4)
    for k, v in cart.items.items():
        print(f"{k} : {v}")
    cart.remove_all()


if __name__ == "__main__":
    main()
