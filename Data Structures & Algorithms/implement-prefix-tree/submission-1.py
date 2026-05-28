class TreeNode:
    def __init__(self):
        self.val = None
        self.children = {}
       

class PrefixTree:

    def __init__(self):
        self.trie = TreeNode()
        

    def insert(self, word: str) -> None:
        temp = self.trie
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TreeNode()
            temp = temp.children[ch]
        temp.val = word         



    def search(self, word: str) -> bool:
        temp = self.trie
        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                return False
        return temp.val == word               
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for ch in prefix:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                return False
        return True            
        
        