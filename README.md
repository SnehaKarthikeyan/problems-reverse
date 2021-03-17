# problems-reverse

Question:

Given a number N, array of N integers and an integer k, print the reversed array after deleting elements less than the integer k. Input Size : |N| <= 1000000

Input Description:

The first line contains an integer N. The second line contains N space-separated integers, which denotes array elements. The third line contains an integer k.

Output Description:

Print the reversed array after deleting elements less than the integer k.

Hints:

Reverse the array and then delete elements less than the integer k.

Sample Input:

8\n
1 4 16 2 19 7 3 2\n
3

Sample Output:

3 7 19 16 4

Explanation:

The resultant reversed array after deleting elements less than the integer 3 is 3 7 19 16 4

Testcase 1:

Input:

40\n
34 56 78 67 22 43 54 66 23 45 68 11 25 45 55 67 11 73 67 34 56 78 87 67 23 45 68 11 25 45 55 67 11 73 67 34 56 78 67 22\n
45

Output:

67 78 56 67 73 67 55 45 68 45 67 87 78 56 67 73 67 55 45 68 45 66 54 67 78 56

Testcase 2:

Input:

22\n
45 78 93 22 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 67 29\n
29

Output:

29 67 35 44 32 66 78 34 43 34 51 54 99 79 56 45 93 78 45

Testcase 3:

Input:

15\n
56 32 43 11 78 33 11 23 89 33 12 45 78 23 66\n
56

Output:

66 78 89 78 56

Testcase 4:

Input:

38\n
11 78 33 11 23 89 33 12 45 23 56 79 99 54 51 12 34 43 34 78 66 32 44 35 45 78 23 66 34 56 78 87 67 23 45 68 11 25\n
78

Output:

87 78 78 78 99 79 89 78

Testcase 5:

Input:

54\n
11 25 45 55 67 11 73 67 23 56 79 99 54 51 12 34 43 34 78 66 32 44 34 56 78 87 67 23 45 68 11 25 34 56 78 67 22 43 54 66 23 45 68 45 55 67 11 73 67 34 56 78 67 22\n
25

Output:

67 78 56 34 67 73 67 55 45 68 45 66 54 43 67 78 56 34 25 68 45 67 87 78 56 34 44 32 66 78 34 43 34 51 54 99 79 56 67 73 67 55 45 25
