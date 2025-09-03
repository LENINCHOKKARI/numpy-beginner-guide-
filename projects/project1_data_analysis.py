# Project 1: Sales Data Analysis
# A comprehensive data analysis project using NumPy and Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class SalesAnalyzer:
    """A class to analyze sales data and generate insights"""
    
    def __init__(self, data_path):
        """Initialize with sales data"""
        self.df = pd.read_csv(data_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        print(f"Loaded {len(self.df)} sales records")
    
    def basic_statistics(self):
        """Generate basic statistics about the sales data"""
        print("\n=== BASIC STATISTICS ===")
        print(f"Date range: {self.df['Date'].min()} to {self.df['Date'].max()}")
        print(f"Total sales: ${self.df['Sales'].sum():,.2f}")
        print(f"Average daily sales: ${self.df['Sales'].mean():.2f}")
        print(f"Number of products: {self.df['Product'].nunique()}")
        print(f"Number of regions: {self.df['Region'].nunique()}")
        print(f"Number of salespeople: {self.df['Salesperson'].nunique()}")
    
    def product_analysis(self):
        """Analyze sales by product"""
        print("\n=== PRODUCT ANALYSIS ===")
        
        product_stats = self.df.groupby('Product').agg({
            'Sales': ['sum', 'mean', 'count', 'std']
        }).round(2)
        
        product_stats.columns = ['Total_Sales', 'Avg_Sales', 'Count', 'Std_Dev']
        product_stats = product_stats.sort_values('Total_Sales', ascending=False)
        
        print("Sales by Product:")
        print(product_stats)
        
        # Find best and worst performing products
        best_product = product_stats.index[0]
        worst_product = product_stats.index[-1]
        
        print(f"\nBest performing product: {best_product}")
        print(f"Worst performing product: {worst_product}")
        
        return product_stats
    
    def regional_analysis(self):
        """Analyze sales by region"""
        print("\n=== REGIONAL ANALYSIS ===")
        
        regional_stats = self.df.groupby('Region').agg({
            'Sales': ['sum', 'mean', 'count']
        }).round(2)
        
        regional_stats.columns = ['Total_Sales', 'Avg_Sales', 'Count']
        regional_stats = regional_stats.sort_values('Total_Sales', ascending=False)
        
        print("Sales by Region:")
        print(regional_stats)
        
        # Calculate market share
        total_sales = self.df['Sales'].sum()
        regional_stats['Market_Share'] = (regional_stats['Total_Sales'] / total_sales * 100).round(2)
        
        print("\nMarket Share by Region:")
        for region, share in regional_stats['Market_Share'].items():
            print(f"{region}: {share}%")
        
        return regional_stats
    
    def salesperson_performance(self):
        """Analyze salesperson performance"""
        print("\n=== SALESPERSON PERFORMANCE ===")
        
        salesperson_stats = self.df.groupby('Salesperson').agg({
            'Sales': ['sum', 'mean', 'count']
        }).round(2)
        
        salesperson_stats.columns = ['Total_Sales', 'Avg_Sales', 'Count']
        salesperson_stats = salesperson_stats.sort_values('Total_Sales', ascending=False)
        
        print("Performance by Salesperson:")
        print(salesperson_stats)
        
        # Performance ranking
        print("\nTop Performers:")
        for i, (person, stats) in enumerate(salesperson_stats.head(3).iterrows(), 1):
            print(f"{i}. {person}: ${stats['Total_Sales']:,.2f} total sales")
        
        return salesperson_stats
    
    def time_series_analysis(self):
        """Analyze sales trends over time"""
        print("\n=== TIME SERIES ANALYSIS ===")
        
        # Daily sales trend
        daily_sales = self.df.groupby('Date')['Sales'].sum().sort_index()
        
        print("Daily Sales Summary:")
        print(f"Highest sales day: {daily_sales.idxmax()} (${daily_sales.max():,.2f})")
        print(f"Lowest sales day: {daily_sales.idxmin()} (${daily_sales.min():,.2f})")
        
        # Calculate growth rate
        if len(daily_sales) > 1:
            growth_rate = ((daily_sales.iloc[-1] - daily_sales.iloc[0]) / daily_sales.iloc[0] * 100)
            print(f"Overall growth rate: {growth_rate:.2f}%")
        
        return daily_sales
    
    def generate_insights(self):
        """Generate key business insights"""
        print("\n=== KEY INSIGHTS ===")
        
        # Product insights
        product_revenue = self.df.groupby('Product')['Sales'].sum()
        top_product = product_revenue.idxmax()
        
        # Regional insights
        regional_revenue = self.df.groupby('Region')['Sales'].sum()
        top_region = regional_revenue.idxmax()
        
        # Salesperson insights
        salesperson_revenue = self.df.groupby('Salesperson')['Sales'].sum()
        top_salesperson = salesperson_revenue.idxmax()
        
        print(f"1. {top_product} is the best-selling product with ${product_revenue[top_product]:,.2f} in sales")
        print(f"2. {top_region} region generates the highest revenue: ${regional_revenue[top_region]:,.2f}")
        print(f"3. {top_salesperson} is the top performer with ${salesperson_revenue[top_salesperson]:,.2f} in sales")
        
        # Additional insights
        avg_transaction = self.df['Sales'].mean()
        print(f"4. Average transaction value: ${avg_transaction:.2f}")
        
        # Product diversity by region
        product_diversity = self.df.groupby('Region')['Product'].nunique()
        most_diverse_region = product_diversity.idxmax()
        print(f"5. {most_diverse_region} has the most product diversity ({product_diversity[most_diverse_region]} products)")
    
    def create_visualizations(self):
        """Create visualizations for the analysis"""
        print("\n=== CREATING VISUALIZATIONS ===")
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Sales by Product
        product_sales = self.df.groupby('Product')['Sales'].sum().sort_values(ascending=True)
        axes[0, 0].barh(product_sales.index, product_sales.values)
        axes[0, 0].set_title('Total Sales by Product')
        axes[0, 0].set_xlabel('Sales ($)')
        
        # 2. Sales by Region (Pie Chart)
        region_sales = self.df.groupby('Region')['Sales'].sum()
        axes[0, 1].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
        axes[0, 1].set_title('Sales Distribution by Region')
        
        # 3. Daily Sales Trend
        daily_sales = self.df.groupby('Date')['Sales'].sum()
        axes[1, 0].plot(daily_sales.index, daily_sales.values, marker='o')
        axes[1, 0].set_title('Daily Sales Trend')
        axes[1, 0].set_xlabel('Date')
        axes[1, 0].set_ylabel('Sales ($)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 4. Salesperson Performance
        salesperson_sales = self.df.groupby('Salesperson')['Sales'].sum().sort_values(ascending=True)
        axes[1, 1].barh(salesperson_sales.index, salesperson_sales.values)
        axes[1, 1].set_title('Total Sales by Salesperson')
        axes[1, 1].set_xlabel('Sales ($)')
        
        plt.tight_layout()
        plt.savefig('numpy-beginner-guide-/projects/sales_analysis_report.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Visualizations saved as 'sales_analysis_report.png'")

def main():
    """Main function to run the sales analysis"""
    print("🚀 SALES DATA ANALYSIS PROJECT")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = SalesAnalyzer('../datasets/sample_sales.csv')
    
    # Run all analyses
    analyzer.basic_statistics()
    analyzer.product_analysis()
    analyzer.regional_analysis()
    analyzer.salesperson_performance()
    analyzer.time_series_analysis()
    analyzer.generate_insights()
    analyzer.create_visualizations()
    
    print("\n✅ Analysis complete! Check the generated visualizations.")

if __name__ == "__main__":
    main()