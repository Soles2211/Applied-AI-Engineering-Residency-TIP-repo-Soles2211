#Problem 1

"""
Javascript:
const runningSum = (nums) => {
    let sums = [];
    let sum = nums[0];
    sums.push(sum);
    for (let i=0; i < nums.length - 1; i++) {
    	sum = sum + nums[i + 1];
    	sums.push(sum);
    }
    return sums;
};
"""

def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sum = nums[0]
        sums.append(sum)
        for num in range(len(nums) - 1):
            sum = sum + nums[num + 1]
            sums.append(sum)
        return sums

#Problem 2

"""
var maxVowels = function(s, k) {
    let count = 0;
    for (let i = 0; i <= s.length; i++) {
        if (s.length - i < k) {
            break
        }
        if (s[i] = s[i])
    }
};
"""