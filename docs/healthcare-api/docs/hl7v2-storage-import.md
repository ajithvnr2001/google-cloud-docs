---
url: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-storage-import/
title: Import HL7v2 messages from Cloud Storage \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:16.403786+00:00
---

# Import HL7v2 messages from Cloud Storage  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-storage-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Import HL7v2 messages from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to import HL7v2 messages from [Cloud Storage](https://docs.cloud.google.com/storage/docs) into an HL7v2 store. Bulk importing HL7v2 messages is faster and simpler than storing them individually using the [REST API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#overview_of_creating_and_ingesting_hl7v2_messages).

## Before you begin

See [Import HL7v2 messages from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#importing-hl7v2-resources) for the roles you must grant to the **Cloud Healthcare Service Agent** service account.

## Input file format requirements

To import HL7v2 messages, you must first create one or more newline-delimited JSON (`.ndjson`) files in Cloud Storage containing one or more messages. Each line of the file is a single [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Message) resource which contains a base64-encoded HL7v2 message. The `Message` resource can also include optional labels.

For example, the following file, named `messages.ndjson`, contains two HL7v2 messages. A label is defined in the second message.
    
    
    {"data" :"TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZXzF8QXxBfDIwMTgwMTAxMDAwMDAwfHxUWVBFXkF8MjAxODAxMDEwMDAwMDB8VHwwLjB8fHxBQXx8MDB8QVNDSUkNRVZOfEEwMHwyMDE4MDEwMTA0MDAwMA1QSUR8fDE0ATExMV5eXl5NUk58MTExMTExMTFeXl5eTVJOfjExMTExMTExMTFeXl5eT1JHTk1CUg=="}
    {"data" :"TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZXzJ8QXxBfDIwMTgwMTAxMDAwMDAwfHxUWVBFXkF8MjAxODAxMDEwMDAwMDB8VHwwLjB8fHxBQXx8MDB8QVNDSUkNRVZOfEEwMHwyMDE4MDEwMTA0MDAwMA1QSUR8fDE0ATExMV5eXl5NUk58MTExMTExMTFeXl5eTVJOfjExMTExMTExMTFeXl5eT1JHTk1CUg==","labels":{"foo":"bar"}}
    

## Import HL7v2 messages

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.hl7V2Stores.import` on the requested HL7v2 store



**Roles**

  * [Healthcare HL7v2 Store Administrator (`roles/healthcare.hl7V2StoreAdmin`](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.hl7V2StoreAdmin)) 



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### Console

To import HL7v2 messages from a Cloud Storage bucket, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the dataset that contains the HL7v2 store to which you are importing HL7v2 messages.

  3. In the list of data stores, choose **Import** from the **Actions** list for the HL7v2 store.

The **Import to HL7v2 store** page appears.

  4. In the **Project** list, select a Cloud Storage project.

  5. In the **Location** list, select a Cloud Storage bucket.

  6. To set a specific location for importing files, do the following:

     1. Expand **Advanced Options**.
     2. Select **Override Cloud Storage Path**.
     3. To set a specific source for importing files, define the path in the **Location** text box. You can use wildcards to import multiple files from one or more directories. For more information on object naming, see [Object naming guidelines](https://docs.cloud.google.com/storage/docs/objects#naming).

The following wildcards are supported: 
        * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.ndjson` matches Example.ndjson and Example22.ndjson in DIRECTORY.
        * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .ndjson), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.ndjson` imports all files with the .ndjson filename extension in DIRECTORY and its subdirectories. 
        * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.ndjson` matches Example1.ndjson but does not match Example.ndjson or Example01.ndjson. 
  7. Click **Import** to import HL7v2 messages from the defined source. 

  8. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### API

The following samples show how to import HL7v2 messages from Cloud Storage using the [`projects.locations.datasets.hl7V2Stores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/import) method.

Note the following when calling the import operation:

  * The location of the file within the bucket is arbitrary and does not have to adhere exactly to the format specified in the following samples.
  * When specifying the location of the HL7v2 messages in Cloud Storage, you can use wildcards to import multiple files from one or more directories. The following wildcards are supported: 
    * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.ndjson` matches Example.ndjson and Example22.ndjson in DIRECTORY.
    * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .ndjson), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.ndjson` imports all files with the .ndjson filename extension in DIRECTORY and its subdirectories. 
    * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.ndjson` matches Example1.ndjson but does not match Example.ndjson or Example01.ndjson. 



### curl

To import HL7v2 messages into an HL7v2 store, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the HL7v2 store
  * The location of the object in a Cloud Storage bucket
  * An access token



The following sample shows how to import a single file using a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'gcsSource': {
            'uri': 'gs://BUCKET/DIRECTORY/HL7V2_MESSAGE_FILE'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:import"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ImportMessages",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.ImportMessagesResponse"
      }
    }
    

### PowerShell

To import HL7v2 messages into an HL7v2 store, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the HL7v2 store
  * The location of the object in a Cloud Storage bucket
  * An access token



The following sample shows how to import a single file using a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'gcsSource': {
          'uri': 'gs://BUCKET/DIRECTORY/HL7V2_MESSAGE_FILE'
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:import" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ImportMessages",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.ImportMessagesResponse"
      }
    }
    

## Troubleshoot HL7v2 import requests

If errors occur while importing HL7v2 messages, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If a long-running operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
