class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                sec_val = stack.pop()
                first_val = stack.pop()

                if token == "+":
                    output = first_val + sec_val

                elif token == "-":
                    output = first_val - sec_val

                elif token == "*":
                    output = first_val * sec_val

                else:
                    output = int(first_val / sec_val)

                stack.append(output)

            else:
                stack.append(int(token))

        return stack[-1]
            