import time
import bisect

start = time.time()

p1_start = time.time()
with open("input.txt", "r") as input_file:
    right_locations = []
    left_locations = []
    running_count = 0
    for line in input_file:
        left, right = line.split("   ")
        left = int(left)
        right = int(right)

        if running_count == 0:
            left_locations.append(left)
            right_locations.append(right)
            running_count += 1
            continue

        bisect.insort(right_locations, right)
        bisect.insort(left_locations, left)

        running_count += 1

running_total = sum(abs(r - l) for r, l in zip(right_locations, left_locations))

p1_end = time.time()
print(f"Part 1 Running total: {running_total}")
print(f"Part 1 Elapsed time: {(p1_end-p1_start):.6f} seconds")


p2_start = time.time()
with open("input.txt", "r") as input_file:
    right_locations = {}
    left_locations = []

    for line in input_file:
        left, right = line.split("   ")
        left = int(left)
        right = int(right)

        left_locations.append(left)
        right_locations[right] = right_locations.get(right, 0) + 1

running_total = sum(location_id * right_locations.get(location_id, 0) for location_id in left_locations)

p2_end = time.time()
print(f"Part 2 Running total: {running_total}")
print(f"Part 2 Elapsed time: {(p2_end-p2_start):.6f} seconds")


end = time.time()
print(f"Total Elapsed time : {(end-start):.6f} seconds")
