#Meeting Rooms III
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x : x[0])
        used_room = [0] * n
        unused_rooms = [i for i in range(n)] 
        heapq.heapify(unused_rooms)
        min_heap = []
        for start, end in meetings:
            while min_heap and min_heap[0][0] <= start:
                _,room = heapq.heappop(min_heap)
                heapq.heappush(unused_rooms, room)

            if unused_rooms:
                next_room = heapq.heappop(unused_rooms)
                used_room[next_room] += 1
                heapq.heappush(min_heap, (end, next_room))
            else:
                earliest_end, room = heapq.heappop(min_heap)
                duration = end-start
                new_end = earliest_end+duration
                heapq.heappush(min_heap, (new_end, room))
                used_room[room] += 1

        most_meetings = max(used_room)
        print(used_room)
        return used_room.index(most_meetings) if most_meetings > 0 else 0           







        