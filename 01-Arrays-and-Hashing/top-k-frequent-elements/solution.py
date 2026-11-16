def topKFrequent(nums, k):
        l=[]
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in sorted(freq,key=freq.get,reverse=True):
            l.append(num)
        return l[:k]
nums=[1,2,2,3,3,3]
k=2
print(topKFrequent(nums,k))is this correct
