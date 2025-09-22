class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_final = 0
        number_final = 0

        while True:

            if len(nums) == 0:
                break

            number = nums[0]


            index = 0
            count = 0

            while True:


                if nums[index] == number:
                    count = count + 1
                    nums.pop(index)
                else:
                    index = index + 1

                if index + 1 > len(nums):
                    break

            if count > count_final:
                count_final = count
                number_final = number



        return number_final        
