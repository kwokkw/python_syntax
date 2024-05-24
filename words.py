def print_upper_words(words, must_start_with = {"h", "y"}):

    """ Given a list of words and a set of letters, print out words all in uppercase that start with one of those letters.
    """

    for w in words:
        if w[0] in must_start_with:
            upper_w = w.upper()
            print(upper_w)
    return

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"g"})
