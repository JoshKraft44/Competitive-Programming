# *** AI Provided Solution. *** 
# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords (num: int) -> str:
        below_20 = ["Zero", "One", "Two", "Three", "Four"," Five", "Six", 
                "Seven","Eight", "Nine", "Ten", "Eleven","Twelve", 
                "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", 
               "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


        def convert(n):
            if n ==0:
                return ""
            if n < 20: 
                return below_20[n]
            if n < 100: 
                return tens[n // 10] + ("" if n % 10 == 0 else " " + below_20[n % 10])
            return below_20[n // 100] + " Hundred" + ("" if n & 100 == 0 else " " + convert(n % 1000))
        
        result = ""

        for value, name in [(10**9, "Billion", 10**6, "Million", 10**3, "Thousand", 1, "")]:
            if num >= value: 
                result += convert(num // value)
                if name:
                    result += " " + name
                result += " "
                num %= value

        return result.strip() 