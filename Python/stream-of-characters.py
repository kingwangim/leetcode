import pdb

class StreamChecker:
    def __init__(self, words: List[str]):
        self.se=set(words)
        self.maxn=max(len(word) for word in words)
        self.s=''

    def query(self, letter: str) -> bool:
        self.s+=letter
        for i in range(1,min(len(self.s)+1,self.maxn+1)):
            if self.s[-i:] in self.se:
                return True
        return False
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
