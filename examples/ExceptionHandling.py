# TypeError is thrown
# test_type_error : In Finally !
# Throwing back TypeError
def test_type_error():
    try:
        result = "foo" / 1

    except TypeError:
        print("TypeError is thrown")
        return "Throwing back TypeError"

    finally:
        print("test_type_error : In Finally !")


# ZeroDivisionError is thrown
# test_zero_division_error : In Finally !
# Throwing back ZeroDivisionError
def test_zero_division_error():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError is thrown")
        return "Throwing back ZeroDivisionError"
    finally:
        print("test_zero_division_error : In Finally !")


# Exception is thrown
# test_exception : In Finally !
# Throwing back Exception
def test_exception(items):
    try:
        items.pop()
    except Exception:
        print("Exception is thrown")
        return "Throwing back Exception"
    finally:
        print("test_exception : In Finally !")


# In try no exception thrown
# In try else !
# test_try_else: In finally !
# Giving back control
def test_try_else():
    try:
        # If return statement present in "try" the "try else" part won't execute
        print("In try no exception thrown")
    except TypeError:
        print("TypeError is thrown")

    else:
        print("In try else !")
        return "Giving back control"
    finally:
        print("test_try_else: In finally !")


# TypeError is thrown
# test_raise_exception : In Finally !
# Raise TypeError

def test_raise_exception():
    try:
        result = "foo" / 1
    except TypeError:
        print("TypeError is thrown")
        raise TypeError("Raise TypeError")

    finally:
        print("test_raise_exception : In Finally !")


print("*******TypeError*******")
print(test_type_error())
print()
print("*******ZeroDivisionError*******")
print(test_zero_division_error())
print()
print("*******Exception*******")
print(test_exception((1, 2, 3)))
print()
print("*******TryElse*******")
print(test_try_else())
print()
print("*******Raise*******")
try:
    test_raise_exception()
except TypeError as e:
    print(e)
