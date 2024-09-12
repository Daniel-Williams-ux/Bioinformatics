#                                                                                                      Proteomics Data Analysis
# Background
# We will be focusing our analyses on a patient (i.e. Patient Z) from the Integrated Personal Omics Profiling (iPOP) study. 
# Designed and performed at Stanford University, iPOP aims to understand what “healthy" biochemical and physiological profiles look like at a personal level, and what happens when people become ill. 
# This provides the basis for personalized precision medicine, which attempts to tailor medical decisions and treatments to a patient's individual omics profile.

# IPOP is a longitudinal study that follows 106 patients, and collects samples at regular intervals over several years through sickness and health. The iPOP cohort also contains a significant proportion of pre-diabetic patients. 
# Therefore, another focus of the study was to better understand how omics are influenced by a pre-diabetic state and the progression from pre-diabetes to either a normal healthy state or diabetes.

# In this module, we will be reading and visualizing the proteomics data using Python. In our analyses, we will focus on a specific time period when Patient Z experienced an infection (and eventually recovered). 
# By the end of this module, we will be able to interpret visualizations of the data and find interesting correlations.

# Load data
# Let's read our proteome abundances file named abundance.csv using the Python Pandas library. index_col=0 sets the first entry in each row of the file as the row name.

# In our data, labeled row indices are the timepoint when each of the samples were collected (corresponding to different stages of the infection). Unlabeled (integer) row indices are other samples that were collected from Patient Z. 
# Each column name represents a different protein.

import pandas as pd

data = pd.read_csv('data/abundance.csv', index_col=0)
data
# 	IGLL5	MASP2	APOL1	CEP290	CD5L	FCN3	ATRN	ATRN.1	APOM	CP	...	PCYOX1	SERPINA10	MAN2B2	ATP11B	TLN1	AFG3L2	LYVE1	FCGBP	ZNF10	FAM161B
# Infection_Early	3.007525	-3.538002	2.075924	-5.796386	-0.099187	0.712399	-1.041871	-2.023487	2.810211	5.597555	...	-2.354241	-1.762042	-2.280897	-1.049495	-1.076730	-4.657650	-2.812472	-1.663895	-1.682703	-5.757788
# Infection_Middle	0.863756	-3.620376	1.965186	-6.757326	1.682255	0.403723	-1.336249	-1.117450	3.030691	5.299970	...	-2.562540	-0.846520	-5.044808	-0.978259	-2.068356	-4.457742	-3.100214	-1.893479	-4.537362	-6.926365
# Infection_Late	2.889091	-3.485240	2.132138	-4.976074	-1.264688	1.003873	-1.166469	-2.992944	2.661346	5.969330	...	-2.978880	-2.449609	-3.713851	-0.540103	-1.085205	-4.092226	-3.221125	-1.842757	-4.067586	-4.967957
# Infection_Recovery_Early	0.824791	-3.374524	1.733176	-4.988127	-1.224756	0.681956	-1.045665	-1.378891	1.851585	5.516712	...	-3.447273	-3.854187	-0.042026	-2.945349	-4.562067	-4.352034	-3.225586	-1.946335	-4.634648	-5.068154
# Infection_Recovery_Late	3.557581	-5.187031	2.344245	-3.159375	-1.788122	0.423707	-0.381359	-2.145862	2.875468	4.459722	...	-3.860832	-2.685537	-5.922687	-1.291413	-4.724151	-2.354904	-4.209470	-3.957724	-5.360170	-5.433125
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 945	2.500616	-3.522353	2.020096	-4.831130	-0.722484	0.449396	-1.210629	-1.703472	2.584753	5.697784	...	-2.066328	-2.370973	-4.046711	-1.458394	-3.368627	-3.431323	-3.600972	-2.425012	-5.150124	-4.364632
# 946	2.392775	-3.323587	1.259214	-5.601685	-0.495903	0.436228	-1.273842	-1.935246	2.416891	5.719248	...	-2.547156	-1.782187	-1.932357	-1.428483	-1.487231	-5.292956	-3.795883	-3.887947	-3.760686	-5.376896
# 947	0.408994	-5.489279	2.259605	-4.252906	-0.508294	0.250123	-1.486528	-1.899872	3.167179	6.521357	...	-3.465681	-4.518335	-2.614612	-1.060737	-0.629035	-3.861400	-3.036173	-1.470154	-5.475474	-6.099372
# 948	6.597984	-3.821952	1.000675	-4.090896	-0.930555	1.531808	-1.339883	-3.493927	3.002731	3.426317	...	-4.456287	0.108330	-0.489510	-0.411444	-1.890894	-3.963952	-5.263563	-2.481273	-3.685620	-6.556203
# 949	2.136551	-3.320252	1.934733	-4.823840	-0.899162	0.278172	-1.484490	-2.267659	2.576371	5.914509	...	-2.800058	-2.187146	-2.187981	-1.517041	-3.063948	-3.241324	-3.819436	-2.353275	-6.722829	-4.466754
# 950 rows × 302 columns

