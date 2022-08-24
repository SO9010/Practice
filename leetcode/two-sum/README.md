<h1>Two Sum</h1>
<h5>Easy</h5>
 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

<h3>Solution walkthrough:</h3>
   
I knew for this, I knew i would need to have nested search algorithms. I chose the linear search algorith. Even though this may not be the most efficient for big arrays it does the job well enough for smaller ones. Furthermore, it will save memory and time as we dont have to reorder it.
    
<h3>Example 1:</h3>

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

<h3>Example 2:</h3>

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

<h3>Example 3:</h3>

    Input: nums = [3,3], target = 6
    Output: [0,1]

 

<h3>Constraints:</h3>

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

