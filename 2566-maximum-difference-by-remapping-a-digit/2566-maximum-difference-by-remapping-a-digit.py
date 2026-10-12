class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str=str(num)
        max_digit=next((c for c in num_str if c!='9'),'9')
        max_val=int(num_str.replace(max_digit,'9'))
        min_digit=num_str[0]
        min_val=int(num_str.replace(min_digit,'0'))
        return max_val-min_val