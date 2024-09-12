# Genomics is the branch of molecular biology concerned with the structure, function, evolution, and mapping of genomes.
# In this module, you will be learning about how to process and annotate Variant Call Format (VCF) file using Amazon Athena. The Variant Call Format specifies the format of a text file used in bioinformatics for storing gene sequence variations.
# The format has been developed with the advent of large-scale genotyping and DNA sequencing projects, such as the 1000 Genomes Project.

# Tables you can query
# ['default.g1000vcf_csv_int', 'default.g1000vcf_csv', 'default.g1000vcf_parquet', 'default.g1000vcf_partitioned']
# COSMIC68 Annotation Dataset ['1000_genomes.hg19_cosmic68_int']
# UCSC RefGene Annotation Dataset ['1000_genomes.hg19_ucsc_refgene_int']


#                                                      Initial Setup
# We'll use the PyAthena library to get access to a database stored in AWS S3. You can read more about PyAthena here:
# • https://pypi.org/project/pyathena/
# • https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc

import sys
import pyathena
import pandas as pd

from IPython import display

conn = pyathena.connect(s3_staging_dir="s3://athena-output-351869726285/", region_name='us-east-1', encryption_option='SSE_S3')

#                                                     Query the 1000 Genomes Project Dataset
# It's usually helpful to picture the data before performing any analysis, so we are going to import the database as the first step, and then view a few random rows.

# Tip: If you are new to Jupyter Notebook, try run the code cell below using keyboard shortcut: "Shift" + "Enter". You could look up more keyboard shortcuts by pressing "H".
