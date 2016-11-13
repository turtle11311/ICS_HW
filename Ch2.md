Ch2 Homework
============

EXERCISE
--------

### 21. Caesar cipher

```{.numberLines }
foreach character in line do line 2~5
    if ch is a alphabet then do line 3~5
        let offset is ch sub 'a' order
        let ch is ('a' + (offset + k) % 26)

print line
```

### 25. Adjancent equal

```{.numberLines }
foreach elem in numberList do line 2~3
    if elem equals its next elem then do line 3
        print "Yes"

print "No"
```

CHALLENGE WORK
--------------

### 2. Sorting

```{.numberLines }
let i = 1
while i not equals to length of the list then do line 2~8
    let maximumPos = i
    let j = i
    while j is not equals to length of the list then do line 5~7
        if list's j-th number greater than its maximumPos-th number then do line 6~7
            let maximumPos = j
    swap the list's i-th and maximumPos-th
```
