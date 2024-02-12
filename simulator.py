class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        self.children[child.name] = child

    def get_child(self, name):
        return self.children.get(name)

    def list_children(self):
        return list(self.children.keys())

class FileSystem:
    def __init__(self):
        self.root = Directory('/')

    def mkdir(self, path):
        current_dir = self.root
        for directory in path.split('/'):
            if directory:
                if directory not in current_dir.children:
                    new_dir = Directory(directory)
                    current_dir.add_child(new_dir)
                current_dir = current_dir.get_child(directory)

    def touch(self, path):
        current_dir = self.root
        components = path.split('/')
        filename = components[-1]
        parent_path = '/'.join(components[:-1])

        if parent_path:
            for directory in parent_path.split('/'):
                if directory:
                    current_dir = current_dir.get_child(directory)
        new_file = File(filename)
        current_dir.add_child(new_file)

    def ls(self, path):
        current_dir = self.root
        if path:
            for directory in path.split('/'):
                if directory:
                    current_dir = current_dir.get_child(directory)
        return current_dir.list_children()

    def cd(self, path):
        if path == "..":
            return "/".join(self.current_path.split("/")[:-1])
        else:
            return self.current_path + "/" + path


class File:
    def __init__(self, name):
        self.name = name


def main():
    fs = FileSystem()
    while True:
        command = input("$ ")
        if command.startswith("mkdir"):
            _, path = command.split()
            fs.mkdir(path)
        elif command.startswith("touch"):
            _, path = command.split()
            fs.touch(path)
        elif command.startswith("ls"):
            _, path = command.split()
            files = fs.ls(path)
            print("\n".join(files))
        elif command.startswith("cd"):
            _, path = command.split()
            new_path = fs.cd(path)
            print(f"Current directory: {new_path}")
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()