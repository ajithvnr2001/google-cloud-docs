---
url: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-storage-export/
title: Export HL7v2 messages to Cloud Storage \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:02.052108+00:00
---

# Export HL7v2 messages to Cloud Storage  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/hl7v2-storage-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Export HL7v2 messages to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export HL7v2 messages from an HL7v2 store to [Cloud Storage](https://docs.cloud.google.com/storage/docs). You can bulk export HL7v2 messages to Cloud Storage for downstream processing.

## Before you begin

See [Export HL7v2 messages from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#exporting-hl7v2-resources) for the roles you must grant to the **Cloud Healthcare Service Agent** service account.

## Export HL7v2 messages to Cloud Storage

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.hl7V2Stores.export` on the requested HL7v2 store



**Roles**

  * [Healthcare HL7v2 Store Administrator (`roles/healthcare.hl7V2StoreAdmin`](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.hl7V2StoreAdmin)) 



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

The Cloud Healthcare API exports each HL7v2 message as a line in an NDJSON `.ndjson` file. The HL7v2 messages are ordered chronologically by their [`sendTime`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Message.FIELDS.send_time) value.

Export to a Cloud Storage bucket or folder, rather than an object, because the Cloud Healthcare API might create multiple NDJSON files when there are many HL7v2 messages.

If you export to a Cloud Storage folder that doesn't exist, the folder is created.

### Console

To export HL7v2 messages to Cloud Storage, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the dataset that contains the HL7v2 store from which you are exporting HL7v2 messages.

  3. In the list of data stores, choose **Export** from the **Actions** list for the HL7v2 store.

The **Export HL7v2 messages** page appears.

  4. In the **Project** list, select a Cloud Storage project.

  5. In the **Location** list, select a Cloud Storage bucket.

  6. Click **Export** to export HL7v2 instances to the defined location in Cloud Storage. 

  7. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



## Export HL7v2 messages to Cloud Storage using filters

By default, exporting HL7v2 messages to Cloud Storage includes all HL7v2 messages in an HL7v2 store and all fields in each [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#resource:-message) object.

You can filter the exported HL7v2 messages as follows:

  * Use filters to export a subset of HL7v2 messages that match a filter criteria. For more information, see Export a subset of HL7v2 messages using a filter.
  * Use the [`MessageView`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/MessageView) object to select the fields in each [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#resource:-message) to export. For more information, see Export HL7v2 messages by `Message` field.



### Export a subset of HL7v2 messages using a filter

You can use the following fields in your filter criteria:

  * [`startTime`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.start_time)
  * [`endTime`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.end_time).



You can specify the following filter parameters as your filter criteria in the [`filter`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export#body.request_body.FIELDS.filter) field. To learn the filter syntax and construct queries, see [Query strings](https://docs.cloud.google.com/appengine/docs/standard/python/search/query_strings).

  * `message_type`: from the MSH.9.1 field. For example, `NOT message_type = "ADT"`.
  * `send_date`: the `YYYY-MM-DD` date the message was sent from the MSH.7 segment, specified in the time zone of the dataset. For example, `send_date < "2017-01-02"`.
  * `send_time`: the timestamp when the message was sent. This parameter is from the MSH.7 segment of the message. This parameter uses the [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) time format for comparisons. For example, `send_time < "2017-01-02T00:00:00-05:00"`.
  * `create_time`: the timestamp when the message was created in the Cloud Healthcare API, using the RFC 3339 time format for comparisons. For example: `create_time < "2017-01-02T00:00:00-05:00"`.
  * `send_facility`: the care center that the message came from, from the MSH.4 segment. For example, `send_facility = "ABC"`.

**Note:** Filtering with `startTime` and `endTime` is more efficient than specifying a filter using `send_time`. A filter created using the `startTime` and `endTime` fields defines a range of HL7v2 messages to which the filter is applied. A `send_time` filter only applies to HL7v2 messages with the exact send time.

The following samples show how to specify a filter to only export HL7v2 messages of type `ADT`.

### REST

  1. Use the [`hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export) method to export the HL7v2 messages:

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the HL7v2 store's parent dataset
     * `HL7V2_STORE_ID`: the HL7v2 store ID
     * `CLOUD_STORAGE_LOCATION`: the name of a Cloud Storage bucket or folder where exported HL7v2 messages are written

Request JSON body: 
    
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION"
      },
      "filter": "message_type = \"ADT\""
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION"
      },
      "filter": "message_type = \"ADT\""
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION"
      },
      "filter": "message_type = \"ADT\""
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `DATASET_ID`: the dataset ID
     * `LOCATION`: the dataset location
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      // The `response` field only displays if there were no errors.
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.ExportMessagesResponse",
        
      },
      // If there were any errors, an `error` field displays instead of a `response` field.
      // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
      "error": {
        "code": ERROR_CODE,
        "message": "DESCRIPTION",
        "details": [
          {
            "@type": "...",
            FIELD1: ...,
            ...
          }
        ]
      }
    }
    




### Export HL7v2 messages by `Message` field

In the Cloud Healthcare API, HL7v2 messages are stored in [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#resource:-message) resources. You can use the [`MessageView`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/MessageView) enum to determine which fields in the `Message` resource are included in each exported HL7v2 message.

The following samples show how to use the [`BASIC`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/MessageView#ENUM_VALUES.BASIC) value in `MessageView` to only include the [`name`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages#Message.FIELDS.name) field in the exported HL7v2 messages.

### REST

  1. Use the [`hl7V2Stores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/export) method to export the HL7v2 messages:

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the HL7v2 store's parent dataset
     * `HL7V2_STORE_ID`: the HL7v2 store ID
     * `CLOUD_STORAGE_LOCATION`: the name of a Cloud Storage bucket or folder where exported HL7v2 messages are written

Request JSON body: 
    
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION",
        "messageView": "BASIC"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION",
        "messageView": "BASIC"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "gcsDestination": {
        "uriPrefix": "gs://CLOUD_STORAGE_LOCATION",
        "messageView": "BASIC"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:export" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Use the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method to get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `DATASET_ID`: the dataset ID
     * `LOCATION`: the dataset location
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The output is the following. When the response contains `"done": true`, the long-running operation has finished. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "https://console.cloud.google.com/CLOUD_LOGGING_URL"
        "counter": {
          "success": "SUCCESS_COUNT",
          // If there were any failures, they display in the `failure` field.
          "failure": "FAILURE_COUNT"
        }
      },
      "done": true,
      // The `response` field only displays if there were no errors.
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.hl7v2.ExportMessagesResponse",
        
      },
      // If there were any errors, an `error` field displays instead of a `response` field.
      // See [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting) for a list of response codes.
      "error": {
        "code": ERROR_CODE,
        "message": "DESCRIPTION",
        "details": [
          {
            "@type": "...",
            FIELD1: ...,
            ...
          }
        ]
      }
    }
    




## Troubleshoot HL7v2 export requests

If errors occur while exporting HL7v2 messages, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If a long-running operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
