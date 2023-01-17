import enchant
dictionary = enchant.Dict("en_US")

import inflect
inflect = inflect.engine()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_len = len(alphabet)
caeser_max = 5 # 動かす最大値
now_percent = 0

def caeser_decode(word, move_array):
    if(len(word) != len(move_array)):
        raise Exception("Error")
    
    result = ""
    for index, element in enumerate(move_array):
        word_index = alphabet.find(word[index])
        word_index = (word_index + alphabet_len + element) % alphabet_len
        result += alphabet[word_index]

    # パーセント表示
    all = (caeser_max * 2) ** len(word)
    now = 0
    for i in range(len(word)):
        now += (5 + move_array[i]) * (10 ** (len(word) - i - 1))
    percent = round(now * 100 / all)

    global now_percent
    if(percent != now_percent):
        now_percent = percent
        print(str(now_percent) + "%")

    return result


def main():
    input_word = "pewx" #"yttq" # tool になるはず
    result = {}

    def check(input_word, move_array, check_place):
        # 配列のコピー
        copied_array = []
        for element in move_array:
            copied_array.append(element)

        # 一番右の文字を変える時
        if(len(input_word) == check_place + 1):
            for i in range(-caeser_max, caeser_max):
                new_moved_array = []
                distance = 0
                for element in copied_array:
                    new_moved_array.append(element)
                    distance += element
                new_moved_array.append(i)

                decoded_word = caeser_decode(input_word, new_moved_array)
                if(dictionary.check(decoded_word)):
                    if(inflect.singular_noun(decoded_word) == False):
                        result[decoded_word] = distance

        # それ以外の時
        else:
            for i in range(-caeser_max, caeser_max):
                new_moved_array = []
                for element in copied_array:
                    new_moved_array.append(element)
                new_moved_array.append(i)

                check(input_word, new_moved_array, check_place + 1)                    

    check(input_word, [], 0)
    print(sorted(result.items(), key=lambda x:x[1]))

if __name__ == "__main__":
    main()