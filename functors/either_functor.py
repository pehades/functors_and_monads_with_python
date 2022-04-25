from functors.base_functor import Functor
from typing import Generic, TypeVar, Callable

A = TypeVar("A")
B = TypeVar("B")


class Either(Functor, Generic[A]):
    pass


class Right(Either[A]):

    def __init__(self, val: A):
        self.val = val

    def fmap(self, func: Callable[[A], B]) -> Either[B]:
        try:
            new_val = func(self.val)
            return Right(new_val)
        except Exception as e:
            return Left(e.args[0])

    def __str__(self):
        return f"Right({self.val})"

    def __repr__(self):
        return self.__str__()


class Left(Either[str]):

    def __init__(self, exc: str):
        self.exc = exc

    def fmap(self, func: Callable[[A], B]) -> Either[str]:
        return Left(self.exc)

    def __str__(self):
        return f"Left({self.exc})"

    def __repr__(self):
        return self.__str__()
