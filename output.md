Numpy output:

array:
[19  6 19 13  2  2 15 12  9  8 13  7  3 17  1]
[[19  6 19 13  2]
 [ 2 15 12  9  8]
 [13  7  3 17  1]]
(3, 5)
maximum value replaced by 0:
[[ 0  6  0 13  2]
 [ 2  0 12  9  8]
 [13  7  3  0  1]]
 
 
 Pandas output:
 
 #Read the provided CSV file ‘data.csv’.
 |Duration|	Pulse |	Maxpulse	|Calories |
 | -----  | ----- | -------- | -----
|  60	   |  110	 |  130	    | 409.1.  |
|	 60	   |  117	 |  145	    | 479.0.  |
|	 60	   |  103	 |  135	    | 340.0.  | 
|	 45	   |  109	 |  175	    | 282.4.  |
|	 45	   |  117	 |  148	    | 406.0.  |

#Show the basic statistical description about the data.
Duration|	Pulse|	Maxpulse|	Calories|
--------  -----  --------   -------
count	|169.000000	169.000000	169.000000	164.000000|
mean	 |63846154	107.461538	134.047337	375.790244|
std	  |42.299949	14.510259	16.450434	266.379919|
min	  |15.000000	80.000000	100.000000	50.300000|
25%	 |45.000000	100.000000	124.000000	250.925000|
50%	 |60.000000	105.000000	131.000000	318.600000|
75%	|60.000000	111.000000	141.000000	387.600000|
max	|300.000000	159.000000	184.000000	1860.400000|

# Check if the data has null values
Duration    False
Pulse       False
Maxpulse    False
Calories     True
dtype: bool

#Replace the null values with the mean
Duration    False
Pulse       False
Maxpulse    False
Calories    False
dtype: bool

#4. Select at least two columns and aggregate the data using: min, max, count, mean.
Duration	Pulse
min	15.000000	80.000000
max	300.000000	159.000000
count	169.000000	169.000000
mean	63.846154	107.461538


#5. Filter the dataframe to select the rows with calories values between 500 and 1000.
Duration	Pulse	Maxpulse	Calories
51	80	123	146	643.1
62	160	109	135	853.0
65	180	90	130	800.4
66	150	105	135	873.4
67	150	107	130	816.0
72	90	100	127	700.0
73	150	97	127	953.2
75	90	98	125	563.2
78	120	100	130	500.4
90	180	101	127	600.1
99	90	93	124	604.1
103	90	90	100	500.4
106	180	90	120	800.3
108	90	90	120	500.3


#6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
Duration	Pulse	Maxpulse	Calories
65	180	90	130	800.4
70	150	97	129	1115.0
73	150	97	127	953.2
75	90	98	125	563.2
99	90	93	124	604.1
103	90	90	100	500.4
106	180	90	120	800.3
108	90	90	120	500.3


#7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
Duration	Pulse	Calories
0	60	110	409.1
1	60	117	479.0
2	60	103	340.0
3	45	109	282.4
4	45	117	406.0


#8. Delete the “Maxpulse” column from the main df dataframe
Duration	Pulse	Calories
0	60	110	409.1
1	60	117	479.0
2	60	103	340.0
3	45	109	282.4
4	45	117	406.0


#9. Convert the datatype of Calories column to int datatype.
Duration    int64
Pulse       int64
Calories    int64
dtype: object


#10. Using pandas create a scatter plot for the two columns (Duration and Calories).
<AxesSubplot:xlabel='Duration', ylabel='Calories'>

![download](https://user-images.githubusercontent.com/86486466/196581797-f4234d09-5063-4737-8202-0704acba18e9.png)

matplotlib output:


![download 1](https://user-images.githubusercontent.com/86486466/196589633-4525f80c-f0ba-4f03-b2aa-563d272cd2b7.png)





