# Data Visualization Examples
# Creating compelling charts with NumPy and Pandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_plots():
    """Basic plotting examples"""
    print("=== Creating Basic Plots ===")
    
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Line plot
    axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
    axes[0, 0].plot(x, y2, label='cos(x)', color='red')
    axes[0, 0].set_title('Trigonometric Functions')
    axes[0, 0].legend()
    axes[0, 0].grid(True)
    
    # Scatter plot
    np.random.seed(42)
    x_scatter = np.random.randn(100)
    y_scatter = 2 * x_scatter + np.random.randn(100)
    axes[0, 1].scatter(x_scatter, y_scatter, alpha=0.6)
    axes[0, 1].set_title('Scatter Plot')
    axes[0, 1].set_xlabel('X values')
    axes[0, 1].set_ylabel('Y values')
    
    # Histogram
    data = np.random.normal(100, 15, 1000)
    axes[1, 0].hist(data, bins=30, alpha=0.7, color='green')
    axes[1, 0].set_title('Normal Distribution')
    axes[1, 0].set_xlabel('Values')
    axes[1, 0].set_ylabel('Frequency')
    
    # Bar plot
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    axes[1, 1].bar(categories, values, color='orange')
    axes[1, 1].set_title('Bar Chart')
    axes[1, 1].set_xlabel('Categories')
    axes[1, 1].set_ylabel('Values')
    
    plt.tight_layout()
    plt.savefig('numpy-beginner-guide-/examples/basic_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

def pandas_visualization():
    """Pandas built-in visualization examples"""
    print("\n=== Pandas Visualization ===")
    
    # Create sample sales data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=365)
    sales_data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(1000, 5000, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 500,
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet'], 365),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 365)
    })
    
    # Set date as index
    sales_data.set_index('Date', inplace=True)
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Time series plot
    sales_data['Sales'].resample('M').mean().plot(ax=axes[0, 0], title='Monthly Average Sales')
    axes[0, 0].set_ylabel('Sales ($)')
    
    # Box plot by product
    sales_data.boxplot(column='Sales', by='Product', ax=axes[0, 1])
    axes[0, 1].set_title('Sales Distribution by Product')
    axes[0, 1].set_xlabel('Product')
    
    # Sales by region (pie chart)
    region_sales = sales_data.groupby('Region')['Sales'].sum()
    axes[1, 0].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
    axes[1, 0].set_title('Sales Distribution by Region')
    
    # Correlation heatmap (create additional numeric columns)
    sales_data['Month'] = sales_data.index.month
    sales_data['DayOfYear'] = sales_data.index.dayofyear
    correlation_data = sales_data[['Sales', 'Month', 'DayOfYear']].corr()
    
    im = axes[1, 1].imshow(correlation_data, cmap='coolwarm', aspect='auto')
    axes[1, 1].set_xticks(range(len(correlation_data.columns)))
    axes[1, 1].set_yticks(range(len(correlation_data.columns)))
    axes[1, 1].set_xticklabels(correlation_data.columns)
    axes[1, 1].set_yticklabels(correlation_data.columns)
    axes[1, 1].set_title('Correlation Matrix')
    
    # Add colorbar
    plt.colorbar(im, ax=axes[1, 1])
    
    plt.tight_layout()
    plt.savefig('numpy-beginner-guide-/examples/pandas_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

def advanced_visualization():
    """Advanced visualization techniques"""
    print("\n=== Advanced Visualization ===")
    
    # Create complex dataset
    np.random.seed(42)
    n_samples = 1000
    
    data = pd.DataFrame({
        'x': np.random.randn(n_samples),
        'y': np.random.randn(n_samples),
        'category': np.random.choice(['A', 'B', 'C'], n_samples),
        'size': np.random.randint(20, 200, n_samples),
        'value': np.random.exponential(2, n_samples)
    })
    
    # Create advanced plots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Bubble chart
    for category in data['category'].unique():
        subset = data[data['category'] == category]
        axes[0, 0].scatter(subset['x'], subset['y'], s=subset['size'], 
                          alpha=0.6, label=category)
    axes[0, 0].set_title('Bubble Chart')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Density plot
    axes[0, 1].hexbin(data['x'], data['y'], gridsize=20, cmap='Blues')
    axes[0, 1].set_title('Density Plot (Hexbin)')
    axes[0, 1].set_xlabel('X values')
    axes[0, 1].set_ylabel('Y values')
    
    # Violin plot
    category_data = [data[data['category'] == cat]['value'].values for cat in ['A', 'B', 'C']]
    axes[1, 0].violinplot(category_data, positions=[1, 2, 3])
    axes[1, 0].set_xticks([1, 2, 3])
    axes[1, 0].set_xticklabels(['A', 'B', 'C'])
    axes[1, 0].set_title('Violin Plot')
    axes[1, 0].set_ylabel('Values')
    
    # Stacked area chart
    dates = pd.date_range('2024-01-01', periods=50)
    area_data = pd.DataFrame({
        'A': np.cumsum(np.random.randn(50)),
        'B': np.cumsum(np.random.randn(50)),
        'C': np.cumsum(np.random.randn(50))
    }, index=dates)
    
    axes[1, 1].stackplot(dates, area_data['A'], area_data['B'], area_data['C'],
                        labels=['A', 'B', 'C'], alpha=0.7)
    axes[1, 1].set_title('Stacked Area Chart')
    axes[1, 1].legend(loc='upper left')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('numpy-beginner-guide-/examples/advanced_plots.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Creating visualization examples...")
    basic_plots()
    pandas_visualization()
    advanced_visualization()
    print("All plots saved to examples/ folder!")