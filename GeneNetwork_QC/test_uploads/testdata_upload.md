## Data Curation, Upload, and Testing the GN system 
### The following represents a series of datasets and scripts used to process them before uploading to the GeneNetwork database

### The datasets involved included:
* Test datasets shared by Fred. Below are the links to the datasets:
  * Average file: https://gitlab.com/fredmanglis/gnqc_py/-/blob/main/tests/test_data/average.tsv?ref_type=heads
  * Standard error file: https://gitlab.com/fredmanglis/gnqc_py/-/blob/main/tests/test_data/standarderror_1_error_at_end.tsv?ref_type=heads
* Datasets from Public Database repositories (NCBI and AraQTL):
  * Arabidopsis Dataset from NCBI: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247158
  * Arabidopsis Dataset shared by Harm, from AraQTL: https://gsajournals.figshare.com/articles/dataset/Supplemental_Material_for_Hartanto_et_al_2020/12844358
  * Mice experiment dataset from NCBI: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE241528

### The following are the Python scripts that were used to perform data curation on each of the datasets mentioned above. This is prior to successfully uploading them to the GeneNetwork database 
#### Test datasets 
01 Fred average dataset {`avg_Fred_valid.tsv`}
```python
## import python modules for data wrangling 
import pandas as pd 
import numpy as np

## open the file to dataframe 
df_avg = pd.read_csv('../test_data/average.tsv', sep='\t')
print(df_avg.shape) # provides the number of (rows, columns)
print(df_avg.info()) # general information on the type of data values 
print(df_avg.head(10)) # display the first 10 rows of the dataframe

## data curation begins., 
## change column name 'D6' to 'BXD52'; D6 was flagged as invalid in the QC uploader 
df_avg = df_avg.rename(columns={'D6':'BXD52'})
df_avg.columns

## Remove the first row of the dataframe, as it containcs a series of invalid values 
df_avg.drop(0, axis = 0, inplace = True)
df_avg.shape

## change the object to float type 
## convert data type in BXD39 from object to float 
df_avg['BXD39'] = df_avg['BXD39'].astype(float)
df_avg.info()

## Experiment on some mathematical transformation and see what you get 
cols1 = ['BXD95', 'BXD27', 'BXD98', 'BXD99', 'BXD39', 'BXD33',
       'BXD45', 'BXD51', 'BXD56', 'BXD76', 'BXD52', 'BXD12', 'BXD83', 'DBA/2J',
       'BXD87', 'BXD81', 'BXD86', 'BXD84', 'BXD85', 'BXD40', 'BXD8', 'BXD79',
       'BXD77', 'BXD70', 'BXD71', 'BXD73', 'BXD68', 'BXD67', 'BXD66', 'BXD63',
       'BXD64', 'BXD65', 'BXD48', 'BXD50', 'BXD55', 'BXD6', 'BXD100', 'BXD11',
       'BXD24', 'BXD18', 'BXD21', 'BXD20', 'BXD14', 'BXD16', 'BXD44', 'BXD38',
       'BXD42', 'BXD43', 'BXD28', 'BXD25', 'BXD2', 'BXD23', 'BXD29', 'BXD22',
       'C57BL/6J', 'D2B6F1', 'BXD19', 'BXD92', 'BXD97', 'BXD1', 'BXD101',
       'BXD90', 'BXD62', 'BXD9', 'BXD89', 'BXD96', 'BXD69'] ## to be computed

col2 = ['ProbeSetID'] # id column not to be computed 

## start the computation 
## multiply using the multiply() function, then round off to three 
df_avg_computed = df_avg[cols1].multiply(0.01).round(3).add(0.0001).multiply(10).round(3)
df_avg_computed.head(10)

## return the first column containing information about the ids 
df_avg_computed = pd.concat([df_avg[col2], df_avg_computed], axis = 1)
df_avg_computed.head()
## Write the dataframe to a tsv file format
df_avg_computed.to_csv('../test_data/avg_Fred_valid.tsv', index = None, header = True, sep = '\t')
```
#### Public datasets 
01 Arabidopsis dataset from NCBI (GSE247158) 
```python
## import python modules for data wrangling 
import pandas as pd 
import numpy as np

## Write the file into a dataframe 
Arabid_df = pd.read_csv('../test_data/GSE247158_gene_count.tsv', sep='\t')

## Explore the dataset 
Arabid_df.head(10)
Arabid_df.shape
Arabid_df.columns

## data curation begins., 
# Remove rows containing '-inf' values
Arabid_df_curated = Arabid_df[~Arabid_df.isin([np.inf, -np.inf]).any(axis=1)]

# Remove rows containing '-'
Arabid_df_curated1 = Arabid_df_curated[Arabid_df_curated['gene_name'] != '-']

## Create a list of column names, and save them in a file 
arabid_col = []
for col in Arabid_df_curated1.columns: 
    arabid_col.append(col)
print(arabid_col) 

## Since the strain names (column names) were not identified, the following Python script was used to create
## a text file with column names to be added to the GN database 
## open a file, write the list of values to the file, then save and close it
with open('../test_data/Arabid_GSE247158_colnames.txt', 'w') as file:
    ## write the elements of the list into the file 
    for items in arabid_col:
        file.write('%s\n' %items)
    print('file written successfully')

## save and close the file 
file.close()

# write the dataframe to a tsv file format 
Arabid_df_curated1.to_csv('../test_data/Arabid_GSE247158_curated.tsv', index = None, header = True, sep = '\t')
```
Ideally, the above script should work. However, the only challenge left is for the column names to be added to the GeneNetwork database
which is the same case with the following public datasets whose scripts are displayed below:

