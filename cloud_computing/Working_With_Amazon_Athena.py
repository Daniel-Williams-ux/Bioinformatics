# we will use Amazon Athena which is considered as a Platform-as-a-Service. You bring your queries and data. Athena is a serverless, interactive query service that reads data directly from Amazon S3 object storage.
# We do not need to manage any servers.

# Initial setup
# We'll use the PyAthena library to get access to a database stored in AWS S3. You can read more about PyAthena here:

# • https://pypi.org/project/pyathena/

# • https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
import sys
import pyathena
import pandas as pd

#from IPython.core.display import display, HTML  ==>Specifically, importing display from IPython.core.display is deprecated, meaning it’s an older way that is no longer recommended, and you should import it from the IPython.display module.
from IPython.display import display, HTML


conn = pyathena.connect(s3_staging_dir="s3://athena-output-351869726285/", region_name='us-east-1', encryption_option='SSE_S3')
# Explanation of the Code:
# 1. Library Imports:
# sys: Provides access to system-specific parameters and functions. It’s not directly used here, but it’s often imported for handling system-level tasks.
# pyathena: A Python library used to interact with Amazon Athena, which allows running SQL queries on data stored in Amazon S3.
# pandas (pd): A widely used library for data manipulation and analysis. It is often used to store query results in a structured tabular format (DataFrame).
# IPython.display: Provides tools to display data in various formats in Jupyter notebooks. In this case, it’s used to format HTML output (display, HTML).

# 2. Connecting to Amazon Athena:
# pyathena.connect(): Establishes a connection to Amazon Athena, a serverless SQL query service.
# s3_staging_dir: Specifies the Amazon S3 bucket location (s3://athena-output-351869726285/) where the results of the Athena queries will be saved. 
# Athena temporarily stores query results in S3 before sending them back to the client.
# region_name: The AWS region (us-east-1) where your Athena instance and the S3 bucket reside.
# encryption_option: Specifies that SSE-S3 (Server-Side Encryption with Amazon S3-managed keys) is used to encrypt the data stored in the S3 staging directory.
# What's Happening?
# Connection Setup: This code establishes a connection between your local Python environment and the Amazon Athena service, allowing you to run SQL queries on data stored in Amazon S3 without managing servers. 
# Athena handles the querying process.

# Serverless Architecture: No need to manage the infrastructure. You just point to the data in Amazon S3, run queries, and get the results.

# PyAthena: The pyathena.connect() method is used to configure the connection with AWS services, leveraging the S3 storage and Athena query engine.

# This setup enables you to easily interact with large datasets stored in Amazon S3, execute SQL queries on them using Amazon Athena, and analyze the results in your Python environment.





#                                                        Query the 1000 Genomes Project dataset
# It's usually helpful to picture the data before performing any analysis, so we are going to import the database as the first step, and then view a few random rows. 

# Query the 1000 Genomes Project dataset
# It's usually helpful to picture the data before performing any analysis, so we are going to import the database as the first step, and then view a few random rows. 
# We will provide more information about this genomics dataset in Introduction to Genomics Module.

# pd.set_option('display.max_colwidth', None) # This code expands the table horizontally so that all table cells are visible.
pd.read_sql('SELECT * FROM default.g1000vcf_csv_int LIMIT 10', conn).head(10)
# pd.set_option('display.max_colwidth', None) # This code expands the table horizontally so that all table cells are visible.
pd.read_sql('SELECT * FROM default.g1000vcf_csv_int LIMIT 10', conn).head(10)
# /tmp/ipykernel_60/653230635.py:2: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection.
# Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
###############################################################################################################################################################################
# The warning you are seeing indicates that the pandas.read_sql() function is designed to work primarily with SQLAlchemy connections, or database string URIs (e.g., for SQLite),
# and it’s notifying you that it might not fully support the connection object provided by PyAthena (which is based on DBAPI2).

# Solution:
# You can avoid the warning and improve compatibility by using SQLAlchemy along with PyAthena. 
# Below is the modified version of the code that uses SQLAlchemy with PyAthena to execute SQL queries on Amazon Athena:
# Steps:
# Install SQLAlchemy (if you don't have it installed yet):
pip install sqlalchemy
# Update the Code: You can set up your connection using SQLAlchemy and PyAthena together:
from sqlalchemy.engine import create_engine
from pyathena.sqlalchemy_athena import AthenaDialect
import pandas as pd
# Set up the connection using SQLAlchemy
engine = create_engine('awsathena+rest://@athena.us-east-1.amazonaws.com/default?s3_staging_dir=s3://athena-output-351869726285/')
# Query using pd.read_sql with SQLAlchemy engine
df = pd.read_sql('SELECT * FROM default.g1000vcf_csv_int LIMIT 10', engine)
# Display the dataframe
pd.set_option('display.max_colwidth', None)
display(df.head(10))
##############################################################################################################################################################################

  pd.read_sql('SELECT * FROM default.g1000vcf_csv_int LIMIT 10', conn).head(10)
