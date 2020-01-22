import time



def main():
    print("Find sum of target in given array")
    tstart = time.time()
    found = has_target_sum(22, [4, 2, 1, 7, 3, 6, 6, 13])
    tend = time.time()
    if found: print("Target 22 Found")
    else: print("Target 22 not found")
    print(tend - tstart)


    tstart = time.time()
    found = has_target_sum(12, [4, 2, 1, 7, 3, 6, 6, 13])
    tend = time.time()
    if found: print("Target 12 Found")
    else: print("Target 12 not found")
    print(tend - tstart)

    tstart = time.time()
    found = has_target_sum(17, [4, 2, 1, 7, 3, 6, 6, 13])
    tend = time.time()
    if found: print("Target 17 Found")
    else: print("Target 17 not found")
    print(tend - tstart)

def has_target_sum(target, values):
    lookup = dict()
    for i in range(len(values)):
        leftover = target - values[i]
        if leftover in lookup:
            return True
        else:
            lookup[values[i]] = values[i]
    return False
	
def has_target_sum_sorted(target, values)
	start = 0
	end = len(values) - 1
	while (start < end):
		leftover = target = values[start]
		if(leftover == target[end]):
			return True
		else if( leftover < values[end]):
			end--
		else
			start++
	return False
	
if __name__ == "__main__":
    main()
