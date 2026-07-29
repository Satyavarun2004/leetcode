class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_sum=0
        left=0
        right=len(height)-1
        while left<=right:
            l=min(height[left],height[right])
            b=right-left
            area=l*b
            max_sum=max(max_sum,area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_sum

        
        