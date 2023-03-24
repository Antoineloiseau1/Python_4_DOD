def square(x: int | float) -> int | float:
    """returns the x squared"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """returns x pow x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """declare an inner function and returns its return"""
    count = 0

    def inner() -> float:
        """apply function(x) on x"""
        inner.count += 1
        inner.x = function(inner.x)
        return (inner.x)

    inner.count = count
    inner.x = x
    return (inner)
