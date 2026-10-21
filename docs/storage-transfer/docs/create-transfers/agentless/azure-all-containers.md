---
url: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/azure-all-containers/
title: Transfer all containers in an Azure Storage account \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:53.231151+00:00
---

# Transfer all containers in an Azure Storage account  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/azure-all-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer all containers in an Azure Storage account Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service can transfer data from all containers within a single Microsoft Azure Storage account in a single transfer job. This simplifies the workflow for use cases such as ingesting logs that are spread across multiple containers.

## Configure a transfer for all containers

To transfer all containers within a storage account, specify the source container as `*` (a single asterisk) in the `AzureBlobStorageData` public API object or as `https://AZURE_ACCOUNT_NAME.blob.core.windows.net/*` when specifying the source in a `gcloud` command.

Specifying a source folder or `path` is not supported for multi-container transfers. See Filter which containers and objects to transfer to specify paths using prefixes instead.

When the transfer job runs, Storage Transfer Service first queries Azure to get an updated list of all containers in the specified storage account. Then, for each container found, it creates a corresponding folder at the destination and transfers the container's data into that new folder.

###  gcloud 

The following command creates a transfer job that transfers all containers from the specified Azure Storage account to a Cloud Storage bucket.
    
    
    gcloud transfer jobs create \
      https://AZURE_ACCOUNT_NAME.blob.core.windows.net/* \
      gs://GCS_BUCKET_NAME \
      --source-creds-file="PATH_TO_AZURE_SAS_FILE" \
      --project="PROJECT_ID"
    

Where:

  * AZURE_ACCOUNT_NAME: The name of your Azure Storage account.
  * GCS_BUCKET_NAME: The name of the destination Cloud Storage bucket.
  * PATH_TO_AZURE_SAS_FILE: The local path to a text file containing your account-level Azure SAS token. For example: `~/.azure/sas_token.txt`. The SAS token must be created at the storage account level with **Service** , **Container** , and **Object** selected for **Allowed resource types**. See [Configure access to a source: Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure) for details.
  * PROJECT_ID: The Google Cloud project ID that owns the transfer.



###  REST 

To create this transfer with the REST API, make a POST request to the `https://storagetransfer.googleapis.com/v1/transferJobs` endpoint.

Request Body:
    
    
    {
      "description": "Transfer all containers from my Azure account",
      "projectId": "PROJECT_ID",
      "status": "ENABLED",
      "transferSpec": {
        "azureBlobStorageDataSource": {
          "storageAccount": "AZURE_ACCOUNT_NAME",
          "container": "*",
          "azureCredentials": {
            "sasToken": "AZURE_SAS_TOKEN"
          }
        },
        "gcsDataSink": {
          "bucketName": "GCS_BUCKET_NAME"
        }
      }
    }
    

Where:

  * PROJECT_ID: The Google Cloud project ID that owns the transfer.
  * AZURE_ACCOUNT_NAME: The name of your Azure Storage account.
  * AZURE_SAS_TOKEN: The full account-level SAS token string, such as `?sv=2020-08-04&ss=bfqt&srt=sco&...`. The SAS token must be created at the storage account level with **Service** , **Container** , and **Object** selected for **Allowed resource types**. See [Configure access to a source: Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure) for details.
  * GCS_BUCKET_NAME: The name of the destination Cloud Storage bucket.



###  Client library 

