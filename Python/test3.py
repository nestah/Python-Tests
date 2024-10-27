# write a python program to find common letters between 2 strings
def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # create a set to only include unique letter
    s1 = set(str1)
    s2 = set(str2)

    # use & to extract the common letter from the sets
    common = s1 & s2
    print(common)
common_letters()
