class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.content = ""
        self.children = {}


class Filesys:
    def __init__(self):
        self.root = Node("/")
    
    def _traverse(self, path):
        parts = [p for p in path.split("/") if p]
        node = self.root
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node
    
    def mkdir(self, path):
        parts = [p for p in path.split("/") if p]
        node = self.root

        for part in parts:
            if part not in node.children:
                node.children[part] = Node(part)
            node = node.children[part]

    def addFile(self, path, content):
        parts = [p for p in path.split("/") if p]
        filename = parts[-1]
        node = self.root
        for part in parts[:-1]:
            if part not in node.children:
                node.children[part] = Node(part)
            node = node.children[part]
        if filename not in node.children:
            node.children[filename] = Node(filename, is_file=True)
        node.children[filename].content = content
        
    def readFile(self, path):
        node = self._traverse(path)
        if node and node.is_file:
            return node.content
        return None

    def ls(self, path):
        node = self._traverse(path)
        if not Node:
            return []
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())
    
fs = Filesys()
fs.mkdir("/a/b")
fs.addFile("/a/b/c.txt", "hello world")
print(fs.ls("/"))          # ["a"]
print(fs.ls("/a"))         # ["b"]
print(fs.readFile("/a/b/c.txt"))  # "hello world"
