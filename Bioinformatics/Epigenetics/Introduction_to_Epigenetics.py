#                                                 Introduction to Epigenetics
# Epigenetics is a field of study focused on changes in DNA that do not involve alterations to the underlying sequence. 
# In comparison to static nature of the genome, epigenetics is dynamic, and change substantially during development, aging, cancers and in response to environmental exposure.

# Chemical modification of DNA and the protein that interact with DNA can change the degrees to which genes are switched ON or OFF, causing an effect on the phenotype. 
# The most common epigenetic regulation include DNA methylation, histone modifications, and non-coding RNAs.

# The collection of all epigenetic changes in a genome is called an epigenome. In this module, you will learn approaches to study epigenomes, and interpret them.

                                               # Epigenetic assays
# DNA methylation analysis

# Cytosine methylation (5-methylcytosine, 5mC) is one of the main covalent base modifications in eukaryotic genomes, generally observed on CpG dinucleotides. 
# Once methyl compounds are present on a gene, the gene is muted, or turned off. As a result, no protein is generated. That is how DNA methylation regulates gene expression.

# Genome-wide DNA methylation can be mapped using either Whole Genome Bisulphite Sequencing (WBGS), Reduced-Representation Bisulfite Sequencing (RRBS), Methylation-sensitive Restriction Enzyme (MRE)
# and immunoprecipitation based assays.


#                                              Histone modification analysis

# DNA is wrapped around a protein complex called the histone complex. Histones form a chain of beads along the DNA. 
# Histone modifications at specific locations (e.g., lysine acetylation and methylation) can affect whether a gene is wrapped or unwrapped ("ON" versus "OFF"). This alters the expression of genes.

# Proteins that read genes cannot reach DNA wrapped tightly around histones. 
# Consequently, this mechanism switches some genes off because the DNA is wrapped around the histone proteins, and is inaccessible to the proteins that read DNA to make RNA, whereas other genes 
# get expressed because they are not wrapped around histones.

# Genome-wide histone modifications can be measured using ChIP-Sequencing. 
# ChIP-Seq, a combination of chromatin immunoprecipitation (ChIP), and massively parallel sequencing, delves into the interactions between proteins, DNA, and RNA, revealing critical regulatory events in many biological processes and disease states. 
# ChIP-Seq is used to identify transcription factor binding sites, track histone modifications across the genome, and constrain chromatin structure and function.

                                                The data
# In this module we will take a look at the epigenome data (DNA methylation and histone modifications) from human reference epigenomes generated as part of NIH Roadmap Epigenomics Program. 
# You can learn more at: https://egg2.wustl.edu/roadmap/web_portal/index.html

# Differentially Methylated Region (DMR) calls across reference epigenomes

# As a general resource for epigenomic comparisons across all epigenomes, Differentially Methylated Region (DMR) were defined using the Lister et al method (Lister et al., 2013), combining all 
# Differentially Methylated Sites (DMSs) within 250bp of one another into a single DMR, and excluding any DMR with less than 3 DMSs.

# For each DMR in each sample, average methylation level was computed, weighted by the number of reads overlapping it (Schultz et al., 2012). 
# This resulted in a methylation level matrix with rows of DMRs and columns of samples.


#Whole Genome Bisulphite Sequencing data from 111 reference epigenomes
import sys
import os
# import pyathena
import pandas as pd

import gzip
wgbs = pd.read_csv('https://egg2.wustl.edu/roadmap/data/byDataType/dnamethylation/DMRs/WGBS_DMRs_v2.tsv.gz',sep='\t')

! wget https://egg2.wustl.edu/roadmap/data/byDataType/dnamethylation/DMRs/WGBS_DMRs_v2.tsv.gz

print(wgbs.head(10))
# chr  start    end  methylation_level_E003  methylation_level_E004  \
# 0   1  10469  10525                0.858447                0.900000   
# 1   1  10577  10620                0.918367                0.944444   
# 2   1  10641  10776                     NaN                     NaN   
# 3   1  10931  11184                     NaN                     NaN   
# 4   1  13417  13537                0.882353                1.000000   
# 5   1  13823  14062                     NaN                     NaN   
# 6   1  14553  15189                0.666667                0.912281   
# 7   1  17406  17492                0.907216                0.904762   
# 8   1  19132  19189                     NaN                     NaN   
# 9   1  26790  27026                0.200000                0.733333   

