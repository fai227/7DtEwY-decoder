import inflect
import enchant
dictionary = enchant.Dict("en_US")

inflect = inflect.engine()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_len = len(alphabet)
caeser_max = 7  # 動かす最大値


def caeser_decode(word, move_array):
    if (len(word) != len(move_array)):
        raise Exception("Error")

    result = ""
    for index, element in enumerate(move_array):
        word_index = alphabet.find(word[index])
        word_index = (word_index + alphabet_len + element) % alphabet_len
        result += alphabet[word_index]

    # 進捗表示

    return result


def main():
    input_word = "ymje"  # "pewx" #"yttq" # tool になるはず
    result = {}

    def check(input_word, move_array, check_place):
        # 配列のコピー
        copied_array = []
        for element in move_array:
            copied_array.append(element)

        # 一番右の文字を変える時
        if (len(input_word) == check_place + 1):
            for i in range(-caeser_max, caeser_max):
                new_moved_array = []
                distance = 0
                for element in copied_array:
                    new_moved_array.append(element)
                    distance += abs(element)
                new_moved_array.append(i)

                decoded_word = caeser_decode(input_word, new_moved_array)
                if (dictionary.check(decoded_word)):
                    if (inflect.singular_noun(decoded_word) == False):
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
    print(sorted(result.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    main()
