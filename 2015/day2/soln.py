def calculate_wrapping_paper_and_ribbon(dimensions):
    total_paper = 0
    total_ribbon = 0

    for dim in dimensions:
        l, w, h = map(int, dim.split('x'))
        
        surface_area = 2 * (l*w + w*h + h*l)
        smallest_side = min(l*w, w*h, h*l)
        total_paper_for_present = surface_area + smallest_side
        total_paper += total_paper_for_present
        
        smallest_perimeter = 2 * (min(l + w, w + h, h + l))
        volume = l * w * h
        total_ribbon_for_present = smallest_perimeter + volume
        total_ribbon += total_ribbon_for_present
    
    return total_paper, total_ribbon

with open('input.txt') as file:
    dimensions = file.read().strip().splitlines()

total_paper, total_ribbon = calculate_wrapping_paper_and_ribbon(dimensions)

print(f"Total square feet of wrapping paper needed: {total_paper}")
print(f"Total feet of ribbon needed: {total_ribbon}")

