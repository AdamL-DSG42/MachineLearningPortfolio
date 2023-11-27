# Adam Lambert's Machine Learning Portfolio

I am a fourth year software development student in SETU Carlow. 
This is a repository of projects that I have worked on or am currently working that demonstrate my machine learning experience.

### Table of Contents

- [Projects](#projects)
- [Technologies Used](#technologies)

## Projects

### Crime rates and their impact on property prices
This project aims to assess whether there is an affect on property prices in areas of high crime in Ireland. It will initially provide a high level overview of the overall project goal, with later iterations providing more detailed information.

#### Datasets:
As the datasets are too large to upload to GitHub, they can be found at these links
- [Property Price Register Ireland from Kaggle](https://www.kaggle.com/datasets/erinkhoo/property-price-register-ireland)
- [Recorded Crime in Ireland from the CSO - Search CJQ06 for dataset](https://data.cso.ie/)

Both datasets were contained within csv files. The Property Price register dataset was originally sourced from [this website](https://propertypriceregister.ie/) which is produced by the Property Services Regulatory Authority in accordance with the Property Services Act 2011. It contains the sale price of recorded properties in Ireland between 2010 and 2021, with relevant information such as the date and location of sale. The Kaggle Dataset was created to allow easier access to this data. The Recorded Crime in Ireland dataset was obtained from the Central Statistics Office (CSO) website. It contains the amount of times that each type of offence occured per quarter from 2003 to 2023 as well as the Garda division that reported it. The data is currently under reservation as the quality of the data provided by An Garda Síochana can not be guaranteed by the CSO as of present, however as this is the only data published by an official government body on the topic it must be used.

#### Data Preprocessing
The data preprocessing on these datasets was completed in the "Data-Preprocessing" Jupyter notebook provided above. 
The Property Price Register dataset was read using the Pandas Python library. After analysis of the structure of the data, all columns containing a majority null value (POSTAL_CODE and PROPERTY_SIZE_DESC) were removed as the columns where these were present were not pertinent to the data required for analysis. The ADDRESS, IF_MARKET_PRICE, IF_VAT_EXCLUDED and PROPERTY_DESC were removed to due irrelevance, leaving the SALE_DATE, COUNTY and SALE_PRICE columns. The sale price was limited to properties under €10,000,000 to remove outliers caused by the purchase of large complexes.
The Recorded Crime in Ireland dataset was also read in using Pandas. After analysis of this dataset's structure, a list of all unique offence types recorded was created. After analysis of this list, all rows containing offences that were deemed highly unlikely to affect property prices, such as "Robbery of Cash or Goods in Transit", were removed from the dataset. To better align with the property price register dataset, the dataset was trimmed to remove the data before 2010 and after 2021. The Garda Divisions column was replaced with the County column, with the county name being stripped from the Division and seperated to it's own column.

---

### Decision Trees and Random Forests
The second project in this portfolio is an analysis of the Decision Tree and Random Forest Jupyter notebook created by Jake Vanderplas as part of a data science handbook, which can be found [here](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.08-Random-Forests.ipynb).

Various changes were made to the code in this data science handbook in an attempt to see what effects they would have on the predictions made. 

---

## Technologies

- These projects were both created using [Python](https://www.python.org/), as it is one of the top programming languages for data science and machine learning.

- Both projects were completed in a [Jupyter Notebook](https://jupyter.org/), created by Project Jupyter. They can be used to create informative and easy to follow notebooks of projects.

- The Python libraries [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/) and [numpy](https://numpy.org/) were used extensively to carry out the requirements of these projects.