02 Arabidopsis Harm's dataset 
```python
## import python modules for data wrangling 
import pandas as pd 
import numpy as np

## Write the file into a dataframe
Harm_df = pd.read_csv('../test_data/table-s9.csv', index_col= 0)
print(Harm_df.head())
print(Harm_df.shape)

# data curation begins., 
## Reset the index to create a column, and rename the 'index' to 'AraSeqID'
Harm_df1 = Harm_df.reset_index().rename(columns = {'index':'AraSeqID'})

## Create a list of column names and send them to Fred 
Harm_colnames = []
for col in Harm_df1.columns:
    Harm_colnames.append(col)
print(Harm_colnames)

## Write the list of values in a file 
with open('../test_data/Harm_colnames.txt', 'w') as file:
    ## write elements of a list 
    for items in Harm_colnames:
        file.write('%s\n' %items)
    print('file written successfully')

## close the file 
file.close()

## write the dataframe into a tsv file format 
Harm_df1.to_csv('../test_data/Harm_Arabid_data.tsv', index = None, sep = '\t')
```
Harm's data did not require a lot of processing. The only challenge is to upload the strain names 

03 Mice experiment dataset (GSE241528)
```python
## import python modules for data wrangling 
import pandas as pd 
import numpy as np

## Try the new dataset on mice. cerebral experiment 
mus_df = pd.read_table('../test_data/GSE241528_Gene_expression-CX_cpm.txt.gz')
mus_df.shape
mus_df.columns

## data curation begins
## update the colnames with known mouse strain names (ideally the plan with this code block was to replace colnames with the ones already in the database). But the plan failed
#new_mus_names = ['geneID',
'BXS1',
'BXS2',
'BXS3',
'BXS4',
'BXS5',
'BXS6',
'BXS7',
'BXS8',
'BXS9',
'BXS10',
'BXS11']
#print(new_mus_names)

mus_df.columns = new_mus_names
mus_df.columns
mus_df_colnames = ['Gene', 'naive.CX_naive.CX', 'PT1M.CX.L_PT1M.CX.L',
       'PT1M.CX.R_PT1M.CX.R', 'PT1M.LEV.CX.L_PT1M.LEV.CX.L',
       'PT1M.LEV.CX.R_PT1M.LEV.CX.R', 'PT2M.LEVW2W.CX.L_PT2M.LEVW2W.CX.L',
       'PT2M.LEVW2W.CX.R_PT2M.LEVW2W.CX.R', 'PT7d.CX.L_PT7d.CX.L',
       'PT7d.CX.R_PT7d.CX.R', 'PT7d.LEV.CX.L_PT7d.LEV.CX.L',
       'PT7d.LEV.CX.R_PT7d.LEV.CX.R']

## save them in a txt file, then send Fred 
with open('../test_data/GSE241528_CX_GExp_mice_strain_names.txt', 'w') as file1:
    for col in mus_df_colnames:
        file1.write('%s\n' %col)
    print('file written successfully')

# close file 
file1.close()

# write the dataframe to a tsv file format 
mus_df.to_csv('../test_data/GSE241528_CX_GExp_mice.tsv', index = None, header = True, sep = '\t')
```
This dataset did not have any invalid float values. The only challenge was with the strain names 
