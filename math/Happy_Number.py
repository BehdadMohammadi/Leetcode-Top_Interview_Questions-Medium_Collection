class Solution:
    
    def AddSquare(self, n: int):

            remaining = 0
            quotient = n
            count = 0

            while True:

                if quotient < 10:
                    count = count + quotient**2
                    break

                remaining = quotient%10
                quotient = quotient//10


                count = count + remaining**2

            return count
        
    def isHappy(self, n: int) -> bool:

        JustAList = [n]
        square_added = n

        while True:

            square_added = self.AddSquare(square_added)


            if square_added == 1:
                return True
                break
            else:

                if square_added in JustAList:
                    return False
                    break

                JustAList.append(square_added)
        
        
    
        
