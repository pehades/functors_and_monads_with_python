from functors.base_functor import Functor
from monads.base_monad import Monad
from typing import Generic, TypeVar, Callable


A = TypeVar("A")
B = TypeVar("B")


class Maybe(Monad, Functor, Generic[A]):
    pass


class Just(Maybe[A]):

    def __init__(self, val: A):
        self.val = val

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return Just(new_val)
        except Exception as e:
            return Nothing()

    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return new_val
        except Exception as e:
            return Nothing()

    def __str__(self):
        return f"Just({self.val})"

    def __repr__(self):
        return self.__str__()


class Nothing(Maybe[A]):

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        return self

    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        return self

    def __str__(self):
        return "Nothing"

    def __repr__(self):
        return self.__str__()