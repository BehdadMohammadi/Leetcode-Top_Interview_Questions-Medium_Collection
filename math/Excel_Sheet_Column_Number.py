class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
      
        index = len(columnTitle) - 1
        count = 0

        for i in columnTitle:
            count = count + (ord(i)-64)*26**index
            index = index - 1

        return count
