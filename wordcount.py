"""Word count solution"""
def words(argument):
    """Counts the occurrences or characters in a word"""
    if isinstance(argument, str):
        wordcount = {}
        for word in argument.split():
            if word in wordcount.keys():
                if word == int:
                    wordcount[word] += 1
                else:
                    wordcount[word] += 1
            else:
                if word.isdigit():
                    word = int(word)
                    wordcount[word] = 1
                else:
                    wordcount[word] = 1
        return wordcount
    else:
        return "please enter a string"