# 7. Create a program that uses a thread pool to calculate the factorial of numbers from 1 to 10 concurrently. Use concurrent.futures.ThreadPoolExecutor to manage the threads.

import concurrent.futures
import math

# Function to calculate factorial
def calculate_factorial(n):
    return math.factorial(n)

# Main function to execute the thread pool
def main():
    numbers = range(1, 11)  # Numbers from 1 to 10

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        futures = {executor.submit(calculate_factorial, num): num for num in numbers}
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(futures):
            num = futures[future]
            try:
                result = future.result()  # Get the result from the future
                print(f"Factorial of {num} is {result}")
            except Exception as e:
                print(f"Error calculating factorial of {num}: {e}")

if __name__ == "__main__":
    main()
