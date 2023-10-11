# GeneNetwork_23FL
## PYTHON CODES FOR FETCHING REST API ENDPOINTS FROM GENENETWORK WEB SERVICE 
### The Python library used is called `requests`. In this work, the GET method was used to retrieve information from the GeneNetwork Web Service  
#### Used 'python -m pip install requests' to install the requests library which contains the rest API request methods 
```python 
python -m pip install requests
```
#### Imported the library on my jupyter notebook working environment
```python
import requests
```


## Fetching Dataset/Trait Info/Data 
### Fetch Species list 
```python

## To get a list of species with data available in GN (and their associated names and ids):

api_url = "https://genenetwork.org/api/v_pre1/species"
response = requests.get(api_url) # the get request method accesses the resources in the webservice 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `{'FullName': 'Mus musculus', 'Id': 1, 'Name': 'mouse', 'TaxonomyId': 10090},...., {'FullName': 'Bat (Glossophaga soricina)', 'Id': 12, 'Name': 'bat', 'TaxonomyId': 27638}]`
##### Content-type: `application/json`
##### The Python code worked as expected
   
```python
## Get a species info (in this case, a mouse), 

api_url = "https://genenetwork.org/api/v_pre1/species/mouse"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

## OR

api_url = "https://genenetwork.org/api/v_pre1/species/mouse.json"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `{'FullName': 'Mus musculus', 'Id': 1, 'Name': 'mouse', 'TaxonomyId': 10090}`
##### Content type: `application/json`
##### The python code worked as expected 

### Groups 
```python
## Fetch the groups in the dataset (for all the species)
api_url = "https://genenetwork.org/api/v_pre1/groups"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

## OR (only for the mice)

api_url = "https://genenetwork.org/api/v_pre1/groups/mouse"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `[{'DisplayName': 'BXD', 'FullName': 'BXD Family', 'GeneticType': 'riset', 'Id': 1, 'MappingMethodId': '1', 'Name': 'BXD',...},...,{...,'SpeciesId': 1, 'public': 2}]`
##### Content type: `application/json`
##### The Python code worked as expected 

### Fetch Genotypes for Groups/RISet

```python
''' 
Returns a group's genotypes in one of several formats - bimbam, rqtl2, or geno (a format used by 
qtlreaper which is just a CSV file consisting of marker positions and genotypes
curl https://genenetwork.org/api/v_pre1/genotypes/bimbam/BXD
curl https://genenetwork.org/api/v_pre1/genotypes/BXD.bimbam
'''

## BXD
api_url = "https://genenetwork.org/api/v_pre1/genotypes/bimbam/BXD"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

## BXD.bimbam
api_url = "https://genenetwork.org/api/v_pre1/genotypes/BXD.bimbam"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Response content is not valid `JSON`
##### Content type: `text/csv`
##### Python code failed to work. File format, not JSON

```python
'''
Rqtl2 genotype queries can also include the dataset name and will return a zip of the genotypes, phenotypes, 
and gene map (marker names/positions). For example: 
'''

## Fetch genotypes for groups/RIsets (zipped files)
api_url = "https://genenetwork.org/api/v_pre1/genotypes/rqtl2/BXD/HC_M2_0606_P.zip"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Response content is not valid `JSON`
##### Content type: `application/zip`
##### Python code failed to work. File format, not JSON

### Fetch Datasets 
```python
api_url = "https://genenetwork.org/api/v_pre1/datasets/bxd"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `[{'AvgID': 1, 'CreateTime': 'Fri, 01 Aug 2003 00:00:00 GMT', .....},...,{..., 'Short_Abbreviation': 'UTHSC_BXDYgEyeRNAseq_DESeq2-rlog2_0422', 'confidentiality': 0, 'public': 1}]`
##### Content type: `application/json`
##### The Python code worked as expected

```python
api_url = "https://genenetwork.org/api/v_pre1/datasets/mouse/bxd"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Response content is not valid `JSON`
##### Content type: `text/html; charset=utf-8`
##### Python code failed to work. File format, not JSON

### Fetch Individual Dataset Info 
#### For mRNA Assay/"Probeset"

```python
api_url = "https://genenetwork.org/api/v_pre1/dataset/HC_M2_0606_P"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

## OR

api_url = "https://genenetwork.org/api/v_pre1/dataset/bxd/HC_M2_0606_P"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Content: `{'confidential': 0, 'data_scale': 'log2', 'dataset_type': 'mRNA expression',..., 'tissue': 'Hippocampus mRNA', 'tissue_id': 9}`
##### Content type: `application/json`
##### The Python code worked as expected

#### For "Phenotypes" (basically non-mRNA Expression; stuff like weight, sex, etc)

```python
''' 
For these traits, the query fetches publication info and takes the group and phenotype 'ID' as input. For example:
'''
api_url = "https://genenetwork.org/api/v_pre1/dataset/bxd/10001"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `{'dataset_type': 'phenotype', 'description': 'Central nervous system, morphology: Cerebellum weight, whole, bilateral in adults of both sexes [mg]',..., 'year': '2001'}`
##### Content type: `application/json`
##### The Python code worked as expected

### Fetch Sample Data for Dataset 

```python
''' 
Returns a CSV file with sample/strain names as the columns and trait IDs as rows
'''
api_url = "https://genenetwork.org/api/v_pre1/sample_data/HSNIH-PalmerPublish.csv"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Response content is not valid `JSON`
##### Content type: `text/csv`
##### Python code failed to work. File format, not JSON

