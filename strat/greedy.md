# Greedy

Make locally optimal choice at each step, hoping it leads to global optimum. Works when local best choices don't prevent finding global solution.

**Key insight:** Don't overthink - pick the best option available right now. Often involves sorting first, then making choices based on current state.

**Common problems:** Jump game, gas station, meeting rooms, activity selection, minimum arrows to burst balloons, assign cookies.

**Example:** Maximum meetings you can attend. Sort by end time, greedily pick meetings that end earliest and don't conflict with previously selected ones.

```python
def max_meetings(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    last_end = -1
    
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count
```
