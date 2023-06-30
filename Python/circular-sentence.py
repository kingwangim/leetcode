import pdb
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words, word = [], ""
        sentence += " "
        for i in sentence:
            if i != " ":
                word += i
            else:
                words.append(word)
                word = ""
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                pdb.set_trace()
                return False
        if words[-1][-1] != words[0][0]:
            pdb.set_trace()
            return False
        return True

sentence = "leetcode exercises sound delightful"
print(Solution().isCircularSentence(sentence))  