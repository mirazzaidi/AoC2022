from day07.classes import Directory, File


def create_filesystem(lines):
    root = Directory('/')
    current = root
    ls = False

    for line in lines:
        line_tokens = line.split()
        command = None
        if line_tokens[0] == '$':
            ls = False
            command = line_tokens[1]

        if command == 'cd':
            path = line.split()[2]

            if path == '/':
                current = root
            elif path == '..':
                current = current.parent
            else:
                for child in current.children:
                    if isinstance(child, Directory) and child.name == path:
                        current = child
                        break

        elif command == 'ls':
            ls = True

        elif ls == True:
            if line_tokens[0] == 'dir':
                name = line_tokens[1]
                current.add_child(Directory(name, current))
            else:
                name, size = line_tokens[1], line_tokens[0]
                current.add_child(File(name, int(size)))
    return root
