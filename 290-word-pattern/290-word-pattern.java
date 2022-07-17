import java.util.HashMap;
class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<String,Character> map = new HashMap<String,Character> ();
        String[] lstStr = s.split(" ", 0);
        if (pattern.length() != lstStr.length) {
            return false;
        }
        for (int i=0; i<pattern.length(); i++) {
            System.out.println(map);
            Character charMap = pattern.charAt(i);
            if (map.containsKey(lstStr[i])) {
                Character requiredchar = map.get(lstStr[i]);
                if (!requiredchar.equals(charMap)) {
                    return false;
                }
            } else {
                if (map.containsValue(charMap)) {
                    return false;
                } else {
                    map.put(lstStr[i],charMap);
                }
            }
        }
        return true;
    }
}