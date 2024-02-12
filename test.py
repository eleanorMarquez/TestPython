class Node:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

class FileSystem:
    def __init__(self):
        self.root = Node("/", is_directory=True)
        self.current_directory = self.root

    def ls(self):
        for child in self.current_directory.children:
            print(child.name)

    def mkdir(self, name):
        new_directory = Node(name, is_directory=True)
        self.current_directory.add_child(new_directory)

    def cd(self, name):
        if name == "..":
            if self.current_directory != self.root:
                self.current_directory = self._get_parent_directory(self.current_directory)
        else:
            child = self.current_directory.get_child(name)
            if child and child.is_directory:
                self.current_directory = child
            else:
                print("Directory not found.")

    def touch(self, name):
        new_file = Node(name)
        self.current_directory.add_child(new_file)

    def _get_parent_directory(self, directory):
        current_dir = self.root
        for child in self.root.children:
            if child == directory:
                return current_dir
            current_dir = child
        return None

# Example usage:
fs = FileSystem()
fs.mkdir("documents")
fs.cd("documents")
fs.touch("file1.txt")
fs.touch("file2.txt")
fs.mkdir("images")
fs.ls()  # Should print "file1.txt" and "file2.txt"
fs.cd("..")
fs.ls()  # Should print "documents" and "images"