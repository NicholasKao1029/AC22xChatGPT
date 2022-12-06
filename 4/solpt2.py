def ranges_overlap(range1, range2):
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    return start1 <= end2 and end1 >= start2

def solve(filename):
    counter = 0
    with open(filename) as f:
        # read the lines of the file into a list
        lines = f.readlines()
        
        # iterate through the lines
        for line in lines:
            # split the line into the two ranges
            range1, range2 = line.strip().split(",")
            
            # check if the ranges have any numbers in common
            if ranges_overlap(range1, range2):
                # increment the counter
                counter += 1
    
    # return the result
    return counter

result = solve("input.txt")
print(result)
