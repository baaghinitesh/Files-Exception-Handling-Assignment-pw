# 8. Create a Python program that uses multiprocessing.Pool to compute the square of numbers from 1 to 10 in parallel. Measure the time taken to perform this computation using a pool of different sizes (e.g., 2, 4, 8 processes).8. Create a Python program that uses multiprocessing.Pool to compute the square of numbers from 1 to 10 in parallel. Measure the time taken to perform this computation using a pool of different sizes (e.g., 2, 4, 8 processes).

import multiprocessing
import time

# Function to compute the square of a number
def square(n):
    return n * n

# Main function to execute the pool
def main():
    numbers = range(1, 11)  # Numbers from 1 to 10
    pool_sizes = [2, 4, 8]   # Different pool sizes

    for pool_size in pool_sizes:
        print(f"\nUsing a pool size of: {pool_size}")

        # Measure time taken
        start_time = time.time()
        
        with multiprocessing.Pool(processes=pool_size) as pool:
            results = pool.map(square, numbers)  # Compute squares in parallel

        end_time = time.time()
        
        # Print results
        print("Squares:", results)
        print(f"Time taken with pool size {pool_size}: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
