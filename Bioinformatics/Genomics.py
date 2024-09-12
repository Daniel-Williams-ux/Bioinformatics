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
import pyarrow as pa

from IPython import display


conn = pyathena.connect(s3_staging_dir="s3://athena-output-351869726285/", region_name='us-east-1', encryption_option='SSE_S3')

#                                                     Query the 1000 Genomes Project Dataset
# It's usually helpful to picture the data before performing any analysis, so we are going to import the database as the first step, and then view a few random rows.

# pd.set_option('display.max_colwidth', None) # This code expands the table horizontally so that all table cells are visible.
pd.read_sql('SELECT * FROM default.g1000vcf_csv_int LIMIT 10', conn).head(10)
#  chrm	start_position	end_position	reference_bases	alternate_bases	rsid	qual	filter	info	chromosome
# 0	13	48057851	48057852	C	A	rs187909946	100	PASS	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=17667;E...	13
# 1	13	48060685	48060686	C	A	rs185890309	100	PASS	AC=19;AF=0.00379393;AN=5008;NS=2504;DP=20692;E...	13
# 2	13	48151181	48151182	C	A	rs114158741	100	PASS	AC=2;AF=0.000399361;AN=5008;NS=2504;DP=19875;E...	13
# 3	13	48187023	48187024	C	A	rs569655592	100	PASS	AC=2;AF=0.000399361;AN=5008;NS=2504;DP=18383;E...	13
# 4	13	48199661	48199662	C	A	rs140367488	100	PASS	AC=3;AF=0.000599042;AN=5008;NS=2504;DP=20396;E...	13
# 5	13	48264832	48264833	C	A	rs7981870	100	PASS	AC=2176;AF=0.434505;AN=5008;NS=2504;DP=15064;E...	13
# 6	13	48292391	48292392	C	A	rs187307733	100	PASS	AC=2;AF=0.000399361;AN=5008;NS=2504;DP=12150;E...	13
# 7	13	48429425	48429426	C	A	rs558157149	100	PASS	AC=2;AF=0.000399361;AN=5008;NS=2504;DP=18915;E...	13
# 8	13	48472751	48472752	C	A	rs112665619	100	PASS	AC=221;AF=0.0441294;AN=5008;NS=2504;DP=16577;E...	13
# 9	13	48505064	48505065	C	A	rs147348319	100	PASS	AC=29;AF=0.00579073;AN=5008;NS=2504;DP=18225;E...	13

# We will go through a few important columns for you to understand in the table above. If you want to dive deeper, you may find this document helpful:https://samtools.github.io/hts-specs/VCFv4.2.pdf

# chrm is the chromosome location.
# start_position is the start position of the DNA variant.
# end_position is the end position of the DNA variant.
# reference_base is the allele at a specific location in the reference genomes, which are considered as the "approximated normal". 
# alternate_base is the allele that shows up at a specific location in the sample, but does not exist at the corresponding location in the reference genomes.
# rsid is the identification number of the SNPs (Single Nucleotide Polymorphism), see here: https://www.snpedia.com/index.php/SNPedia
# qual is the Phred-scaled quality score for the assertion made in ALT.
# filter indicates PASS when the position has passed all filters.



#                                                Search for SNPs (Single Nucleotide Polymorphism)
# Next, pick a SNPs you are interested in investigating from this website: https://www.snpedia.com

# The website has SNPs associated with a wide range of phenotypes. You could start exploring the popular SNPs on the homepage.

# Here are a few examples:

# rs53576 is highly associated with the ability to empathize with others.
# rs72921001 is responsible for certain population's dislike towards the taste of cilantro.
# rs28936679 is associated with sleep disorder.
# rs1805009 is associated with skin cancer.


