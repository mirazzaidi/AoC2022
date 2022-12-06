input_str = open('day-5/input.txt').read()
parts = input_str.strip().split('\n')

stacks = parts[0].split()
print(stacks)
steps = [[int(x) for x in step.split()] for step in parts[1:]]

for step in steps:
    from_stack, to_stack, num_crates = step

    # Move the crates one at a time from the source to the destination stack
    for _ in range(num_crates):
        # Get the crate to move
        crate = stacks[from_stack - 1][-1]

        # Remove the crate from the source stack
        stacks[from_stack - 1] = stacks[from_stack - 1][:-1]

        # Add the crate to the destination stack
        stacks[to_stack - 1] += crate

# Get the top crate from each stack
top_crates = [stack[-1] for stack in stacks]

# Combine the top crates to get the answer
answer = ''.join(top_crates)
