# Measuring Ram Usage for python `str.join()`

Inspired by a comment on StackOverflow which suggested that the following idiom:

```python
" ".join(list(some_str))
```

might *save* ram over the (IMHO more natural):

```python
" ".join(some_str)
```

This is of course a micro-optimisation, and you should just use whatever you
find clearer (which is obviously avoiding the cast to `list` ;).

## Random things

- running git push from multiple jobs at the same time hits race
  conditions. Here's a crude way to avoid that:

  ```bash
  for attempt in $(seq 10); do
      echo "uploading attempt $attempt"
      git pull
      git push && break
      sleep $(echo "$RANDOM / 10000" | bc -l)
  done
  ```

  `$RANDOM` is, helpfully, a random number.  `bc` is the Basic Calculator.

- `git commit` errors if there are no changes.  I guess that makes sense.

- `sed` lets you invert commands with `!`. So `!p` means 'don't print', which is
  handy.
  
- `awk` is often easier than sed.  (sed didn't work as it was doing what it
  ought to do---finding a match in a stream---rather than what I wanted it to
  do.)  The awk version is very easy:
  
  ```bash
   awk '/##_Results/{i++} !i; i==1 {exit}' readme.md.bak > readme.md
   ```
   which means: increment counter `i` when match; if not match (do default action=print); if match, exit.
   
   Note that I have replaced a space with `_` here---else the regex will match...
 
 
## Reliability

These results are hopefully indicative.  It's *possible* something odd with
garbage collection is happening, although altering the order of running appears
to have no affect which suggests otherwise.  This is definitely not a scientific
test however!

## Results
```
3.10-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20Without list
10 loops, best of 5: 20.9 msec per loop
With list
10 loops, best of 5: 21.4 msec per loop


3.6-results.txt
Without list:
11,000,096 : 20
With list:
11,000,160 : 20Without list
10 loops, best of 3: 22.9 msec per loop
With list
10 loops, best of 3: 23.1 msec per loop


3.7-results.txt
Without list:
11,000,096 : 20
With list:
11,000,168 : 20Without list
20 loops, best of 5: 16.8 msec per loop
With list
20 loops, best of 5: 16.1 msec per loop


3.8-results.txt
Without list:
11,000,096 : 20
With list:
10,000,104 : 20Without list
10 loops, best of 5: 21.2 msec per loop
With list
10 loops, best of 5: 20.8 msec per loop


3.9-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20Without list
20 loops, best of 5: 18.3 msec per loop
With list
20 loops, best of 5: 19.1 msec per loop


```
