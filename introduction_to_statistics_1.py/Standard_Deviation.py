# An important characteristic of datasets is how much variability exists among individual samples. Without a measure of variability, you can’t effectively compare two datasets.

# For example, if one dataset consists of the values [99, 100, 101], and another dataset consists of the values [0, 100, 200], they both have the same mean and median values of 100, 
# yet they have very different amounts of variability. T
# here is a large amount of variability in the second dataset compared to the first.

# The variability is often a defining characteristic of a dataset. The standard deviation is perhaps the most informative and certainly the most widely used measure of a dataset's variability. 
# Let's look at how it's calculated.

# Let's use the ten values below to calculate the standard deviation of a dataset. We are interested in the average difference between each value in the distribution and the mean of the distribution.

# We first need to calculate the mean, as shown below.


# Next, the average difference (or deviation) is calculated by taking each individual value and subtracting the mean from that value. 
# Once we calculate a deviation score for each individual value in the distribution, we can then sum the deviation scores and divide by n to get the average, which would be the standard deviation.

# However, there's one problem. Half of the deviation scores fall below the mean, and half fall above the mean. This means that when we sum these deviation scores together, we will get zero, as shown below. 
# And zero divided by any number will be zero. 
# Therefore, we need to do something to work around this issue.


# We can make each deviation score positive by squaring it. Hence, for each value in the distribution, we subtract the mean of the distribution and then square the deviation. We then add up all of these squared deviations, giving us the sum of the squared deviations. 
# The calculations are shown below.


# Note: In the image above, notice that the original column is named "Feature". In bioinformatics, what some may call a column, field, or independent variable is called a "feature". 
# A feature is the generic name for any column within a dataset. 
# It will be helpful to get used to the terminology commonly used in data science and bioinformatics.
# We next divide by n (the number of samples in the distribution) minus one to get the average of the squared deviations. This is known as the variance. See the calculation below.

# Alert: To get the variance, if the dataset is a sample, then we divide the sum of squares by n-1. If the dataset is a population, then we divide by n. 
# Here, we divide by n-1 (10 - 1 = 9) as we assume that this small dataset is a sample from a larger population. 
# In brief, the reason that this is done is because most of the time we do not know the population average and we estimate it with the sample average. The sample average tends to underestimate the population average, 
# so we compensate for this by dividing by n-1 rather than n.

# Because we previously needed to square each deviation score to avoid getting a sum of zero, we now need to reverse that process. 
# This is accomplished by taking the square root of the variance, and the result gets our values back into their original terms. 
# The square root of the variance is known as the standard deviation.



# Note: You rarely, if ever, will need to calculate the standard deviation on your own, but it can be instructive to understand how it's calculated and, particularly, what it means. 
# It is a measure of, on average, how much individual samples within a data set vary from the middle. This enables us to compare the columns within a data set that may be measured on different scales. 
# And it allows a to compare differences between different data sets.

import pandas as pd
dataset = pd.DataFrame(data =[0, 1, 2, 3, 4, 5, 5, 6, 7, 7], columns = ["numbers"])
dataset
# numbers
# 0	0
# 1	1
# 2	2
# 3	3
# 4	4
# 5	5
# 6	5
# 7	6
# 8	7
# 9	7

# Display the standard deviation
dataset["numbers"].std()
# 2.449489742783178





# An effective way to understand a data distribution is to describe the center of the data--it's central tendency. 
# The mean, median and mode are the fundamental ways to do this and are the most basic descriptive statistics functions.

# Create a basic data set
# We'll create a Pandas DataFrame containing ten values. We'll name the column "numbers".
import pandas as pd
dataset = pd.DataFrame(data =[0, 1, 2, 3, 4, 5, 5, 5, 7, 8], columns = ["numbers"])
dataset
numbers
# 0	0
# 1	1
# 2	2
# 3	3
# 4	4
# 5	5
# 6	5
# 7	5
# 8	7
# 9	8

