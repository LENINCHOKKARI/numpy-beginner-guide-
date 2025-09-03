# NumPy Basics Examples
# Real-world examples for beginners

import numpy as np
import matplotlib.pyplot as plt

def array_creation_examples():
    """Examples of different ways to create NumPy arrays"""
    print("=== Array Creation Examples ===")
    
    # From lists
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"From list: {arr1}")
    
    # Using built-in functions
    zeros = np.zeros(5)
    ones = np.ones((3, 3))
    range_arr = np.arange(0, 10, 2)
    linspace_arr = np.linspace(0, 1, 5)
    
    print(f"Zeros: {zeros}")
    print(f"Ones:\n{ones}")
    print(f"Range: {range_arr}")
    print(f"Linspace: {linspace_arr}")

def mathematical_operations():
    """Examples of mathematical operations with NumPy"""
    print("\n=== Mathematical Operations ===")
    
    # Create sample arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    
    # Basic operations
    print(f"Addition: {a + b}")
    print(f"Multiplication: {a * b}")
    print(f"Square root: {np.sqrt(a)}")
    print(f"Mean: {np.mean(a)}")
    print(f"Standard deviation: {np.std(a)}")

def real_world_example():
    """Real-world example: Analyzing temperature data"""
    print("\n=== Real-World Example: Temperature Analysis ===")
    
    # Simulate temperature data for a week (in Celsius)
    temperatures = np.array([22, 25, 28, 30, 27, 24, 21])
    days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    
    # Analysis
    avg_temp = np.mean(temperatures)
    max_temp = np.max(temperatures)
    min_temp = np.min(temperatures)
    hottest_day = days[np.argmax(temperatures)]
    
    print(f"Average temperature: {avg_temp:.1f}°C")
    print(f"Hottest day: {hottest_day} ({max_temp}°C)")
    print(f"Coldest temperature: {min_temp}°C")
    print(f"Temperature range: {max_temp - min_temp}°C")

if __name__ == "__main__":
    array_creation_examples()
    mathematical_operations()
    real_world_example()