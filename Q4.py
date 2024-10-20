# 4. Write a Python program using multithreading where one thread adds numbers to a list, and another thread removes numbers from the list. Implement a mechanism to avoid race conditions using threading.Lock.

import threading
import time
import random

# Shared list
shared_list = []
# Lock for synchronizing access to the shared list
lock = threading.Lock()

# Function to add numbers to the list
def add_numbers():
    for _ in range(10):
        num = random.randint(1, 100)
        with lock:
            shared_list.append(num)
            print(f"Added: {num}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

# Function to remove numbers from the list
def remove_numbers():
    for _ in range(10):
        with lock:
            if shared_list:  # Check if the list is not empty
                removed_num = shared_list.pop(0)  # Remove the first number
                print(f"Removed: {removed_num}")
            else:
                print("List is empty, nothing to remove.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

# Creating threads
adder_thread = threading.Thread(target=add_numbers)
remover_thread = threading.Thread(target=remove_numbers)

# Starting threads
adder_thread.start()
remover_thread.start()

# Wait for both threads to finish
adder_thread.join()
remover_thread.join()

print("Final shared list:", shared_list)
import threading
import time
import random

# Shared list
shared_list = []
# Lock for synchronizing access to the shared list
lock = threading.Lock()

# Function to add numbers to the list
def add_numbers():
    for _ in range(10):
        num = random.randint(1, 100)
        with lock:
            shared_list.append(num)
            print(f"Added: {num}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

# Function to remove numbers from the list
def remove_numbers():
    for _ in range(10):
        with lock:
            if shared_list:  # Check if the list is not empty
                removed_num = shared_list.pop(0)  # Remove the first number
                print(f"Removed: {removed_num}")
            else:
                print("List is empty, nothing to remove.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

# Creating threads
adder_thread = threading.Thread(target=add_numbers)
remover_thread = threading.Thread(target=remove_numbers)

# Starting threads
adder_thread.start()
remover_thread.start()

# Wait for both threads to finish
adder_thread.join()
remover_thread.join()

print("Final shared list:", shared_list)
