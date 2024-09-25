# Function to insert element at the bottom of the stack
def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    if len(stack) > 0:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

# Test the reverse function
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)

reverse_stack(stack)
print("Reversed Stack:", stack)
