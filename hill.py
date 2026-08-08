def hill_climbing(data, start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        best = current

        # Check left neighbour
        if left >= 0 and data[left] > data[best]:
            best = left

        # Check right neighbour
        if right < len(data) and data[right] > data[best]:
            best = right

        # If no better neighbour exists, stop
        if best == current:
            return current, data[current]

        current = best


# Sample dataset
data = [12, 18, 25, 40, 56, 28, 20, 15]

# Start searching from index 1
start = 1

peak_index, peak_value = hill_climbing(data, start)

print("Dataset:", data)
print("Starting Index:", start)
print("Peak Index:", peak_index)
print("Peak Value:", peak_value)