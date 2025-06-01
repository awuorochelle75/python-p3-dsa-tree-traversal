class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id_to_find):
        def dfs(node):
            if node is None:
                return None
            if node.get('id') == id_to_find:
                return node
            for child in node.get('children', []):
                found = dfs(child)
                if found:
                    return found
            return None

        return dfs(self.root)