# To get an overview of our data, we could take a look at the number of samples and proteins by examining the shape of the DataFrame.

nRows, nCols) = data.shape
print('Our dataset contains the abundance data for', nCols, 'proteins from', nRows, 'samples.')
# Our dataset contains the abundance data for 302 proteins from 950 samples.


# Checking our data
# Now, let's make sure our data makes sense. You do not have to worry to much about this code, but we are using a for loop and the iloc function to locate each row. np.argmax gets the index of the maximum value within each row. 
# We can then print the most abundant protein and sample name by using our indices to access the indices (timepoints) and columns (protein names) from our data table.

import numpy as np

for i in range(5):
  j = np.argmax(data.iloc[i, :])
  print(data.columns[j], 'is the protein with the highest abundance in the', data.index[i], 'sample.')
# ALB is the protein with the highest abundance in the Infection_Early sample.
# ALB is the protein with the highest abundance in the Infection_Middle sample.
# ALB is the protein with the highest abundance in the Infection_Late sample.
# ALB is the protein with the highest abundance in the Infection_Recovery_Early sample.
# ALB is the protein with the highest abundance in the Infection_Recovery_Late sample.
# Sanity Check: ALB (albumin) is the most abundant protein in human blood. It checks out that each of our 5 labeled samples has albumin as the most abundant protein.

# Plotting
# Since the quantities of each of the proteins assayed vary in scale, we will scale these measurements to a value between 0 and 1. We obtain this relative abundance for each protein 
# by subtracting the minimum abundance from all measurements the measurements of the specific protein. This gives us the minimum value of 0. Then, we can ensure the maximum value is 1 by dividing all of the shifted measurements 
# by the maximum value (maximum abundance - minimum abundance).

relativeAbundance = []
for protein in range(data.shape[1]):
  minAbundance = min(data.iloc[:, protein])
  maxAbundance = max(data.iloc[:, protein])
  relativeAbundance.append((data.iloc[:, protein] - minAbundance) / (maxAbundance - minAbundance))
relativeAbundance = pd.DataFrame(relativeAbundance)
relativeAbundance.iloc[0:10, :5]
# Infection_Early	Infection_Middle	Infection_Late	Infection_Recovery_Early	Infection_Recovery_Late
# IGLL5	0.593908	0.388380	0.582554	0.384645	0.646643
# MASP2	0.612012	0.600172	0.619595	0.635509	0.374994
# APOL1	0.793306	0.776706	0.801732	0.741927	0.833527
# CEP290	0.449252	0.337372	0.544759	0.543356	0.756273
# CD5L	0.496534	0.711321	0.356010	0.360824	0.292899
# FCN3	0.645706	0.598971	0.689837	0.641097	0.601997
# ATRN	0.614819	0.555043	0.589518	0.614048	0.748940
# ATRN.1	0.514654	0.635750	0.385082	0.600808	0.498298
# APOM	0.928950	0.952998	0.912713	0.824390	0.936068
# CP	0.739081	0.687215	0.803877	0.724991	0.540770


# Now, we are ready to plot our data using a heatmap. Using the seaborn package, we can plot our relative abundances for the first 20 of our proteins of interest from our samples. 
# We choose to plot this data using a heatmap, because it allows us to easily visualize changes in protein abundance over time (by simply comparing colors). Here, we choose to plot just the first 20 proteins to produce a reasonably sized heatmap. 
# However, we could make additional plots for all the remaining proteins.

import seaborn as sns

df = relativeAbundance.iloc[0:20, :5]
ax = sns.heatmap(df, vmin=0, vmax=1)
ax.figure
#===> Heat map diagram
