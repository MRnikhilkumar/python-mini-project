import time
import random
sentences = ["The quick brown fox jumps over the lazy dog.",
                "Python is a great programming language.",
                "Typing speed tests are fun and challenging.",
                "Practice makes perfect when it comes to typing.",
                "The rain in Spain stays mainly in the plain."
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for u, t in zip(user_input, test_sentence) if u == t)
    accuracy = (correct_chars / len(test_sentence)) * 100
    return accuracy


def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("\nstart typing here: \n")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_in_minutes = time_taken / 60
    words_typed = len(user_input.split())

    print("results:")
    print(f"Time taken: {time_taken}seconds")
    print(f"Words typed: {words_typed}")
    print(f"Typing speed: {words_typed / (time_taken/60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")
  

   
typing_test()