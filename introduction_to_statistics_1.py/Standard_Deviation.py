# An important characteristic of datasets is how much variability exists among individual samples. Without a measure of variability, you can’t effectively compare two datasets.

# For example, if one dataset consists of the values [99, 100, 101], and another dataset consists of the values [0, 100, 200], they both have the same mean and median values of 100, yet they have very different amounts of variability. T
# here is a large amount of variability in the second dataset compared to the first.

# The variability is often a defining characteristic of a dataset. The standard deviation is perhaps the most informative and certainly the most widely used measure of a dataset's variability. Let's look at how it's calculated.

# Let's use the ten values below to calculate the standard deviation of a dataset. We are interested in the average difference between each value in the distribution and the mean of the distribution.

# We first need to calculate the mean, as shown below.


# Next, the average difference (or deviation) is calculated by taking each individual value and subtracting the mean from that value. 
# Once we calculate a deviation score for each individual value in the distribution, we can then sum the deviation scores and divide by n to get the average, which would be the standard deviation.

# However, there's one problem. Half of the deviation scores fall below the mean, and half fall above the mean. This means that when we sum these deviation scores together, we will get zero, as shown below. And zero divided by any number will be zero. 
# Therefore, we need to do something to work around this issue.


# We can make each deviation score positive by squaring it. Hence, for each value in the distribution, we subtract the mean of the distribution and then square the deviation. We then add up all of these squared deviations, giving us the sum of the squared deviations. 
# The calculations are shown below.


# Note: In the image above, notice that the original column is named "Feature". In bioinformatics, what some may call a column, field, or independent variable is called a "feature". A feature is the generic name for any column within a dataset. 
# It will be helpful to get used to the terminology commonly used in data science and bioinformatics.
# We next divide by n (the number of samples in the distribution) minus one to get the average of the squared deviations. This is known as the variance. See the calculation below.

# Alert: To get the variance, if the dataset is a sample, then we divide the sum of squares by n-1. If the dataset is a population, then we divide by n. Here, we divide by n-1 (10 - 1 = 9) as we assume that this small dataset is a sample from a larger population. 
# In brief, the reason that this is done is because most of the time we do not know the population average and we estimate it with the sample average. The sample average tends to underestimate the population average, 
# so we compensate for this by dividing by n-1 rather than n.

# Because we previously needed to square each deviation score to avoid getting a sum of zero, we now need to reverse that process. This is accomplished by taking the square root of the variance, and the result gets our values back into their original terms. 
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
