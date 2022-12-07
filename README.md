# MCA ucbqsort with script

**Best performance defined as smallest time * area**

## 1. Starting from the init state
Init state

## 2. Increasing the memory
From 1 to 10. 
Improve stop at memory = 2.

## 3. Increase connection to the data cache
For three parameter.
Each sweep {1..3}, find the best combination.
Found that 2, 1, 1 has the best performance.
Now the configuration: 4	2	1	1	4	2	1	0	0	64	8

## 4. Increase the number of Alu
Decrease the number of Mul at the same time.
Alu from 2 to 6. (When Alu = 1, crash)
Mul from 0 to 3.
Found that 4, 0 has the best performance.
Now the configuration: 4	2	1	1	4	2	1	0	0	64	8
(What happens when Mul is 0, but mul is still needed? Explain.)

## 5. Increase issue width
Sweep Alu from 4 to 10.
And sweep issue width from 4 to 10.
Performace did not change much, best still: 4	2	1	1	4	2	1	0	0	64	8

## 6. Increase r0 and b0
Sweep r0 among 32 64 128 160
Sweep b0 among 4 8 12 16 20 24
Performance is at: 4	2	1	1	4	2	1	0	0	32	4




# MCA convolution_5x5 bash script

**The performance below means that Time * Area is the smallest**

## 1. Init state
With init values: 4	1	1	1	4	2	1	0	0	64	8
Set.

## 2. Increase the Mul
From 1 to 10.
Performanace stops increasing after exceeding 4.
We keep Mul at 4.
Configuration: 4	1	1	1	4	4	1	0	0	64	8

## 3. Increase the Alu
From 2 to 10.
Performance stops increasing after Alu exceeds 6.
We keep Alu at 6.
Configue: 4	1	1	1	6	4	1	0	0	64	8

## 4. Increase the Issue Width
From 4 to 30. (Seems very parallelizable)
Performance stops to increase after exceeding 6.
Configue: 6	1	1	1	6	4	1	0	0	64	8

## 5. Increase connection to data cache
Each from 1 to 5.
Performance does not change.
Still: 6	1	1	1	6	4	1	0	0	64	8

## 6. Increase r0 and b0
r0: 32 64 96 128 160 192 224 256 288 310
b0: 4 8 12 16 20 24 28 32 36 40
After r0 exceeding 64 and b0 exceeding 4, performance does not improve.
Configure: 6	1	1	1	6	4	1	0	0	64	4

## 7. Increase the memory
From 1 to 10.
Still: 6	1	1	1	6	4	1	0	0	64	4

## 8. Double check things done at the very first above
Mul, Alu and IssueWidth might have coupled influence on the performance.
Sweep three parameters: Mul. Alu and IssueWidth
Mul from: 4 to 10
Alu from: 6 to 10
IssueWidth: 6 to 15

Analyze the result:
 - When IssueWidth (call it IW from now on) = 6, Alu and Mul sweeping. No improvement.
 - When IW = 7, and since then, the improvement starts.
 - IW = 7, Alu = 7, Mpy = 4. Best
 - IW = 8, Alu = 8, Mpy = 4. Best, however, result a bit wierd. As shown in figure below:
![](https://i.imgur.com/5pzViTQ.png)
 - IW = 9, ALu = 10, Mpy = 4. Best.
 - IW = 10, ALu = 10, Mpy = 4. Best.
 - IW = 11, ALu = 10, Mpy = 4. Best. (But same as above)
 - IW = 12, ALu = 10, Mpy = 4. Best. (But same as well)
 - IW = 13, ALu = 10, Mpy = 4. Best. (Same too)
 - IW = 14, ALu = 10, Mpy = 4. Best. (Same)
 - IW = 15, ALu = 10, Mpy = 4. Best. (Same)
Set: 10	1	1	1	10	4	1	0	0	64	4

## 9. The guess above is confirmed. The similar test continues.
Mul constant = 4
Alu from 10 to 20.
IW from 10 to 20.

Analyze the result:
 - IW = 10, ALu = 11. Best.
 - IW = 11, ALu = 12. Best. (Perf. same as above)
 - IW = 12, ALu = 13. Best. (Same)
 - IW = 13, ALu = 13. Best. **Better than above**
 - IW = 14, ALu = 13. Best. (Perf. same as above)
 - IW = 15, ALu = 13. Best. (Perf. same as above)
 - IW = 16, ALu = 13. Best. (Perf. same as above)
 - IW = 17, ALu = 13. Best. (Perf. same as above)
 - IW = 18, ALu = 13. Best. (Perf. same as above)
 - IW = 19, ALu = 13. Best. (Perf. same as above)
 - IW = 20, ALu = 13. Best. (Perf. same as above)
Set: 13	1	1	1	13	4	1	0	0	64	4

## 10. Double check that Mul has no effect
Mul sweep 4 to 20.
Mul has no more influence.
Mul always stays at 4.
Set: 13	1	1	1	13	4	1	0	0	64	4

## 11. Check influence on other parameters
IW, Mul and Alu kinda the best combination already.
Adjust the rest.
Memload:1 2 3
Memstore:1 2 3
MemPft:1 2 3
r0:16 32 48 80
b0:2 6 10 14
Analyze the result: (First of all, the best performance remains the same: 654627)
 - The three: 1 1 1, r0: 48, b0: 6
The three connections to the data cache are basically unrelated.
Set: 13	1	1	1	13	4	1	0	0	48	6

Check with set: 13	1	1	1	13	4	1	0	0	48	4 (**Same**)

Use: 13	1	1	1	13	4	1	0	0	48	4

## 12. Make the graph better
Useful information ends at 1203.



