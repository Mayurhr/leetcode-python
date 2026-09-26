class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r=round((purchaseAmount/10)+0.001)*10
        return 100-r