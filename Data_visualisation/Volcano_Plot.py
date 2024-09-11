# A volcano plot is a 2-dimensional scatter plot that has the shape of a volcano. 
# It makes it easy to visualize the expression of thousands of genes obtained from -omics research (e.g., transcriptomics, genomics, proteomics, etc.) and to identify genes with significant changes. 
# It is used to plot the log fold change in the observation between two conditions (e.g., the gene expression between comparison and control conditions) on the x-axis. 
# On the y-axis is the corresponding p-value for each observation, representing the statistical significance of the change (if any) between the different conditions.

# A volcano plot can visualize a lot of complex information in one plot. The wider the dispersion of data points in the volcano plot the greater the significance in gene expression changes between two conditions.

# Image: refer to Volcano Plot.png
# In the volcano plot shown above, the x-axis displays the magnitude of the log2-fold change in gene expression between control and treatment conditions. On the y-axis is the level of statistical significance 
# of the observed change. For example, the red points indicate genes that display both large-magnitude fold changes (x-axis) as well as high statistical significance (-log10 p-value, y-axis). 
# The dashed green line shows the p-vaule cutoff of 0.01 (10-2) with points above the line having a p-value < 0.01 and points below the line having a p-value > 0.01. 
# The vertical dashed blue lines indicate log2-fold changes of ±2. 
# Therefore, all red dots exhibit log2-fold changes beyond ±2 (four-fold change) and statistical significance less than 0.01.

# Reading a Volcano Plot
# To be clear, the x-axis of a Volcano plot represents the amount of change following a condition or experiment. The zero (0) point on the x-axis represents no change. 
# For every point increment to the right of 0, the amount of the change doubles. For example, 1 on the x-axis represents an increase of twice the original (control) value,
# 2 on the x-axis represents an increase of 4 times the original value, and 3 on the x-axis represents an increase of 8 times the original value. 
# Every point below 0 is interpreted similarly except that it represents a decrease in the original (control) value.

# The y-axis of a Volcano plot represents the significance of the change on the x-axis in p-values (probability values). The zero (0) point on the y-axis represents a p-value of 1.0. 
# For every point increase on the y-axis, the decimal point of the p-value moves one place to the left. For example, 2 on the y-axis is equivalent to a p-value of .01, 
# which can be interpreted as there's appoxiamtely a 1% chance that you could get the value that you observed, assuming that there is no difference between the control and experimental conditions. 
# In other words, it suggests that the observation appears to be significant. (A 3 on the y-axis would represent a p-value of .001, a 4 would represent a p-value of .0001, etc.)



# Sample data set
The sample data below shows gene names, log2-fold changes, and the p-values for the observed changes.

import pandas as pd
from bioinfokit import analys, visuz

df = pd.read_csv("data/data_volcano_plot/volcano_data.csv")

df.head()
#     GeneNames	         log2FC  	p-value
# 0	LOC_Os09g01000.1	-1.886539	1.250000e-55
# 1	LOC_Os12g42876.1	3.231611	1.050000e-55
# 2	LOC_Os12g42884.2	3.179004	2.590000e-54
# 3	LOC_Os03g16920.1	5.290677	4.690000e-54
# 4	LOC_Os05g47540.4	4.096862	2.190000e-54

