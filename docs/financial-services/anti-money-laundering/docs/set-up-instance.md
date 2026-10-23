---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance/
title: Create an AML AI instance \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:30.941310+00:00
---

# Create an AML AI instance  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Create an AML AI instance Stay organized with collections  Save and categorize content based on your preferences. 

To use AML AI, create an instance. The AML AI [Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances) resource sits at the root of all other AML AI resources. Multiple instances can be created in the same region within a Google Cloud project. If the same parties are used in the instances, then you can share party registrations between instances to reduce costs. For more information, see [Party registration sharing for multiple instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing). and the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing).

Instances adhere to the following:

  * Each instance is specific to a Google Cloud region, ensuring data residency within the Google Cloud region.
  * Each instance requires all input and output data to exist in the same Google Cloud region and project.
  * Each instance requires a single associated customer-managed encryption key (CMEK) which is used to encrypt any data created by AML AI.
  * An instance's child resources inherit the parent instance's location and encryption settings.
  * Each instance supports customized access management.



The list of available Google Cloud regions can be found on the [AML AI locations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations) page. You can map one (or several) geographies in which you operate to one (or several) available AML AI locations, based on your policies. You need to create at least one AML AI instance per AML AI location that you use.

You can run risk scoring both for commercial and retail customers in one AML AI instance. However, create a separate instance to do any of the following:

  * Restrict access to different sets of AML data to disparate members within your organization.
  * Use different CMEK keys for different sets of AML data.
  * Keep production AML AI alerting pipelines separated from training and evaluation of new AML AI models. For more information, see [Party registration sharing for multiple instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/registration-sharing).



## Steps

To create a Google Cloud project and enable the API, see [Set up a project and permissions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-project-permissions).

Follow these steps to create a CMEK key and an AML AI instance.

### Create an encryption key

