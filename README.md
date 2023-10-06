# Simplease Spark ETL on AKS
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

## Usefull tips
we will have access to Azure blob from pyspark console if we start pyspark this way:
```
pyspark \
  --conf spark.hadoop.fs.azure.account.key.<acc>.blob.core.windows.net=<key> \
  --packages org.apache.hadoop:hadoop-azure:3.2.0,com.microsoft.azure:azure-storage:8.6.3
```
where:   
**acc** - storage account name,   
**key** - storage account key.


## Terraform   
We can create Azure resourses by Terraform, but container for terraform status management file should be created in advance:
```
az group create --name tf-state-rg \
  --location westeurope

az storage account create --name sa4tdyfstate \
  --location westeurope \
  --resource-group tf-state-rg

az storage account keys list --account-name sa4tdyfstate
```
Use key from abow, create a container so Terraform can store the state management file:
```
az storage container create --account-name sa4tdyfstate \
  --name tfstate \
  --public-access off \
  --account-key <account-key>
```

go to the terraform directory and perform terraform actions:
```
terraform init
terraform plan -out terraform.plan
terraform apply terraform.plan
....
terraform destroy
```

## Build
python3 setup.py build bdist_egg

## Docker  
Create Azure container registry an login to it:
```
az group create --name RG-4ContainerRegistry --location eastus
az acr create --resource-group RG-4ContainerRegistry \
  --name dycr1 --sku Basic
az acr login --name dycr1

```

build docker image (option -p is for generating pyspark image):
```
source /opt/spark/bin/docker-image-tool.sh \
  -r dycr1.azurecr.io \
  -t sparktest1 -p docker/Dockerfile build
```



docker build -t sparktest . -f docker/Dockerfile

