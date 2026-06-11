def greet(name):
    return "Hello, " + name + "!"


def week_message(week):
    return "You are on week " + str(week) + " of 12."


# Test cases
assert greet("Sofiya") == "Hello, Sofiya!"
assert week_message(0) == "You are on week 0 of 12."
assert week_message(12) == "You are on week 12 of 12."

print("All tests passed.")