To create an encryption key, first create a key ring and then the key itself. For more information, see [Create encryption keys with Cloud KMS](https://docs.cloud.google.com/kms/docs/create-encryption-keys).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `cloudkms.keyRings.create`
  * `cloudkms.cryptoKeys.create`



#### Create a key ring

To create a key ring, use the [`projects.locations.keyRings.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create) method.

### REST

Before using any of the request data, make the following replacements: 

  * `KMS_PROJECT_ID`: the Google Cloud project ID for the project containing the key ring 
  * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `KEY_RING_ID`: a user-defined identifier for the key ring



To send your request, choose one of these options:

#### curl

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudkms.googleapis.com/v1/projects/KMS_PROJECT_ID/locations/LOCATION/keyRings?key_ring_id=KEY_RING_ID"

#### PowerShell

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudkms.googleapis.com/v1/projects/KMS_PROJECT_ID/locations/LOCATION/keyRings?key_ring_id=KEY_RING_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID",
      "createTime": "2023-03-14T15:52:55.358979323Z"
    }
    

### gcloud

Before using any of the command data below, make the following replacements: 

  * `KMS_PROJECT_ID`: the Google Cloud project ID for the project containing the key ring 
  * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `KEY_RING_ID`: a user-defined identifier for the key ring



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create KEY_RING_ID \
      --project KMS_PROJECT_ID --location LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create KEY_RING_ID `
      --project KMS_PROJECT_ID --location LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create KEY_RING_ID ^
      --project KMS_PROJECT_ID --location LOCATION

You should receive an empty response: 
    
    
    $

#### Create a key

To create a key, use the [`projects.locations.keyRings.cryptoKeys`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method.

### REST

Before using any of the request data, make the following replacements: 

  * `KMS_PROJECT_ID`: the Google Cloud project ID for the project containing the key ring 
  * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `KEY_RING_ID`: the user-defined identifier for the key ring
  * `KEY_ID`: a user-defined identifier for the key



Request JSON body: 
    
    
    {
      "purpose": "ENCRYPT_DECRYPT"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "purpose": "ENCRYPT_DECRYPT"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudkms.googleapis.com/v1/projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys?crypto_key_id=KEY_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "purpose": "ENCRYPT_DECRYPT"
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
        -Uri "https://cloudkms.googleapis.com/v1/projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys?crypto_key_id=KEY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID",
      "primary": {
        "name": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID/cryptoKeyVersions/1",
        "state": "ENABLED",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "protectionLevel": "SOFTWARE",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION",
        "generateTime": "2023-03-14T15:52:55.358979323Z"
      },
      "purpose": "ENCRYPT_DECRYPT",
      "createTime": "2023-03-14T15:52:55.358979323Z",
      "versionTemplate": {
        "protectionLevel": "SOFTWARE",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION"
      },
      "destroyScheduledDuration": "86400s"
    }
    

### gcloud

Before using any of the command data below, make the following replacements: 

  * `KMS_PROJECT_ID`: the Google Cloud project ID for the project containing the key ring 
  * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `KEY_RING_ID`: the user-defined identifier for the key ring
  * `KEY_ID`: a user-defined identifier for the key



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create KEY_ID \
      --keyring KEY_RING_ID \
      --project KMS_PROJECT_ID \
      --location LOCATION \
      --purpose "encryption"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create KEY_ID `
      --keyring KEY_RING_ID `
      --project KMS_PROJECT_ID `
      --location LOCATION `
      --purpose "encryption"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create KEY_ID ^
      --keyring KEY_RING_ID ^
      --project KMS_PROJECT_ID ^
      --location LOCATION ^
      --purpose "encryption"

You should receive an empty response: 
    
    
    $

### Create an instance

Create an instance for the specific region where the data should reside. This instance references the encryption key you created. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To create an instance, use the [`projects.locations.instances.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/create) method. 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1instances.create`



(The following information is also available in [Create and manage instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances).)

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the [location of the key ring](https://docs.cloud.google.com/kms/docs/locations) and the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: a user-defined identifier for the instance
  * `KMS_PROJECT_ID`: the Google Cloud project ID for the project containing the key ring
  * `KEY_RING_ID`: the user-defined identifier for the key ring
  * `KEY_ID`: the user-defined identifier for the key **Note** : You can't change to a different CMEK key after the instance has been created.



Request JSON body: 
    
    
    {
      "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID"
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
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

If successful, the response body contains a [long-running operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations) that contains an ID which can be used to retrieve the ongoing status of the asynchronous operation. Copy the returned OPERATION_ID to use in the next section.

#### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method to check if the instance has been created. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. These operations can take a few minutes to several hours to complete.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.operations.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "endTime": "2023-03-14T16:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.Instance",
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID",
        "state": "ACTIVE"
      }
    }
    

### Grant access to the CMEK key

The API automatically creates a service account in your project. The service account needs access to the CMEK key so it can use the key to encrypt and decrypt the underlying data. Grant access to the key.

For PROJECT_NUMBER, use the project number associated with PROJECT_ID. You can find the project number on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `cloudkms.cryptoKeys.getIamPolicy`
  * `cloudkms.cryptoKeys.setIamPolicy`


    
    
    gcloud kms keys add-iam-policy-binding "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID" \
      --keyring "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID" \
      --location "LOCATION" \
      --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com" \
      --role="roles/cloudkms.cryptoKeyEncrypterDecrypter" \
      --project="PROJECT_ID"

### Contact support

Every time you create an AML AI instance, reach out to [support](https://docs.cloud.google.com/support). Include the following information so the AML AI product team can optimally configure your instance based on your needs:

  * Project ID
  * Google Cloud region
  * Instance ID
  * Expected number of parties in the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table in datasets within this instance
  * Expected number of transactions per year in the [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction) table in datasets within this instance



To request additional quota limits, see [Quotas](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/quotas).

AML AI makes multiple types of logs available, including platform logs, audit logs, and data access logs. Learn more about each type of logging:

  * [Platform logs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/logging)
  * [Audit logs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/audit-logging)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
