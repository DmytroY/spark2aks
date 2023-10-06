import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

acc = "dystorageacc"
# key=""
# container="container1"
    
try:
    # get DefaultAzureCredential
    default_credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    account_url = f"https://{acc}.blob.core.windows.net"
    blob_service_client = BlobServiceClient(account_url, credential=default_credential)

    # # Create container client
    container_client = blob_service_client.get_container_client(container="container2") 

    # List of the blobs in the container
    blob_list = container_client.list_blobs()
    # for blob in blob_list:
    #     print(blob.name)

    # read all blobs to local files
    local_path = "."
    for blob in blob_list:
        file_path = os.path.join(local_path, blob.name)
        print("=== downloading ", file_path )
        with open(file=file_path, mode="wb") as download_file:
            download_file.write(container_client.download_blob(blob.name).readall())

except Exception as ex:
    print('Exception:')
    print(ex)
    