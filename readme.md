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




