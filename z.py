import pandas as pd
import numpy as np
import scipy.stats as stats
import random

# Step 1: Read original dataset
student_df = pd.read_csv('C:/Users/brais/OneDrive/Desktop/today/students-1.csv')

# Step 2: Filter the students who are graduated
graduated_student_df = student_df[student_df['graduated'] == 1]

# Step 3: Random sample for 500 students
unique_student_id = list(graduated_student_df['stud.id'].unique())
random.seed(30)  # Set seed for reproducibility
sample_student_id = random.sample(unique_student_id, min(500, len(unique_student_id)))  # Ensure max of 500 samples
sample_df = graduated_student_df[graduated_student_df['stud.id'].isin(sample_student_id)].reset_index(drop=True)

# Step 4: Select two variables of interest: 'major' and 'salary'
sample_df = sample_df[['major', 'salary']]

# Step 5: Remove rows with missing salary values (NA)
sample_df = sample_df.dropna(subset=['salary'])

# Step 6: Create ANOVA backbone table
data = [['Between Groups', '', '', '', '', '', ''], 
        ['Within Groups', '', '', '', '', '', ''], 
        ['Total', '', '', '', '', '', '']]
anova_table = pd.DataFrame(data, columns = ['Source of Variation', 'SS', 'df', 'MS', 'F', 'P-value', 'F crit'])
anova_table.set_index('Source of Variation', inplace = True)

# Step 7: Calculate SSTR (Sum of Squares for Treatment/Between Groups)
x_bar = sample_df['salary'].mean()  # Overall mean salary
group_means = sample_df.groupby('major')['salary'].mean()  # Mean salary per major
group_counts = sample_df.groupby('major')['salary'].count()  # Number of students per major
SSTR = np.sum(group_counts * (group_means - x_bar) ** 2)
anova_table.loc['Between Groups', 'SS'] = SSTR

# Step 8: Calculate SSE (Sum of Squares for Error/Within Groups)
group_stds = sample_df.groupby('major')['salary'].std()  # Standard deviation per major
SSE = np.sum((group_counts - 1) * (group_stds ** 2))
anova_table.loc['Within Groups', 'SS'] = SSE

# Step 9: Calculate SST (Total Sum of Squares)
SST = SSTR + SSE
anova_table.loc['Total', 'SS'] = SST

# Step 10: Calculate degrees of freedom (df)
df_between = sample_df['major'].nunique() - 1  # Degrees of freedom for Between Groups
df_within = sample_df.shape[0] - sample_df['major'].nunique()  # Degrees of freedom for Within Groups
df_total = sample_df.shape[0] - 1  # Total degrees of freedom

anova_table.loc['Between Groups', 'df'] = df_between
anova_table.loc['Within Groups', 'df'] = df_within
anova_table.loc['Total', 'df'] = df_total

# Step 11: Calculate Mean Square (MS)
anova_table.loc['Between Groups', 'MS'] = anova_table.loc['Between Groups', 'SS'] / df_between
anova_table.loc['Within Groups', 'MS'] = anova_table.loc['Within Groups', 'SS'] / df_within

# Step 12: Calculate F-ratio
anova_table.loc['Between Groups', 'F'] = anova_table.loc['Between Groups', 'MS'] / anova_table.loc['Within Groups', 'MS']

# Step 13: Calculate P-value
p_value = 1 - stats.f.cdf(anova_table.loc['Between Groups', 'F'], df_between, df_within)
anova_table.loc['Between Groups', 'P-value'] = p_value

# Step 14: Calculate F-critical (at significance level 0.05)
alpha = 0.05
f_critical = stats.f.ppf(1 - alpha, df_between, df_within)
anova_table.loc['Between Groups', 'F crit'] = f_critical

# Step 15: Print the final ANOVA table
print(anova_table)