# The example code below calls the data in the 1000 Genomes Project that has rs12913832, see the code  WHERE rsid='rs12913832'.
# rs12913832 is the SNP associated with blue or brown eye color.
pd.set_option('display.max_colwidth', None) # This code expands the table horizontally so that all table cells are visible.
pd.read_sql("SELECT * FROM \"default\".g1000vcf_csv_int WHERE rsid='rs12913832'", conn).head()
# chrm	   start_position	  end_position	reference_bases 	alternate_bases	 rsid	    qual	  filter	                                              info	                                                                                 chromosome
# 0	15	     28365617	        28365618	        A	                  G	     rs12913832	 100	   PASS     	AC=888;AF=0.177316;AN=5008;NS=2504;DP=19161;EAS_AF=0.002;AMR_AF=0.2017;AFR_AF=0.028;EUR_AF=0.6362;SAS_AF=0.0706;AA=A|||;VT=SNP	       15
# Does the result above make sense to you?
# We can see allele frequency of rs12913832 among Ad Mixed American and European populations are 20.17% and 63.62% respectively, while only 0.2% among East Asian and 2.8% among African populations.



#                                                 Query COSMIC68 Annotation Dataset (hg19)
# COSMIC database is short for Catalogue of Somatic Mutations in Cancer [hg19 cosmic 68]. Learn more at https://cancer.sanger.ac.uk/cosmic.
# Now, let's take a look at few random rows of the COSMIC database:
pd.read_sql('SELECT * FROM "1000_genomes".hg19_cosmic68 LIMIT 10', conn).head(10)
# chrm	start_position	end_position	reference_bases	alternate_bases	cosmic_info
# 0	10	22209854	22209855	G	A	ID=COSM917032;OCCURENCE=1(endometrium)
# 1	10	22880596	22880597	G	A	ID=COSM1262222;OCCURENCE=1(oesophagus)
# 2	10	24762254	24762255	G	A	ID=COSM1651216,COSM917097;OCCURENCE=1(endometrium)
# 3	10	24832945	24832946	G	A	ID=COSM917132;OCCURENCE=1(endometrium)
# 4	10	25877983	25877984	G	A	ID=COSM268400;OCCURENCE=1(large_intestine)
# 5	10	26825105	26825106	G	A	ID=COSM1347396;OCCURENCE=1(large_intestine)
# 6	10	27037564	27037565	G	A	ID=COSM295113;OCCURENCE=1(large_intestine)
# 7	10	27504517	27504518	G	A	ID=COSM917430,COSM917429;OCCURENCE=1(endometrium)
# 8	10	27702227	27702228	G	A	ID=COSM119734;OCCURENCE=1(ovary)
# 9	10	27702717	27702718	G	A	ID=COSM1347457;OCCURENCE=1(large_intestine)

# Like previous datasets, we see the chromosome location, start and end positions in DNA sequence, reference allele and alternate allele.
# The cosmic_info column tells us the types of cancer and mutation occurence.



#                                                         Query UCSC RefGene Annotation Dataset (hg19)
# The NCBI RefSeq Genes composite track shows human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq) [hg19 refGene]. You could learn more at the following:
# https://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/
# https://genome.ucsc.edu/cgi-bin/hgTables?db=hg19&hgta_group=genes&hgta_track=refSeqComposite&hgta_table=refGene&hgta_doSchema=describe+table+schema (Schema for NCBI RefSeq - RefSeq genes from NCBI)


# Now, let's take a look at random rows of the dataset:
# pd.read_sql('SELECT * FROM "1000_genomes".hg19_ucsc_refgene_int LIMIT 10', conn).head(10)
#  chrm	start_position	end_position	bin	name	strand	cdsstart	cdsend	exoncount	exonstarts	exonends	score	name2	cdsstartstat	cdsendstat	exonframes
# 0	2	   102407181	     102407238	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 1	2	   102460562	     102460773	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 2	2  	 102314164	     102314599	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 3	2	   102486756	     102486877	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 4	2	   102486083	     102486259	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 5	2	   102490543	     102490714	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 6	2	   102459070	     102459143	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 7	2	   102475457	     102475544	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 8	2	   102501648	     102501749	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# 9	2	   102441780	     102441891	170	NM_001242560	+	102314542	102507711	31	102314164,102314934,102407181,102440389,102441780,102445965,102448182,102450870,102452361,102456280,102459070,102460562,102472438,102475457,102476197,102480282,102481391,102482889,102483673,102484490,102486083,102486756,102490108,102490543,102493464,102499012,102501648,102503549,102504239,102505257,102507627,	102314599,102315000,102407238,102440515,102441891,102446056,102448313,102450925,102452440,102456456,102459143,102460773,102472600,102475544,102476326,102480513,102481498,102483041,102483771,102484499,102486259,102486877,102490226,102490714,102493608,102499147,102501749,102503699,102504399,102505397,102511152,	0	MAP4K4	cmpl	cmpl	0,0,0,0,0,0,1,0,1,2,1,2,0,0,0,0,0,2,1,0,0,2,0,1,1,1,1,0,0,1,0,
# Here are what some of the columns mean according to Schema for NCBI RefSeq - RefSeq genes from NCBI:
# cdsstart: Coding region start.
# cdsend: Coding region end.
# exoncount: Number of exons.
# strand: + or - for strand

