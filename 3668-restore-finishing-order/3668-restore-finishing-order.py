class Solution(object):
    def recoverOrder(self, order, friends):
        friends=set(friends)
        final=[]
        for x in order:
            if x in friends:
                final.append(x)
        return final
        
        