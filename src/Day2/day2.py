import time


p1_start = time.time()
with open("input.txt", "r") as input_file:
    total_safe_part1 = 0
    
    for line in input_file:
        nums = line.split()
        current_change = -1 if int(nums[0]) > int(nums[1]) else 1
        
        if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
            continue
        failed = False
        for i in range(1, len(nums)-1):
            if (int(nums[i]) - int(nums[i+1])) * current_change >= 1:
                failed = True
                break
            if abs(int(nums[i]) - int(nums[i+1])) > 3 or abs(int(nums[i]) - int(nums[i+1])) < 1:
                failed = True
                break
        if failed:
            continue
        
        total_safe_part1 += 1

p1_end = time.time()
print(f"Part 1 total safe: {total_safe_part1}")
print(f"Part 1 execution time: {(p1_end-p1_start):.4f} seconds\n")


p2_start = time.time()

with open("input.txt", "r") as input_file:
    total_safe_part2 = 0
    curr_line = 0
    for line in input_file:
        curr_line += 1

        done = False
        current_remove_index = -1

        while not done:
            nums = line.split()

            if current_remove_index > len(nums)-1:
                break
            if current_remove_index > -1:
                nums.pop(current_remove_index)
            current_change = -1 if int(nums[0]) > int(nums[1]) else 1

            if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
                current_remove_index += 1
                continue
            
            number_of_failed = 0
            i = 1
            cond = len(nums)-1

            while i < cond:
                if (int(nums[i]) - int(nums[i+1])) * current_change >= 1:
                    number_of_failed += 1
                    i += 1
                    continue
                elif (int(nums[i]) - int(nums[i+1])) * current_change == 0:
                    number_of_failed += 1
                    i += 1
                    continue
                if abs(int(nums[i]) - int(nums[i+1])) > 3:
                    number_of_failed += 1
                    i += 1
                    continue

                i += 1

            if number_of_failed >= 1:
                current_remove_index += 1
            else:
                done = True

        if done:
            total_safe_part2 += 1

p2_end = time.time()
print(f"Part 2 total safe: {total_safe_part2}")
print(f"Part 2 execution time: {(p2_end-p2_start):.4f} seconds\n")



