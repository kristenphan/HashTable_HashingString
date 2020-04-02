# HashTable_HashingString

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/learn/data-structures/. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Assignment Description:__
<br/>
Task: In this task your goal is to implement a hash table with lists chaining. You are already given the
number of buckets 𝑚 and the hash function. It is a polynomial hash function. 
<br/>
<br/>
Your program should support the following kinds of queries:
-----∙ add string — insert string into the table. If there is already such string in the hash table, then
just ignore the query.
-----∙ del string — remove string from the table. If there is no such string in the hash table, then
just ignore the query.
-----∙ find string — output “yes" or “no" (without quotes) depending on whether the table contains
string or not.
-----∙ check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of
the list. If 𝑖-th list is empty, output a blank line.
<br/>
<br/>
When inserting a new string into a hash chain, you must insert it in the beginning of the chain.
Input Format. There is a single integer 𝑚 in the first line — the number of buckets you should have. The
next line contains the number of queries 𝑁. It’s followed by 𝑁 lines, each of them contains one query
in the format described above.
<br/>
<br/>
Constraints: 1 ≤ 𝑁 ≤ 10^5; 𝑁/5 ≤ 𝑚 ≤ 𝑁. All the strings consist of latin letters. Each of them is non-empty
and has length at most 15.
<br/>
<br/>
Output Format: Print the result of each of the find and check queries, one result per line, in the same
order as these queries are given in the input.
<br/>
<br/>
Time Limits. C: 1 sec, C++: 1 sec, Java: 5 sec, Python: 7 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 7
sec, Ruby: 7 sec, Scala: 7 sec.
<br/>
<br/>
Memory Limit. 512MB.<br/>
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)"
