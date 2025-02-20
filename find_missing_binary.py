import sys

def find_missing_binary(nums: list[str]) -> str:
    """Given a list of length N where each binary string is of length N, find
    a binary string not in the list."""
    
    n = len(nums)
    # Sort the array to allow fast bisection, O(n log n)
    nums.sort()
    
    print(f"Processing: {nums}")

    low = 0
    high = n
    digit = 0
    result = []

    # Iterate through the array, grabbing the midpoint each time, O(n).  Could 
    # optimize to O(log n) by binary searching remaining entries instead of
    # linearly walking, but we are dominated by the sort time above and it 
    # could make the average runtime worse.
    while digit < n:
        midpoint = low + ((high - low) // 2)
        
        if 0 <= midpoint < n:
        
            entry = nums[midpoint]

            # Whatever digit is found, add the opposite to the result.
            if entry[digit] == "0":
                result.append("1")
                low = midpoint

                # Skip any remaining entries whose substring starts with 0
                while low < n and nums[low][digit] == "0":
                    low += 1

            else:
                result.append("0")
                high = midpoint

                # Skip any remaining entries whose substring starts with 1
                while high >= -1 and nums[high][digit] == "1":
                    high -= 1
        else:
            # The search is off the end of the array so we can fill  
            # remaining values with anything.
            result.append("0")

        digit += 1

    return "".join(result)


if __name__ == "__main__":
    print(find_missing_binary(sys.argv[1:]))
