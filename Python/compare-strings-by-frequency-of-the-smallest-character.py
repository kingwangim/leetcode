import pdb
class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        f_queries = [] 
        f_words = []
        res = []
        for query in queries:
            query_list = list(query)
            query_list.sort()
            n = len([index for (index, value) in enumerate(query_list) if value == query_list[0]])
            f_queries.append(n)
        for word in words:
            word_list = list(word)
            word_list.sort()
            n = len([index for (index, value) in enumerate(word_list) if value == word_list[0]])
            f_words.append(n)
        for fq in f_queries:
            ans = 0
            for fw in f_words:
                if fq < fw:
                    ans += 1
            res.append(ans)
        return res
queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(Solution().numSmallerByFrequency(queries, words))