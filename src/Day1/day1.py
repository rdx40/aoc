import time


start = time.time()


p1_start = time.time()
with open("input.txt", "r") as input_file:
    right_locations = []
    left_locations = []
    running_count = 0
    for line in input_file:
        left, right = line.split("   ")
        if running_count == 0:
            left_locations.append(int(left))
            right_locations.append(int(right))
            running_count += 1
            continue
        right_done, left_done = False, False

        saved_len = len(right_locations)
        for i in range(0, saved_len):
            if not right_done and int(right) < right_locations[i]:
                right_locations.insert(i, int(right))
                right_done = True
            if not left_done and int(left) < left_locations[i]:
                left_locations.insert(i, int(left))
                left_done = True
            if left_done and right_done:
                break

        if not left_done:
            left_locations.append(int(left))
        if not right_done:
            right_locations.append(int(right))

        running_count += 1

running_total = 0
for i in range(0, len(right_locations)):
    running_total += abs(right_locations[i] - left_locations[i])

p1_end = time.time()
print(f"Part 1 Running total: {running_total}")
print(f"Part 1 Elapsed time: {(p1_end-p1_start):.6f} seconds")



p2_start = time.time()
with open("input.txt", "r") as input_file:
    right_locations = {}
    left_locations = []

    for line in input_file:
        left, right = line.split("   ")
        left_locations.append(int(left))
        if int(right) in right_locations:
            right_locations[int(right)] += 1
        else:
            right_locations[int(right)] = 1


running_total = 0
for location_id in left_locations:
    if location_id in right_locations:
        running_total += location_id * right_locations[location_id]


p2_end = time.time()
print(f"Part 2 Running total: {running_total}")
print(f"Part 2 Elapsed time: {(p2_end-p2_start):.6f} seconds")

end = time.time()
print(f"Total Elapsed time : {(end-start):.6f} seconds")
