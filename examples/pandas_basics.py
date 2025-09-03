# Pandas Basics Examples
# Real-world examples for data manipulation

import pandas as pd
import numpy as np

def dataframe_creation():
    """Examples of creating DataFrames"""
    print("=== DataFrame Creation Examples ===")
    
    # From dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'London', 'Tokyo', 'Paris'],
        'Salary': [50000, 60000, 70000, 55000]
    }
    df = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df)
    print()

def data_exploration():
    """Basic data exploration techniques"""
    print("=== Data Exploration ===")
    
    # Create sample data
    np.random.seed(42)
    df = pd.DataFrame({
        'Product': ['A', 'B', 'C', 'A', 'B', 'C'] * 10,
        'Sales': np.random.randint(100, 1000, 60),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 60)
    })
    
    print("Dataset info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())

def data_filtering_grouping():
    """Examples of filtering and grouping data"""
    print("\n=== Data Filtering and Grouping ===")
    
    # Create sample sales data
    df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=100),
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet'], 100),
        'Sales': np.random.randint(1000, 5000, 100),
        'Region': np.random.choice(['North', 'South'], 100)
    })
    
    # Filtering
    high_sales = df[df['Sales'] > 3000]
    print(f"High sales records: {len(high_sales)}")
    
    # Grouping
    product_sales = df.groupby('Product')['Sales'].agg(['mean', 'sum', 'count'])
    print("\nSales by Product:")
    print(product_sales)
    
    # Regional analysis
    region_analysis = df.groupby(['Region', 'Product'])['Sales'].mean().unstack()
    print("\nAverage Sales by Region and Product:")
    print(region_analysis)

def real_world_example():
    """Real-world example: Student grade analysis"""
    print("\n=== Real-World Example: Student Grades ===")
    
    # Create student data
    np.random.seed(42)
    students = pd.DataFrame({
        'Student_ID': range(1, 101),
        'Name': [f'Student_{i}' for i in range(1, 101)],
        'Math': np.random.randint(60, 100, 100),
        'Science': np.random.randint(55, 95, 100),
        'English': np.random.randint(65, 100, 100),
        'Grade_Level': np.random.choice(['9th', '10th', '11th', '12th'], 100)
    })
    
    # Calculate total and average scores
    students['Total'] = students[['Math', 'Science', 'English']].sum(axis=1)
    students['Average'] = students[['Math', 'Science', 'English']].mean(axis=1)
    
    # Grade classification
    def classify_grade(avg):
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        else: return 'D'
    
    students['Letter_Grade'] = students['Average'].apply(classify_grade)
    
    # Analysis
    print("Top 5 students:")
    print(students.nlargest(5, 'Average')[['Name', 'Average', 'Letter_Grade']])
    
    print("\nGrade distribution:")
    print(students['Letter_Grade'].value_counts())
    
    print("\nAverage scores by grade level:")
    print(students.groupby('Grade_Level')['Average'].mean().sort_values(ascending=False))

if __name__ == "__main__":
    dataframe_creation()
    data_exploration()
    data_filtering_grouping()
    real_world_example()