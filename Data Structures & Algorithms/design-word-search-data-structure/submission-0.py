class TreeNode:
    def __init__(self):
        self.is_valid = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TreeNode()
        

    def addWord(self, word: str) -> None:
        temp = self.trie
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TreeNode()
            temp = temp.children[ch]
        temp.is_valid = True        
        

    def search(self, word: str) -> bool:

        def dfs(idx, root: TreeNode):
            node = root
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == '.':
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False        
                else:
                    if ch not in node.children:
                        return False
                    node = node.children[ch]
            return node.is_valid            


        return dfs(0, self.trie)


              
        