This sample uses the `google-cloud-storage-transfer` Python client library to create a transfer.
    
    
    from google.cloud import [storage_transfer_v1](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest)
    
    def create_transfer_all_azure_containers(
        project_id: str,
        description: str,
        azure_storage_account: str,
        azure_sas_token: str,
        gcs_sink_bucket: str,
    ):
        """Creates a transfer job from all containers in an Azure account to Cloud Storage."""
    
        client = [storage_transfer_v1](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest).[StorageTransferServiceClient](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html)()
    
        transfer_job_request = [storage_transfer_v1](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest).[CreateTransferJobRequest](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.CreateTransferJobRequest.html)(
            {
                "transfer_job": {
                    "project_id": project_id,
                    "description": description,
                    "status": [storage_transfer_v1](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest).[TransferJob](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferJob.html).Status.ENABLED,
                    "transfer_spec": {
                        "azure_blob_storage_data_source": {
                            "storage_account": azure_storage_account,
                            "container": "*",  # Wildcard for all containers
                            "azure_credentials": {"sas_token": azure_sas_token},
                        },
                        "gcs_data_sink": {"bucket_name": gcs_sink_bucket},
                    },
                }
            }
        )
    
        result = client.[create_transfer_job](https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.services.storage_transfer_service.StorageTransferServiceClient.html#google_cloud_storage_transfer_v1_services_storage_transfer_service_StorageTransferServiceClient_create_transfer_job)(transfer_job_request)
        print(f"Created transfer job: {result.name}")
    
    if __name__ == "__main__":
        create_transfer_all_azure_containers(
            project_id="PROJECT_ID",
            description="All-containers transfer from Azure",
            azure_storage_account="AZURE_ACCOUNT_NAME",
            azure_sas_token="AZURE_SAS_TOKEN",
            gcs_sink_bucket="GCS_BUCKET_NAME",
        )
    

Where:

  * PROJECT_ID: The Google Cloud project ID that owns the transfer.
  * AZURE_ACCOUNT_NAME: The name of your Azure Storage account.
  * AZURE_SAS_TOKEN: The full account-level SAS token string, such as `?sv=2020-08-04&ss=bfqt&srt=sco&...`. The SAS token must be created at the storage account level with **Service** , **Container** , and **Object** selected for **Allowed resource types**. See [Configure access to a source: Microsoft Azure Storage](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure) for details.
  * GCS_BUCKET_NAME: The name of the destination Cloud Storage bucket.



See [Create transfers](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) for more information about creating transfers, and available options.

## Filter which containers and objects to transfer

You can use prefixes or a manifest file to control which containers and objects are included in the transfer.

### Filter by prefix

To transfer specific containers or specific paths within containers, provide an `includePrefixes` or `excludePrefixes` list. When the container field is `*`, the first segment of each prefix path is treated as the container name. This lets you specify different paths for different containers within the same job. To apply a prefix across all containers in the storage account, use `*` as the first segment, such as `*/PREFIX`.

For example, to transfer everything from `container-a` as well as objects below a specific path in `container-b`, set the include prefixes as follows:
    
    
    "transferSpec": {
      ...
      "azureBlobStorageDataSource": {
        "storageAccount": "my-azure-account",
        "container": "*"
      },
      "objectConditions": {
        "includePrefixes": [
          "container-a",
          "container-b/logs/2025/"
        ]
      },
      ...
    }
    

This configuration:

  * Transfers all objects from `container-a`.
  * Transfers all objects under the `logs/2025/` path from `container-b`.
  * Skips all other containers in the storage account.



To transfer all objects under the `logs/2025/` path from every container in the storage account, specify `"*/logs/2025/"` in `includePrefixes`.

See [Filter by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) for more information about include and exclude prefixes.

### Filter using a manifest

To use a manifest file for a multi-container transfer, the path for each object listed in your manifest CSV file must begin with the container's name.

For example:
    
    
    container-a/photos/photo1.jpg
    container-a/photos/photo2.jpg
    container-c/archive.zip
    

See [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) for more details about manifest files.

## Event-driven transfers

Event-driven transfers from Azure are supported for multi-container configurations.

For best performance and to avoid unnecessary event processing, configure your event filter in Azure to specify which containers should trigger events. Without a filter, events will be generated for all container updates within the storage account.

For more details, see [Event-driven transfers from Azure Blob Storage](https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure).

## Azure API quotas

Transferring from many containers can increase the number of API requests made to Azure. Azure Storage accounts have request rate limits, typically around 20,000 requests per second. If you have a very large number of containers, Storage Transfer Service may throttle the listing process to remain within these limits.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
