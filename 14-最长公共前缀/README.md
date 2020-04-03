# 最长公共前缀

```
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix/submissions/
```

思路：如果可以求出最长公共前缀的话，则假设最短的为结果，然后进行判断其他元素是否满足条件，如果有一个不满足，则结束循环，返回结果。

