class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        j = 1
        dict = {}

        while i < len(s):

            if  j == numRows + 1:
                j = j - 2
                while j >1 and i < len(s):
                    self.dict_generator(j,i,s,dict)
                    j =  j - 1
                    i = i + 1
                j = 1
            else:
                self.dict_generator(j,i, s, dict)
                j = j + 1
                i = i + 1


        return  self.dict_add(dict)

    def dict_generator(self, j, i, s,dict):
        if j in dict.keys():
            dict[j] = dict[j] + s[i]
        else:
            dict[j] = ""
            dict[j] = s[i]
    def dict_add(self,dict):
        str = ''
        for i in dict:
            str = str + dict[i]
        return str
        
