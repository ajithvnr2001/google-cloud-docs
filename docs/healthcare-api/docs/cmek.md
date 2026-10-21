---
url: https://docs.cloud.google.com/healthcare-api/docs/cmek/
title: Enable customer-managed encryption keys (CMEK) for Cloud Healthcare API datasets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:13.361419+00:00
---

# Enable customer-managed encryption keys (CMEK) for Cloud Healthcare API datasets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Enable customer-managed encryption keys (CMEK) for Cloud Healthcare API datasets Stay organized with collections  Save and categorize content based on your preferences. 

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK) for your Cloud Healthcare API [datasets](https://docs.cloud.google.com/healthcare-api/docs/projects-datasets-data-stores#datasets_and_data_stores). Instead of Google owning and managing the encryption keys that protect your data, your Cloud Healthcare API datasets are encrypted using a key that you control and manage in [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs).

For more information about CMEK in general, including when and why to enable it, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Before you begin

Decide whether your Cloud Healthcare API dataset and Cloud KMS will be in the same Google Cloud project or different ones. For guidance, see [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties).

For documentation purposes, the following conventions are used:

  * `PROJECT_ID`: the Cloud Healthcare API project ID
  * `KMS_PROJECT_ID`: the project ID where Cloud KMS runs, which might be the same as `PROJECT_ID`



For information about Google Cloud project IDs and project numbers, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Limitations

  * You can only use Cloud KMS keys when creating a Cloud Healthcare API [dataset](https://docs.cloud.google.com/healthcare-api/docs/projects-datasets-data-stores#datasets_and_data_stores). You can't enable, change, or disable Cloud KMS keys on an existing Cloud Healthcare API dataset.
  * Only FHIR, DICOM, and HL7v2 stores are supported in CMEK-encrypted datasets. CMEK protection applies to DICOM, FHIR, and HL7v2 stores in the dataset and their resources.
  * You can't de-identify CMEK-encrypted resources.



## CMEK operations

Cloud KMS keys are used when a CMEK-encrypted resource is created, read, updated, or deleted, and for operational tasks like billing or ensuring the key is available.

## External key considerations

For information on using keys that you manage within a [supported external key management partner system](https://docs.cloud.google.com/kms/docs/ekm#supported_partners) to protect data within Google Cloud, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

If you lose keys that you manage outside of Google Cloud, Google can't recover your data.

## Key unavailability and data loss

If a dataset is encrypted by a key, and that key becomes unavailable and remains unavailable, the Cloud Healthcare API disables and eventually deletes the dataset. Sometimes, a key becomes unavailable if it's disabled or destroyed, or if it's inaccessible due to revoked permissions, but this behavior occurs if the key is unavailable for any reason. The key's protection level or whether it's an external key doesn't affect this behavior. External keys can also become unavailable unpredictably. For example, connectivity issues might arise between your Google Cloud resources and your EKM.

The following process describes how key availability is checked, and how a dataset can be disabled and deleted:

  1. After a CMEK-encrypted Cloud Healthcare API dataset is created, the Cloud Healthcare API checks the key's status every five minutes to ensure the key is available. If the key is unavailable, the Cloud Healthcare API continues to support requests to the dataset for up to one hour.

  2. After one hour, if the Cloud Healthcare API is still unable to connect with Cloud KMS, the Cloud Healthcare API dataset is disabled as a protective measure. To re-enable the Cloud Healthcare API dataset, contact your [support representative](https://docs.cloud.google.com/support/docs#contacting_technical_support).

When disabled, you can only send [`datasets.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/get) and [`datasets.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/delete) requests to the Cloud Healthcare API dataset. Other requests fail with a `400 FAILED_PRECONDITION` error.

  3. If the Cloud Healthcare API dataset remains unavailable for more than 30 days, it's permanently deleted. Any DICOM, FHIR, and HL7v2 stores in the dataset and their associated data are also deleted. If deleted, this data can't be recovered.




## Key creation

The following sections describe how to create a Cloud KMS key ring and key. Only Cloud KMS [symmetric encryption keys](https://docs.cloud.google.com/kms/docs/create-key#create-symmetric) are supported.

### Supported locations

Cloud KMS keys are available in the Cloud Healthcare API [locations](https://docs.cloud.google.com/healthcare-api/docs/regions#available_regions). Create the key ring in a location that matches the region or multi-region of your Cloud Healthcare API dataset.

  * Any multi-regional Cloud Healthcare API dataset must use a multi-regional key ring from a matching location. For example, a Cloud Healthcare API dataset in region `us` must be protected with a key ring from region `us`, and a Cloud Healthcare API dataset in region `eu` must be protected with a key ring from region `europe`.

  * Regional Cloud Healthcare API datasets must use matching regional keys. For example, a Cloud Healthcare API dataset in region `asia-northeast1` must be protected with a key ring from region `asia-northeast1`.

  * You can't use the `global` region when configuring CMEK for a Cloud Healthcare API dataset.




For more information, see [Cloud Healthcare API locations](https://docs.cloud.google.com/healthcare-api/docs/regions) and [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

### Create a key ring and key

Complete the following steps in the Google Cloud project that runs Cloud KMS:

  1. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring).
  2. [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys).



### Grant encryption and decryption permissions

To protect your Cloud Healthcare API data with a Cloud KMS key, grant the [**Cloud Healthcare Service Agent** service account](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#the_cloud_healthcare_service_agent) the [CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role on that key. For instructions, see [Dataset CMEK permissions](https://docs.cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#dataset-cmek).

After granting the service account the role, the Cloud Healthcare API can encrypt and decrypt CMEK-encrypted resources. Your applications don't need to specify keys when reading or writing data. The Cloud Healthcare API handles encryption.

When a requester reads or writes an object encrypted with a Cloud KMS key, they access the object as normal. During the request, the service agent automatically encrypts or decrypts the requested object, provided both of the following conditions are met:

  * The service agent still has the required permissions.
  * The key is available and enabled.



## Create a CMEK-encrypted Cloud Healthcare API dataset

The following samples show how to create a CMEK-encrypted dataset.

You must specify a Cloud KMS key resource ID when creating the dataset. This key is case-sensitive and in the following format:
    
    
    projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

To view your Cloud KMS key resource IDs, see [Getting a Cloud KMS resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).

**Note:** You can't specify a key resource ID that includes the `/cryptoKeyVersions/` token when creating a Cloud Healthcare API dataset.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.datasets.create`



**Roles**

  * [Healthcare Dataset Administrator (`roles/healthcare.datasetAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.datasetAdmin)



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

### Console

  1. In the Google Cloud console, go to the **Browser** page.

[Go to Browser](https://console.cloud.google.com/healthcare/browser)

  2. Click _add_box_ **Create dataset**. The **Create dataset** page is displayed.

  3. In the **Name** field, enter an identifier for the dataset subject to the [dataset permitted characters and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements).

  4. Select one of the following location types:

     * **Region**. The dataset permanently resides within one Google Cloud region. After selecting this option, type or select a location in the **Region** field.

     * **Multi-region**. The dataset permanently resides within a location that spans multiple Google Cloud regions. After selecting this option, type or select a multi-region location in the **Multi-region** field.

  5. In the **Encryption** section, select one of the following encryption types:

     * **Google-managed encryption key** : The default encryption method. Use this method if you want Google to manage the encryption keys that protect your data in this Cloud Healthcare API dataset.

     * **Cloud KMS key** : Use a customer-managed encryption key (CMEK).

**Note:** Enabling CMEK encryption for a Cloud Healthcare API dataset cannot be undone, and you can't change the encryption method for a dataset after enabling CMEK encryption.
  6. Click **Create**. The **Browser** page is displayed. The new dataset is displayed in the list of datasets.




### gcloud

Create the dataset using the [`gcloud healthcare datasets create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/create) command.

Before using any of the command data below, make the following replacements: 

  * `DATASET_ID`: an identifier subject to the [dataset permitted characters and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements)
  * `LOCATION`: a [supported location](https://docs.cloud.google.com/healthcare-api/docs/regions#available_regions) for the dataset
  * `KEY_RESOURCE_ID`: the resource ID for a Cloud KMS key, in the format `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create DATASET_ID \
      --location=LOCATION \
      --encryption-key=KEY_RESOURCE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create DATASET_ID `
      --location=LOCATION `
      --encryption-key=KEY_RESOURCE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare datasets create DATASET_ID ^
      --location=LOCATION ^
      --encryption-key=KEY_RESOURCE_ID

You should receive a response similar to the following:
    
    
    Create request issued for: [DATASET_ID]
    Waiting for operation [projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID] to complete...
    Created dataset [DATASET_ID].
    

### REST

  1. Create the dataset using the [`datasets.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/create) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `DATASET_ID`: an identifier subject to the [dataset permitted characters and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements)
     * `LOCATION`: a [supported location](https://docs.cloud.google.com/healthcare-api/docs/regions#available_regions) for the dataset
     * `KEY_RESOURCE_ID`: the resource ID for a Cloud KMS key, in the format `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`

Request JSON body: 
    
    {
      "encryptionSpec": {
        "kmsKeyName": "KEY_RESOURCE_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "encryptionSpec": {
        "kmsKeyName": "KEY_RESOURCE_ID"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets?datasetId=DATASET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "encryptionSpec": {
        "kmsKeyName": "KEY_RESOURCE_ID"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets?datasetId=DATASET_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations) (LRO). Long-running operations are returned when method calls might take additional time to complete. Note the value of `OPERATION_ID`. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    
    

  2. Get the status of the long-running operation using the [`projects.locations.datasets.operations.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) method.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the dataset ID
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
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.CreateDataset",
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
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.dataset.Dataset",
        "name": "PROJECT_ID/locations/LOCATION/datasets/DATASET_ID",
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
    




## Determine if a dataset is protected by Cloud KMS

For each of the keys you've created or that protect your Cloud Healthcare API datasets, you can see what resources that key protects with key usage tracking. For more information, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

## Key rotation

Cloud KMS supports both automatic and manual [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) to a new version.

Rotating a key results in the following:

  * Cloud Healthcare API datasets created after the rotation use the new key version for encryption and all operations.
  * Resources in an existing dataset that are encrypted with the key aren't automatically re-encrypted with the new primary key version.



For encryption to work, all key versions must be available. Otherwise, the Cloud Healthcare API dataset is disabled and all requests to the dataset fail. For more information, see External key considerations and Disabled datasets and permanent dataset deletion.

## Remove Cloud Healthcare API access to the Cloud KMS key

You have control over your keys and can disable, destroy, or revoke permissions on the key so that the Cloud Healthcare API can't access CMEK-encrypted data. After you destroy a key or key version associated with a Cloud Healthcare API dataset, all data encrypted with that key or key version is permanently lost.

There is a delay between when you disable a key or key version and when it can no longer be used. There's also a delay between when you revoke the **Cloud Healthcare service agent** service account permissions on the key and when it can no longer be accessed. For more information see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency).

## Export and import data to a CMEK-enabled instance

To keep your data encrypted with a customer-managed key during an export operation, you must set a CMEK on the storage destination before beginning the export. There are no special requirements or restrictions for importing data to a CMEK-encrypted dataset when importing from non-CMEK or CMEK-encrypted storage.

## Restrictions

  * [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) with [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm) isn't supported.
  * There is a limit of 10 CMEK datasets per project in a 30-day period. This quota is enforced by the `cmek_datasets` quota metric.
  * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) with CMEK isn't supported.
  * [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) aren't supported.



## Pricing

Datasets are billed the same regardless of whether they're CMEK-encrypted. For more information, see [Cloud Healthcare API pricing](https://cloud.google.com/healthcare-api/pricing).

You're billed by Cloud KMS for both the cost of the key and any cryptographic operations on that key. These operations occur when the Cloud Healthcare API uses the key for encryption or decryption. You can expect these costs to be minimal, based on the expected number of cryptographic operations generated by the Cloud Healthcare API. For more information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Cloud KMS quotas and Cloud Healthcare API

When you use CMEK in Cloud Healthcare API, your projects can consume Cloud KMS cryptographic requests quotas. CMEK-encrypted Cloud Healthcare API datasets and their DICOM, FHIR, and HL7v2 stores consume these quotas for all operations except [`datasets.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/get). Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## What's next

  * For more information about CMEK in general, including when and why to enable it, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
