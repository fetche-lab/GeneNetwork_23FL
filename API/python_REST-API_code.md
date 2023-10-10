# GeneNetwork_23FL
## PYTHON CODES FOR FETCHING REST API ENDPOINTS FROM GENENETWORK WEB SERVICE 
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

### Fetch genotypes for groups/RISet
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

## OR

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
