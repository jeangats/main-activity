# Store the data associated with each element and maintains links between the nodes to implement the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# To enable the program to push characters of the input data into the stack and later pop them in reverse order to compare with the original sentence---determining whether data a palindrome or not.
class Stack:
    def __init__(self):
        self.top = None

    # Adds element to the top of stack, it then creates a new node with that data
    def push(self, data):
        new = Node(data)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    # Removes topmost element from the stack
    # Used a temporary variable temp to point to the current top node and updates the top attribute of the stack to point to the next node
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_element = self.top.data
            temp = self.top
            self.top = temp.next
            temp.next = None
            return popped_element

# Checks if each single character of the data is from the range of a to z and range of numbers 0 to 9
# This allowed me to learn how to manually check alphanumeric instead of using built in functions such as isalpha()
def isAlphanumeric(char):
    return (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9')


def palindromeChecker(data):
    if not data:
        print("Please enter the word/sentence first. We are unable to check an empty input as a palindrome.")
        return False

    # converts the uppercase letters into lowercase for the palindrome checker to ignore capitalization
    # Checks and stores each character of the inputted data if it contains only letters and/or numbers
    # removes the spacing and punctuations before adding into stack
    data = data.lower()
    cleaned_data = ''.join(char for char in data if isAlphanumeric(char))
    stack = Stack()

    # Push each character of the cleaned data (with only letters and numbers) onto the stack
    for char in cleaned_data:
        stack.push(char)

    reversed_data = []
    # Removing elements one by one from the stack and append them to the a list serving as a reversed order of the data
    while not stack.top is None:
        reversed_data.append(stack.pop())

    # Compare the original data to the reversed data to see if it is equal and determine if it is a palindrome or not
    is_palindrome = cleaned_data == ''.join(reversed_data)

    print("-"*65)
    print(f"| Original data: {data} |")
    print(f"| Filtered data: {cleaned_data} |")

    return is_palindrome

def display():
    print("="*65 + "\n\t\t\t\t\tPALINDROME CHECKER")
    while (True):
        menu_option = int(input("-"*65 + "\n\nChoose from options [1 - Check a word/sentence] or [2 - Exit]: "))
        if menu_option == 1:
            data = input("Enter a word/sentence: ")
            is_palindrome = palindromeChecker(data)
            if is_palindrome:
                print(f"\t-> The word/sentence '{data}' IS a palindrome as it reads the same forward and backward, ignoring spaces, punctuation and capitalization.")
            else:
                print(f"\t-> The word/sentence '{data}' IS NOT a palindrome as it does not read the same forward and backward.")
        elif menu_option == 2:
            confirm = input("Are you sure you are done using Palindrome Checker (Y - Yes\tN - No): ").upper()
            if confirm == 'Y':
                print("Exiting Palindrome Checker...")
                print("="*65)
                break
            elif confirm == 'N':
                continue
            else:
                print("Please Try Again. The options in the menu are only 'Y' or 'N'")
        else:
            print("\nPlease Try Again... The options in the menu are only 1 or 2.")

display()

