# 无重复字符的最长子串
```
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
```

思路：外层循环遍历所有元素，内层循环遍历后面的元素，找到重复的元素则内层循环终止，且记录当前字符的长度，让其与定义的最大长度进行比较。最终得出结果。

