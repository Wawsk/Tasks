# Start of the while loop.
while True:
    # Print the start message.
    print("Enter your text or 'exit' to clost the program")
    # Collect user input into a variable.
    text = (input(">>> "))
    # Create a way to exit the loop.
    if text == "exit":
        break
    # Print out user input
    print(text)
