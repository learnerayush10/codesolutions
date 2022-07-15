

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        #Code here
        dict1={}
        temp_ar=nums.copy()
        swap=0
        n=len(nums)
        for i in range(n):
            dict1[nums[i]]=i
        temp_ar.sort()
        init=0
        for j in range(n):
            if nums[j]!=temp_ar[j]:
                swap+=1
                init=nums[j]
                nums[j],nums[dict1[temp_ar[j]]]=nums[dict1[temp_ar[j]]],nums[j]
                dict1[init]=dict1[temp_ar[j]]
                dict1[temp_ar[j]]=j
        return swap

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends