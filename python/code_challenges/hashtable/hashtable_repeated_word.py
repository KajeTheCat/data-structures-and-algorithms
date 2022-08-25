try:
    from hashtable import Hashtable
except:
    from .hashtable import Hashtable


def first_repeated_word(string):
    punctuatuion = ".?,!][}{)($%&#@"
    temp = string
    for char in punctuatuion:
        temp = temp.replace(char , "")
    splitter = temp.split(" ")
    mid_list = []

    for item in splitter:
        if item != "":
            mid_list.append(item.replace("\n", ""))

    temp_list = Hashtable(1024)

    for words in mid_list:
        if temp_list.contains(words.lower()):
            return words.lower()
        else:
            temp_list._set(words.lower(), 1)

if __name__ == "__main__":

    string = """
    apple
    apple.apple-apple
    banana
    apple?apple
    banana
    """

    print(first_repeated_word(string))
