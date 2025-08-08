import time

def find_pairs(nums):
    product_map = {}
    n = len(nums)

    # Iterate through all pairs of numbers
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]

            # Check if the product already exists in the map
            if product in product_map:
                # Extract existing pair from the hash map
                a, b = product_map[product]
                c, d = nums[i], nums[j]

                # Ensure all four numbers are distinct
                if len({a, b, c, d}) == 4:
                    # Print the valid pair and exit
                    print(f"{a} {b}, {c} {d}")
                else:
                    # If no pairs meet the criterion
                    print("No pair exists")
            else:
                # Store the current pair for this product
                product_map[product] = (nums[i], nums[j])

# Input: list of distinct integers
nums = list(map(int, input().split()))

st = time.process_time()
find_pairs(nums)
et = time.process_time()
print(et - st)
