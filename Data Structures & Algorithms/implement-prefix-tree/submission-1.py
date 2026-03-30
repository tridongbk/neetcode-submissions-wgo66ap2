class TrieNode:
    def __init__(self):
        # 1️⃣ children
        self.children = {}
        # 2️⃣ isEnd
        self.isEnd = False
        
class PrefixTree:
    def __init__(self):
        # 1️⃣ root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 2️⃣ bắt đầu từ root
        node = self.root

        # 3️⃣ loop qua từng ký tự
        for c in word:
            # 4️⃣ nếu chưa có child thì tạo
            if c not in node.children:
                node.children[c] = TrieNode()
            # 5️⃣ đi xuống node tiếp theo
            node = node.children[c]

        # 6️⃣ đánh dấu kết thúc từ
        node.isEnd = True

    def search(self, word: str) -> bool:
        # 7️⃣ bắt đầu từ root
        node = self.root

        # 8️⃣ loop từng ký tự
        for c in word:
            # 9️⃣ nếu không tồn tại → False
            if c not in node.children:
                return False
            # 🔟 đi tiếp
            node = node.children[c]

        # 11️⃣ check có phải word hoàn chỉnh không
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        # 12️⃣ bắt đầu từ root
        node = self.root

        # 13️⃣ loop từng ký tự
        for c in prefix:
            # 14️⃣ nếu không tồn tại → False
            if c not in node.children:
                return False
            # 15️⃣ đi tiếp
            node = node.children[c]

        # 16️⃣ chỉ cần tồn tại là True
        return True
        