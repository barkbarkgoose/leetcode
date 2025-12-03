# Greedy

Make locally optimal choice at each step, hoping it leads to global optimum. Works when local best choices don't prevent finding global solution.

**Key insight:** Don't overthink - pick the best option available right now. Often involves sorting first, then making choices based on current state.

**Common problems:** Jump game, gas station, meeting rooms, activity selection, minimum arrows to burst balloons, assign cookies.

**Example:** Maximum meetings you can attend. Sort by end time, greedily pick meetings that end earliest and don't conflict with previously selected ones.

```python
def max_meetings(intervals):
    # lambda x: x[1] is an anonymous function that takes each interval tuple
    # and returns the second element (end time). Sort uses this to order by end time.
    # Example: [(1,3), (2,1), (0,2)] becomes [(2,1), (0,2), (1,3)]
    # -----
    # Equivalent without lambda:
    # intervals.sort(key=lambda x: x[1])
    # is the same as:
    # def get_end_time(interval):
    #     return interval[1]
    # intervals.sort(key=get_end_time)
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    last_end = -1
    
    # Greedy logic: Process meetings in order of end time
    # For each meeting, if it starts after the last selected meeting ends, take it
    # This maximizes count because we always pick the meeting that ends earliest
    # among all non-conflicting options
    for start, end in intervals:
        if start >= last_end:  # No overlap: new meeting starts after last one ends
            count += 1
            last_end = end  # Track when this meeting ends
    
    return count

# Visual example:
# Intervals: [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
# After sorting by end time: [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
#
# Step-by-step:
#   last_end=-1, count=0
#   (1,4): start=1 >= last_end=-1 ✓ → count=1, last_end=4
#   (3,5): start=3 >= last_end=4 ✗ → skip (overlaps)
#   (0,6): start=0 >= last_end=4 ✗ → skip (overlaps)
#   (5,7): start=5 >= last_end=4 ✓ → count=2, last_end=7
#   (8,9): start=8 >= last_end=7 ✓ → count=3, last_end=9
#   (5,9): start=5 >= last_end=9 ✗ → skip (overlaps)
#   Result: 3 meetings
#
# Timeline visualization:
#   0    1    2    3    4    5    6    7    8    9
#   |----|----|----|----|----|----|----|----|----|
#   [1----4]  ✓ selected
#        [3----5]  ✗ overlaps
#   [0--------6]  ✗ overlaps
#              [5----7]  ✓ selected
#                      [8----9]  ✓ selected
#              [5--------9]  ✗ overlaps
```
