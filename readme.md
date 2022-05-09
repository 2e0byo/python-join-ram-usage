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


## Reliability

These results are hopefully indicative.  It's *possible* something odd with
garbage collection is happening, although altering the order of running appears
to have no affect which suggests otherwise.  This is definitely not a scientific
test however!





```
3.10-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20

3.6-results.txt
Without list:
11,000,096 : 20
With list:
11,000,160 : 20

3.7-results.txt
Without list:
11,000,096 : 20
With list:
11,000,168 : 20

3.8-results.txt
Without list:
11,000,096 : 20
With list:
10,000,104 : 20

3.9-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20

```
## Results
```
3.10-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20

3.6-results.txt
Without list:
11,000,096 : 20
With list:
11,000,160 : 20

3.7-results.txt
Without list:
11,000,096 : 20
With list:
11,000,168 : 20

3.8-results.txt
Without list:
11,000,096 : 20
With list:
10,000,104 : 20

3.9-results.txt
Without list:
10,000,048 : 20
With list:
10,000,104 : 20

```
