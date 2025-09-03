# 📊 Practice Datasets

This folder contains sample datasets for practicing NumPy and Pandas operations.

## Available Datasets

### 📈 sample_sales.csv
**Description:** Sales data for different products across regions
- **Columns:** Date, Product, Sales, Region, Salesperson
- **Records:** 30 entries
- **Use Cases:** 
  - Time series analysis
  - Grouping and aggregation
  - Regional sales comparison
  - Salesperson performance analysis

### 🎓 student_grades.csv
**Description:** Student academic performance data
- **Columns:** Student_ID, Name, Math, Science, English, Grade_Level, Gender
- **Records:** 25 students
- **Use Cases:**
  - Grade analysis and statistics
  - Subject performance comparison
  - Grade level analysis
  - Gender-based performance studies

### 🌡️ weather_data.csv (Coming Soon)
**Description:** Daily weather measurements
- Temperature, humidity, precipitation data
- Perfect for time series analysis

### 💰 financial_data.csv (Coming Soon)
**Description:** Stock market data
- Historical stock prices and volumes
- Great for financial analysis practice

## How to Use

```python
import pandas as pd

# Load sales data
sales_df = pd.read_csv('datasets/sample_sales.csv')
print(sales_df.head())

# Load student grades
grades_df = pd.read_csv('datasets/student_grades.csv')
print(grades_df.describe())
```

## Practice Exercises

### Beginner Level
1. Load each dataset and explore basic statistics
2. Find missing values and data types
3. Calculate mean, median, and mode for numeric columns

### Intermediate Level
1. Group sales data by region and calculate total sales
2. Find the top-performing students in each subject
3. Create visualizations for each dataset

### Advanced Level
1. Perform correlation analysis between subjects
2. Create time series forecasts for sales data
3. Build comprehensive data analysis reports

## Contributing

Feel free to add more datasets! Please ensure they are:
- Clean and well-structured
- Include a variety of data types
- Have real-world relevance
- Come with documentation