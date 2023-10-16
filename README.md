# Simple Spark ETL on AKS
## Prerequisites
Installed latest:   
- Azure CLI, 
- terraform, 
- docker, 
- spark installed to /opt/spark/
- setuptools

Login to Azure:
```
az login
```
## Data
Create Azure storage account and put your data to the blob container
so we can acess it from pyspark console. Just start pyspark this way:
```
pyspark \
  --conf spark.hadoop.fs.azure.account.key.<acc>.blob.core.windows.net=<key> \
  --packages org.apache.hadoop:hadoop-azure:3.2.0,com.microsoft.azure:azure-storage:8.6.3
```
where:   
**acc** - storage account name,   
**key** - storage account key.

afer this spark command like "df = spark.read...." will work

## local run
spark-submit \
  --conf spark.hadoop.fs.azure.account.key.<acc>.dfs.core.windows.net=<key> \
  --packages org.apache.hadoop:hadoop-azure:3.2.0,com.microsoft.azure:azure-storage:8.6.3 \
  src/main.py


## Build
```
python3 setup.py build bdist_egg
```

## Docker  

Create Azure container registry and login to it:
```
az group create --name RG-4ContainerRegistry --location eastus
az acr create --resource-group RG-4ContainerRegistry \
  --name dycr1 --sku Basic
az acr login --name dycr1

```
build docker image (option -p is for generating pyspark image):
```
docker-image-tool.sh -r dycr1.azurecr.io -t spart2aks -p ./docker/Dockerfile build
```


Puch docker image to Azure container
```
docker-image-tool.sh -r dycr1.azurecr.io -t v1 push
```



