def mean(args):
    """calculate the mean of tuple args"""
    print("mean :", sum(args) / len(args))


def median(args):
    """calculate the median of tuple args"""
    args = sorted(args)
    size = len(args)
    middle = size // 2
    if size % 2 == 1:
        median = args[middle]
    else:
        median = (args[middle] + args[middle - 1]) / 2
    print("median :", median)


def quartile(args):
    """calculate the quartiles (0.25 and 0.75) of tuple args"""
    args = sorted(args)
    size = len(args)

    middle = size // 2
    # define the quarters
    if size % 2 == 1:
        lower_half = args[:middle + 1]
        higher_half = args[middle:]
    else:
        lower_half = args[:middle]
        higher_half = args[middle:]

    # calculate Q1:
    middle = len(lower_half) // 2
    if len(lower_half) % 2 == 1:
        Q1 = lower_half[middle]
    else:
        Q1 = float((lower_half[middle - 1] + lower_half[middle]) / 2)

    # calculate Q3:
    middle = len(higher_half) // 2
    if len(higher_half) % 2 == 1:
        Q3 = higher_half[middle]
    else:
        Q3 = float((higher_half[middle - 1] + higher_half[middle]) / 2)
    print(f"quartile : [{Q1:.1f}, {Q3:.1f}]")


def std(args):
    """calculate the standard deviation of tuple args"""
    n = len(args)
    mean = sum(args) / n
    var = sum([((i - mean) ** 2) for i in args]) / n
    dev = var ** 0.5
    print("std :", dev)


def var(args):
    """calculate the Variance of tuple args"""
    n = len(args)
    mean = sum(args) / n
    var = sum([((i - mean) ** 2) for i in args]) / n
    print("var :", var)


def error(args):
    """do absolutely nothing but pass"""
    pass


def ft_statistics(*args, **kwargs) -> None:
    """do statistics operations on the list of number passed in *args:
mean, median, quartile(0.25, 0.75), standard deviation and variance"""
    cases = {'mean': lambda args: mean(args),
             'median': lambda args: median(args),
             'quartile': lambda args: quartile(args),
             'std': lambda args: std(args),
             'var': lambda args: var(args)}
    for i in kwargs.values():
        if (len(args) == 0):
            print("ERROR")
            pass
        elif ([True for i in args if not isinstance(i, (int, float))]):
            print("ERROR")
            pass
        else:
            cases.get(i, lambda args: error(args))(args)
