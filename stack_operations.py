# Using a list to act as a stack
stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} to stack.")

def pop():
    if not is_empty():
        removed = stack.pop()
        print(f"Popped {removed} from stack.")
        return removed
    else:
        print("Stack is empty. Cannot pop.")
        return None

def peek():
    if not is_empty():
        print(f"Top of stack is {stack[-1]}")
        return stack[-1]
    else:
        print("Stack is empty. No top element.")
        return None

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

def clear():
    stack.clear()
    print("Stack cleared.")

def search(target):
    if target in stack:
        position = stack.index(target) + 1  # 1-based index from bottom
        print(f"Element {target} found at position {position} from bottom.")
        return position
    else:
        print(f"Element {target} not found in stack.")
        return -1

# Example usage
push(10)
push(20)
push(30)

peek()                 # Shows top element
pop()                  # Removes top (30)
print("Stack size:", size())    # Size = 2
search(10)             # Position of 10
print("Is stack empty?", is_empty())  # False
clear()                # Empties the stack
print("Is stack empty now?", is_empty())  # True
