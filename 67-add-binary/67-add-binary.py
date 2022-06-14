class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binaryToDecimal(n):
            return int(n,2)
        def decimalToBinary(n):
            return bin(n).replace("0b","")
        return(str(decimalToBinary(binaryToDecimal(a) + binaryToDecimal(b))))