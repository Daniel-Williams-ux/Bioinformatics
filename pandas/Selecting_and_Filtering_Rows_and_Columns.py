#Using loc and iloc to select a subset of the rows and columns within the DataFrame.
import pandas as pd
# Create a new DataFrame​
sample_data = [
                [0,1,2,3,4,5,6,7,8,9],
                [10,11,12,13,14,15,16,17,18,19],
                [20,21,22,23,24,25,26,27,28,29],
                [30,31,32,33,34,35,36,37,38,39],
                [40,41,42,43,44,45,46,47,48,49],
                [50,51,52,53,54,55,56,57,58,59],
                [70,71,72,73,74,75,76,77,78,79],
                [80,81,82,83,84,85,86,87,88,89],
                [90,91,92,93,94,95,96,97,98,99],
              ]
​
data = pd.DataFrame(data = sample_data, columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
data
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49
# 5	50	51	52	53	54	55	56	57	58	59
# 6	70	71	72	73	74	75	76	77	78	79
# 7	80	81	82	83	84	85	86	87	88	89
# 8	90	91	92	93	94	95	96	97	98	99


# Using loc
# Using loc (short for location) allows you to select a subset of the rows and columns using the label/name of the row/column. If the rows were not given labels (named), then their index position is their label.
# Within the square brackets, the selection preceding the (optional) comma refers to the rows you would like selected. Following the (optional) comma is the selection referring to the desired columns. The selection is inclusive of the end position.

# Selecting the rows 0 through (and including) 5, and the column "b":
# .loc indicates that you're selecting by using the label (inclusive) of the row and column.​
data.loc[:5, "b"]
# 0     1
# 1    11
# 2    21
# 3    31
# 4    41
# 5    51
# Name: b, dtype: int64
# The comma is optional. No comma assumes all columns will be returned.
​
data.loc[:5]
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49
# 5	50	51	52	53	54	55	56	57	58	59
# Note: If no comma follows the row selection then all columns are returned.

# Selecting the rows 6 through to the end of the DataFrame, and the columns "a" through "e" (inclusive):
data.loc[6:, 'a':'e']     # consecutive (loc selection is inclusive)
# a	b	c	d	e
# 6	70	71	72	73	74
# 7	80	81	82	83	84
# 8	90	91	92	93	94

Selecting all of the rows of the DataFrame, and the columns "c", "f" and "i" (in that order):
data.loc[:, ['c', 'f', 'i']]     # not consecutive
c	f	i
# 0	2	5	8
# 1	12	15	18
# 2	22	25	28
# 3	32	35	38
# 4	42	45	48
# 5	52	55	58
# 6	72	75	78
# 7	82	85	88
# 8	92	95	98
# Alert: When selecting by label, the end point (stopping position) is included, for both rows and columns.



# Using iloc
# Using iloc allows you to select a subset of the rows and columns using their index position. Thus, only integers can be used.

# Within the square brackets, the selection preceding the (optional) comma refers to the rows you would like selected. Following the (optional) comma is the selection referring to the desired columns. The selections will not include the end position.

# Selecting the rows from the beginning of the DataFrame (the first row) through to index position 5 (but not including index position 5). Then, selecting the columns located at index positions 2 through 5 (but not including index 5):

# iloc indicates that you're selecting by using the index position (exclusive) of the rows and columns.
​
data.iloc[:5, 2:5]
# 	c	d	e
# 0	2	3	4
# 1	12	13	14
# 2	22	23	24
# 3	32	33	34
# 4	42	43	44
# Alert: When selecting by index position (location), the end point (stopping position) is NOT included.

# Selecting the rows from the beginning of the DataFrame (the first row) through to index position 5 (but not including index position 5). No comma following the row selection assumes that all columns will be returned:
data.iloc[:5]  # No comma assumes all of the columns will be returned.
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49

# Selecting rows at index 5, 0 and 3 (in that order). Then selecting columns located at index 9, 5 and 0 (in that order):
data.iloc[[5, 0, 3], [9, 5, 0]]  # Returns rows and columns in the order listed.
# j	f	a
# 5	59	55	50
# 0	9	5	0
# 3	39	35	30



# Setting values
# You can modify values within a DataFrame by first selecting the rows and columns to be changed, and then setting that selection to the desired value:

# View the original DataFrame.​
data
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49
# 5	50	51	52	53	54	55	56	57	58	59
# 6	70	71	72	73	74	75	76	77	78	79
# 7	80	81	82	83	84	85	86	87	88	89
# 8	90	91	92	93	94	95	96	97	98	99

# Using loc
# Select the rows where column "j" is greater than 50 (indicated by everything before the comma). Then, just select column "j" (indicated by what follows the comma). Now, set those values equal to 100:
data.loc[data["j"] > 50, 'j'] = 100​
data
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49
# 5	50	51	52	53	54	55	56	57	58	100
# 6	70	71	72	73	74	75	76	77	78	100
# 7	80	81	82	83	84	85	86	87	88	100
# 8	90	91	92	93	94	95	96	97	98	100


# Using iloc
# Select the rows with index positions 5 through 8, but not including 8 (indicated by everything before the comma). Then, just select the column at index position 0, the first column (indicated by what follows the comma). Now, set those values equal to -100:
data.iloc[5:8, 0] = -100​
data
# a	b	c	d	e	f	g	h	i	j
# 0	0	1	2	3	4	5	6	7	8	9
# 1	10	11	12	13	14	15	16	17	18	19
# 2	20	21	22	23	24	25	26	27	28	29
# 3	30	31	32	33	34	35	36	37	38	39
# 4	40	41	42	43	44	45	46	47	48	49
# 5	-100	51	52	53	54	55	56	57	58	100
# 6	-100	71	72	73	74	75	76	77	78	100
# 7	-100	81	82	83	84	85	86	87	88	100
# 8	90	91	92	93	94	95	96	97	98	100
