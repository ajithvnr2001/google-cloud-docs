---
url: https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure/
title: Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2 \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:42.088921+00:00
---

# Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2 Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure event-driven data transfers from Azure Blob Storage or Data Lake Storage Gen2 to Cloud Storage using Storage Transfer Service. Event-driven transfers automatically transfer new objects and updated objects from your Azure container to Cloud Storage. Object deletions are not detected; deleting an object at the source does not delete the associated object in the destination bucket.

Event-driven transfers use Azure Event Grid and Azure Storage Queues to notify Storage Transfer Service about changes in your Azure container. When an event such as a new blob creation occurs in your source container, Azure Event Grid sends a notification to a configured Azure Storage Queue. Storage Transfer Service continuously monitors this queue and initiates a transfer based on the events received.

## Before you begin

Follow the instructions to grant the required permissions on your destination Cloud Storage bucket:

  * [Configure access to a destination: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage)



## Create an Azure Storage queue

Create an Azure Storage queue that will receive notifications from Azure Event Grid.

  1. In the Azure portal, navigate to your Azure Storage account.
  2. In the left navigation menu, under **Data storage** , select **Queues**.
  3. Click **\+ Queue** to create a new queue.
  4. Provide a name for your queue (e.g., `transfer-notifications`) and click **OK**.
  5. Once created, retrieve the address for the Azure Queue. The address will typically be in the format: `AZURE_STORAGE_ACCOUNT_NAME.queue.core.windows.net/AZURE_QUEUE_NAME`.



## Enable Azure Blob Storage event notifications for Azure Queue

Configure Azure Event Grid to send notifications of blob storage events to the Azure queue you created.

  1. In the Azure portal, navigate to the storage account that contains the blob storage container you want to monitor.
  2. In the left navigation menu, under **Blob service** , select **Events**.
  3. Click **\+ Event Subscription**.
  4. Configure the event subscription:

     * **Event Subscription Details** : 
       * Provide an **Event Subscription Name** (e.g., `blob-transfer-events`).
       * Provide a **System Topic Name** (e.g., `my-blob-events-topic`).
     * **Event Types** : 
       * Select the following event types: 
         * Blob Created
         * Directory Created
         * Blob Renamed
         * Directory Renamed
         * Blob Tier Changed
     * **Endpoint Details** : 
       * **Endpoint Type** : Select **Storage Queue**.
       * Click **Select an endpoint** , then select the Azure Queue you created earlier.
     * **Filters** :

       * Click **Enable subject filtering**.
       * Add the following as the **Subject begins with** filter to limit notifications to a specific container:

`/blobServices/default/containers/AZURE_CONTAINER_NAME/`

Replace AZURE_CONTAINER_NAME with the name of your blob storage container.

       * (Optional) To filter events for blobs with a specific prefix within the container, use:

`/blobServices/default/containers/AZURE_CONTAINER_NAME/blobs/BLOB_PREFIX`

  5. Click **Create**.




## Set up access to Azure queue

Storage Transfer Service needs permission to access the Azure queue and read its messages. You can authenticate using either a Shared Access Signature (SAS) token or federated identity.

###  SAS token 

