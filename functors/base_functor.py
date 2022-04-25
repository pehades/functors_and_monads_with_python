from typing import Generic, TypeVar, Callable

A = TypeVar("A")
B = TypeVar("B")


class Functor(Generic[A]):

    def fmap(self, func: Callable[[A], B]):
        pass

    def __or__(self, other):
        return self.fmap(other)