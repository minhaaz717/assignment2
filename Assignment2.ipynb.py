{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f3e5d93c",
   "metadata": {},
   "source": [
    "1. Numpy:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18605fa9",
   "metadata": {},
   "source": [
    "Using NumPy create random vector of size 15 having only Integers in the range 1-20.\n",
    "1. Reshape the array to 3 by 5\n",
    "2. Print array shape.\n",
    "3. Replace the max in each row by 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f16ebb8e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original array:\n",
      "[14 14 16  7  9 10  9 14  6 12  7 15  4  1 19]\n",
      "Maximum value replaced by 0:\n",
      "[14 14 16  7  9 10  9 14  6 12  7 15  4  1  0]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = np.random.randint(1,20,15)\n",
    "print(\"Original array:\")\n",
    "print(x)\n",
    "x[x.argmax()] = 0\n",
    "print(\"Maximum value replaced by 0:\")\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f237f67",
   "metadata": {},
   "source": [
    "2. Pandas"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00e4538e",
   "metadata": {},
   "source": [
    "1. Read the provided CSV file ‘data.csv’.\n",
    "https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing\n",
    "2. Show the basic statistical description about the data.\n",
    "3. Check if the data has null values.\n",
    "a. Replace the null values with the mean\n",
    "4. Select at least two columns and aggregate the data using: min, max, count, mean.\n",
    "5. Filter the dataframe to select the rows with calories values between 500 and 1000.\n",
    "6. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.\n",
    "7. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.\n",
    "8. Delete the “Maxpulse” column from the main df dataframe\n",
    "9. Convert the datatype of Calories column to int datatype.\n",
    "10. Using pandas create a scatter plot for the two columns (Duration and Calories).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96301e85",
   "metadata": {},
   "source": [
    "1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "caa28886",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Maxpulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>60</td>\n",
       "      <td>110</td>\n",
       "      <td>130</td>\n",
       "      <td>409.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>60</td>\n",
       "      <td>117</td>\n",
       "      <td>145</td>\n",
       "      <td>479.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>103</td>\n",
       "      <td>135</td>\n",
       "      <td>340.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>109</td>\n",
       "      <td>175</td>\n",
       "      <td>282.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>45</td>\n",
       "      <td>117</td>\n",
       "      <td>148</td>\n",
       "      <td>406.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Duration  Pulse  Maxpulse  Calories\n",
       "0        60    110       130     409.1\n",
       "1        60    117       145     479.0\n",
       "2        60    103       135     340.0\n",
       "3        45    109       175     282.4\n",
       "4        45    117       148     406.0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = pd.read_csv(\"data.csv\")\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5e4f103",
   "metadata": {},
   "source": [
    "2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0c46f843",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Maxpulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>169.000000</td>\n",
       "      <td>169.000000</td>\n",
       "      <td>169.000000</td>\n",
       "      <td>164.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>63.846154</td>\n",
       "      <td>107.461538</td>\n",
       "      <td>134.047337</td>\n",
       "      <td>375.790244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>42.299949</td>\n",
       "      <td>14.510259</td>\n",
       "      <td>16.450434</td>\n",
       "      <td>266.379919</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>50.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>45.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>124.000000</td>\n",
       "      <td>250.925000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>60.000000</td>\n",
       "      <td>105.000000</td>\n",
       "      <td>131.000000</td>\n",
       "      <td>318.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>60.000000</td>\n",
       "      <td>111.000000</td>\n",
       "      <td>141.000000</td>\n",
       "      <td>387.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>300.000000</td>\n",
       "      <td>159.000000</td>\n",
       "      <td>184.000000</td>\n",
       "      <td>1860.400000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Duration       Pulse    Maxpulse     Calories\n",
       "count  169.000000  169.000000  169.000000   164.000000\n",
       "mean    63.846154  107.461538  134.047337   375.790244\n",
       "std     42.299949   14.510259   16.450434   266.379919\n",
       "min     15.000000   80.000000  100.000000    50.300000\n",
       "25%     45.000000  100.000000  124.000000   250.925000\n",
       "50%     60.000000  105.000000  131.000000   318.600000\n",
       "75%     60.000000  111.000000  141.000000   387.600000\n",
       "max    300.000000  159.000000  184.000000  1860.400000"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b9cec31",
   "metadata": {},
   "source": [
    "3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "b6ff0559",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Duration    False\n",
       "Pulse       False\n",
       "Calories    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "71da4222",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Duration    False\n",
       "Pulse       False\n",
       "Maxpulse    False\n",
       "Calories    False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.fillna(data.mean(), inplace=True)\n",
    "data.isnull().any()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "062dd34e",
   "metadata": {},
   "source": [
    "4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b446fbd3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>300.000000</td>\n",
       "      <td>159.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>169.000000</td>\n",
       "      <td>169.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>63.846154</td>\n",
       "      <td>107.461538</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Duration       Pulse\n",
       "min     15.000000   80.000000\n",
       "max    300.000000  159.000000\n",
       "count  169.000000  169.000000\n",
       "mean    63.846154  107.461538"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.agg({'Duration':['min','max','count','mean'],'Pulse':['min','max','count','mean']})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7972dddb",
   "metadata": {},
   "source": [
    "5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "2a7615d4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Maxpulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>80</td>\n",
       "      <td>123</td>\n",
       "      <td>146</td>\n",
       "      <td>643.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>62</th>\n",
       "      <td>160</td>\n",
       "      <td>109</td>\n",
       "      <td>135</td>\n",
       "      <td>853.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>130</td>\n",
       "      <td>800.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>66</th>\n",
       "      <td>150</td>\n",
       "      <td>105</td>\n",
       "      <td>135</td>\n",
       "      <td>873.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>150</td>\n",
       "      <td>107</td>\n",
       "      <td>130</td>\n",
       "      <td>816.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>72</th>\n",
       "      <td>90</td>\n",
       "      <td>100</td>\n",
       "      <td>127</td>\n",
       "      <td>700.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>150</td>\n",
       "      <td>97</td>\n",
       "      <td>127</td>\n",
       "      <td>953.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>90</td>\n",
       "      <td>98</td>\n",
       "      <td>125</td>\n",
       "      <td>563.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>120</td>\n",
       "      <td>100</td>\n",
       "      <td>130</td>\n",
       "      <td>500.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>180</td>\n",
       "      <td>101</td>\n",
       "      <td>127</td>\n",
       "      <td>600.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>90</td>\n",
       "      <td>93</td>\n",
       "      <td>124</td>\n",
       "      <td>604.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>90</td>\n",
       "      <td>90</td>\n",
       "      <td>100</td>\n",
       "      <td>500.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>106</th>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>120</td>\n",
       "      <td>800.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>90</td>\n",
       "      <td>90</td>\n",
       "      <td>120</td>\n",
       "      <td>500.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Duration  Pulse  Maxpulse  Calories\n",
       "51         80    123       146     643.1\n",
       "62        160    109       135     853.0\n",
       "65        180     90       130     800.4\n",
       "66        150    105       135     873.4\n",
       "67        150    107       130     816.0\n",
       "72         90    100       127     700.0\n",
       "73        150     97       127     953.2\n",
       "75         90     98       125     563.2\n",
       "78        120    100       130     500.4\n",
       "90        180    101       127     600.1\n",
       "99         90     93       124     604.1\n",
       "103        90     90       100     500.4\n",
       "106       180     90       120     800.3\n",
       "108        90     90       120     500.3"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.loc[(data['Calories']>500)&(data['Calories']<1000)]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43ef5d65",
   "metadata": {},
   "source": [
    "6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "887aacde",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Maxpulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>130</td>\n",
       "      <td>800.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>150</td>\n",
       "      <td>97</td>\n",
       "      <td>129</td>\n",
       "      <td>1115.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>150</td>\n",
       "      <td>97</td>\n",
       "      <td>127</td>\n",
       "      <td>953.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>90</td>\n",
       "      <td>98</td>\n",
       "      <td>125</td>\n",
       "      <td>563.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>90</td>\n",
       "      <td>93</td>\n",
       "      <td>124</td>\n",
       "      <td>604.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>103</th>\n",
       "      <td>90</td>\n",
       "      <td>90</td>\n",
       "      <td>100</td>\n",
       "      <td>500.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>106</th>\n",
       "      <td>180</td>\n",
       "      <td>90</td>\n",
       "      <td>120</td>\n",
       "      <td>800.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>90</td>\n",
       "      <td>90</td>\n",
       "      <td>120</td>\n",
       "      <td>500.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Duration  Pulse  Maxpulse  Calories\n",
       "65        180     90       130     800.4\n",
       "70        150     97       129    1115.0\n",
       "73        150     97       127     953.2\n",
       "75         90     98       125     563.2\n",
       "99         90     93       124     604.1\n",
       "103        90     90       100     500.4\n",
       "106       180     90       120     800.3\n",
       "108        90     90       120     500.3"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.loc[(data['Calories']>500)&(data['Pulse']<100)]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d2670e0",
   "metadata": {},
   "source": [
    "7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "a763cd1c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>60</td>\n",
       "      <td>110</td>\n",
       "      <td>409.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>60</td>\n",
       "      <td>117</td>\n",
       "      <td>479.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>103</td>\n",
       "      <td>340.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>109</td>\n",
       "      <td>282.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>45</td>\n",
       "      <td>117</td>\n",
       "      <td>406.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Duration  Pulse  Calories\n",
       "0        60    110     409.1\n",
       "1        60    117     479.0\n",
       "2        60    103     340.0\n",
       "3        45    109     282.4\n",
       "4        45    117     406.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_modified = data[['Duration','Pulse','Calories']]\n",
    "df_modified.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3f243f4",
   "metadata": {},
   "source": [
    "8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6a95fc4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "del data['Maxpulse']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c7c2aa78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Duration</th>\n",
       "      <th>Pulse</th>\n",
       "      <th>Calories</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>60</td>\n",
       "      <td>110</td>\n",
       "      <td>409</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>60</td>\n",
       "      <td>117</td>\n",
       "      <td>479</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>60</td>\n",
       "      <td>103</td>\n",
       "      <td>340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>45</td>\n",
       "      <td>109</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>45</td>\n",
       "      <td>117</td>\n",
       "      <td>406</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Duration  Pulse  Calories\n",
       "0        60    110       409\n",
       "1        60    117       479\n",
       "2        60    103       340\n",
       "3        45    109       282\n",
       "4        45    117       406"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3aedc5d4",
   "metadata": {},
   "source": [
    "9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f3d07928",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Duration      int64\n",
       "Pulse         int64\n",
       "Maxpulse      int64\n",
       "Calories    float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2930a606",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Duration    int64\n",
       "Pulse       int64\n",
       "Maxpulse    int64\n",
       "Calories    int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Calories'] = data['Calories'].astype(np.int64)\n",
    "data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0df8e861",
   "metadata": {},
   "source": [
    "10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "269f4b12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Duration', ylabel='Calories'>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYsAAAEGCAYAAACUzrmNAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAhiUlEQVR4nO3df3Dc9X3n8edLtgQyYEjMwhiwJZKSnAhp5CCctEkpaWxMuE6AuzbF00lIoonTBNH02us0XO8a2ptMm17SXIOnJE7lQnOJKGlCYcgPBxLnR9uALQcHDCrBBAEG1V5MMTYWyLLe98d+hVfrXe2utL/1eszsaPe93+93P1/vSG9/fisiMDMzm01bvQtgZmaNz8nCzMyKcrIwM7OinCzMzKwoJwszMytqcb0LUC2nn356dHd317sYZmZNZceOHc9GRCo33rLJoru7m+Hh4XoXw8ysqUh6Il/czVBmZlaUk4WZmRXlZGFmZkU5WZiZWVFOFmZmVpSThZlVTDp9mO3bx0inD9e7KFZhThZmVhFDQyN0dW1i7dqv0tW1iaGhkXoXySrIycLM5i2dPkx//xbGxyc5cGCC8fFJ+vu3uIbRQpwszGzeRkcP0NEx889Je3sbo6MH6lQiqzQnCzObt+7uU5mYmJoRO3Jkiu7uU+tUIqs0Jwszm7dUagmDg+vo7FzM0qUddHYuZnBwHanUknoXzSqkZdeGMrPaWr++hzVruhgdPUB396lOFC3GycLMKiaVWuIk0aLcDGVmZkU5WZiZWVFOFmZmVpSThZmZFVW1ZCFps6R9knZlxf5B0s7kMSppZxLvljSe9d7ns865UNKDknZL+pwkVavMZmaWXzVHQ90MbAT+fjoQEb81/VzSZ4Ds6Z2PRURvnuvcBGwA7gW+CVwGfKvyxTUzs0KqVrOIiB8Cz+V7L6kdvAcYmu0akpYDSyPixxERZBLPlRUuqpmZFVGvPotfAfZGxKNZsXMl3S/pB5J+JYmdDezJOmZPEstL0gZJw5KG0+l05UttZjaLVl6ivV7JYj0zaxVjwMqIWAX8PvAVSUuBfP0TUeiiEbEpIvoioi+VSlW0wGZms2n1JdprniwkLQb+C/AP07GIeDki9ifPdwCPAa8jU5M4J+v0c4BnaldaM7PiFsIS7fWoWawB/i0iXmlekpSStCh5/hrgPODnETEGHJT01qSf433AHXUos5lZQQthifZqDp0dAn4MvF7SHkn9yVtXc3zH9sXAA5J+Cvwj8DsRMd05/hHgb4HdZGocHgllZg1lISzRXrWhsxGxvkD8/XliXwO+VuD4YeCCihbOzKyCppdo7+/fQnt7G0eOTLXcEu1eddbMrAJafYl2Jwszswpp5SXavTaUmZkV5WRhZmZFOVmYmVlRThZmZlaUk4WZmRXlZGFmZkU5WZiZWVFOFmZmVpSThZmZFeVkYWZmRTlZmJlZUU4WZmZWlJOFmZkV5WRhZmZFOVmYmVlRThZmZlZUNffg3ixpn6RdWbEbJD0taWfyuDzrvesl7Zb0iKR1WfELJT2YvPc5SapWmc3MLL9q1ixuBi7LE/9sRPQmj28CSDofuBp4Q3LO30halBx/E7ABOC955LummdmCl04fZvv2MdLpwxW/dtWSRUT8EHiuxMOvAG6NiJcj4nFgN7Ba0nJgaUT8OCIC+HvgyqoU2MysiQ0NjdDVtYm1a79KV9cmhoZGKnr9evRZDEh6IGmmelUSOxt4KuuYPUns7OR5btzMzBLp9GH6+7cwPj7JgQMTjI9P0t+/paI1jFoni5uA1wK9wBjwmSSerx8iZonnJWmDpGFJw+l0ep5FNTNrDqOjB+jomPnnvL29jdHRAxX7jJomi4jYGxFHI2IK+CKwOnlrD7Ai69BzgGeS+Dl54oWuvyki+iKiL5VKVbbwZmYNqrv7VCYmpmbEjhyZorv71Ip9Rk2TRdIHMe0qYHqk1J3A1ZJOkHQumY7sbRExBhyU9NZkFNT7gDtqWWYzs0aXSi1hcHAdnZ2LWbq0g87OxQwOriOVWlKxz1hcsSvlkDQEXAKcLmkP8AngEkm9ZJqSRoEPA0TEQ5JuAx4GJoFrI+JocqmPkBlZ1Ql8K3mYmVmW9et7WLOmi9HRA3R3n1rRRAGgzCCj1tPX1xfDw8P1LoaZWVORtCMi+nLjnsFtZmZFOVmYmVlRThZmZlaUk4WZmRXlZGFmZkU5WZhZxVRzITurLycLM6uIai9kZ/XlZGFm81aLheysvpwszGzearGQndWXk4WZzVstFrKz+nKyMLN5q8VCdlZfVVtI0MwWlmovZGf15WRhZhWTSi1xkmhRboYyM7OinCzMzKwoJwszMyvKycLMzIpysjAzs6KcLMzMrKiqJQtJmyXtk7QrK/Z/JP2bpAck3S7ptCTeLWlc0s7k8fmscy6U9KCk3ZI+J0nVKrOZmeVXzZrFzcBlObG7gQsi4heBnwHXZ733WET0Jo/fyYrfBGwAzkseudc0M7Mqq1qyiIgfAs/lxL4TEZPJy3uBc2a7hqTlwNKI+HFEBPD3wJVVKK6Zmc2inn0WHwS+lfX6XEn3S/qBpF9JYmcDe7KO2ZPE8pK0QdKwpOF0Ol35EpuZLVB1SRaS/hiYBL6chMaAlRGxCvh94CuSlgL5+iei0HUjYlNE9EVEXyqVqnSxzcwWrJqvDSXpGuDXgXcmTUtExMvAy8nzHZIeA15HpiaR3VR1DvBMbUtsZmY1rVlIugz4I+DdEXE4K56StCh5/hoyHdk/j4gx4KCktyajoN4H3FHLMpuZWRVrFpKGgEuA0yXtAT5BZvTTCcDdyQjYe5ORTxcDfyZpEjgK/E5ETHeOf4TMyKpOMn0c2f0cZmZWA0paglpOX19fDA8P17sYZmZNRdKOiOjLjXsGt5mZFeVkYWZmRTlZmJlZUU4WZmZWlJOFmZkV5WRhZmZFOVmYVVA6fZjt28dIpw8XP9isiThZmFXI0NAIXV2bWLv2q3R1bWJoaKTeRTKrGCcLswpIpw/T37+F8fFJDhyYYHx8kv7+La5hWMsoKVlI+k1JpyTP/6ekr0t6c3WLZtY8RkcP0NEx89epvb2N0dEDdSqRWWWVWrP4XxFxUNLbgXXALWR2sDMzoLv7VCYmpmbEjhyZorv71DqVyKyySk0WR5Of/xm4KSLuADqqUySz5pNKLWFwcB2dnYtZurSDzs7FDA6uI5VaUu+imVVEqavOPi3pC8Aa4FOSTsD9HWYzrF/fw5o1XYyOHqC7+1QnCmsppSaL9wCXAZ+OiOeTvbH/sHrFMmtOqdQSJwlrSSXVDpKNivYBb09Ck8Cj1SqU2ULgORnWTEodDfUJMjvcXZ+E2oH/V61CmbU6z8mwZlNqv8NVwLuBFwEi4hnglGoVyqyVeU6GNaNSk8VEZLbUCwBJJ1WvSGatzXMyrBmVmixuS0ZDnSbpQ8A9wBdnO0HSZkn7JO3Kir1a0t2SHk1+virrvesl7Zb0iKR1WfELJT2YvPc5JZt3m+XTDP0AnpNhzajUDu5PA/8IfA14PfAnEXFjkdNuJjOCKtvHge9GxHnAd5PXSDofuBp4Q3LO30halJxzE7ABOC955F7TDGiefgDPybBmpEzrUpUuLnUDd0XEBcnrR4BLImIsGX77/Yh4vaTrASLiz5PjtgA3AKPA1oj4T0l8fXL+h4t9dl9fXwwPD1f+pqwhpdOH6eraxPj45Cuxzs7FPPHEhob9I5xOH/acDGs4knZERF9ufNZ5FpL+OSLeLukgSX/F9FtARMTSMstxZkSMkTl5TNIZSfxs4N6s4/YksSPJ89x4ofJuIFMLYeXKlWUWzZrZdD/A+Pix2HQ/QKP+IfacDGsmszZDRcTbk5+nRMTSrMcpc0gUs8nXDxGzxPOKiE0R0RcRfalUqmKFs8bnfgCz6iraZyGpLbuTep72Js1PJD/3JfE9wIqs484Bnkni5+SJm83QKP0AzdDBbjYXRZf7iIgpST+VtDIinpzn590JXAP8RfLzjqz4VyT9FXAWmY7sbRFxVNJBSW8F7gPeBxTrWLcFqt5rMw0NjdDfv4WOjjYmJqYYHFzH+vU9NS2DWbWUujbUcuAhSdtIJuYBRMS7C50gaQi4BDhd0h7gE2SSxG2S+oEngd9MrvOQpNuAh8ksJXJtREyvdPsRMiOrOoFvJQ+zvOrVD5A90W6636S/fwtr1nS5X8JaQqnJ4k/LvXBErC/w1jsLHP9J4JN54sPABeV+vlktNWMHu1k5SkoWEfEDSWcCFyWhbRGxb7ZzzBYSd7Bbqyt1IcH3ANvINBu9B7hP0m9Us2BmzaRROtjNqqWkSXmSfgqsna5NSEoB90TEm6pcvjnzpDyrB0+0s2Y3p0l5Wdpymp32453yzI7jiXbWqkpNFt9OluAYSl7/FvDN6hTJzMwaTakd3H8o6b8CbyMzq3pTRNxe1ZKZNSE3Q1mrKrVmQUR8jcyqs2aWhyflWSubtd8hmT39Qp7HQUkv1KqQZo1uLrvfeWkQayaz1iwiwlunmpWg3El5roVYsylrRJOkMyStnH5Uq1BmzaacSXneg9uaUamT8t4t6VHgceAHZDYl8hpNZolyJuV5D25rRqV2cP9v4K1kJuKtkvQOoNDaT2YL0vr1PfT2nsG2bWOsXr2cnp5leY/z0iDWjEpthjoSEfuBNkltEbEV6K1escyaz9DQCBde+CU+9rHvceGFXyq4B7iXBrFmVOpyH/cAVwJ/DpxOZtOiiyLil6taunnwch9WS3PZA7waczJGRvYXrdmYzWaue3D/AnAmcAUwDvw34LeBLuC6KpTTrCnNZYnySi8Nct1197Bx485XXg8M9HLjjWsqdn1b2Io1Q/1f4GBEvBgRUxExGRG3kFnq44ZqF86sWdS7H2JkZP+MRAGwceNORkb21+TzrfUVSxbdEfFAbjDZkKi7KiUya0L17ofYtm2srLhZuYqNhjpxlvc6K1kQs2ZXzz3AV69eXlbcrFzFahbbJX0oN5jsob1jLh8o6fWSdmY9XpD0e5JukPR0VvzyrHOul7Rb0iOS1s3lc81qIZVawkUXLa/5yKaenmUMDPTOiA0M9LqT2ypm1tFQyVaqtwMTHEsOfUAHcFVE/Pu8PlxaBDwNvAX4AHAoIj6dc8z5ZJZGXw2cBdwDvC4ijs52bY+GsoXIo6FsvuY0Gioi9gK/nEzCuyAJfyMivlehcr0TeCwinpBU6JgrgFsj4mXgcUm7ySSOH1eoDGYto6dnmZOEVUWp+1lsBbZW4fOv5tiGSgADkt4HDAN/EBH/AZwN3Jt1zJ4kdhxJG4ANACtXeukqM7NKqdvWqJI6gHcDX01CNwGvJTMzfAz4zPSheU7P23YWEZsioi8i+lKpVGULbGa2gNVzH+13AT9JmrqIiL0RcTQipoAvkmlqgkxNYkXWeecAz9S0pGZmC1w9k8V6spqgJGWP8bsK2JU8vxO4WtIJks4FzgO21ayUVhZv6GPWmkreVrWSJC0B1gIfzgr/paReMk1Mo9PvRcRDkm4DHgYmgWuLjYSy+vCGPmatq6SFBJuRh87W1lwW0jOzxlNo6Gw9m6GshXhDH7PW5mRhFVHvhfTMrLqcLKwi6r2QnplVV106uK25lLpJTz0X0jOz6nKysFmVO8Kp0hv6mFljcDOUFZROH6a/fwvj45McODDB+Pgk/f1bPIfCbAFysrCCPMLJzKY5WVhBcxnh5BncZq3JycIKKneE09DQCF1dm1i79qt0dW1iaGikxiU2J2urFs/gtqJKGQ3lGdz15+VWrBI8g9vmrJStQt2/UV8ejGDV5mRhFeEZ3PXlZG3V5mRhFZHdv3HSSe2ewV1jTtZWbU4WVlGZPrCgVfvCGpWXW7Fqcwe3VYQ7uBtDqUuzmBVSqIPby31YRUy3mY+PH4tNt5n7j1bteLkVqxY3Q1lFuM3crLU5WVhFuM3crLW5GcoqxkuUm7WuutQsJI1KelDSTknDSezVku6W9Gjy81VZx18vabekRyStq0eZrTT33TfGF77wAPfdN1aXzx8Z2c8tt+xiZGR/XT7frFXVs2bxjoh4Nuv1x4HvRsRfSPp48vqPJJ0PXA28ATgLuEfS6yLiaO2L3PjqORrmjW/8O3btyvyRHhx8kDe+cRkPPPCBmn3+ddfdw8aNO195PTDQy403rqnZ55u1skbqs7gCuCV5fgtwZVb81oh4OSIeB3YDq2tfvMY3vZDfO95xW80X8rvrrsdeSRTTHnxwP3fd9VhNPn9kZP+MRAGwceNO1zDMKqReySKA70jaIWlDEjszIsYAkp9nJPGzgaeyzt2TxI4jaYOkYUnD6XS6SkVvTOn0Yd7//m8xPj7Jiy8eYXx8kve//1s1Wxvon/5pd1nxStu2LX+zV6G4mZWnXsnibRHxZuBdwLWSLp7lWOWJ5Z1JGBGbIqIvIvpSqVQlytk07r9/73FDVycmprj//r01+fwrr/yFsuKVtnr18rLiZlaeuiSLiHgm+bkPuJ1Ms9JeScsBkp/7ksP3ACuyTj8HeKZ2pW0Ozz//clnxSnvLW5ajnLQuZeK10NOzjIGB3hmxgYFeenqW1eTzzVpdzZOFpJMknTL9HLgU2AXcCVyTHHYNcEfy/E7gakknSDoXOA/YVttSN77TTjuhrHiljY4eYOnSjhmxU07pqOmqpzfeuIaHH/4AN998GQ8//AF3bptVUD1GQ50J3K7Mf0MXA1+JiG9L2g7cJqkfeBL4TYCIeEjSbcDDwCRwrUdCHW/FiqVlxSutUWZw9/Qsc23CrApqniwi4ufAm/LE9wPvLHDOJ4FPVrloTe2pp14oGK/FH8/pGdz9/Vtob2/jyJEpz+A2ayGewW0V4xncZq3LyaLBzHVS3apVZ9LWJqamjg0Ua2sTq1adWY1iFuRVT81aUyNNylvwpifVrV371bIn1T377PiMRAEwNRU8++x4gTPMzErnZNEg0unD9PdvYXx8kgMHJhgfn6S/f0vJk+puv/1nZcXNzMrhZNEgpjcPyja9eVApHnnkubLiZmblcLJoEN3dp3Lw4MSM2KFDEyUPPX300fxJoVDczKwcThYNItPnMDM2NUXJfQ7//u/5m6sKxc3MyuFk0SDmuxDec8+9VFbczKwcThYNYr4L4S1Z0l5W3MysHE4WDaKnZxkXXDBzpvUb31j60hVnnXVyWfFC0unDbN8+VrOlzc2sOThZNIiRkf15Nw8qdfOeU07pKCueTz03TzKzxuZkUWFz/Z/5Pfc8UVY812OP/UdZ8Vz13jzJzBqbk0UFzWcGdmdn/pVXCsVzvfzyVFnxXPXePMnMGpuTRYXMdwZ2gc3/ZonP9NrX5p+PUShuZlYOJ4sKycy0nvmHPSJKnoGd219RLJ7r2mvfXFY816pVZ9LePnOru/b22i9EaGaNycmiQk4+uYPx8Zl7Mr300lFOPrm0DuYnnsifVArFc23dmr9vo1A8Vyq1hFtuuZwTT1zESSct5sQTF3HLLZd7BVkzA7xEecUcOjRBe7s4cuRY7aK9XRw6NDHLWcecdtqJZcVzbdkyWlY8H+9HYWaFOFlUyMknd8xIFABHjkTJNYuenleXFc911lknsWfPi3nj5fB+FGaWT82boSStkLRV0oikhyR9LInfIOlpSTuTx+VZ51wvabekRyStq3WZS3Ho0MRxI5c6OxeXXLP40Y+eLiueK3ddqWJxM7Ny1KNmMQn8QUT8RNIpwA5JdyfvfTYiPp19sKTzgauBNwBnAfdIel1EzOwgqIPsXe26u09lcnJmkSYnj5a8auyiReXFcx09mn/UVKG4mVk5al6ziIixiPhJ8vwgMAKcPcspVwC3RsTLEfE4sBtYXf2SHpNvol3unIqvf/1nHM1JX7mvZ/P61+df1qNQPNfb3pb/n7BQ3MysHHUdDSWpG1gF3JeEBiQ9IGmzpFclsbOBp7JO20OB5CJpg6RhScPpdLoiZRwaGmHlyi9w8cW3snLlFxgaGsk7p+J3f/d7ebc13br1yZI+58knXygrnmvp0hPKipuZlaNuyULSycDXgN+LiBeAm4DXAr3AGPCZ6UPznJ63bSUiNkVEX0T0pVKpeZcxnT7Me9/7DV566egrj/e+9xvcf//e43a1U75SAnv31mZS3kkn5V9dtlDczKwcdUkWktrJJIovR8TXASJib0QcjYgp4Isca2raA6zIOv0c4JlalHPr1ifzNi09+eQLxy2NoQLZYs2arpI+6/zzTy8rnutXf3VFWXEzs3LUYzSUgEFgJCL+KiuevXHDVcCu5PmdwNWSTpB0LnAesK0WZd279/ihqADj45MMDq6js3MxS5d20Nm5mM2bL2NgoHfGcQMDvSUvMX7aafmbiwrFc734Yv5RV4XiZmblqMdoqLcB7wUelLQzif0PYL2kXjLtLqPAhwEi4iFJtwEPkxlJdW2tRkKtWdNdMN7Ts+y4CWz/+q+lDXMt97PMzOpNEa05tLKvry+Gh4fnfZ11627jO9851kl96aUr2bLlPccdNzKyn/PP/7vj4g8//IGSaxfXXXcPGzfufOX1wEAvN964pqRz0+nDnH32TcfNIH/66Y94kp2ZlUzSjojoy417bahZpNOH+dGPZnaP/OhHz+RdSfb223+W9xqF4pXmtZ3MrJq83McsRkcP0NHRxvj4sVh7exujowfy/BEuMByqYHymkZH9M2oVABs37uSjH11Vcs3EazuZWbW4ZjGL7u5Tjxv1dOTIVN5Z2VdddV7eaxSK59q2bayseCGp1BIuumi5E4WZVZSTxSxSqSXHjXoaHFyX9w9xT88yLr105YzYpZeuLLlWsHr18rLiZma15GaoItav76G39wy2bRtj9erlBf/4z9a/Ucr/8nt6ljEw0HtcB3epycbMrJqcLHJkLw6YSi1haGiED37w2yxaJI4eDTZvvoz163uOO2+2nfJKbRK68cY1fPSjq4omJjOzWnOyyDI0NEJ//xY6OtqYmJjis599B9ddd8+M4ajXXPNN1qzpOi4BzHenvGk9PcucJMys4bjPIpFvccCPfex7eTc0uv/+vced/9RT+Rf8KxSfrRy5K9yamdWbk0Viephstra2/MNen3/+5aqUIXfZ86Ghkap8jplZuZwsEvmGyeYuOT4t33pNK1YszXtsoXiufDWb/v4trmGYWUNwskjkGyb713/9a7S3z6xdtLeLVavOPO78+TZD5avZTE8ANDOrN3dwZ8k3A3rXrvSM4awf/vCb8o5uKtQ0VWqTVTkTAM3Mas01ixzZM6DT6cMMDu6a8f7g4K68TUPzXWK8nAmAZma15ppFjux5FuWsDbVq1ZmvDLmd1tHRlrfJqhCv7WRmjcrJIsvx8ywuYXx8csYxL700mbdpKJVaws03v4v+/i20tYmpqZhTzSCVWuIkYWYNx/tZJNLpw3R1bZqRHDo7F3PkyFEmJ0vfIyJ3BriZWTMptJ+FaxaJfE1ObW3ihBMWMTmZnUDaZ13CwzUDM2tFThaJQvMscmteHqFkZgtR04yGknSZpEck7Zb08Upfv9BopM2bL/MIJTNb8Jqiz0LSIuBnwFpgD7AdWB8RDxc6Z657cOfrc3A/hJktFM3eZ7Ea2B0RPweQdCtwBVAwWcxVvj4H90OY2ULXLM1QZwNPZb3ek8RmkLRB0rCk4XQ6XbPCmZm1umZJFvmWfz2u/SwiNkVEX0T0pVKpGhTLzGxhaJZksQdYkfX6HOCZAseamVmFNUuy2A6cJ+lcSR3A1cCddS6TmdmC0RQd3BExKWkA2AIsAjZHxEN1LpaZ2YLRFENn50JSGnii3uWooNOBZ+tdiCpoxfvyPTWPVryv+d5TV0Qc1+nbssmi1Ugazjf2udm14n35nppHK95Xte6pWfoszMysjpwszMysKCeL5rGp3gWokla8L99T82jF+6rKPbnPwszMinLNwszMinKyMDOzopwsGpSkUUkPStopaTiJvVrS3ZIeTX6+qt7lnI2kzZL2SdqVFSt4D5KuT/YreUTSuvqUurgC93WDpKeT72unpMuz3mv4+5K0QtJWSSOSHpL0sSTetN/XLPfUtN+VpBMlbZP00+Se/jSJV/97igg/GvABjAKn58T+Evh48vzjwKfqXc4i93Ax8GZgV7F7AM4HfgqcAJwLPAYsqvc9lHFfNwD/Pc+xTXFfwHLgzcnzU8jsH3N+M39fs9xT035XZBZVPTl53g7cB7y1Ft+TaxbN5QrgluT5LcCV9StKcRHxQ+C5nHChe7gCuDUiXo6Ix4HdZPYxaTgF7quQpriviBiLiJ8kzw8CI2S2AWja72uWeyqkGe4pIuJQ8rI9eQQ1+J6cLBpXAN+RtEPShiR2ZkSMQeYXATijbqWbu0L3UNKeJQ1uQNIDSTPVdDNA092XpG5gFZn/tbbE95VzT9DE35WkRZJ2AvuAuyOiJt+Tk0XjeltEvBl4F3CtpIvrXaAqK2nPkgZ2E/BaoBcYAz6TxJvqviSdDHwN+L2IeGG2Q/PEGvK+8txTU39XEXE0InrJbNWwWtIFsxxesXtysmhQEfFM8nMfcDuZquNeScsBkp/76lfCOSt0D029Z0lE7E1+iaeAL3Ksqt809yWpncwf1S9HxNeTcFN/X/nuqRW+K4CIeB74PnAZNfienCwakKSTJJ0y/Ry4FNhFZg+Pa5LDrgHuqE8J56XQPdwJXC3pBEnnAucB2+pQvjmZ/kVNXEXm+4ImuS9JAgaBkYj4q6y3mvb7KnRPzfxdSUpJOi153gmsAf6NWnxP9e7d9yPviIfXkBnB8FPgIeCPk/gy4LvAo8nPV9e7rEXuY4hMNf8Imf/h9M92D8Afkxmt8QjwrnqXv8z7+hLwIPBA8gu6vJnuC3g7meaJB4CdyePyZv6+Zrmnpv2ugF8E7k/Kvgv4kyRe9e/Jy32YmVlRboYyM7OinCzMzKwoJwszMyvKycLMzIpysjAzs6KcLMxmIelosjLpQ8lKn78vqWK/N5LeL+msrNd/K+n8Sl3frFI8dNZsFpIORcTJyfMzgK8A/xIRnyjjGosi4miB975PZgXU4UqU16xaXLMwK1Fkll7ZQGYROiW1go3T70u6S9IlyfNDkv5M0n3AL0n6E0nbJe2StCk5/zeAPuDLSe2lU9L3JfUl11ivzJ4muyR9KutzDkn6ZFLTuVfSmTX8Z7AFysnCrAwR8XMyvzfFVvw9icx+F2+JiH8GNkbERRFxAdAJ/HpE/CMwDPx2RPRGxPj0yUnT1KeAXyOz4N1Fkq7Muva9EfEm4IfAhyp2g2YFOFmYlS/fSp65jpJZwG7aOyTdJ+lBMgngDUXOvwj4fkSkI2IS+DKZTZcAJoC7kuc7gO5SC242V4vrXQCzZiLpNWQSwT5gkpn/4Tox6/lL0/0Ukk4E/gboi4inJN2Qc2zej5rlvSNxrLPxKP49thpwzcKsRJJSwOfJNCkFma1veyW1SVpB4R3IphPDs8neCr+R9d5BMlt+5roP+FVJp0taBKwHflCB2zCbE/+PxGx2ncmuZO1kahJfAqaXu/4X4HEyK5juAn6S7wIR8bykLybHjQLbs96+Gfi8pHHgl7LOGZN0PbCVTC3jmxHRjEvSW4vw0FkzMyvKzVBmZlaUk4WZmRXlZGFmZkU5WZiZWVFOFmZmVpSThZmZFeVkYWZmRf1/TvPpwJ6twaMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3ccf3e8",
   "metadata": {},
   "source": [
    "3. Matplotlib"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "484d50b1",
   "metadata": {},
   "source": [
    "1. Write a Python programming to create a below chart of the popularity of programming Languages.\n",
    "2. Sample data:\n",
    "Programming languages: Java, Python, PHP, JavaScript, C#, C++\n",
    "Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b638f95d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAV0AAADrCAYAAADKbEVrAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABMbElEQVR4nO2dd3hc1bW33z1No1G1VW25yMbCEi4YA1HAQOgJ2J8hBELaF8hNSEhIIQkhSrk3JITEXD5SSCOhhxqqMYhig8FgG4QBV1mW5SJbGmnU6/Q5Z39/nDHYlkaS5dEUab/PM4+ks0/5jTTz05511l5LSClRKBQKRWwwxVuAQqFQTCSU6SoUCkUMUaarUCgUMUSZrkKhUMQQZboKhUIRQ5TpKhQKRQxRpquYUAghCoUQTwgh9gohdgohXhJCnHjY+ONCiGIhxI1CiC/EU6tifKJMVzFhEEII4DngTSnlCVLKk4CfAwWH7TZLSlkPfAp4O/YqFeMdoRZHKCYKQojzgVuklOcMMvYocAowBTgAlAB1wF+llPfGVKhiXGOJtwCFIobMBz4YbEBK+WUhxOeB6cAzwB1SyqtiKU4xMVDhBYXiY04BtgALwl8ViqijZrqKiUQ1cOXRG4UQlwK/A2YBy4A8wC2EuFBKeV5sJSrGO2qmq5hIrAVShBDXHdoghDgdcAOnAjuklAswzPkUZbiKsUCZrmLCII27xp8FLgqnjFUDtwBNGKGFrUIIG2CVUvbGT6liPKOyFxQKhSKGqJmuQqFQxBBlugqFQhFDlOkqFApFDFGmq1AoFDFE5ekqkoq/Xb/WBmQDKeGHbZCHCSMNrD/86AW6brj7fD0OkhWKI1DZC4qE4m/Xry3CqHsw7ajH9PDXPECM4tQS6AY6gFZgH0Zthd2HHjfcfX7/ccpXKIZFma4ibvzt+rXFwGKMhQmLw4/8OEpyYRhwLfAesP6Gu8/fFUc9inGIMl1FTPjb9WutwBnAheGvpwA5cRU1MtqADcD68OODG+4+PxRfSYpkRpluAiGEKAT+BJwO+IF64EYp5e44yho1d169bIYw5VyQknXNFVLKc4UQ6fHWFAU8wLvAC8AzN9x9fkOc9SiSDGW6CUK4wPZG4CEp5d3hbYuADCnl2+GfrwWKpZS3DHGeeill8VjrjcSdVy8rA74kpVwuhFgopQxZs76tWcyOlHhpGkMksAl4Gnj6hrvP3x9nPYokQJlugjBUge3D9rmWBDTdO69elgN8UZfyayYhFh897qG8efKkJVNiqSlOfIhhwE/dcPf5e+ItRpGYqJSxxCFige1E5M6rl1mBpbqU1wpYKoSwmMTgSQV6cHcQlsRWYHw4dDPwd3+7fu064B/AszfcfX4wvrIUiYQy3QRHCJEDvB7+cTJgE0JcHv75/0optwsh/sbHrjZVCLEl/P1TUsrboqnnzquXTZZSfkfCD0xC5EYy2sNJMXVNjqaGJOFT4UfLS5/+0R2zDrz8eNmumqZ4i1LEHxVeSBCEEBcAv0rU8MKdVy+bFdL0m00mca1JCPuxHq+lXN6R5pidDNkK0UXK/nPW36RbNF8q8B/gj2W7aj6MtyxF/FDLgBOHQQtsCyE+FUdN3Hn1slNXXHnJc1LKPRaz6frRGC6A17N1Qi48MLd84LJovkzACnwF+KCmtOy1mtKyT8RZmiJOqPBCgiCllEKIzwJ/EkJUAD7CKWPx0HPHVZeWhXR5l81ivtBqNh/3+Ux646jMOtk5sb4yb5DNFwBVNaVlzwK/KNtVoxZgTCBUeEFxBLdfeWlhUNP+ZLdarhJCRO2TkJRSt2R+K2i1pI/H1LFBCXTta/vM1jsHM93D0YAHgVvKdtU0jr0qRbxRpqsA4M6rl6V7A8Ff2yzm75pNJttYXMMrPtE4KfusaWNx7kSkcNu/nCd1bi0a4e4+4C/A78t21XSNoSxFnFExXQW3fvbiG0Ka3phqs/5orAwXQAvsnjBVvgK+bk9px9apx3CIHfgJsK+mtOz6mtKy0RT1USQBKqY7gfnlsgsW2K2WRx0224JYXC/F1J2j6zom0/j/X5/lXN9qEhSP4tBsjPzeq2tKy75Rtqtmb1SFKeLO+H/1Kwbws6XnWX657IK7slLtm1Nt1pgYLoDVTJrHt689VteLF5oW1Bc63yw4ztOcC2yrKS37UU1pWdTfp0KIqGaTCCF+IYSoFkJsE0JsEUKUH8OxU4UQTw+zT7YQ4jvHrzT+KNOdYNz06XPOdNiseyelpX7PZBLHn5ZwjPg828Z96pho29aUpntTo3AqB3AnsLGmtOykKJxvTBBCnAEsAxZLKRdiVJIbUSEgIYRFStkkpbxymF2zAWW6iuThK2csFj+99Ny/FGRlvO2w2WbES4dJb4yGGSU0Jx18NdrPsRzYXFNa9t81pWXWaJ1UCJEuhHhdCPGhEGK7EOKy8PbbD59VCiFuEUL8ONL+wBSgXUrpB5BStkspm8LHni6E2CiE2CqEeE8IkSGEuFYI8ZQQ4gVgtRCiWAixI7z/tUKI54UQrwghaoUQvwpfYwVwQngWfUe0fgfxQGUvTAC+csbiWbNyJ72Q7UidF28tUkppyfym32rJGJd5u/6egx2XbL59LFfebQCuKttV03w8JwmHF7IBh5SyVwiRi1GysgRYBPxJSvmp8L47gc8ATRH2T8OoNewAXgP+I6VcJ4SwAbuAq6WUm4QQmRilMb8C/BZYKKXsFEIUAy9KKeeHV13+HqMWiQejitu1QPuhfY7neScCaqY7zrnunE9cXTYlb2siGC4YJSz7+7e0xVvHWDGt4XXvGF9iCfBhTWnZWVE4lwB+J4TYhmGWRUCBlHIzkB+OtZ4MdEkpDw6xfz9G949vYhR9/0/YPOcCzVLKTQBSyl4p5aEC8GuklJ0RdK2RUnZIKb3As0A0nmvCoEx3nDKvqNDygwvP+teJBXmP2a3WjHjrORwtsHtcfrwK+Pt8Ze0fHEua2GgpBNbWlJZ97zjP82WMnnOnSikXAS0YqWtglKi8ErgaeGK4/aWUmpTyTSnlr4DvAp/DMOlIf2v3ELqOPmZcvV6U6Y5Drjh1ftHyRWXvz8jJvs5kit6qsmiRYurJ1fXxl7Kb0bSxxYKM1e/bCtxVU1r2cE1p2WhjyFlAq5QyKIQ4D5h52NgTwBcwjPfpofYXQswVQpQcduwi4ABGaGGqEOL08H4ZQoiRpKleJISYLIRIBS7HCKn0AQk1eRgtCfeGVBwfl50y78yF06Z8mJuednK8tUTCasbh8e4dV6ljuh7SFzS+PtyS37HgKxjZDbNGekDY+PzAo8BpQoj3MWaxH9WAkFJWY5icU0p5KH4caf904CEhxM5w6OEkjIL8AYyZ8l+EEFuBNXw8kx6K9cDDwBbgGSnl+1LKDmCDEGKHupGmSAjmFRWKkvyca04rnvaXVJs14XuR9YdmHMjNu3Lm8HsmB1rLVudFNf8a6ZLfsaALWF62q2b9cDuG47T3SCkTrtJZOBZ8mpTyu/HWMlaome44YF5RoXne1IJfls+ecXcyGC6AWTaNq9SxuQdfjVoq1yiZBKyuKS1bNtROQojrgceBX8ZElWIAaqab5MwrKkw5dWbRn+YXFVxnNplivthhtEgppTnjGz6bNSvpzdff19R1yQe3TYq3jjAh4Otlu2r+HW8hisFRM90kZl5RYcYnZ894fOG0wm8lk+HCR6lj4yKuO6Xh9b54azgMC/BgFDIbFGOEMt0kZV5RYd5pxdOeKJuS99lw+/akQw/WxVvCcRMMuP3zWt+LZyx3MARGZsNN8RaiGIgy3SRkXlFhwSkzpj68oKjgkiT1WwDspt5cXdeTOr6V2vyuy4qeqJ8y7qgpLVOx2wRDmW6SMa+oMG/htML7Fk2fcnGyznAPYTGT6vHuTtoQg65rcmHja4nebPPWmtKym+MtQvExynSTiHlFhTnziwruWTyz6JJkN9xD+Dzbh1qZlNDoHTWu7GBvMmSLrKgpLftSvEUoDJTpJgnzigonnzQl/+7Tiqf9H1MUe5fFG7NsSou3htFScnBNsvwdBPBATWnZBfEWolCmmxTMKyrMnjE5+/+dPmva5ePJcAHsllBeINDtibeOY8Xf39Izq2/P8RYqjyU24Nma0rKEXak4URhXb+DxyLyiwrScNMevzz6x+GqzyTTu2isJIeh3b+6It45jpaDxjZ54axgFmcBLNaVlcaunrFCmm9DMKyq0At8qnZK3JMViccRbz1ihB/fEW8IxEQp6g/Nb3olFNbGxYCrwSk1pWaIs5phwjLuZ03hhXlGhAL4InLxhz4EXTUJ0zsnPuXC83EA7HLu5N0/XdWkymQY8t0fevIMdB94lIzWbX3z+PgDcvl7uf+1WOvtamJxRwNcv+h8cKQMLUK3d9jQbd72EQDB18iy+cu7NWC02Vr77L3Y2vMe0nDl89fwKAN7bvQa3v5fzFnxuWL0pzZuabTKUzLPFMuD5mtKyC8p21QTjLWaioWa6iYsVo02LG+DtuvqN79c7n9B0PRBfWdHHYhJ2t2fXoIXNP3nip7nh0t8fsW3NlseZW7SYX33x38wtWszqzY8POK7b3ca6Hc9x8xX/4Befvw9d6nywdy1efz/7W6r5+VX3oksdZ8c+AiE/79a+yjknXTbgPEcjpc78xjXZo3umCcXZwG3xFjERUaYbR4orKq8rrqj81mBj1U5XAONN0Y/xkZDtTtfutbv23u8PhZIxnjgkPu+OQW+mzZm6EIc984ht2+o3Un7ixQCUn3gx2+o3DHpOTdcIhvxoukYg5CPLkYsQJkJ6CCklwZAfs8nC61v/w7kLPovZPPwHv1BnnSsn0Jk57I7JwU01pWWXxFvEREOZbhxwlJTnFl33z2XA34C7iysq/1RcUTlgVVO109WE0UtqD1AMmBo6e1oqt+66p8/nb4yp6DHGIptHnO/a5+0iK81Yk5CVlkOft3vAPtlpeVxw8lX896Nf5BcPX0WqLZ2y6adhtzlYNOtsVjzzLXIyC0m1pXGgtZaFxUtGdO0TDq4eqcxkQAD/riktS7RlzOMaZboxxlFSnm3OzPudOTP3SYwQAsAPgBeKKyoHzKCqna5e4I/AGxjGa+32+twrN+98qLWvf3usdI81dkso1x/ojFrqmMffx/b6jfz6S49y21eeJBDy8t7uNQBctOgL/OzKf3HFGd/mxfcfYOnp17KxppL71vyGVz58JOI5/Z72vjk9uwqjpTFByAUeqyktS9SlzOMOZboxxFFSbhWWlBuyzrj6cpPVfnRJw0uAjcUVlQM6AFQ7XUHg38AjwDQgLahpoRe37np2X1vnG+OhPKcQAvcIU8cyUifR4zZ27XF3kJGaPWCfXY0fkpNRSEZqNmazhZNnnc3+lp1H7NPQbhTcyc+aRtXuNXz9ov+hqXM/rT2Df4jIbVwXqZFisnMO8Kth91JEBWW6McJRUi6Az2eWf+5aS/rkSG1d5gFVxRWVA7qfVjtdstrpWg3cidGrajLAm7X73tp8sOkpXddDRx+TbOjBvSPKzFgw80yqdhsf86t2r2Zh8ZkD9pmcns/+1hoCQR9SSmqdH1Iw6ciEgxc3PcDS065F0zWkNHq2CWEiEPIPOF8o5A8tdK2fcsxPKnn4RU1p2fnxFjERUKYbO5akzj7tGymFc+YMs18e8HpxReVXBxusdrq2AbcCQWAKwJaG5p3rdu9/IBDS+qOqOMbYzX15uh46Ytr+wGu/5c6V36Olp4FfPnI1G3e9xEWnfIFdjR/w68e/yq7GD7ho0RcB6Ha38/eXfgZAcUEZp8w6h9ufvZ7fPfUNpJQsKVv60Xm37l/PzLxSstNycaSkU1xwErc99Q0Egmk5JwzQZm35oClFD9jG8vnHGRPwqMrfHXtU54gY4Cgpn2myp982+eLvXGay2o+lQMoK4Of1K5YO+CPNKyrMxmh1fQJwEJCT01IzLjqp5EtpKbakjTsGrJ9uyUyfl1DLa6WULHj3lu58f3t2vLXEgH+W7aq5Pt4ixjNqpjvGOErKrcA3Mk+7/JRjNFyACuCZ4orKAUVhqp2ubuAOYCMwC7B0ur19KzdX39/R7645Xt2H8/bu/dzxyjrueGUdb+3eH3G/g53d/OSpSrY2GM1j+31+/rp2I3e8so4dTtdH+z2w/n16vL5BzxHwbh98II4Eu/a2ThDDBfhmTWlZebxFjGeU6Y49F6VMX3C6rWD2SaM8/rPA28UVldOOHqh2uvzAfcB/gOlAqj+kBZ/fUvPkgY6ut0cv+WOae/p4d99BfnDhWfzo4rOpaWqhrW9gNUZdl1Ru28Xcgo/D1ZsPNnHazGl874IlvLlrn6G5qYWiSZlkpQ7eidsiXQlXKnFWw5qJtGpLAHerbIaxQ5nuGOIoKZ8qrCmfzzj508c7czgFeK+4ovL0oweqnS692umqBO4CcoBsgNdr9q7d1tD8nC6ldjwXbu3tZ2bOJGwWM2aTidl5OUfMWg+xfk89C4sKSbenfLTNbDIR1DQ0XUcI0HSdt3fv59y5A2Omh7Bb9Ry/vz1hYtMBb5e7pHP7RMtjXYQRulKMAcp0xwhHSbkZ+FrGqcsXmVIc2VE45RRgXXFF5ecHG6x2uj7AWEgBUAjw/gHntvV19Q8FNW3U+a+FWensa+vE7Q8QCGnscrXS7fEesU+Px8cOp4szTph5xPZTZkyltqWNe956j4vnncjGPQc4tXgaNsvQkyi3e3PCpGZlO99qN42/chcj4daa0rJkLeqT0CjTHTvOsRWWnJkytXRhFM+ZCjxRXFE5aE5ltdNVD/wGaAZmAGJPa0fDKzt23+MJBFpHc8GCzAzOK53Nv9ZVcc9b7zElKxPTUSV9n99SzdKFpRxdrybVZuUbZ3+CGy86i6JJWdQ0t7KwqJCnNm3joY0fUN/eNeg19dC+hHhdalpAO7npraS9KXmcZGAsylFEGZW9MAY4SsrzMFl+l/OZ711mTs2IlJN7vDwBfK1+xdIBN57mFRWmAl/DKJjTAIRSrVbbZ+afeOWktNSS47noS9t2keWws2RO8UfbbqtcC+GXkTsQwGo2c9VpC5hf9LFfPb95J/OLCmjrc6NLyeKZU3lg/ft8+7wzBlxD06XfPukHVrPJElfzlU3vNVyw+6Hp8dSQAFxctqtmTbxFjCcSYkYxnggvgvi/GadcesoYGi7AF4A3iysqB8zEqp0uL/BPYCXGjNfuDQYDz2/Z+XhjV8+7x3qhPp+xWKDL7WW708UpM44Mcf5i6fn8YpnxWDhtClcsnn+E4bb1uen1+TghP4egpmF8XBeEdH3Q65lNIsXtrhnVzDyanNTw6qCthH7R3MxZe+pYvn/fR9te6evl/+zfx7zaXezweQc7DL+uc/WBej5bv5//s38ff2n/uLDanW2tXL5/PxXNTR9tW9XTw8NdcY+03F5TWjYh4ytjhTLd6PMJa870T9lnLFwUg2uVY9xgG9CCpdrp0qqdrueAvwP5QJYupVxdXfdqdVPLi/qhJVgj4N8bP+B/X1nH/es3ccXi+ThsVjbuOcDGPQdGdPzL22v5zPy5ACyaMZVN9Q385fUNfGru7IjHBHw74po65u+ub5/idU0ebOyzWVn8a9qRE+ASWwp3FRVxWurRq7s/xiYE90+fwXPFs3i2eBbr3W62er30aRqbvV5WzpqFJmG334dP13mut4cvZMd9rcIpwPBFhhUjRhUxjyKOkvJs4Jr0hReXCpMpVik304H1xRWVX65fsXTV0YPVTte784oK2zGK6uQDrVX7Gj7o9vg6ymdNv9piNg2eu3UYN5w/cJntmXNmDrInfOETA1twffXMxR99n2FP4XsXDF/Ry0LLwKrkMWTGwdcimv5pDgfO4JFljU9ISYmw98cIIUgL35QLSUkoHNozCQhKiZQSv9SxILi/s5OvZE/Cmhg38X5dU1r2bNmumhH/o1ZERs10o8tV1twZeZZJU0+M8XXTgeeKKypvHmyw2unag3GDrROjYA61rrb61Tvr7vEGgwnZn8xu0XN8/ra+eFw74OvxlnZsHpM0MU1KPlu/n7P21HFmWhonp6aSZjJzcXoGVxyop8hqJcNsZofPywUZcf2/8xESpr14urg83jrGC8p0o4SjpHwqcGb6/Avnxqmjjgm4vbii8v7iisoBNQKqna424HfAdowSkWZXT1/nC1tq7u32+CIvM4sjHvfmwdMbxpjMpg2tZsGY/BHNQvBc8SzeOGEO270+6vxGvPzrOTk8VzyLn+YXcFd7G9/NzePp7m5+2OTk7o72sZAyLAEpg+tm6Vu/fqNZ//eF5lsXPLQgIabdyY4y3ehxiWVSkd0yuWh+nHV8DVhTXFGZc/RAtdPlwSic/jIwE0jp9wd8z2+ufqSpu/f9GOscFhnaF/NVUZoW1Bc61+aP9XUyzWZOdzh4233kOpCdPiOqUWyz8XxvD3+cWkSd3099IHZdmgJS+l+dFmr41ndM4m9fsJ3cnyqygZOAy2MmYhyjTDcKOErKC4Cz0hdcWJogjSPPwbjBVnb0QLXTFQKeBO7FWESRoUmpv7Jjd+UuV9srMoFyCO1md56mB2MaRxRt25vSNW/ku2HHQWcoRK9mLBD06TrveNzMth0ZC/5Lexvfy80lJCV6+C9hQuCLkOkRTQJS+l+eEWr85ndM5vv+r326O3tA/6KfjbmICYAy3ejwaUtWgd2aOz2aCyGOl9nAu8UVlZ8+eiBcm/ct4HaMBRd5ABv3HKh6b3/DY5quDywoGwfMJmFzu3fGNHWs9OArw95YvKnJyRcPHKA+EOC8vXt4prub1/r6OG/vHrb4fHy7sZHrGhoAaA0F+Vaj8X1bKMS1DQe5fP9+Pn+gnjMdaZyb/nGpidf6+phvTyXfYiXTbObk1FQu229Efkrtw8oaNQEpfS/PCDV+87sm8wNftk/zDDTbQ5y+4KEFF46ZkAmCWhxxnDhKynOB27PP+srJtoLZp8ZbzyBowA/rVyz9y2CD84oKC4EbMdq2NAIUZWfmnTt39pdSrJbsWImMRF+w8EBe/pcGT5WIMv7exs5LPvz9oGli4xG/lL7XirX2J5dZp3gzzSMN5Ty3/ZrtV4ypsHGOmukePxeZM3Ls1rziRfEWEgEzcFdxReXfiysqB8xgqp0uF0bNhhqMEpEmZ3dv2wtba+7p9foOxljrAKyiJWadd4saXh9YPm0c4pe694XiUON13zdZH/qSfdoxGC7AsgUPLRjLRT/jHmW6x4GjpHwScEH6govnxDAvd7R8G3i5uKIy++iBaqerH6NK2WqMzAZbr8/vWbl5579bevu3xlTlUdgtcpLP39I71tcJBvp9J7VtGtfVxPxS966aFWq87vtm28NftE/zpR+T2R7CCnwl2tomEsp0j48LTGnZqbaC2afEW8gIuRAjzjugZVC4+eVjwINAEZAe0nWtctuulXtaO16LZxjK3T/2qWNpTe+0WJDj8v3gk7r3+dmG2T7yhVGb7eH8V1SETVDG5YssFjhKyrOAT6fPv2CGMJmtwx6QOMzFaH557tED4Rtsa4H/xagylQPw1u79Gz444PyPpuvxKeat7R/TlZO6rsmFja/ljuU14oFP6p6Vs0ON1/3AnPLo1VEx20PMX/DQgtOidK4JhzLd0XMeYLLlzZoXbyGjYDKwurii8huDDVY7XdUYK9j8wFSAbY2uXW/s2nd/IBQa84/6R2M3e/I1zX9cxdiHQm+vbsoM9Q9a3CYZ8Und8+wJIed1PzDbH7vaPs2fZh6L97ma7Y4Slb0wChwl5SnAn1OKylKyPnnVtfHWc5z8AfhJ/YqlAxJB5xUVZgI3ACcSbn45yZGaftFJc76Ybk+JaYFrv/m85qzMU8akBfoJ79/ROrO/fswXRIw1Xql7XjpR73ruUuuUgGNMjPZwuoEp269JvJ52iY6a6Y6OuYDNPnPR3HgLiQI/AlYVV1QOWOhf7XT1AncCb2NkNli7PN7+lVt2PtDW566OpciAr3pMcof9fc3dyW64Xqm7ny4JOa+70WL/z5X2ohgYLhhtoT4bg+uMO5Tpjo4zAb81d3oyhhYGYymwobiickA+bLXTFQAeAB7HKJbjCIS00Atba57e19b5ZqwE2kRb9lict7BhbczDJdHCK3X3kyeGnNfdaEl98kp7UcBhivX7+doYX29coMILx4ijpDwVuMs+82Rr5mmXXRNvPVGmFfhs/YqlGwcbnFdUuAgj3ODFqFjGKTOmzjt52pTLTSYx9mVCU7/Ya7dPiVrebjDgDpy/8WdmK1qip/sdgQe9/4W5es+qS21TgvaYG+3hBIDJ26/ZPiHym6OFmukeO2WA2T59wWhbqicy+cDa4orKQfMwq52uLcCtGKvcpgBsPthU/dbu/Q8GQtqYd/B1u7dENXUstfm95mQyXA96/xOloaZv/NCS9swV9qI4Gy6ADTg3zhqSjnj/0ZKRMxEmn2Vy0Xg0XYAU4OHiisrbiisqBxTvqXa6DmJkNjRiVCoT+9o7nS/vqL3H7Q8M7M0eTaKYOqZLXS5oXJMUS37d6P2PlRlm++xn7VNDdlMiFFU6xMXxFpBsKNM9Bhwl5WnAotRZizNM1pRxk2IUgZ8DTxVXVDqOHqh2urqAO4B3MW6wWTr6Pb3Pb955f0e/p3asBNnN3nxN84eicS6tY5drUrAnMaqER8CN3vfoSaGm635sSVt5ecKZ7SGU6R4jynSPjZMAU8q0eePlBtpwfA54q7iicsDy2GqnywfcAzyF0TIo1RcKBVdt2fmfgx3dG8ZCjNkkrP3uHW3D7zk8JQdXJ6KBAdCP3vfovFDTdT+2pD9/mX1qyJaQZnuI0gUPLZjoHZOPCWW6x8Y5mCxe66SpA+rUjmNOxajNO6CCWrXTpVc7XS8Af8WoUpYtQb5Ws+e17Y2u53Upo76gIeDbedzVvP3u1t7ZvXUDuijHm3703ofnhZq/+WNL+vPLE95sD+eieAtIJpTpjhBHSXkmMC919qnZwmIdu+KmiclUjBnvoF1hq52uTRiVykxAAcCm+sYtG/Yc+HdQ0zzRFGIT7dnHe478xje7j19J9OhD7/33Aq35uh9bMl5Ybp+SRGZ7CBViOAaU6Y6ceQC2/Nmz4i0kTjgwYry/HGyw2unaD/waI+1sOiDqWtoPvlpdd683EIxKSAAgxSKzvD5n92iPDwW9wfmuDWOysu1Y6UPvfWih1nzdTZaMF5elTNGSz2wPceGChxYoLxkh6hc1cs4G+i2ZeRM5fiWAW4srKh8prqgc0HO82unqAFYAmwk3v2zt7e96fsvO+7o83j3REuFxb+kZ7bE21/vNKTIU1wJFveg9D5ysua67yZJRuTRlim5NWrM9RA6QLJX24o4y3RHgKCm3AicKS0qfKTUzIWZJcebLwJvFFZUFRw9UO11e4B/AKoyUMrsnEPQ/v3nnY41dPVVRubpWPyrTlFJnQePq7KhoGAW96D33L9Jc37zJkvnypSmF48BsD0dVHRshynRHRhEgUorKpiRBsfJY8UmMG2wLjh6odro04FngbowYb6YupVxdXffKzqbWSinlcXVZTLX48kOjSB0Lde5pyfF3xqwTxSF60LvvXaS5rvuJJeuVS8ad2R5iomT0HDfKdEfGDMBkyy+eEW8hCcYMYGNxReWyowfCtXk3Ar/DWHCRD/DuvoPvv7vv4KMhTR91dSqTEBZ3/7aWYz1uVsPqMSsPORg9Qu+6Z3HI9c2fWLJXX5JSKC3j+u02P94CkoVx/SqIIgsAtyWrYCLHcyORDjxfXFH548EGq52uOowbbF0YN9ioaW7bt2Zn3b2+YLBztBcN+muOaabr93T0z+naGZNylN1C7/rXqaGWb/7EMmnNp+3j3WwPoUx3hEyIV8Px4CgpFxiLInpNjiwVzx0cE/D/iisq7y2uqBwQb612uloxZrzbMVawmZt7+jpWbam5t8frqx/NBY81dSyncV2HSYztp/puoXXdfarW8q2fWCa9drG9QMakwmLCkLfgoQVJXSIzVkyoV8UoyQVSzek5FpPVntDLRhOAr2N0pBhQ06Da6XJjLKJ4BeMGW0q/P+Bdubn64eaevg+P9UI2C1leX2P3SPYNhfyhBa63x+wfZpfQu+4+TWv91k+sk9ZenDLRzPZwVFx3BEzYV8cxMAWQtoLZCbeCKUE5F6MH24AC79VOVwh4Argf4/eaoelSf3l77Qu7XW2vymOsM+pxb+4eyX6Wlg+bU/WA7VjOPRI6hdb5909ordf/xDJp7UUp+RPYbA+hQgwjYMK/SkbANADLpKkqtDBy5mB0HR6wPDR8g+1N4HaMBRe5AOv3HHh3U33j45quj3yZr3ZwQK7w0UgpmX/w1ah+QukUWsdfy7XW62+2Tn7zAmW2h6FMdwSoV8vwnAi4LRm5aqZ7bGQDLxVXVN4w2GC101WDUSLSjZGSxw5nS93amr33+UOhES1+MFLHvEN2KA5272vN90en60SHSev46ye1tutvtua8dX5KPnEvZ5twKNMdAepVMwThm2izgX5TamZevPUkIRbgr8UVlX8trqgckN9c7XQ1Y9RsqMNYwWZq6OppfXHrrnv6fP6G4U5uEsLc37+tdah9Zja8dtxt49tNWsddZ2ht3/6JNeet81LylNlGZPax7CyE0IQQW4QQO4QQTwkhHOHt/Uftd60Q4q/h728RQjgPO2559OTHBvXqGZoMjJSogLCmpMdbTBJzA8asN+vogWqnqw/4I7AWw3htPV6fe+Xm6odae/u3DXfikH9XxNSxgK/bM7dj26jTxNpNWvufz9Tav/MTa876c5XZjoC8BQ8tOJYUEa+UcpGUcj5G65/rR3jcH6WUi4CrgPuFEEn1h0kqsXEgD9ARQgizdUAxb8UxcTHwTnFF5QlHD1Q7XUHg4fBjKpAW1HTtxW27ntvb2rF2qPtrNlPHpEhj2Y1vt5kEx5wn1mbS2v+0RGv/zk9Tcjd8KiVXme2IMWPUYRgNb2PcCxgxUsoaIET4vkCyoF5NQ5MGYE6blCrEGCd5TgzKMDIbzjl6IHyDbQ1Gy/cswm/edbv3v/3hwaYnNV0fNExgM5Pp8R4c0DtN0wLaguY3B9SGGIpWk9b2h7O09ht+mpK78ZyUpHojJxDH9DsHEEJYgEsw8rgBUsPhgy1CiC0Ysf/BjisHdCBqVexiwdh3cE1u0gCT2ZGtZrnRIwdYU1xReX39iqUPHD1Y7XRtn1dU+BvgRoxZb9PWhuaaHo+3+6yS4i/aLJYBmQge95ZeR+qMI2a8ptZtTWmab0QrCFvNWtvDSzBVLUmJady+8b5G+rb0Ycm0UHJbCQCuJ1z0bulFWAS2fBvTvj4Nc9rg5T6kLtl7y16sk6zM/OFM4/gnXfRt6yN1RirTvjkNgK4NXWhujdyLY/J/JB+oHuG+qWFTBWOme1/4e284fAAYMV2OLKjzQyHEV4A+4OpjTTWMN2qmOzQZgDA5ssZ7P7RYYwPuL66ovKO4onLAa7Da6WrE6DpcT7j5ZX1Hd/NL22vv6ff7m47e36QPTB076eArw/7NWsxa6x3naB3fvTklr2pJymg/Fo+aSWdNovjHxUdsS5ufRsltJZT8toSUwhTaKiNP4jpWd5Ay9eOnrnk0PHs8lPy2BKlLfA0+9IBO9/pucs6P2dOLGO4ZhEMx3UVSyu9JKUeaLvjH8DFnSynfHo3IeKJMd2gmAQFTaoYy3bHhJuC54orKATcpq52uHoxQwwaMpcPWTre3b+XmnQ+097t3Hr6v3eLPC2mej96w/p4DHVO8zRE7/brMWusd52od37s5JX9THMz2EGlz0wbMYjPmZyDMRiTLcYKDYOfgyRfBziB9W/uYdM5hHidAhiRSSmRQIsyC9pfbybkoB2GJWXQs5lXckg1lukMzGQiaUtKU6Y4dy4H1xRWVAyq4VTtdfozVa09gLFJxBEJaaNWWmqfq27veOrSfSQhzf9/Wj6aE0w++7h3sQs0WrfX2c7XO79+ckr/pjPiZ7UjpequLjIWDr+tofqyZwqsLOfw2oTnVTOZpmez9n71Yc62YHCa8+7xkLo6pDyrTHQYV0x2abCBgSnGomO7YcjJGbd7L61csfffwgWqnSwdemldU6AK+g1Emsmvtrr1vzJta6DituOhUs0mIUKBWgzMI+Hu9pR0fHpEm1mTRWv59DtYPy1OSpiBL66pWMEPWGQOy7Ojd0osl00JqcSr9NUektJJ3aR55lxqhaef9TvKvyKdzXSf9O/qxT7eTv3zMfwUjNl0p5aBpmEdvl1I+CDwY/v6W0UtLDNRMd2iygaDJlqpmumNPAfBGcUXllwYbrHa6PsRYSKEDhQDVTS3rX60+UB/UpNsqOnMAMpwbWy1IE4DTorX8/gK968afpBR8WJ4SMdyQaHSt76Jvax/TvzWdwZJmPHUeejf3UvvjWhr/0Uh/TT8N/zxyLYn3gDHZTylMoXtDNzNumIG/0Y/f5R9r+eq9Mgxqpjs0mUCHsNrVCyk22IFHiysqS4Ff1a9YesRd6Wqnq35eUeGtwPeAmSAbXD19vZXVHRvPL8m+vK9nZ9/pztfzGq2a66FPiZStp6ccc/pSvOnb1kf7S+3MqpiFKWXwOVHhVYUUXmWsSu+v6afjlQ6mf+vIRI3WZ1uZeu1UZEga/6YATKAHjqtpx0iIaaH4ZETNdCPgKCm3YJhASJluzPlv4D/FFZWpRw9UO12dGMVyNgGzQOvs7OsveGVzU4OvdWXtXef2+X90U0rh1tNtx3IXPS40/KOBfb/dh9/lZ9cPd9G5rpPmR5rRfBr1d9Sz57/34HzQCUCwK0j9H+pHdN7eD3pJnZWKdZIVc5qZ1Dmp1P2yDoDUGQN+pdFmzKfSyY5IshS3mOEoKc8C/gA05Fzyg2+aVQHzeLAJuKx+xdLmowfmFRWagOUgrhekn5gaDHruvqxzekG+Ke1+i6NjzaT0UFeWrUCYhOppF1sqtl+z/fZ4i0hk1Ew3MmmA8R9J14+5CaIiKpwObCquqBzQ3rva6dKrna6VwC0Cb4bJ0Z29YArp06zS/D/Cnf92d8vU1+sbg18+2NEwucvvlLpUH3tjg5rpDoMy3ch81HZG6tpxV6pSjJoijJSyQUtrnpDefqAwreW1zy0ItNlMRxY+KRDSXqG5p6/rbil6a3+Dds2BjobcTp9TalL9Ex07lOkOg7qRFpmP3phSDynTjS+dQKTuvyelCryXF5uGfC1PNmG7SXdPv6nHTVcXgYcsjoYX0tNFS3ZKgTCLAX3dFKNm5EXoJyjKdCMT5FDquZrpxpvnj85kOIyzU8z0FWebSkZ6skkmbDfqnuk39nro6SH4iMnRuDIjTTZn2wuEWUS9rc8EQ810h0GZbmQ+Mlo10407zw22cflc62RgxsUnWGw2sxi2dc9gZAmsN0jPtBt6PfT3yNAjJofzufR03ZltzxeW0Z1zgqNmusOgTDcyH890NWW68UJK2S2EWBdhuBSgfJq5NBrXShfCcr30Fl3f58XbI7XHzI6mp9PSQg2T7AXCYlIGPDLUTHcYlOlG5iPTlcp044YQ4oX6FUsj3fhaIqB/zmTTgM7Dx0uqSZi/Lr1Tv97vxdcn9SdEatPT6emhA9n2PKymMU92TWLa4y0g0VGmG5mPTVeFF+LJysE2Lp9rTQdKP1VsFg6rGNNWSnYhTNfim3ptvw9/n9SfEanN/0lLD+6bZM/FalJ1OY6kPt4CEh1luhHw1FXpjpLyEGBSM934IKX0CSFeiTA8FxBnzbBEfZY7FClCmL6Eb8qX3D6C/VI+J+yux9PS/XuyU3OxmSb6ysUAMKDeseJIlOkOjR8wyVBQmW58WF2/YqknwtgnAN/cHFNU4rmjwSqE+Dz+ws+7/YT6pVwl7C2POdJ9tdmpOaSYJmIj04bt12xXS1yHQZnu0AQAM1pQJdPHASHEysG2L59rTQFOOaXQpGfZRUJUD7MIIa7AX3CFx4/ulrwoUloeTU331UxKnSxTzIMXxR1/1MdbQDKgTHdo/IBJ8/X3D7unIqpIKTUhxAsRhucAlvNnWWbGUtNIMQnBcgIFy72d6B7JqyKl7eHUdM+O7NRJ0m4ez0W+6+MtIBlQpjs0fsAR6mxUd2Rjz/r6FUsj/d4XA6GT8uIXWhgpJiG4hEDeJd5O8MLrWNsftKf3b8t2TNJTzQMrlCc3B+ItIBlQpjs0XcCkYGdjl9S1kDCZ1e8rRgwRWjADn5yVLfx5aaapg+2TyFxAMPcCX1curi7elNaOB+3p/VsmOTK1VHPCl6IcAfXxFpAMKBMZmv3AfKTs1P3udnNq5qBFV6KFDAVwPfZTZCgIuo5j7hKyz/4y7l3r6Vn/GMGOBgq/+gdSpgxc8RrpWICuNx/Au+8DbPmzyF32YwD6d6xF9/WRedplY/mUjodBV6FhNKm0f2aOJelLbZ4rgjnn+rtycHWxQVo67ren932Q7cjSHJZkNWA10x0BynSHpolwJTbd29s21qaL2UrBF36HyZaK1EK4Hr2Z1NmnYsudSd5nf07Hq3895mOtudPxO2uY+l9/pe2FOwi01WPJnoJ7x2vkX/WbMX06o0VKueXA7csivYFPBvQFBdFZhZYoLBGhnCX+7hxauqmSlq77U9J7NmU7MoJploRvoHkYu+MtIBlQpjs0bYRr6mru7nbr5GljejEhBMJmLHaSegh0DYTAmjt9mCMjHwsCqYWMttyhAMJkpve9Z8k4dTkiQaMlQohItRYEcGauQ7inZoiEvIkWDcpFaFJ5oHsSrd18KM3d96Wkd7+blZYeSLfkxlvbENRvv2a7K94ikoHEfNclDm2EV6WFetvahtk3Kkhdo/mhGwl1NZOxeCkpU0ee+x/pWMfcM2l+8PvYZ56MSEkj0Lyb7CVfHKunEA1WRtheBEy6tMSSbRJiQtSCXiy07MWBnmzaetjWau65NyW9e2OWw+FPt+bFW9tRvBNvAcmCMt2h8QD9gC3U6YyJ6QqTmalf+wu6r5/W524j0FaPLa/4uI7NKr+SrPIrAeh4+S6yz/4KfVtfxbd/M9b8YrLP/MIYPqNjQ0q5/8Dty7ZFGJ4PyMVTzGWx1JQoLBRa1l2BnizaetjZYuq9JyW9c31WmsObbskfrGtwjFGmO0ImxGxhtHjqqiTQADgC7Qc6pdTHvJXqIUz2dOzTF+Dd92HUjg207AXAMqkI94615F1eQbDtAMFOZ1Q0R4NhQgtnpVnpn5ElToixrITjJJOe+cdgb/Gm9ub8Z/c7+z7T2H3A0RtokfFreqhMd4Qo0x2eeiANXdN1v6djLC+keXrQfcY6DD3ox3dgC9ackcWRR3Js99uPkHXWl0EPgQz//xAmZCihqvGtjLA9F5j6mTmWfItJdXo4nBOFnnFHsHdmVYerYNU+p2dZQ9eBtBgasJTSA2yJxbXGAyq8MDwNhH9Purev3WxPH7NYmtbfSXvlHw1DlDqO0rNxzPkEnt0b6VzzTzRvD61P/xpb/iwKrr6VUF8HHa/cRcFVv4547CE8u9/BVliCJcO4GZ4ytZSm+27Aml+MLX/2WD2lY0JK2SaE2BBhuAzg9KLxlbUQbWab9LTfh/rS6OjjQLvw3GtJb389K83Wm2ktEGMUgxBCvL/9mu1qqfwIUS3Yh8FRUn4C8HOgIbP8ynPt0076VLw1jWPuq1+x9BuDDSyfa/2ZWTDl8StTv263CFVO8RhplMJznyWtfXVmmqUn01YoTFG9EXn79mu2V0TxfOMaFV4Yno8yGIIdBxvirGW8s3KwjcvnWjOBkgtmmzOV4Y6OaUI6fqX1z9jQ1TJ1zf5G/9UHOw9md/mbotSaXsVzjwFlusPTB/gAq+/AtgNS16PxIlUchZTSDayJMFwKcOZ0iwotRIEpJpn6S61/xtvdLVPfqG8IfeVAR8PkTr9zNAYspdSBjWMgc9yiTHcYwhkMNUCWDPpCmrvrYLw1jVNerl+xNNIdvU8CnhPjWDt3vJInSPmp7p6+rqel6K39Ddo1Bzoacjt9TqnJEcVohRBV26/ZHpN0yvGCMt2R8QGQBhDqdO6Ls5ZxyRCpYqnAwk9OM9vSbWK8VeVKKCabsN2ku6e/0dNatP5Ag/zGgfbG/A5fo9TkUEX8n4+ZwHFC0puuECIWtW73EV4O7G+u3RuD600opJRBoDLCcAlg+tRM84kxlDThyRZYf6B7pr3e2zptw4EGrq9vbyzs8DZITR7dYj1SYSJFBFTK2MhoAXoAu99Z0yxDAY+w2NQNnejxZv2KpT0Rxk4HAmV5E3MVWiKQJbDeID3Tbuj10N8jQ4+aHE3PpKaZW/JSG7d+bYcqcnOMJP1MF0AIkS6EeF0I8aEQYrsQ4rLw9tuFEN85bL9bhBA/jrR/JMJx3Q+ASQDBbpd6oUWRIUILVuD00lyTNjlV5MdYlmIQ0oWwfEt6p672tBdsPdDwcrz1JCPjwnQxsgs+K6VcDJwH3BlOBH8CuPqw/T4PPDXE/kOxHbACBJp374qy/glLeNVUpLjgbMB60WzLnBhKUoycx+MtIBkZL6YrgN8JIbYBr2FUoyqQUm4G8oUQU4UQJwNdUsqDkfYf5hp7MOK6Ju/+D/ZKXbVljxLv1a9YGqlt9yJAn5+vshYSDU2XO7mlZ2e8dSQj48V0vwzkAadKKRdhxGDt4bGngSsxZrxPjGD/QfHUVbmBncAkGfSHQj1te6L8HCYkQ7TlMQFLpmYIb0G6GL6gsCKmmE3ikXhrSFbGi+lmAa1SyqAQ4jzg8ALXTwBfwDDep0ew/1BsANIBAq37VIghOqyMsH0GkHZpiaXYlAB1CxUfE14QoUILoySpTVcIYcHo2PsocJoQ4n2MWexHhiilrAYyAKeUsjm8OeL+w1CLEWIQ3r2bdktdUyGG40BKWVu/Ymmk3/0CgIXjrC3PeECXVHJLT328dSQryZ4yNg/YK6VsB86ItJOUcsFRPw+5fyQ8dVVdjpLy/cBk3dvbE+xo2GbLKz71WM+jMBimdu6SzBT6pmeKxCiBpvgIs0ncGW8NyUzSznSFENdjfMT5ZYwv/TaQDeCp3VgV42uPNyIl1hcABZeWWKaaTcIcS0GKoQlosppbetbFW0cyk7SmK6W8W0p5kpRydYwv/T4QAqyBlj1tob6O/TG+/rhAStkEbIowPA+Qp05RoYVEw2Li9nhrSHaS1nTjhaeuqh9YSzjFzFe/Wc12R4EQ4vn6FUsjFXNeYjPTN2uSSS39TSCCmmwzCfHE8HsqhkKZ7uhYB5gB4al7Z7fu93TFW1ASEimeOwkovvgEy2SbWaTEWJNiCITgLm7pUTePjxNluqPAU1fVBOwAcpFS+ptq34u3pmRCStkDvBlhuBSgXLXlSSh0Kf0Wk/hHvHWMB5Tpjp5XAAeAu+bNzVILHV19SREBIcSL9SuWRpoxnSnAXZJjmhtTUYohCek8wi09Y9qYdaKgTHf07ALagXTd2+cPth/cGm9BScTKwTYun2tNA046e6bZ4bCKjNhKUkRClzJkM4vfx1vHeEGZ7ijx1FVpwItADoC7dkOVavI5PFJKHxCpOtVcQJw9w6xmuQmEO8B93NKj6khHCWW6x8cmIAhYg237O7S+dvXCHJ7X6lcsdUcY+wTgm5ur4rmJQkCT7owUoTr9RhFluseBp67Kg1GlrMD4+d2346so8RmiwI0NOGVRoUlk20VObFUpItHnl7dxS093vHWMJ5TpHj8fpY/56jcfCHY1qXJ3EZBSasCqCMNzAOv5sywlsdLT0KNz3kNuyv7Wz7y/9/Pnd4/si/n/NvoRv+6l3aMPevwf3/Ez7+/9zP97P198xoMvZISXfrrGx8J/9PPV57wf7fvw1sCA8yc67oB05jhMd8Rbx3hDme5x4qmrasFYpVYI0Lf5pdVS10bUSXUCsrF+xdJInWMXA6GT8mJXO9digjsvtlNzQzrvfj2Nv20KsrPN6ELe0KOzZl+IGVmDFzhz9urc9V6A969LY8d30tF0eGJHkB6fZGOjxrZvp6NJyfYWDW9Q8uDWIN853RarpxYVAho3ckuPei1HGWW60eEpjOJB1lBXU4+/adf6eAtKRIYocGMGPlmcLXx5DlEUKz1TMkwsnmKUdshIEZTlmXD2GrPVH77q438vtDNUTcmQDt4QhHSJJwhTM0yYBAQ0iZQSbxCsZrhjY4Dvf8KG1Zw8FSp7fPKDSbf3Pj38nopjRZluFPDUVbVifGyeAtD34Ysb9IC3O66iEpOVEbYXA6mfmWM5IV6lc+u7dTY3a5RPM7OqNkhRhomTCyPX2inKNHHTGTZm/LGPKXf2k2WHi0+wkJEi+FyZlVP+6WZWtomsFMGmJo3LSq0xfDbHhy6lNJv4Zrx1jFeU6UaP1UAvkC6D/pCn7t1YF+JJaKSU2+tXLI1UHGghIONVO7c/IPnckx7+9Bk7FhPc9raf35w39ArkLq/k+doQ+3+QTtOP0nEH4JFtxvqYm5eksOX6dO78tJ3/fsPPb85N4d4PA3z+KQ+/fSvx47qdXvlk+u96P4y3jvGKMt0o4amr8gIPY7QBwrPr7ZpQX7uqQBZGCPHsYNvDtXPPykkV7inpoji2qiCoGYb75QVWriizsrdTZ3+X5OS7+yn+Ux+NvZLF/3Tj6j/yZtpr+0LMyjaRl2bCahZcUWZhY4N2xD6bm42fT8wx8e+tQZ68ysGOVo26jiP3SyT6/LLNahJfj7eO8Ywy3eiyGagB8gH6t65+WUp98FvfE4+VEbZPBSZdWmKZZjaJmL4epZR8fZWPslwzPzrDmNkuKDDT+pMM6m80HtMyBR9+K43C9COlzcgSvOvU8ASN+O3r+zXKco8MR/z3G8aMOaiDFl43YxLgSdCSMZou5e4O/b+yVvRGyqNWRAFlulHEU1elA49h1GQwB1r2tAVa978fZ1lxR0p5oH7F0i0RhucDcvEUc1kMJQGwoUHj4W1B1u4Psejufhbd3c9LdZEdsalP59JHPQCUT7NwZZmFxf90s+AfbnQJ3zz147jtyl1BTp9qZmqGiWy74IxpZhb8ox8hGDJWHE/qOvXHTv1X/4vx1jHeEWrpavRxlJR/GTgfaDClZtpzLv7O94TF5oi3rjjyp/oVS3842MDyudZbUy1kPHJF6nesZpE8d5vGGW1uvaHKqc1Z9phHFW4aY9RMd2xYhdEwM1X39vq8+95fE29BcWblYBuXz7XmAkWXlFjyleHGj4AmQ7va9auU4cYGZbpjgKeuqg/4D+Hlwf3bX9sS7GjcFl9V8UFK2QFEylsuA8TpU1WthXhS267/4ewH3KoDSoxQpjt2bAAOEM5m6N74xIuarz/SaqxxixBiVf2KpZFu1y8xC/pOmKxq58YLZ6++/Rdr/aqgTQxRpjtGeOqqQsDdgA1wyIAn2Ltp5ZMTsNh5pFVomcCJ588yZ9gtYiLHu+NGj0/2VLfpy1fVBtWNnRiiTHcM8dRVNQP/wqjLYAq27mv37H7nhTjLihlSSg8QKZ49F+DM6RYVWogDvpAMrN4b+srFD7vr461loqFMd+x5H6O1z3QA9843dkygNLJX6lcs9UUY+yTgPTEndgVuFAaaLvXnd4VWXPWUR6WHxQFlumOMp65KAk8D+wnfWOvZ+MQrmqenKa7CYsAQBW7swMJPFJktGSkiO7aqFKv3hh5/dHvwN/HWMVFRphsDPHVVAeBQJ9V0qQW1nqpnnpKhYKRZYNIjpQxhtDMajBLAfG6x+cQYSlIAVY2h9f94P3jdqtpg4q5FHuco040RnrqqNuDvGNkMllBnY7e75s3nxvHilDfrVyztjjB2GhAoyzXFfBXaRKa2Xav7wzuBy1bVBr3D760YK5TpxhBPXdV2jIUC0wA8u9/ZHWjePS5r7w7RlscCfOLEHFMox2EqiK2qiUtTn976wJbg0v9UBzvjrWWio0w39rwA7MQo9ELPu0+uHW8tfqQxfX8+wvBsIOXTJ1jmxFDShKbNrXc/tj34+RXr/XXx1qJQphtzwvm7/wJ8QBZSyq51Dz4T6mndE2dp0eT9+hVLGyOMLQK0+fkqayEWuPr1zjvfCXztptW+dfHWojBQphsHPHVV3cCfgQwgHS2kd6178D+h/s4D8VUWHYYILZiAMwvThacgXcyIraqJh7NXb791nf/HO9v0SJ86FHFAmW6c8NRV7QX+AOQADhn0hbrXPfS45ulpjrO0aDBoqhhGrnLmpSWWYlO8+vJMEA506y2/Wee/saFXPqRWnCUWynTjiKeuaifGjDcfsOu+Pn/3W/9+WPP2tcRZ2qiRUu6uX7G0JsLwAkAuKlQFbsaSvZ1686/X+b/b3C8fU4abeCjTjTOeuqotwD8xbqzZNHeXt3vdgw9p3l5XfJWNjiFCCwJYkmGjb1qmmB1bVROH2nat8ZY3fde3e+QzynATE2W6CYCnruod4AGMVDKb5u7ydr35wENJumotUmghHyi8tMQyxWISllgKmihUt2oHfr3O/189fl5Qhpu4KNNNEDx1VW8A92MYb4ru6fF1vXn/vzV3d6QsgIRDSukCItVlPQmQp6rauVFHSsnqvaGtv1jr/+pj24NrlOEmNsp0EwhPXdWbwD0YoQa77u3zd715/8Ohvo6k6CoshFhZv2JppDf8WRYTvbOyTWrpbxTxh6T/b5sCr//1vcD1K3cF34q3HsXwKNNNMDx1VW/zcYzXrvv6A51r/vGw31X3bpyljYSVg21cPteaDcy6+ATL5BSLsMdU0Tim3aN3/mKt/5nVe7UfrKoNJsPrQ4Ey3YTEU1e1EaNOQwGQidRlz4bHX3XvevtZqWuhOMsbFCllL7A2wnApID45TYUWokV1q1Z/4yu+e3Z36D9cVRusjrcexchRppugeOqq3gVWAFbCJSHd1W9s73n36Xv1gLc7ntoGQwhRWb9iaaT+5WcK6C+ZrFahHS+6lPKF2uAHP3vd/7teP7esqg22xluT4thQppvAeOqqaoFbgGZgJmAKNNe2dL5+z79Cve374ipuICsH27h8rtUBzDtrhjk1zSYyYitpfOEOSPef3w2suefD4E+Be1fVjt/SoOMZZboJjqeuqgO4HVgHFAMpuqfb2/na3Y/4m2o3xFVcGCmlH3g5wvBcQJw906yaTx4Hm5u1mhte8j36Rr32/VW1wddVhkLyokw3CfDUVfmBhzBSygqBLKQue975z2v9O998SuqhSB/rY8Xr9SuW9kUYOx3wl+aqeO5o6PXLrjs3+l/91Zv+Jzq98ueraoO18dakOD5UknqSEG7786ajpLwR+D6G+bo8NW/tDHU1tWeedvnVphTH5HhoG6Itjw04dWGBScu2i9wYy0pqdCnlOw3a1ruqAtu8IZ4EVq+qDcb7n6siCqiZbpLhqavagxHnbeBQnNe1p7Vj9d/v9jfv3iilrsdSj5RSB1ZFGD4BsJ4/y1ISQ0lJT7tHb711nf+l2zcEnvaG+Nmq2mClMtzxgxjH7WLGNY6SchvwBeBCwAV4AGyFc/IzTv7MUnP65JiUTpRSbjhw+7KzBhtbPtf6JeDce5fbL81PMxXFQk8yE9Jl6PV92uZ/fhDYGtJ5FHhb9TIbf6jwQpLiqasKOErKHwZ2AV/FKBHZFHDtae1w/fWB9AUXLUqdfepFwmJzjKWOIUILZuCMGVnCl+cQynCHQJdS39aib//n+4Hdzj65EXhkVW2wPd66FGODMt0kJhznfc9RUr4TuBxj1tsHdPRvX7PFs3dTbeZpl11ozZ2xeAzL166MsH0m4PjMHEuBKp07OFJK9nTqNf/6IFhd26G3Ytws3aQyE8Y3KrwwjnCUlM8GrsEwPBdGSyDsMxZOT5t/wVJzakZUG0FKKXccuH3ZgsHGls+1Xg4s+9ul9nOnZ5lOiOZ1kx0pJfu65K6HtwVqPmzWu4BXgFdX1QZ7461NMfaome44wlNXtc9RUn4rcDZGvFcAzb6D2xp8jdX/yjjl0nL79AXnCrPFFo3rDRFaEMBZk1NF/9QMMSsa1xoPSCnZ26XXPLQlWL21Re8H3gZWqVDCxEKZ7jgj3PjyDUdJ+Rbg88CZQBe61t33wQvveOqqtqfPP/8MW/6sU4XZmnKcl1sZYfsUYPKlJZYss0lM+AwZX0h6trfoW5/eGTxY0657gfeAF1bVBpOmbKcieqjwwjjGUVIuMIrNXItRRLyFcMjBZM9ISZt33uKUotJPmqz2zGM9t5Ty4IHbl80cbGz5XOvFwBf+8OmU8jmTzSeN+gkkMVJKnH1y/1sHQpufrQl1BTTMwDtA5araoDPe+hTxQ810xzHhG201jpLy/wHOB5ZhFM/p0H19/X0frHqnb8tLVWml58y3z1x4pjk1c8Qx30htecIssVvom5FlmnNcTyAJ8QRl/7YWbcvTO0N1uzt0AA0jjPDaqtpgMnYCUUQZZboTgPAy4pcdJeVvAKcBl2HcbOtDC3W6q9duc1ev3ZZ6wumzU2efvsSSmTuSHmaR4rk5wIzPzLHYbGYRldhxohPQZKChR+5dfzBU/XxtqDukYwEaMW6QbVlVG/Qcy/mEEBqwHeP9WQNcI6Uc9BxCiGLgTCnlY+GfrwVOk1J+d9RPSDGmKNOdQHjqqnzAekdJ+TvAfGA5MBsj5NDq3btpn3fvpn22KXML0uYuOdMyeep8IUwDYrJSyk4hxNsRLlMGSGev3rPFpW2aM9l0YrpNZI3Vc4oXnV7ZuqdT3/N+k1a3dn+oL6CRDviBt4ANwMHjSP3ySikXAQghHgWuB/4QYd9i4EvAY6O8liLGqJjuBCYc8z0BuARYDIQw4r4hAHNmfrrjhNPn2fJnzzOlZU8/LN/2ofoVS68d7JzL51pvBqYDHYe2nT7VlH/WDMuJcyabZuWnianJ2D0ioMlAY6/cV92q7Vm7P7Rvb5c0A4cWntRjzGq3r6oNeo/3WkKIfillevj764GFGL/Pdinln8Pbb8P4W30J4x/dfow83y6Mf6YOjL/tc1LKm8PHfBH4OUZWS6WU8qeHrgf8GSP85AUuk1K2HO/zUAyOMl0FAI6S8inABcC5GDU5OoH+Q+OWrMIM+8yFS+wzT84w2VJ/Vr9i6aD1FsJLf88PnyMUPs9HdV8FMC/fNHlRoblozmRTUVGGKMpxiMJE6hAc0mWoyytbW9zS1dCjt+zu0F1vH9Q6AxrZGE9BB3YAm4A6oD2aCxoOma4QwgI8g2HoLwPPSikXCyFM4et+AlgA3CSlXBY+9lrgf4BTMGbetcBZGLHld4FTMYx5NXCXlHKlEEICy6WULwgh/hfolVL+NlrPR3EkynQVR+AoKc8GzgA+hZHxIDGM0w3MAH7uqatyDXWO5XOtKRhhi4Xhcx3KjtAxVsz1hb8HwGrCdNpUc/78fFPRjCxTYZZdZGbYyEyziUy7RYzZMmZdSt0TpL/DI1ua+/WW+m7p2tmmtexo1TtCOnYgHUgN796O0el4B7B/VW0wMFa6DovpgnET7sdSyoAQYg1wM8bN0G9IKa8UQpzLQNNdIqW8Lvzzy8BtGMvEPyel/Gp4+9eBeVLKHwkh/IBdSimFEFcDF0kpvzFWz2+ikzCzC0Vi4Kmr6sa46fYKRnPMU4BzMGKHzRgfaYdkVW3Qj3EDqGb5XOuTQF74XLMxPgoXY8yEBRAM6vS906i1vNOoDTBzhxVLcbYpoyhDZBakmzJzHSIz2y4yrCYsQmAyCYTA+GoSmIQQxlcQmpRafwB3f0C6e3zS3e2T7g6vdLd7pKe5T7pb3dIrwQykhR82DJOdjvGPZgewlTGYzQ7DRzHdo7gXI/2vEKO2ciT8h32vYbzPh1qLHZQfz74O7a8YI9QvVzEo4XQzJ+B0lJRXAtOAYHj7iAkbVWv4sQVg+VyrBWO2VgSUYBjxdIxZtcQwCBOgeYL4d7bp/p1tuEA7GB4fKRaMHnO2w75aMOKdh2awGkaZzE0YcdEWwBWN2OwY8BzwG4zn8qXwtj5gJG2QqoA/CyFyMcILXwT+MhYiFUOjTFcxLGGjbYjW+VbVBkOEDR1jdRbL51qtGOaRedgjF8Occw/7HgxTPmS+MsLPJoxYcg+GkXaFH50YRuXG+EfQkSzlE8MhhjeAbinlIc3bgJAQYivwIMZzHOzYZiHEz4A3MH4/L0kpn4+BbMVRqJiuImlYPtdq4uOPyqYhvmqAZ7wV/g7fQPsQuEpKWRdvPYrRoUxXoUgChBAnAS9ipID9ON56FKNHma5CoVDEkAlfAUqhUChiiTJdhUKhiCHKdBUKhSKGKNNVKBSKGKJMV6FQKGKIMl2FQqGIIcp0FQqFIoYo01UoFIoYokxXoVAoYogyXYVCoYghynQVCoUihijTVSgUihiiTFehUChiiDJdhUKhiCHKdBUKhSKG/H+sIzJ2RHW0dgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "# Data to plot\n",
    "languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'\n",
    "popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]\n",
    "colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n",
    "# explode 1st slice\n",
    "explode = (0.1, 0, 0, 0,0,0)  \n",
    "# Plot\n",
    "plt.pie(popuratity, explode=explode, labels=languages, colors=colors,\n",
    "autopct='%1.1f%%', shadow=True, startangle=140)\n",
    "\n",
    "plt.axis('equal')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c493f9eb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