#                                                                Variant-Based Annotation
# Variant-based annotation aims to look for exact matches between a query variant and a record in annotation datasets 
# (i.e., two items have identical chromosome, start position, end position, reference allele and alternative allele).

# The code below uses the JOIN function to look for exact matches between the 1000 Genomes Project dataset and the COSMIC dataset. 
# It compares the start and end positions, reference allele, alternate allele at chromosome 2 between the two datasets.
pd.read_sql("SELECT A.chrm, A.start_position, A.end_position, A.reference_bases, A.alternate_bases,B.cosmic_info, A.info "
+ " FROM (SELECT * FROM \"default\".g1000vcf_csv_int WHERE chrm='2') as A "
+ " JOIN "
+ " (SELECT * FROM \"1000_genomes\".hg19_cosmic68_int WHERE chrm='2') as B "
+ " ON A.start_position=B.start_position AND A.alternate_bases=B.alternate_bases "
+ " ORDER By  A.start_position", conn).head()
# chrm	start_position	end_position	reference_bases	alternate_bases	cosmic_info	info
# 0	2	55184	55185	G	A	ID=COSN206912;OCCURENCE=1(large_intestine)	AC=60;AF=0.0119808;AN=5008;NS=2504;DP=19415;EAS_AF=0;AMR_AF=0.0043;AFR_AF=0.0431;EUR_AF=0;SAS_AF=0;AA=G|||;VT=SNP
# 1	2	95490	95491	C	T	ID=COSN42681;OCCURENCE=4(central_nervous_system)	AC=17;AF=0.00339457;AN=5008;NS=2504;DP=16854;EAS_AF=0.0169;AMR_AF=0;AFR_AF=0;EUR_AF=0;SAS_AF=0;AA=C|||;VT=SNP
# 2	2	128457	128458	G	A	ID=COSN181337,COSN181637;OCCURENCE=1(stomach),2(large_intestine)	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=17605;EAS_AF=0.001;AMR_AF=0;AFR_AF=0;EUR_AF=0;SAS_AF=0;AA=G|||;VT=SNP
# 3	2	133636	133637	G	A	ID=COSN33464;OCCURENCE=1(breast),1(large_intestine)	AC=3;AF=0.000599042;AN=5008;NS=2504;DP=19368;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0;SAS_AF=0.0031;AA=G|||;VT=SNP
# 4	2	218857	218858	G	A	ID=COSM1404910,COSM1404911;OCCURENCE=1(large_intestine)	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=17149;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.001;SAS_AF=0;AA=G|||;VT=SNP;EX_TARGET
# The returned table tells us information about genes associated with different types of cancers.
# In the example below, the cancer related to central nervous system is at chromosome 2, where the reference allele is C and alternate allele is T. 
# It appears to only happen to East Asian population with a frequency of 1.69% while absent among other populations.


                                                               # Interval-Based Annotation [TP53: chrm17]
