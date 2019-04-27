# establishes formatter variable, which can passed through to .format which will line up the following variables with the {}
formatter = "{} {} {} {}"

# prints text; passes through to format function to fill the brackets -{}- in variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

# similar to above print format functions but allows you to use multiple lines
print(formatter.format(
    "The quick",
    "brown fox",
    "jumps over",
    "the lazy dog"
))
