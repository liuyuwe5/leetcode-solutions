import java.util.HashMap;
class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();
        for (int i=0; i < s.length(); i++) {
            Character c = s.charAt(i);
            charMap.put(c, charMap.getOrDefault(c, 0)+1);
        }
        Integer cnt = 0;
        Integer numOfOdd = 0;
        for (Integer v: charMap.values()) {
            cnt += v - (v & 1);
            numOfOdd += v & 1;
        }
        if (numOfOdd >= 1) {
            cnt++;
        }
        return cnt;
    }
    
}