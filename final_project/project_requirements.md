# Capstone Project: Data Analysis and Visualization Dashboard

## Project Overview
Create a comprehensive data analysis and visualization dashboard that demonstrates mastery of Python programming, data manipulation, statistical analysis, and machine learning concepts covered throughout the course.

## Project Requirements

### Dataset
Students will work with a **sales and customer data** dataset containing:
- Customer demographics (age, gender, location, income)
- Product information (category, price, brand)
- Sales transactions (date, quantity, revenue)
- Customer behavior metrics (purchase frequency, average order value)

**Dataset Size**: ~10,000 records with 15+ features
**Format**: CSV file provided (`sales_data.csv`)

### Core Requirements

#### 1. Data Loading and Exploration (20 points)
- Load the dataset using pandas
- Display basic dataset information (shape, columns, data types)
- Identify and handle missing values appropriately
- Perform exploratory data analysis (EDA) with summary statistics
- Create initial data quality assessment

#### 2. Data Cleaning and Preprocessing (25 points)
- Clean inconsistent data formats
- Handle outliers using appropriate statistical methods
- Create derived features (e.g., customer lifetime value, purchase recency)
- Encode categorical variables appropriately
- Normalize/scale numerical features where needed

#### 3. Statistical Analysis (20 points)
- Perform descriptive statistics for key metrics
- Conduct correlation analysis between variables
- Implement hypothesis testing (e.g., t-tests, chi-square tests)
- Calculate confidence intervals for key business metrics
- Identify statistically significant patterns

#### 4. Data Visualization (25 points)
- Create at least 8 different types of visualizations using matplotlib/seaborn
- Include: histograms, scatter plots, box plots, heatmaps, time series plots
- Design interactive visualizations (optional bonus)
- Ensure all plots are properly labeled and formatted
- Create a dashboard layout organizing multiple visualizations

#### 5. Machine Learning Implementation (30 points)
- Implement at least 2 different ML algorithms:
  - Classification: Predict customer segment or purchase behavior
  - Regression: Predict sales revenue or customer value
- Split data into training/testing sets appropriately
- Evaluate model performance with multiple metrics
- Visualize model results and feature importance
- Discuss model limitations and business implications

#### 6. Business Insights and Recommendations (20 points)
- Summarize key findings from analysis
- Provide actionable business recommendations
- Identify opportunities for revenue growth
- Suggest customer retention strategies
- Create executive summary of insights

### Deliverables

#### Required Files:
1. **`analysis_notebook.ipynb`** - Main Jupyter notebook with complete analysis
2. **`requirements.txt`** - Python dependencies
3. **`README.md`** - Project documentation and setup instructions
4. **`presentation.pdf`** - 10-15 slide presentation of findings

#### Optional Bonus:
- Interactive dashboard using Streamlit or Dash (+10 points)
- Advanced ML techniques (ensemble methods, feature engineering) (+5 points)
- Automated report generation (+5 points)

## Input/Output Specifications

### Input:
- `sales_data.csv` - Main dataset file
- Project requirements document
- Technical hints document

### Output:
- Comprehensive analysis notebook
- Visualizations (saved as PNG/PDF files)
- Trained ML models (pickle files)
- Business insights report
- Presentation slides

## Correctness Criteria

### Technical Correctness (60%):
- **Code Quality**: Clean, well-commented, modular code
- **Data Handling**: Proper data cleaning and preprocessing
- **Statistical Methods**: Correct application of statistical tests
- **ML Implementation**: Proper train/test split, appropriate algorithms
- **Visualization**: Clear, informative, properly formatted plots

### Analysis Quality (25%):
- **Insight Depth**: Meaningful business insights derived from data
- **Statistical Rigor**: Appropriate use of statistical methods
- **Interpretation**: Clear explanation of results and implications
- **Recommendations**: Actionable business recommendations

### Presentation (15%):
- **Documentation**: Clear README and code comments
- **Organization**: Logical flow of analysis
- **Communication**: Effective presentation of findings
- **Professional Quality**: Polished deliverables

## Grading Rubric

### Excellent (90-100 points):
- All requirements met with exceptional quality
- Advanced techniques implemented
- Deep business insights with clear recommendations
- Professional presentation and documentation
- Bonus features implemented

### Good (80-89 points):
- All core requirements met
- Solid technical implementation
- Good business insights
- Clear presentation
- Minor areas for improvement

### Satisfactory (70-79 points):
- Most requirements met
- Adequate technical implementation
- Basic business insights
- Acceptable presentation
- Some technical or analytical gaps

### Needs Improvement (60-69 points):
- Several requirements not fully met
- Technical implementation has issues
- Limited business insights
- Presentation needs work
- Significant gaps in analysis

### Unsatisfactory (<60 points):
- Major requirements missing
- Poor technical implementation
- No meaningful insights
- Inadequate presentation
- Fundamental understanding gaps

## Timeline
- **Week 1**: Data exploration and cleaning
- **Week 2**: Statistical analysis and visualization
- **Week 3**: Machine learning implementation
- **Week 4**: Business insights and presentation preparation

## Submission Guidelines
- Submit all files in a single ZIP archive
- Ensure notebook runs without errors
- Include all generated visualizations
- Provide clear setup instructions in README
- Presentation should be 10-15 minutes for live demo

## Academic Integrity
- Original work required
- Proper citation of external resources
- Collaboration allowed for discussion, but individual submission required
- Plagiarism will result in project failure

