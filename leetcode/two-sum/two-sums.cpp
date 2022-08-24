class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        for(int i = 0; i < nums.size(); i++){
            for(int sI = i + 1; sI < nums.size(); sI++){
                if(nums[i] + nums[sI] == target){
                    answer = {i, sI};
                }
            }
        }
        return answer;
    }
};
