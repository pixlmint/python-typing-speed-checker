import os
import time
import random
import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd


def get_poem_lines(num_lines=1):
    try:
        response = requests.get("https://poetrydb.org/random")
        if response.status_code == 200:
            poem = response.json()[0]
            lines = poem['lines']
            if len(lines) < num_lines:
                print("The poem doesn't have enough lines. Using available lines.")
                num_lines = len(lines)
            lines_to_return = random.sample(lines, num_lines)
        else:
            print("Could not fetch poem, using default sentence.")
            lines_to_return = ["The quick brown fox jumps over the lazy dog"] * num_lines
    except Exception as e:
        print(f"An error occurred: {e}")
        lines_to_return = ["The quick brown fox jumps over the lazy dog"] * num_lines
    return lines_to_return


def plot_stats():
    df = pd.read_csv('typing_stats.csv')

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.title('Time Taken for Each Attempt')
    plt.xlabel('Attempt')
    plt.ylabel('Time Taken (s)')
    plt.plot(df['Time Taken'], marker='o')

    plt.subplot(1, 2, 2)
    plt.title('Words Per Minute for Each Attempt')
    plt.xlabel('Attempt')
    plt.ylabel('WPM')
    plt.plot(df['WPM'], marker='o')

    plt.tight_layout()
    plt.show()


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def log_to_csv(time_taken, wpm, is_correct):
    file_exists = False
    try:
        with open('typing_stats.csv', 'r') as csvfile:
            file_exists = bool(len(csvfile.read()))
    except FileNotFoundError:
        pass

    with open('typing_stats.csv', 'a', newline='') as csvfile:
        fieldnames = ['Time Taken', 'WPM', 'Is Correct']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Time Taken': time_taken, 'WPM': wpm, 'Is Correct': is_correct})


def display_menu():
    print("\n--- Typing Speed Test Menu ---")
    print("1. Start a new test")
    print("2. Change the number of lines")
    print("3. Show statistics")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def count_words(lines):
    pass


def main():
    while True:
        print("Menu:")
        print("1. Start a new typing test")
        print("2. Change the number of lines to type")
        print("3. Show statistics")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            print("Typing speed test: Type the following line from a poem as fast as you can.")
            sentences = get_poem_lines()

            input("Press Enter when you are ready to start...")

            is_correct = True
            start_time = time.time()

            for i, sentence in enumerate(sentences, 1):
                clear_screen()
                print(f"{sentence}\n")
                typed_sentence = input("Now, type the line: ")

                if typed_sentence != sentence:
                    is_correct = False

            end_time = time.time()
            time_taken = end_time - start_time

            words = len(typed_sentence.split())
            wpm = (words / time_taken) * 60

            clear_screen()
            print(f"\n- Time taken: {time_taken:.2f} seconds\n- WPM: {wpm:.2f} WPM.")

            log_to_csv(time_taken, wpm, is_correct)

        elif choice == '2':
            # Code to change the number of lines (you'll need to implement this)
            pass
        elif choice == '3':
            plot_stats()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
