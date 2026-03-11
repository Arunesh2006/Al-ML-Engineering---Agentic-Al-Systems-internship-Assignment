import heapq
def can_attend_all(events):
    if not events:
        return True
    # sort events by start time
    events.sort(key=lambda x: x[0])
    for i in range(len(events) - 1):
        current_end = events[i][1]
        next_start = events[i + 1][0]
        if current_end > next_start:
            return False
    return True
def min_rooms_required(events):
    if not events:
        return 0
    # sort events by start time
    events.sort(key=lambda x: x[0])
    heap = []
    # add end time of first meeting
    heapq.heappush(heap, events[0][1])
    for i in range(1, len(events)):
        start, end = events[i]
        # if earliest meeting finished, reuse that room
        if heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)
#some test cases 
events = [(9,10), (10,11), (11,12)]
print(can_attend_all(events))
print(min_rooms_required(events))