# The aim of interval-based annotation is to look for overlap of a query variant with a region (this region could be a single position) in annotation databases.
# The code below uses the JOIN function to compare two datasets using overlapping condition.
# Rather than comparing whether the two datasets are exactly the same, this method focuses on overlapping regions. 
# In the following example, we are running chromosome 17 from the 1000 Genomes Project against gene TP53 from chromosome 17 in the UCSC RefGene Annotation dataset.
# The ON condition is trying to see if there is any overlapping between the two datasets in the selected region. See the graph below:
pd.read_sql("SELECT A.chrm, A.start_position, A.end_position, A.reference_bases, A.alternate_bases,B.name, B.name2, A.info "
+ " FROM (SELECT * FROM \"default\".g1000vcf_csv_int WHERE chrm='17') as A "
+ " JOIN "
+ " (SELECT * FROM \"1000_genomes\".hg19_ucsc_refgene_int WHERE chrm='17' and name2='TP53') as B "
+ " ON A.start_position<=B.end_position AND B.start_position<=A.end_position "
+ " ORDER By  A.start_position", conn).head()
# chrm	start_position	end_position	reference_bases	alternate_bases	name	name2	info
# 0	17	7571751	7571752	T	G	NM_001276696	TP53	AC=13;AF=0.00259585;AN=5008;NS=2504;DP=19133;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.0129;SAS_AF=0;AA=T|||;VT=SNP
# 1	17	7571751	7571752	T	G	NM_001126114	TP53	AC=13;AF=0.00259585;AN=5008;NS=2504;DP=19133;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.0129;SAS_AF=0;AA=T|||;VT=SNP
# 2	17	7571751	7571752	T	G	NM_001276695	TP53	AC=13;AF=0.00259585;AN=5008;NS=2504;DP=19133;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.0129;SAS_AF=0;AA=T|||;VT=SNP
# 3	17	7571751	7571752	T	G	NM_001126113	TP53	AC=13;AF=0.00259585;AN=5008;NS=2504;DP=19133;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.0129;SAS_AF=0;AA=T|||;VT=SNP
# 4	17	7571751	7571752	T	G	NM_000546	TP53	AC=13;AF=0.00259585;AN=5008;NS=2504;DP=19133;EAS_AF=0;AMR_AF=0;AFR_AF=0;EUR_AF=0.0129;SAS_AF=0;AA=T|||;VT=SNP

# For your information, TP53 gene provides instructions for making a protein called tumor protein p53 (or p53). 
# This protein acts as a tumor suppressor, which means that it regulates cell division by keeping cells from growing and dividing (proliferating) too fast, or in an uncontrolled way. 
# TP53 acts like a conductor in an orchestra.
# The table gives us a view of all the mutations on gene TP53 on chromosome 2. Typically, mutations on TP53 are considered as rare mutations.




# Question 1

# Which of the following are true ?

# The reference base is that without the mutation, and the alternate base is that with the mutation  =======> CORRECT
# Alternate and reference base both refer to the same nucleotide
# The reference base is the mutation that we care about and the alternate base is what it would be if there were no mutation
# The reference base is the starting location for the gene in question


# Question 2

# Looking only at the examples from the SNPedia in the notebook, which of these is associated with a SNP?
# Dislike for the taste of cilantro   =======> CORRECT
# Preference or dislike for citric smells
# Likelihood to get the annual Flu
# Ability to recognize faces

# Question 3

# Why do we care about SNPs?
# They’re variants of single nucleotides that we can trace to populations, personal characteristics, or likelihood for disease    =======> CORRECT
# They’re the chemical basis of DNA and thus encode all the genetic information that make us
# Working with SNPs allows researchers to see damage to the DNA from environmental factors
# Since one SNP often covers thousands of base pairs in DNA, they can tell us all about the features of the individual from whom the DNA sample was taken

# Question 4

# What’s interval-based notation?
# A method for researchers to know if they both discovered the same findings when studying a sample
# A method for overlaying a sample of DNA with existing annotation databases.   =======> CORRECT
# A method for labeling DNA every N bases where N depends on the resolution desired
# A type of annotation labeling DNA that averages the number of mutations in an interval

# Question 5

# What is gene TP53 involved in?
# One’s likelihood to suffer from infectious diseases, particularly water-borne
# A tumor suppressor protein that prevents cancer  =======> CORRECT
# A yet unidentified mechanism that has been shown to impact capacity for collaboration under stress
