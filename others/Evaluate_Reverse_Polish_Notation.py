class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        if len(tokens) == 1:
            int(tokens[0])


        index = 0

        while True:


            if tokens[index + 2] == "+":

                tokens[index] = str(int(tokens[index]) + int(tokens[index+1]))

                tokens.pop(index+1)
                tokens.pop(index+1)

                index = 0

                if len(tokens) == 1:
                    break

                continue


            if tokens[index + 2] == "-":

                tokens[index] = str(int(tokens[index]) - int(tokens[index+1]))

                tokens.pop(index+1)
                tokens.pop(index+1)

                index = 0

                if len(tokens) == 1:
                    break

                continue

            if tokens[index + 2] == "*":

                tokens[index] = str(int(tokens[index]) * int(tokens[index+1]))

                tokens.pop(index+1)
                tokens.pop(index+1)

                index = 0

                if len(tokens) == 1:
                    break

                continue

            if tokens[index + 2] == "/":

                if int(tokens[index]) < 0 or int(tokens[index+1]) < 0:

                    tokens[index] = math.floor(abs(int(tokens[index]) / int(tokens[index+1])))*-1


                else:
                    tokens[index] = str(int(tokens[index]) // int(tokens[index+1]))

                tokens.pop(index+1)
                tokens.pop(index+1)

                index = 0

                if len(tokens) == 1:
                    break

                continue


            index = index + 1



        return int(tokens[0])
    


        
