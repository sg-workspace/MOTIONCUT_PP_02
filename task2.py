import time

def word_count(text):
    #Function to count the number of words in the input text.
    if not text.strip():
        return 0  # Return 0 if the input is empty or contains only whitespace
    return len(text.split())

def display_intro():
    #Display an introduction to the Word Counter program.
    print("\nWelcome to Word Counter!")
    print("This program counts the number of words in a sentence or paragraph.")
    print("Let's get started!\n")

def get_user_input():
    #Prompt the user to enter a sentence or paragraph.
    print("Please enter your sentence or paragraph:")
    user_input = input("> ")  # Prompt the user to enter input
    return user_input

def display_word_count(count):
    #Display the word count to the user.
    print(f"\nYour text contains {count} words.")

def display_thank_you():
    #Display a thank you message and simulate loading animation.
    print("\nThank you for using Word Counter!")
    print("Exiting the program...")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(1)  # Wait for 1 second
    print("\nGoodbye!")

def main():
    #Main function to implement the Word Counter program.
    display_intro()
    user_input = get_user_input()
    word_count_result = word_count(user_input)
    display_word_count(word_count_result)
    display_thank_you()

if __name__ == "__main__":
    main()