Follow the instructions for [authenticating with a SAS token](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure#sas-token) and include the following items:

  * **Allowed services** : Blob and Queue
  * **Allowed permissions** : Read, List, and Process



###  Federated identity 

Follow the instructions for [authenticating with federated identity](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure#option_3_authenticate_using_federated_identity). In addition to granting the application access to your Azure Storage container, you must also grant it access to the Azure queue. To do this, add the **Storage Queue Data Message Processor** role to the application for the Azure queue.

## Create a transfer job with an event stream

Once your Azure queue and event notifications are configured, create your Storage Transfer Service job with an event stream.

Once created, the transfer job starts running and an event listener waits for notifications on the Azure queue. The job details page shows one operation each hour, and includes details on data transferred for each job.

###  Google Cloud console 

  1. Go to the **Create transfer job** page in the Google Cloud console.

[Go to **Create transfer job**](https://console.cloud.google.com/transfer/create)

  2. For **Source type** , select **Azure Blob Storage or Data Lake Storage Gen2**.

  3. For **Destination type** , select **Google Cloud Storage**.

  4. For **Scheduling mode** , select **Event-driven**.

  5. In the **Event stream name** field, enter the address of your Azure queue.

  6. Complete the remaining steps as normal for creating a transfer job, including source and destination details, and authentication.

Optionally, enter a start and end time for the transfer. If you don't specify a time, the transfer will start immediately and will run until manually stopped.




###  Google Cloud CLI 

To create an event-driven transfer job using the gcloud CLI, use the `gcloud transfer jobs create` command with the `--event-stream-name` flag:
    
    
    gcloud transfer jobs create \
      https://AZURE_STORAGE_ACCOUNT_NAME.blob.core.windows.net/AZURE_CONTAINER_NAME \
      gs://DESTINATION_BUCKET \
      --source-creds-file=SOURCE_CREDS_FILE \
      --event-stream-name=AZURE_STORAGE_ACCOUNT_NAME.queue.core.windows.net/AZURE_QUEUE_NAME \
      --event-stream-starts=EVENT_STREAM_STARTS \
      --event-stream-expires=EVENT_STREAM_EXPIRES
    

Replace the placeholders with your actual values:

  * AZURE_STORAGE_ACCOUNT_NAME and AZURE_CONTAINER_NAME: Your Azure Blob Storage account name and container name.
  * DESTINATION_BUCKET: Your destination Cloud Storage bucket.
  * SOURCE_CREDS_FILE: The relative path to a local file on your machine containing your SAS token or federated identity configuration.
  * AZURE_QUEUE_NAME: The name of your Azure Queue (e.g., `my-queue`).
  * EVENT_STREAM_STARTS: When to start listening for events using the %Y-%m-%dT%H:%M:%S%z datetime format (e.g., `2020-04-12T06:42:12+04:00`). If not set, the job starts running and listening for events upon the successful submission of the create job command.
  * EVENT_STREAM_EXPIRES: When to stop listening for events. If not set, the job continues until manually stopped.



For a full list of supported fields, refer to the [`gcloud transfer jobs create`](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create) reference.

###  REST API 

Define an event-driven transfer job using the TransferJob proto:
    
    
    {
      "description": "Event-driven Azure to Cloud Storage transfer",
      "project_id": "PROJECT_ID",
      "transfer_spec": {
        "azure_blob_storage_data_source": {
          "storage_account": "AZURE_STORAGE_ACCOUNT_NAME",
          "container": "AZURE_CONTAINER_NAME",
          "federated_identity_config": {
            "client_id": "CLIENT_ID",
            "tenant_id": "TENANT_ID"
          }
        },
        "gcs_data_sink": {
          "bucket_name": "DESTINATION_BUCKET"
        },
        "object_conditions": {
          // optional object conditions (include_prefixes, etc)
        },
        "transfer_options": {}
      },
      "event_stream": {
        "name": "AZURE_STORAGE_ACCOUNT_NAME.queue.core.windows.net/AZURE_QUEUE_NAME",
        "event_stream_start_time": EVENT_STREAM_START_TIME,
        "event_stream_expiration_time": EVENT_STREAM_EXPIRATION_TIME
      },
      "status": "ENABLED"
    }
    

The start and expiration time fields are optional:

  * `event_stream_start_time`: The time from which to start listening for events in the format `YYYY-MM-DDTHH:MM:SSZ`. If not specified, the listener starts immediately.
  * `event_stream_expiration_time`: The time at which the event stream listener expires in the format `YYYY-MM-DDTHH:MM:SSZ`. If not specified, the listener continues until the transfer job is disabled or deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
