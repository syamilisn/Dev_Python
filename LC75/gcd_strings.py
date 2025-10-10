class Solution:
    def numOfPattern(self, s1: str) -> int:
        self.count = 0
        self.pattern=self.getStringPattern(s1)
        self.leng_pattern = len(self.pattern)
        for i in range(len(s1)):
            if s1[i:i + self.leng_pattern] == self.pattern:
                # print(f"i={i} s1[i:self.leng_pattern]={s1[i:self.leng_pattern]} pattern={self.pattern}")
                self.count += 1
        # print(f"pattern={self.pattern}, count={self.count} len_pattern={self.leng_pattern}")
        return self.count
    def getStringPattern(self, s1: str) -> str:
        n = len(s1)
        x = len(set(s1))
        for i in range(1,n):
            if n == x:
                return s1
            if s1[i] == s1[0]:
                return s1[:i]
                return ""
        return s1[0:x]
    def temp(self, s1: str, s2: str) -> str:
        print(f"s1={self.getStringPattern(s1)}, s2={self.getStringPattern(s2)}")
        if self.getStringPattern(s1) == self.getStringPattern(s2):
            if(self.numOfPattern(s1) == self.numOfPattern(s2)):
                return self.getStringPattern(s2)
            else:
                return self.getStringPattern(s2)*self.numOfPattern(s2)
        else:
            return "emptemp"
    def temp2(self, s1: str, s2: str) -> str:
        x=self.numOfPattern(s1)
        y=self.numOfPattern(s2)
        if self.getStringPattern(s1) != self.getStringPattern(s2):
            return ""
        if x%y == 0:
            return s2
        else:
            return self.getStringPattern(s2)
        
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        str1, str2 = s1, s2
        if(len(s2) > len(s1)):
            str1, str2 = str2, str1
        if set(str1) == set(str2):
            #start case1,case2
            for i in range(len(str1)):  #assume s1>s2
                if str1[i:len(str2)] == str2:
                    if(len(set(str2)) != len(str2)):
                        start = 0
                        for j in range(len(str2)):
                            if str2[:j] == str2[j:]:
                                print("here")
                                return str2[:j]
                    print("here2")
                    return str2
            #end case1,case2
            return(''.join(set(str1)))  #del
        return "emptygcd"  # ret empty
        

res = Solution()
print(f"pattern = {res.getStringPattern('ABCABC')}")  # ABC
print(f"pattern = {res.getStringPattern('ABABAB')}")  # AB
print(f"1. actual_rs = ABC     res={res.gcdOfStrings('ABCABC', 'ABC')} temp={res.temp2('ABCABC', 'ABC')}")        # ABCx2, ABCx1          s1 == s2
print(f"2. actual_rs = AB      res={res.gcdOfStrings('ABABAB', 'ABAB')} temp={res.temp2('ABABAB', 'ABAB')}")       # ABx3, ABx2            s1 == s2
print(f"3. actual_rs = 'empty' res={res.gcdOfStrings('ABCDEF', 'ABC')} temp={res.temp2('ABCDEF', 'ABC')}")        # ABCDEFx1, ABCx1       s1 != s2
print(f"4. actual_rs = 'empty' res={res.gcdOfStrings('LEET', 'CODE')} temp={res.temp2('LEET', 'CODE')}")         # LEETx1, CODEx1        s1 != s2
print(f"5. actual_rs = 'TAUXX' res={res.gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX')} temp={res.temp2('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX')}")        
print(f"6. actual_rs = 'TAUXX' res={res.gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXX')} temp={res.temp2('TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXX')}")         
print(f"7. actual_rs = ABAB     res={res.gcdOfStrings('ABABABAB', 'ABAB')} temp={res.temp2('ABABABAB', 'ABAB')}")        # ABCx2, ABCx1          s1 == s2