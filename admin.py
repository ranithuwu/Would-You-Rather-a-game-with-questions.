# Name: Ranithu Dinsara
# Student Number: 10635536
# Import the json module to allow us to read and write data in JSON format.
import json

# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        something = input(prompt).strip()
        if something:
            return something
        else:
            print("Invalid input. Please enter something other than whitespace.")

# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    try:
        with open("data.txt", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Something went wrong while saving data: {e}")

def display_question(question):
    print(f"Option 1: {question['option_1']}")
    print(f"Option 2: {question['option_2']}")
    print(f"Children: {'Yes' if question['children'] else 'No'}")
    print(f"Votes for Option 1: {question['votes_1']} {'vote' if question['votes_1'] == 1 else 'votes'}")
    print(f"Votes for Option 2: {question['votes_2']} {'vote' if question['votes_2'] == 1 else 'votes'}")
    print(f"Likes: {question['likes']} {'vote' if question['likes'] == 1 else 'votes'}")
    print(f"Dislikes: {question['dislikes']} {'vote' if question['dislikes'] == 1 else 'votes'}")
    if question["votes_1"] + question["votes_2"] > 0:
        percentage = (question["votes_1"] / (question["votes_1"] + question["votes_2"])) * 100
        print(f"Percentage: {percentage:.1f}%")
        if 50 <= percentage <= 60:
            print("This question is divisive!")

def add_question(data):
    print("Both options should be phrased to follow 'Would you rather...'")
    option_1 = input_something("Option 01:- ")
    option_2 = input_something("Option 02:- ")
    while True:
        children = input_something("Is this question appropriate for children? [Y/N]: ").lower()
        if children == "y":
            children = True
            break
        elif children == "n":
            children = False
            break
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
    question = {
        "option_1": option_1,
        "option_2": option_2,
        "children": children,
        "votes_1": 0,
        "votes_2": 0,
        "likes": 0,
        "dislikes": 0,
    }
    data.append(question)
    save_data(data)
    print("Question added.")

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
def load(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data

FILENAME = "data.txt"
data = load(FILENAME)

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Would You Rather" Admin Program.')
while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, or [q]uit.")
    choice = input("> ").lower() # Convert input to lowercase to make choice selection case-insensitive.
    if choice == "a":
        # Add a new question.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        add_question(data)
    elif choice == "l":
        # List the current questions.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No questions saved.")
        else:
            print("List of questions:")
            for index, question in enumerate(data, start=1):
                print(f"{index}: {question['option_1']} / {question['option_2']}")
    elif choice == "s":
        # Search the current questions.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No questions saved.")
        else:
            search_keywords = input_something("Enter search keywords: ").lower()
            found = False
            print("Search results:")
            for index, question in enumerate(data, start=1):
                if (search_keywords in question["option_1"].lower()
                        or search_keywords in question["option_2"].lower()):
                    print(f"{index}: {question['option_1']} / {question['option_2']}")
                    found = True
            if not found:
                print("No results found.")
    elif choice == "v":
        # View a question.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No questions saved.")
        else:
            index_to_view = input_int("Enter the index number of the question you want to view: ")
            if 1 <= index_to_view <= len(data):
                question_to_view = data[index_to_view - 1]
                display_question(question_to_view)
            else:
                print("Invalid index number.")
    elif choice == "d":
        # Delete a question.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No questions saved.")
        else:
            index_to_delete = input_int("Enter the index number of the question you want to delete: ")
            if 1 <= index_to_delete <= len(data):
                del data[index_to_delete - 1]
                save_data(data)  # Save the updated data after deleting the question
                print("Question deleted successfully!")
            else:
                print("Invalid index number.")
    elif choice == "q":
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break
    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice. Please choose from [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, or [q]uit.")
