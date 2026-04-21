"""
工厂方法模式（Factory Method）- Python 最小可运行示例。
场景：披萨店将“创建披萨”的变化点下放给不同门店（纽约店/芝加哥店）。
运行: python3 pizza_store.py
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def prepare(self) -> None:
        print(f"Preparing {self.name}")

    def bake(self) -> None:
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official box")


class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__("NY Style Sauce and Cheese Pizza")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        super().__init__("Chicago Deep Dish Cheese Pizza")

    def cut(self) -> None:
        print("Cutting the pizza into square slices")


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)

        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        raise NotImplementedError


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        raise ValueError(f"Unknown NY pizza type: {pizza_type}")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        raise ValueError(f"Unknown Chicago pizza type: {pizza_type}")


def main() -> None:
    ny_store: PizzaStore = NYPizzaStore()
    chicago_store: PizzaStore = ChicagoPizzaStore()

    ny_pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {ny_pizza.name}\n")

    chicago_pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {chicago_pizza.name}")


if __name__ == "__main__":
    main()
