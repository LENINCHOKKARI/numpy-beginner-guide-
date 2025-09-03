# Project 2: Student Performance Analysis
# Comprehensive analysis of student academic performance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class StudentPerformanceAnalyzer:
    """Analyze student academic performance data"""
    
    def __init__(self, data_path):
        """Initialize with student data"""
        self.df = pd.read_csv(data_path)
        self.subjects = ['Math', 'Science', 'English']
        
        # Calculate derived metrics
        self.df['Total_Score'] = self.df[self.subjects].sum(axis=1)
        self.df['Average_Score'] = self.df[self.subjects].mean(axis=1)
        self.df['Grade'] = self.df['Average_Score'].apply(self._assign_letter_grade)
        
        print(f"Loaded data for {len(self.df)} students")
    
    def _assign_letter_grade(self, score):
        """Assign letter grade based on average score"""
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        elif score >= 60: return 'D'
        else: return 'F'
    
    def basic_statistics(self):
        """Generate basic statistics"""
        print("\n=== BASIC STATISTICS ===")
        print(f"Total students: {len(self.df)}")
        print(f"Grade levels: {sorted(self.df['Grade_Level'].unique())}")
        print(f"Gender distribution: {dict(self.df['Gender'].value_counts())}")
        
        print("\nOverall Performance:")
        print(f"Average score across all subjects: {self.df['Average_Score'].mean():.2f}")
        print(f"Highest average score: {self.df['Average_Score'].max():.2f}")
        print(f"Lowest average score: {self.df['Average_Score'].min():.2f}")
        print(f"Standard deviation: {self.df['Average_Score'].std():.2f}")
    
    def subject_analysis(self):
        """Analyze performance by subject"""
        print("\n=== SUBJECT ANALYSIS ===")
        
        subject_stats = self.df[self.subjects].describe().round(2)
        print("Subject Statistics:")
        print(subject_stats)
        
        # Find best and worst subjects
        subject_means = self.df[self.subjects].mean()
        best_subject = subject_means.idxmax()
        worst_subject = subject_means.idxmin()
        
        print(f"\nBest performing subject: {best_subject} (avg: {subject_means[best_subject]:.2f})")
        print(f"Most challenging subject: {worst_subject} (avg: {subject_means[worst_subject]:.2f})")
        
        # Subject correlations
        correlations = self.df[self.subjects].corr()
        print("\nSubject Correlations:")
        print(correlations.round(3))
        
        return subject_stats, correlations
    
    def grade_level_analysis(self):
        """Analyze performance by grade level"""
        print("\n=== GRADE LEVEL ANALYSIS ===")
        
        grade_level_stats = self.df.groupby('Grade_Level').agg({
            'Average_Score': ['mean', 'std', 'count'],
            'Math': 'mean',
            'Science': 'mean',
            'English': 'mean'
        }).round(2)
        
        print("Performance by Grade Level:")
        print(grade_level_stats)
        
        # Statistical significance test between grade levels
        grade_groups = [group['Average_Score'].values for name, group in self.df.groupby('Grade_Level')]
        f_stat, p_value = stats.f_oneway(*grade_groups)
        
        print(f"\nANOVA Test Results:")
        print(f"F-statistic: {f_stat:.4f}")
        print(f"P-value: {p_value:.4f}")
        print(f"Significant difference between grade levels: {'Yes' if p_value < 0.05 else 'No'}")
        
        return grade_level_stats
    
    def gender_analysis(self):
        """Analyze performance by gender"""
        print("\n=== GENDER ANALYSIS ===")
        
        gender_stats = self.df.groupby('Gender').agg({
            'Average_Score': ['mean', 'std', 'count'],
            'Math': 'mean',
            'Science': 'mean',
            'English': 'mean'
        }).round(2)
        
        print("Performance by Gender:")
        print(gender_stats)
        
        # T-test for gender differences
        male_scores = self.df[self.df['Gender'] == 'Male']['Average_Score']
        female_scores = self.df[self.df['Gender'] == 'Female']['Average_Score']
        
        t_stat, p_value = stats.ttest_ind(male_scores, female_scores)
        
        print(f"\nT-test Results:")
        print(f"T-statistic: {t_stat:.4f}")
        print(f"P-value: {p_value:.4f}")
        print(f"Significant gender difference: {'Yes' if p_value < 0.05 else 'No'}")
        
        return gender_stats
    
    def grade_distribution_analysis(self):
        """Analyze letter grade distribution"""
        print("\n=== GRADE DISTRIBUTION ANALYSIS ===")
        
        grade_dist = self.df['Grade'].value_counts().sort_index()
        grade_percentages = (grade_dist / len(self.df) * 100).round(2)
        
        print("Grade Distribution:")
        for grade, count in grade_dist.items():
            percentage = grade_percentages[grade]
            print(f"Grade {grade}: {count} students ({percentage}%)")
        
        # Grade distribution by gender
        print("\nGrade Distribution by Gender:")
        grade_gender = pd.crosstab(self.df['Grade'], self.df['Gender'], normalize='columns') * 100
        print(grade_gender.round(2))
        
        return grade_dist, grade_gender
    
    def identify_top_performers(self):
        """Identify top performing students"""
        print("\n=== TOP PERFORMERS ===")
        
        # Overall top performers
        top_students = self.df.nlargest(5, 'Average_Score')[['Name', 'Average_Score', 'Grade_Level', 'Grade']]
        print("Top 5 Students Overall:")
        print(top_students.to_string(index=False))
        
        # Top performers by subject
        print("\nTop Performers by Subject:")
        for subject in self.subjects:
            top_in_subject = self.df.nlargest(3, subject)[['Name', subject, 'Grade_Level']]
            print(f"\n{subject}:")
            for i, (_, student) in enumerate(top_in_subject.iterrows(), 1):
                print(f"  {i}. {student['Name']}: {student[subject]} ({student['Grade_Level']})")
        
        return top_students
    
    def identify_at_risk_students(self):
        """Identify students who need additional support"""
        print("\n=== AT-RISK STUDENTS ===")
        
        # Students with average below 70
        at_risk = self.df[self.df['Average_Score'] < 70][['Name', 'Average_Score', 'Grade_Level', 'Math', 'Science', 'English']]
        
        if len(at_risk) > 0:
            print(f"Students needing support ({len(at_risk)} students):")
            print(at_risk.to_string(index=False))
            
            # Identify specific subject weaknesses
            print("\nSubject-specific support needed:")
            for subject in self.subjects:
                weak_in_subject = self.df[self.df[subject] < 70]['Name'].tolist()
                if weak_in_subject:
                    print(f"{subject}: {', '.join(weak_in_subject)}")
        else:
            print("Great news! No students are currently at risk.")
        
        return at_risk
    
    def generate_recommendations(self):
        """Generate actionable recommendations"""
        print("\n=== RECOMMENDATIONS ===")
        
        # Subject-based recommendations
        subject_means = self.df[self.subjects].mean()
        lowest_subject = subject_means.idxmin()
        
        print(f"1. Focus on {lowest_subject} improvement - it has the lowest average score ({subject_means[lowest_subject]:.2f})")
        
        # Grade level recommendations
        grade_means = self.df.groupby('Grade_Level')['Average_Score'].mean()
        if grade_means.std() > 5:  # If there's significant variation
            lowest_grade = grade_means.idxmin()
            print(f"2. Provide additional support for {lowest_grade} grade students")
        
        # Individual recommendations
        at_risk_count = len(self.df[self.df['Average_Score'] < 70])
        if at_risk_count > 0:
            print(f"3. Implement intervention programs for {at_risk_count} at-risk students")
        
        # Correlation insights
        correlations = self.df[self.subjects].corr()
        highest_corr = correlations.unstack().drop_duplicates().nlargest(2).iloc[1]  # Second highest (first is 1.0)
        subjects_pair = highest_corr.name
        print(f"4. {subjects_pair[0]} and {subjects_pair[1]} are highly correlated - integrated teaching approach recommended")
        
        print("5. Continue monitoring student progress and adjust teaching strategies accordingly")
    
    def create_visualizations(self):
        """Create comprehensive visualizations"""
        print("\n=== CREATING VISUALIZATIONS ===")
        
        # Set up the plotting style
        plt.style.use('default')
        fig, axes = plt.subplots(3, 2, figsize=(15, 18))
        
        # 1. Subject Performance Distribution
        self.df[self.subjects].boxplot(ax=axes[0, 0])
        axes[0, 0].set_title('Subject Performance Distribution')
        axes[0, 0].set_ylabel('Scores')
        
        # 2. Grade Distribution
        grade_counts = self.df['Grade'].value_counts().sort_index()
        axes[0, 1].bar(grade_counts.index, grade_counts.values, color='skyblue')
        axes[0, 1].set_title('Grade Distribution')
        axes[0, 1].set_xlabel('Letter Grade')
        axes[0, 1].set_ylabel('Number of Students')
        
        # 3. Performance by Grade Level
        grade_level_avg = self.df.groupby('Grade_Level')['Average_Score'].mean()
        axes[1, 0].bar(grade_level_avg.index, grade_level_avg.values, color='lightgreen')
        axes[1, 0].set_title('Average Performance by Grade Level')
        axes[1, 0].set_xlabel('Grade Level')
        axes[1, 0].set_ylabel('Average Score')
        
        # 4. Gender Performance Comparison
        gender_subject_means = self.df.groupby('Gender')[self.subjects].mean()
        x = np.arange(len(self.subjects))
        width = 0.35
        
        axes[1, 1].bar(x - width/2, gender_subject_means.loc['Male'], width, label='Male', alpha=0.8)
        axes[1, 1].bar(x + width/2, gender_subject_means.loc['Female'], width, label='Female', alpha=0.8)
        axes[1, 1].set_title('Performance by Gender and Subject')
        axes[1, 1].set_xlabel('Subjects')
        axes[1, 1].set_ylabel('Average Score')
        axes[1, 1].set_xticks(x)
        axes[1, 1].set_xticklabels(self.subjects)
        axes[1, 1].legend()
        
        # 5. Correlation Heatmap
        correlation_matrix = self.df[self.subjects + ['Average_Score']].corr()
        im = axes[2, 0].imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
        axes[2, 0].set_xticks(range(len(correlation_matrix.columns)))
        axes[2, 0].set_yticks(range(len(correlation_matrix.columns)))
        axes[2, 0].set_xticklabels(correlation_matrix.columns, rotation=45)
        axes[2, 0].set_yticklabels(correlation_matrix.columns)
        axes[2, 0].set_title('Subject Correlation Matrix')
        
        # Add correlation values to heatmap
        for i in range(len(correlation_matrix.columns)):
            for j in range(len(correlation_matrix.columns)):
                axes[2, 0].text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', 
                               ha='center', va='center', color='black')
        
        # 6. Score Distribution Histogram
        axes[2, 1].hist(self.df['Average_Score'], bins=15, alpha=0.7, color='orange', edgecolor='black')
        axes[2, 1].axvline(self.df['Average_Score'].mean(), color='red', linestyle='--', 
                          label=f'Mean: {self.df["Average_Score"].mean():.1f}')
        axes[2, 1].set_title('Distribution of Average Scores')
        axes[2, 1].set_xlabel('Average Score')
        axes[2, 1].set_ylabel('Number of Students')
        axes[2, 1].legend()
        
        plt.tight_layout()
        plt.savefig('numpy-beginner-guide-/projects/student_performance_report.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Visualizations saved as 'student_performance_report.png'")

def main():
    """Main function to run the student performance analysis"""
    print("🎓 STUDENT PERFORMANCE ANALYSIS PROJECT")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = StudentPerformanceAnalyzer('../datasets/student_grades.csv')
    
    # Run all analyses
    analyzer.basic_statistics()
    analyzer.subject_analysis()
    analyzer.grade_level_analysis()
    analyzer.gender_analysis()
    analyzer.grade_distribution_analysis()
    analyzer.identify_top_performers()
    analyzer.identify_at_risk_students()
    analyzer.generate_recommendations()
    analyzer.create_visualizations()
    
    print("\n✅ Analysis complete! Check the generated report and visualizations.")

if __name__ == "__main__":
    main()