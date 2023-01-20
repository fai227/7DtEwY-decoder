import inflect
import enchant
dictionary = enchant.Dict("en_US")

alphabet = "abcdefghijklmnopqrstuvwxyz"

for first in alphabet:
    for second in alphabet:
        for third in alphabet:
            for fourth in alphabet:
                for fifth in alphabet:
                    for sixth in alphabet:
                        for seventh in alphabet:
                            word = first + second + third + fourth + first + sixth + seventh + fourth
                            if (dictionary.check(word)):
                                if (inflect.singular_noun(word) == False):
                                    print(word)
