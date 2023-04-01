class Solution:
    def maskPII(self, s: str) -> str:
        res = ""
        r = ["(",")","-","+", " "]
        # 电话数字
        if "@" not in s:
            for i in r:
                s = s.replace(i, "")
            if len(s) == 10:
                return "***-***-"+s[-4:]
            elif len(s) == 11:
                return "+*-***-***-"+s[-4:]
            elif len(s) == 12:
                return "+**-***-***-"+s[-4:]
            else:
                return "+***-***-***-"+s[-4:]
        # 邮箱
        else:
            name = s[:s.index("@")]
            return (name[0]+"*****"+name[-1]+s[s.index("@"):]).lower()

s = "(3906)2 07143 711"
print(Solution().maskPII(s))