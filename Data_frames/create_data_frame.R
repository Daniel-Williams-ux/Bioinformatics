# Data Frames
# Data frames are the most common way of storing and analyzing data in R. The columns (which are vectors) can be of different types, but they must be the same length.
# You can think of a data frame as a collection of vectors that all must be the same length.

df <- data.frame(name=c("Carl","Diane","Sally","Ben","Kimmy"),
                 age=c(42,40,17,14,12),
                 sex=c("Male","Female","Female","Male","Female"))

df
# A data.frame: 5 × 3
# name	age	sex
# <chr>	<dbl>	<chr>
# Carl	42	Male
# Diane	40	Female
# Sally	17	Female
# Ben	14	Male
# Kimmy	12	Female
