import enchant
dictionary = enchant.Dict("en_US")

alphabet = "abcdefghijklmnopqrstuvwxyz"

word_length = 7
word_list = [0, 1, 2, 3, 0, 4, 5, 6, 3]


def check(num, left_alphabet, words):
    # 辞書チェック
    if num > word_length:
        result = ""
        for num in word_list:
            result += words[num]
        if (dictionary.check(result)):
            print(result)
        return

    # 次の文字を調べる
    for letter in left_alphabet:
        check(num + 1, left_alphabet.replace(letter, ""), words + letter)


print("Starting")
check(1, alphabet, "")
