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

# average file (from Fred) 
# import the file as a dataframe and examine it 
avg_df = pd.read_csv('../test_data/average.tsv', sep = '\t')

avg_df.head()

```