### Phenotype matrix 
```python
api_url = "https://genenetwork.org/api/v_pre1/sample_data/BXDPublish.csv > BXDPublish.csv"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Content: `{'errors': [{'detail': '','source': {'pointer': '/api/v_pre1/sample_data/<path:dataset_name>.<path:file_format>'}, 'status': 415, 'title': 'Unsupported file format'}]}`
##### Content type: `application/json`
##### The Python code worked as expected, although the content values seemed to flag an error message 

```python
api_url = "https://genenetwork.org/api/v_pre1/datasets/mouse/bxd > bxd_datasets.json"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Response content is not valid `JSON`
##### Content type: `text/html; charset=utf-8`
##### Python code failed to work. File format, not JSON

### Fetch Sample Data for Single Trait

```python
api_url = "https://genenetwork.org/api/v_pre1/sample_data/HC_M2_0606_P/1436869_at"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `[{'data_id': 23415463, 'sample_name': '129S1/SvImJ', 'sample_name_2': '129S1/SvImJ', 'se': 0.123, 'value': 8.201},...,{..., 'sample_name_2': 'WSB/EiJ', 'se': 0.993, 'value': 10.472}]`
##### Content type: `application/json`
##### The Python code worked as expected

### Fetch Trait List for Dataset

```python
api_url = "https://genenetwork.org/api/v_pre1/traits/HXBBXHPublish.json"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Content: `[{'Additive': 0.0499967532467532,...},..., {..., 'LRS': 2.51271460779984, 'Locus': 'rs64731945', 'Mb': 163.277656, 'Year': '2022'}]`
##### Content type: `application/json`
##### The Python code worked as expected

### Fetch Trait Info (Name, Description, Location, etc)
#### For mRNA Expression/"ProbeSet"

```python
api_url = "https://genenetwork.org/api/v_pre1/trait/HC_M2_0606_P/1436869_at"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `{'additive': -0.214087568058076, 'alias': 'HHG1; HLP3; HPE3; SMMCI; Dsh; Hhg1', ..., 'name': '1436869_at', 'p_value': 0.306, 'se': None, 'symbol': 'Shh'}`
##### Content type: `application/json`
##### The Python code worked as expected

#### For "Phenotypes"
```python
'''
For phenotypes this just gets the max LRS, its location, and additive effect (as calculated by qtlreaper)
Since each group/riset only has one phenotype "dataset", this query takes either the group/riset name or the group/riset name + "Publish" 
(for example "BXDPublish", which is the dataset name in the DB) as input
'''

api_url = "https://genenetwork.org/api/v_pre1/trait/BXD/10001"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `{'additive': 2.39444435069444, 'id': 4, 'locus': 'rs48756159', 'lrs': 13.4974911471087}`
##### Content type: `application/json`
##### The Python code worked as expected

## Analyses 
### Mapping 
#### GEMMA 
```python
api_url = "https://genenetwork.org/api/v_pre1/mapping?trait_id=10015&db=BXDPublish&method=gemma&use_loco=true"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `[..., {'Mb': 166.686631, 'additive': 0.2294681, 'chr': 'X',...}, ... {..., 'lod_score': 0.22501147868503496, 'name': 'rsm10000014695', 'p_value': 0.5956464}, ...]`
##### Content type: `application/json`
##### The Python code worked as expected. However, the output was very large, so only snapshots of the results are presented here. 

#### R/qtl

```python
api_url = "https://genenetwork.org/api/v_pre1/mapping?trait_id=1418701_at&db=HC_M2_0606_P&method=rqtl&num_perm=100"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)
```
##### Content: `[{'Mb': 3.010274, 'cM': 3.010274, 'chr': 1, 'lod_score': 0.246232487190071,...},...,{..., 'lod_score': 0.0821116048891781, 'name': 'rs31639754'}]`
##### Content type: `application/json`
##### The Python code worked as expected

### Calculate Correlation 
```python
api_url = "https://genenetwork.org/api/v_pre1/correlation?trait_id=1427571_at&db=HC_M2_0606_P&target_db=BXDPublish&type=sample&return_count=100"
response = requests.get(api_url) 

if response.status_code == 200:
    try:
        data = response.json()
        print(f'Content: {data}')
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
    except ValueError:
        print("Response content is not valid JSON")
        print()
        print(f'Content type: {response.headers["Content-Type"]}')
else:
    print("Request failed with status code:", response.status_code)

```
##### Content: `[{'#_strains': 6, 'p_value': 0.004804664723032055, 'sample_r': -0.942857142857143, 'trait': 20511},...,{...,'sample_r': 0.642857142857143, 'trait': 10152}]`
##### Content type: `application/json`
##### The Python code worked as expected

