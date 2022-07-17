import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
class Solution {
    private static Integer[] append(Integer[] arr, int element){
        List<Integer> list = new ArrayList<>(Arrays.asList(arr));
        list.add(element);
 
        return list.toArray(new Integer[0]);
    }
 
    public List<Integer> partitionLabels(String s) {
        HashMap<Character, Integer[]> map = new HashMap<Character, Integer[]>();
        for (int i=0; i< s.length(); i++) {
            Character curChar = s.charAt(i);
            if (map.containsKey(curChar)) {
                Integer start = map.get(curChar)[0];
                Integer[] tuple = {start,i};
                map.put(curChar,tuple);
            } else {
                Integer[] tuple = {i,i};
                map.put(curChar,tuple);
            }
        }
        Integer end = 0;
        Integer start = 0;
        List<Integer> res = new ArrayList<Integer>();
        for (int i=0; i<s.length(); i++) {
            Character curChar = s.charAt(i);
            if (end<map.get(curChar)[1]) {
                end = map.get(curChar)[1];
            }
            if (i == end) {
                res.add(end - start+1);
                start = end + 1;
            }
            
        }
        return res;
    }
}