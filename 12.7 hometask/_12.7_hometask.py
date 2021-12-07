import time

# For loop control
run = True
# For unrepeating the entry 
entry_shown = False

# Time for sleep
delay = 0.001

# Dictionary of methods
methods = {
    1   : "append",
    2   : "extend",
    3   : "insert",
    4   : "remove",
    5   : "pop",
    6   : "count",
    7   : "reverse",
    8   : "clear",
    9   : "copy",
    10  : "index"
}

# Descritions of methods
descriptions = {
    "append"    : "Add element to end of the array",
    "extend"    : "Extends array, adding to the end all elements from another array",
    "insert"    : "Put element by index",
    "remove"    : "Remove first element from array which matches value",
    "pop"       : "Remove element by value and return it",
    "count"     : "Return count of elements which macthes value",
    "reverse"   : "Reverse all elemets of the array",
    "clear"     : "Remove all elements",
    "copy"      : "Return array with all elemets",
    "index"     : "Return index of element which matches value"
}

# Main loop
while run:
    # Entry
    if not entry_shown:
        for s in "\n\n\n\n\nWelcome to the grand arena of methods !\n\n":
            print(s, flush=True, end='')
            time.sleep(delay)
        # Show list of commands
        for s in "\nHere are some commands...\n":
            print(s, flush=True, end='')
            time.sleep(delay)
        for key in methods:
            for s in "\n"+str(key)+"\t"+methods[key]+"\t -> \t"+descriptions[methods[key]]:
                print(s, flush=True, end='')
                time.sleep(delay/10)
        entry_shown = True

    # Get response from user
    for s in "\nWrite index or name of the command to execute... ":
        print(s, flush=True, end='')
        time.sleep(delay)
    response = input().lower()

    command_index = 0

    # Check if
    if response.isdigit() and int(response) in methods:
        command_index = int(response)
    elif response in methods.values():
        command_index = list(methods.keys())[list(methods.values()).index(response)]
    else:
        for s in "\nPlease write correctly !":
            print(s, flush=True, end='')
            time.sleep(delay)
        continue

    a = ["a", "b", "c"]
    b = [1, 1, 2]

    if command_index == 1:
        # Title
        print("\nAppend\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = input("Write element to add : ")
        # Add new value in array
        a.append(value)
        # List output
        print("List a : ")
        print(a)
    elif command_index == 2:
        # Title
        print("\nExtend\n")
        # Lists input
        print("List a : ")
        print(a)
        print("List b : ")
        print(b)
        # Extend b to a
        a.extend(b)
        # List output
        print("List a : ")
        print(a)
    elif command_index == 3:
        # Title
        print("\nInsert\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = input("Write element to add : ")
        idx = int(input("Write index : "))
        # Insert value at index
        a.insert(idx, value)
        # List output
        print("List a : ")
        print(a)
    elif command_index == 4:
        # Title
        print("\nRemove\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = ""
        while value not in a:
            value = input("Write element to remove : ")
        # Remove element from array
        a.remove(value)
        # List output
        print("List a : ")
        print(a)
    elif command_index == 5:
        # Title
        print("\nPop\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = int(input("Write index of element to remove : "))
        # Remove element from array
        removed = a.pop(value)
        # Output
        print("Removed element : "+removed)
        # List output
        print("List a : ")
        print(a)
    elif command_index == 6:
        # Title
        print("\nCount\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = input("Write element to count  : ")
        # Return count
        print("Elements count : "+str(a.count(value)))
    elif command_index == 7:
        # Title
        print("\nReverse\n")
        # List input
        print("List a : ")
        print(a)
        # Reverse
        a.reverse()
        # List output
        print("Reversed list a : ")
        print(a)
    elif command_index == 8:
        # Title
        print("\nClear\n")
        # List input
        print("List a : ")
        print(a)
        # Clear the list
        a.clear()
        # List output
        print("Cleared list a : ")
        print(a)
    elif command_index == 9:
        # Title
        print("\nCopy\n")
        # List input
        print("List a : ")
        print(a)
        print("List b : ")
        print(b)
        # Copy b list
        a = b.copy()
        # List output
        print("List a : ")
        print(a)
    elif command_index == 10:
        # Title
        print("\nIndex\n")
        # List input
        print("List a : ")
        print(a)
        # Get value
        value = input("Write element : ")
        # Output
        print(str(a.index(value)))
