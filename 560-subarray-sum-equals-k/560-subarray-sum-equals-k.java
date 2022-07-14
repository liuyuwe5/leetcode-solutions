import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> mapSum = new HashMap<Integer, Integer>();
        mapSum.put(0,1);
        Integer sum = 0;
        Integer cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            Integer required = sum - k;
            cnt += mapSum.getOrDefault(required, 0);
            if (mapSum.containsKey(sum)) {
                mapSum.put(sum,mapSum.get(sum)+1);
            } else {
                mapSum.put(sum,1);
            }
        }
        return cnt;
    }
}