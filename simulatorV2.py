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
        self.current_directory = self.root = Directory('/')

    def mkdir(self, name):
        self.current_directory.add_child(Directory(name))

    def touch(self, name):
        self.current_directory.add_child(File(name))

    def ls(self):
        return self.current_directory.list_children()

    def cd(self, directory):
        if directory == "..":
            if self.current_directory != self.root:
                self.current_directory = self.root
        else:
            child = self.current_directory.get_child(directory)
            if child and isinstance(child, Directory):
                self.current_directory = child

class File:
    def __init__(self, name):
        self.name = name


def main():
    fs = FileSystem()
    while True:
        command = input("$ ")
        if command.startswith("mkdir "):
            _, name = command.split(" ", 1)
            fs.mkdir(name)
        elif command.startswith("touch "):
            _, name = command.split(" ", 1)
            fs.touch(name)
        elif command == "ls":
            files = fs.ls()
            print("\n".join(files))
        elif command.startswith("cd "):
            _, directory = command.split(" ", 1)
            fs.cd(directory)
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()