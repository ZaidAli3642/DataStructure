package blind75;

import java.util.Arrays;
import java.util.HashMap;

public class Array {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();

        for(int num : nums){
            if (hashMap.containsKey(num)) return true;

            hashMap.put(num, num);
        }

        return false;
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        Arrays.sort(sArr);
        Arrays.sort(tArr);

        return Arrays.equals(sArr, tArr);
    }

    public boolean isAnagramByHashMap(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> countS = new HashMap<Character, Integer>();
        HashMap<Character, Integer> countT = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i++){
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }

        for (char item : s.toCharArray()) {
            if (!countS.get(item).equals(countT.get(item))) {
                return false;
            }
        }

        return true;
    }

    public boolean isAnagramOptimal(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int item : count)
            if(item != 0) return false;

        return true;
    }


}
