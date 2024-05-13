package com.stevens.test;
public class Test {
    public int[] twoSum(int[] numbers, int target) {
        if (numbers == null || numbers.length < 2) {
            return new int[0];
        }
        
		// maintain two pointers to traverse the array
        int i = 0, j = numbers.length - 1;
        while (i < j) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                return new int[] {i + 1, j + 1};
            } else if (sum > target) { 
                j--;
            } else {
                i++;
            }
        }
        
        return new int[0];
    }
}
