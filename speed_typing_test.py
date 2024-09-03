import time

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence:")
    print(text)
    input("Press Enter when you are ready.")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words = text.split()
    total_words = len(words)
    typed_words = user_input.strip().split()
    correct_words = 0

    for i in range(min(total_words, len(typed_words))):
        if words[i] == typed_words[i]:
            correct_words += 1

    accuracy = correct_words / total_words * 100
    words_per_minute = len(typed_words) / elapsed_time * 60

    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f}".format(words_per_minute))

speed_typing_test()
