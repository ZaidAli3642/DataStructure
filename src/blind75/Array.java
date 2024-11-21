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
}