# Preview our dataset
# The numbers on the right are the values in our dataset. 
# The numbers on the left are the index positions of the respective values.​
dataset["numbers"]
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# 6    5
# 7    5
# 8    7
# 9    8
# Name: numbers, dtype: int64



# Mean
# The mean is the average of a set of values. To attain the mean value, we sum the values and then divide by the number of values. The mean of our dataset is 4.0.
# The mean is useful because it typically indicates where the "center of gravity" is for a set of values.

# Sum the values
# sum() is the method that adds up a set of values.​
dataset["numbers"].sum()
# 40

# Get the number of values
# len() is the "length" function and returns how many values are in the dataset passed to it.​
len(dataset["numbers"])
# 10

# Calculate the mean value
dataset["numbers"].sum()/len(dataset)
# 4.0

# Get the mean value
# mean() is the method that returns the average value of a set of values.​
dataset["numbers"].mean()
# 4.0



# Median
# If our values are ordered (as the values in our dataset are), the median is the middle-most value if there are an odd number of values.
# If there are an even number of values, then we average the two center-most values. In our dataset, we have an even number of values so we will average the two center values ( 4 and 5) to attain a median value of 4.5. 
# This value is slightly different from our mean value, but is another way to describe the center of our data.

# The median is useful in that, unlike the mean, it is fairly unaffected by outliers.

# Get the median value
dataset["numbers"].median()
# 4.5



# Mode
# The mode is the most frequently occurring value or set of values. If any values are tied in terms of their frequency, then those values will be reported as modes together, 
# and the dataset is said to be bimodal or multimodal. 
# It's most useful when your data is repetitive and you want to identify which values occur most frequently. For our dataset, the most frequently occuring value is 5.
# Our mode value is a little different from both the mean (4.0) and median (4.5) values, but can also be used to describe the central tendency of a dataset.

# Get the mode value
# mode() is the method that returns the most frequently occuring value(s) within a set of values.
dataset["numbers"].mode()[0]
# 5

# However, if there are extreme outliers (a value that is much higher or lower than the rest of the values), they will cause the mean to shift significantly in the direction of the outliers,
# whereas the median is fairly unaffected.

# Alert: When the mean and median have a wide difference between them, that means the data is skewed and there are outliers present.
# Therefore, the median is especially useful when the mean is skewed by outliers -- it can more accurately describe the center of the data.

# Tip: Feel free to edit the sample numbers and observe how it affects the mean, median, and mode. You will notice that if you skew the data with very large or very small values, the median is fairly unaffected, 
# while the mean will be pulled in the direction of the outlier.
# The NightSignal Algorithm uses wearable data to detect pre-symptomatic and asymptomatic COVID-19 infections. The NightSignal Algorithm module on the Research page provides an example of the use of central tendency.

# It calculates the average resting heart rate (RHR) overnight each day for each individual, and then uses the median value as the healthy baseline. 
# The median often gives a better sense of what a “typical” value is, which helps provide an intuition about the dataset.


# Question 1

# Which of the following is true regarding standard deviation?


# It is the average squared distance from the mean value.

# It is the average absolute distance from the mean value.

# It measures the variability among the individual samples.   ====> correct-answer

# It is the square of the variance


# Question 2

# Which of the following is false regarding normalization?


# It may also be referred to as min-max scaling.

# It allows us to convert all values into numeric values so that they can be compared. ====> correct-answer

# It effectively enables us to compare numeric values that may be measured in different units.

# It is scaling numeric values to within a standard range.

  
# Question 3

# Which of the following is false?


# If two data sets have the same mean, their variances can differ.

# If two data sets have the same variance, their means can differ.

# For a given data set, the variance and standard deviation are equivalent.  ====> correct-answer

# The standard deviation of a data set can be said to represent the expected distance of a data point from the mean.




# Question 4

# Which of the following is false regarding central tendency?


# The median value will always be a value belonging to the dataset.  ====> correct-answer

# The mean is the average value in the dataset.

# The mode may not be a value at the center of the dataset.

# The mode is a value in the dataset that occurs at least as frequently as any other value.