#    methylation_level_E005  methylation_level_E006  methylation_level_E007  \
# 0                0.939236                0.952862                0.956916   
# 1                0.943662                0.944785                0.910180   
# 2                     NaN                0.843137                0.777778   
# 3                     NaN                     NaN                     NaN   
# 4                0.976562                0.968421                0.893204   
# 5                     NaN                     NaN                     NaN   
# 6                0.920000                0.912409                0.948905   
# 7                0.935728                0.974026                0.961326   
# 8                     NaN                     NaN                1.000000   
# 9                0.638889                     NaN                0.625000   

#    methylation_level_E008  methylation_level_E011  ...  \
# 0                0.943662                0.957043  ...   
# 1                0.653061                0.777778  ...   
# 2                0.169811                0.390533  ...   
# 3                     NaN                     NaN  ...   
# 4                0.921986                0.917808  ...   
# 5                     NaN                     NaN  ...   
# 6                0.865772                0.843854  ...   
# 7                0.928315                0.881089  ...   
# 8                0.857143                0.722222  ...   
# 9                0.590164                0.640000  ...   

#    methylation_level_E097  methylation_level_E098  methylation_level_E100  \
# 0                0.766798                0.822034                0.815094   
# 1                0.526786                0.575342                0.687500   
# 2                0.372093                0.280000                0.000000   
# 3                0.000000                     NaN                0.000000   
# 4                0.674419                0.491228                0.411765   
# 5                0.375000                0.750000                0.250000   
# 6                0.824324                0.797386                0.832061   
# 7                0.857143                0.926724                0.950820   
# 8                1.000000                0.916667                1.000000   
# 9                0.422222                0.696970                0.540000   

#    methylation_level_E104  methylation_level_E105  \
# 0                0.809160                0.867347   
# 1                0.645833                0.550725   
# 2                0.054795                0.245283   
# 3                0.000000                0.000000   
# 4                0.543860                0.646154   
# 5                0.428571                0.571429   
# 6                0.651515                0.807229   
# 7                0.923077                0.923077   
# 8                1.000000                0.000000   
# 9                0.750000                0.480000   

#    methylation_level_E106_STL001  methylation_level_E106_STL003  \
# 0                       0.829882                       0.922297   
# 1                       0.616393                       0.680723   
# 2                       0.785276                       0.705128   
# 3                       0.565891                            NaN   
# 4                       0.450382                       0.373737   
# 5                       0.500000                            NaN   
# 6                       0.911854                       0.881890   
# 7                       0.968254                       0.945525   
# 8                       0.937500                       1.000000   
# 9                       0.791304                       0.705882   

#    methylation_level_E109  methylation_level_E112  methylation_level_E113  
# 0                0.829787                0.884615                0.857741  
# 1                0.676806                0.540000                0.662745  
# 2                0.757303                0.868421                0.782918  
# 3                0.604651                     NaN                0.473684  
# 4                0.550000                0.425532                0.260870  
# 5                0.666667                1.000000                0.900000  
# 6                0.887147                0.977778                0.888268  
# 7                0.926984                0.975000                0.972050  
# 8                0.941176                     NaN                1.000000  
# 9                0.918605                0.883721                0.666667  

# [10 rows x 43 columns]
# The data matrix shows rows of DMRs and columns of samples including chromosome number, location 'start' and 'end'.

# chr: Chromosome.
# start: Start of the location.
# end: End of the location.
# Metadata on the samples used in the analysis are available here. https://docs.google.com/spreadsheets/d/1yikGx4MsO9Ei36b64yOy9Vb6oPC5IBGlFbYEt-N6gOM/edit#gid=15

# Querying DNA methylation and histone modification states of genes in UCSC genome Browser

# FractionMethylation.tar.gz files are used for visualization of DNA methylation states, and provides fractional methylation calls at CpG. It contains 25 files. One for each chromosome.

# Format of each file: Tab separated table CpGs (rows) X epigenomes (columns) Methylation calls are round to two decimal digits.

# Each file has the same matrix format:

# The first column is a position of C or G in the CpG
# The rest of the columns are epigenomes.
# Only CpG info is present (as it came from EDACC files); for those CpG where coverage was <=3 we - for both coverage and Methylation (as missing data)

# For ChIP-Seq data visualization, negative log10 of the Poisson p-value of ChIP-seq counts relative to expected background counts local were used. 
# These signal confidence scores provides a measure of statistical significance of the observed enrichment.

# The NCBI RefSeq Genes composite track shows human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq) [hg19 refGene]. You could learn more at the following:

# https://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/
# https://genome.ucsc.edu/cgi-bin/hgTables?db=hg19&hgta_group=genes&hgta_track=refSeqComposite&hgta_table=refGene&hgta_doSchema=describe+table+schema (Schema for NCBI RefSeq - RefSeq genes from NCBI)
# Visualize DNA methylation and histone modification (an active marker-H3K4me3) 
# here. http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr6%3A31128153%2D31142413&hgsid=1467202695_p1HPrLZa2tMzJREfrrGplnR1tNsc

