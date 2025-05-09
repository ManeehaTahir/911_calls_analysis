# 911 Calls Data Analysis

A data analysis and visualization project focused on 911 emergency calls in Montgomery County, Pennsylvania. This project was completed as part of the **Coursera practice project** from the course [Applied Data Science with Python and SQL](https://www.coursera.org/projects/practice-applied-data-science-python-sql).

##  Objective

To explore and analyze real-world emergency call data using Python, with a focus on identifying trends, peak times, and common reasons for 911 calls. The project demonstrates data manipulation, visualization, and analytical thinking skills.


## Dataset

- **Source:** Provided in the Coursera practice project
- **File:** `911.csv`
- **Details:** The dataset includes over 50,000 emergency call records with fields such as:
  - `zip`, `twp` (location info)
  - `title` (includes reason for call)
  - `timeStamp`, `addr`
  - `lat`, `lng`


##  Technologies Used

- **Python** (Pandas, NumPy)
- **Data Visualization:** Seaborn, Matplotlib
- **IDE:** PyCharm



##  Key Insights & Visualizations

- **Top 10 Zipcodes** with most calls.
- **Top 4 Townships** receiving calls.
- **Call Reasons** extracted from titles (EMS, Fire, Traffic).
- **Bar Charts and CountPlots** to show distribution by:
  - Reason
  - Day of Week
  - Month
- **Heatmap** to visualize call volume across days and reasons.



##  What I Learned

- Efficient use of `pandas` for grouping, filtering, and manipulating data.
- Creating meaningful visualizations using `seaborn` and `matplotlib`.
- Extracting new features from existing columns (e.g., extracting "Reason" from "title", creating day/month columns from timestamps).
- Understanding real-life application of data analysis to emergency services.



##  Skills Demonstrated

- Data Cleaning & Preparation  
- Exploratory Data Analysis (EDA)  
- Feature Extraction  
- Data Visualization & Interpretation  



##  How to Run

1. Clone the repository.
2. Ensure Python and required libraries are installed:
   ```bash
   pip install pandas matplotlib seaborn

## Profiles
- https://www.linkedin.com/in/maneeha-tahir/
- https://github.com/ManeehaTahir