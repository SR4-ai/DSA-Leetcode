class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sq_nums = list(map(lambda x:x**2,nums))
        neg=[]
        pos=[]
        res =[]
        for i in range(len(nums)):
            if(nums[i]>=0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        if(len(pos)==0):
            return [x * x for x in neg][::-1]

        if(len(neg)==0):
            return [x * x for x in pos]
        
        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]
        n,m = len(neg),len(pos)
        i = 0
        j= 0
        
        while(i<n and j<m):
            if(neg[i] <= pos[j]):
                res.append(neg[i])
                
                i+=1
            else:
                res.append(pos[j])
            
                j+=1

        while(j<m):
            res.append(pos[j])
        
            j+=1
        while(i<n):
            res.append(neg[i])
          
            i+=1

        return res