# Compare Pou5f1 promoter methylation and H3K4me3 levels between ESCs and neuronal progenitor cultured cells.
# You could query other crucial genes in ESC maintenance for e.g., Nanog, Sox2. TDGF1, LEFTY1, GDF3, FOXD3 and in neuronal progenitor cells, PAX6, SIX3, LHX2, OTX2, PLZF, SOX1, FOXG1.

# ChIP-seq peak calls

# For each gene, a region of 10.000bp around the transcription start site of the gene is extracted (5000bp upstream and 5000bp downstream). 
# This region is binned in 100 bins of 100bp. For each bin, five core histone modification marks are counted.





# Question 1

# Which of the following statements about epigenetics is false?
# i. Every cell in your body has almost the exact same DNA sequence, but brains do not contract like a muscle, and hearts do not produce insulin (like the pancreas).
# This is because each cell precisely regulates which genes to use at which time. Scientists study epigenetics because it is an important regulator of gene expression.
# ii. Epigenetics is the study of alterations to the DNA sequence.     =====>CORRECT
# iii. Commonly studied epigenetic features include DNA methylation, histone modifications, and non-coding RNAs.
# iv Epigenetic marks on a person’s DNA (and the subsequent effects it has on the person’s cells and body) can change over a person’s lifetime

# Question 2

# DNA methylation occurs when a methyl compound binds to a cytosine nucleotide. In mammals, the cytosine is always next to a guanine (CpG). Which of the following about DNA methylation is true?
# i. DNA methylation is irreversible. Any CpG that becomes methylated, will stay that way for the rest of a person’s life.
# ii. DNA methylation changes are ALWAYS passed on to offspring. 
      # If a CpG becomes methylated in any cell-type it will always also become methylated in the sperm or egg and the offspring will also carry this methylation mark.
# iii. DNA methylation can affect how well other molecules in the nucleus bind to the DNA. Thus, DNA methylation of a CpG in a gene or regulatory region can affect how that gene is expressed in the cell.  =====>CORRECT
# (ie: If there is more RNA and protein for the gene or less.)
# iv. DNA methylation mutates the underlying DNA sequence. If the methylated CpG is located within a gene, the resulting RNA and protein will have a mutation.
                                                                                                      
# Question 3

# Now that we found the DMR that is most different between people, you may have follow-up questions. Which of the following would NOT make sense as a follow-up question.
# i. What is the nearest gene to the DMR? How does the expression of that gene vary across patients? Is there a correlation between the RNA expression and the DNA methylation level?
# ii. Are there any mutations in the patient’s DNA that lie in the DMR and might have affected why some patients have more DNA methylation than others?
# iii. If we use CRISPR to remove the CpG methylation do the patients have a different phenotype?   =====>CORRECT
# iv. Does the DNA methylation level correlate with other aspects of the patients’ demographics such as ancestry, sex, or disease status?
# v. Often methylation is measured in the blood, since it is easy to get from living patients. However, the cells involved in the disease may be in a different organ. 
# What cell types are involved in this disease, and what is the methylation status of the DMR in those cell types between patients?

# Question 4

# Which of the following is false about histones?
# i. The DNA is organized within the nucleus by being wrapped around histone proteins.
# ii. Small molecules can bind to precise regions of the histone protein. This is called histone modification.
# iii. Certain histone modifications change how tightly the DNA wraps around the histones or what other proteins are recruited to the DNA. 
# As a result, the DNA may become more or less accessible to other regulatory molecules. In this way, histone modifications can regulate gene expression.
# iv None of the above.     ======> CORRECT
   
# Question 5

# The Lister et al paper from 2013 analyzed differentially methylated regions (DMRs) instead of the individual CpGs. Why do you think they chose to do this?
# i. CpGs near each other often have similar methylation states. So by analyzing them together we are not losing too much information.
# ii. There are over 20 million CpGs in the human genome. If we test each one to see if it is differentially methylated between people, we will be performing over 20 million statistical tests. 
# This puts us at risk of finding many false positives. To account for this, scientists need to do “multiple hypothesis correction” statistically. 
# Additionally, scientists need to analyze many thousands of humans to weed out false positives. 
# By collapsing CpGs into bins of nearby CpGs (DMRs), we are not testing as many sites, and so we do not need as large of a sample size to be confident in our results.
# iii. The experimental assay that Lister et al were using did not allow them to measure DNA methylation at the level of the CpG.
# iv. The first and second statements above.  ======> CORRECT
# v. The first three statements above.