# chrm	start_position	end_position	reference_bases	alternate_bases	rsid	qual	filter	info	chromosome
# 0	2	67301616	67301617	T	G	rs540070206	100	PASS	AC=2;AF=0.000399361;AN=5008;NS=2504;DP=19395;E...	2
# 1	2	67873655	67873656	T	G	rs6749904	100	PASS	AC=3992;AF=0.797125;AN=5008;NS=2504;DP=19280;E...	2
# 2	2	67969344	67969345	T	G	rs372985936	100	PASS	AC=15;AF=0.00299521;AN=5008;NS=2504;DP=19653;E...	2
# 3	2	68848824	68848825	T	G	rs115954524	100	PASS	AC=200;AF=0.0399361;AN=5008;NS=2504;DP=15473;E...	2
# 4	2	69046555	69046556	T	G	rs2271833	100	PASS	AC=7;AF=0.00139776;AN=5008;NS=2504;DP=19305;EA...	2
# 5	2	70880211	70880212	T	G	rs528143452	100	PASS	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=18483;E...	2
# 6	2	71103594	71103595	T	G	rs13401201	100	PASS	AC=66;AF=0.0131789;AN=5008;NS=2504;DP=22426;EA...	2
# 7	2	72132708	72132709	T	G	rs545980160	100	PASS	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=18022;E...	2
# 8	2	73290605	73290606	T	G	rs574710388	100	PASS	AC=1;AF=0.000199681;AN=5008;NS=2504;DP=20888;E...	2
# 9	2	74449070	74449071	T	G	rs568270684	100	PASS	AC=17;AF=0.00339457;AN=5008;NS=2504;DP=19721;E...	
# We will provide more information about this genomics dataset in Introduction to Genomics Module.


                                                    #  Query wearable project dataset
# You will learn more about this wearable dataset from a study published on Nature Biomedical Engineering in 2020 in Introduction to Wearables.

# Let's just try Amazon Athena on a sample participant dataset. You will see tables similar to this:

import pyathena
import pandas as pd

conn = pyathena.connect(s3_staging_dir="s3://athena-output-351869726285/", region_name='us-east-1', encryption_option='SSE_S3')

pd.read_sql("SELECT * FROM sid_00000.hr_minute_a6bui4n  WHERE year='2022' and device='fitbit' LIMIT 10", conn).head(10)

# datetime	heartrate	sid	pid	device	year	month	day
# 0	06:00:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 1	06:01:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 2	06:02:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 3	06:03:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 4	06:04:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 5	06:05:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 6	06:06:01	69.0	00000	aw4exxk	fitbit	2022	12	17
# 7	06:07:04	69.0	00000	aw4exxk	fitbit	2022	12	17
# 8	06:08:04	69.0	00000	aw4exxk	fitbit	2022	12	17
# 9	06:09:04	94.6	00000	aw4exxk	fitbit	2022	12	17
# A schema defines what the name of the table is, and what the name and type of each column is. The chart above looks pretty standard:

# Each row is a recorded heartrate per minute associated with the data and time it was recorded.
# The sid and pid columns are id numbers that can be used to track rows across different data tables.
# sid is study ID
# pid is study participant ID. For example, pid a6bui4n could correspond to one participant, letting us track this participant across different rows and data tables.
# Queries are written in a language called SQL (pronounced sequel), and we can break the above SQL query into a few parts:

# SELECT: Like the name suggests, SELECT tells SQL which data tables and columns have the data we want to find.

# "sid_00000.hr_minute_a6bui4n": In this case, we are telling SQL we want heartrate per minute data of participant a6bui4n in the study with ID 00000

# WHERE:

# It lets the query specify conditions that the data must meet. This is the meat of the query that takes over after we specify where to look (SELECT). We now get to say what we want.
# In this case, we're looking for data collected from Fitbit devices in year 2022. Since this is de-identified data, we shifted the date randomly for each participant.
# head(10): We want to display 10 items from the selected table.
