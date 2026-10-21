---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/cmek/
title: Encrypt data using customer-managed encryption keys (CMEK) \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:49.878646+00:00
---

# Encrypt data using customer-managed encryption keys (CMEK)  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Encrypt data using customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to encrypt data stored in AML AI instances with customer-managed encryption keys (CMEK).

## Overview

All customer data in an AML AI instance is encrypted at rest using a CMEK key. You create and manage the key within [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs), and you control access to the key using Identity and Access Management. If you temporarily disable or permanently destroy the CMEK key, data encrypted with that key cannot be accessed.

AML AI only supports CMEK by using [Cloud KMS](https://docs.cloud.google.com/kms/docs/create-encryption-keys). It doesn't support Google Default Encryption.

CMEK gives you control over your keys including their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles, but it also incurs additional [costs](https://cloud.google.com/kms/pricing) for the Cloud KMS service.

Cloud KMS can run in the same Google Cloud project as AML AI or in a separate project where you centrally manage keys for multiple projects.

Encryption configuration is set up when you [create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances). Once an instance has been created, you cannot assign a different Cloud KMS key. You can still rotate the key.

For more information about CMEK in general, see the [Cloud KMS documentation](https://docs.cloud.google.com/kms/docs/cmek).

## Protection levels

Cloud KMS lets you choose from a variety of different [protection levels](https://docs.cloud.google.com/kms/docs/protection-levels), including the following:

  * Software keys
  * Hardware Security Modules (HSMs) using [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm)



Learn how to configure CMEK in AML AI. Not all protection levels are available in all regions. Note that AML AI does not support Customer Supplied Encryption Keys (CSEK) or Cloud External Key Manager.

## Customer data

All [customer data](https://cloud.google.com/terms/data-processing-addendum) handled by AML AI is encrypted at rest using the CMEK key specified in the corresponding parent [Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances) resource. This includes all customer data associated with AML AI resources, such as datasets, engine configs, models, and more. All temporary and persistent storage of customer data, including copies of inputs and outputs, generated ML features, model hyper parameters, model weights, and prediction results, is encrypted using the CMEK key of the corresponding instance.

See the [service specific terms](https://cloud.google.com/terms/service-terms) for the definition of customer data, which may not include resource identifiers, attributes, or other data labels.

## Encrypting input and output data

The AML AI encryption configuration in an instance is used only for AML AI resources and their data. AML AI doesn't manage the encryption of input or output data in your Google Cloud project. If you want this data to be encrypted using CMEK, then you must set up a Cloud KMS key to match your chosen key protection level configured on the BigQuery dataset. You can also reuse the same key used by AML AI.

Read [more about encryption in BigQuery](https://docs.cloud.google.com/bigquery/docs/encryption-at-rest).

## Key rotation

Periodically and automatically rotating keys is a recommended security practice. With CMEK, key rotation is controlled by you. When you rotate a key, data encrypted with previous key versions is not automatically re-encrypted with the new key version.

A single AML AI resource may internally be stored as multiple units. If, during the lifetime of an AML AI resource, the key version is rotated, not all units may be encrypted with the same key version.

If you rotate a key, there is no way in AML AI to force a re-encryption or to determine if older key versions are safe to delete.

Read more about [key rotation with Cloud KMS](https://docs.cloud.google.com/kms/docs/key-rotation).

## Creating a key and granting permissions

The following instructions explain how to create a key for an instance and grant permissions to encrypt and decrypt instance data with the key.

  1. In the Google Cloud project where you want to manage your keys:

     1. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

     2. Create a key ring using the [`projects.locations.keyRings.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create) method. The Cloud KMS [key ring location](https://docs.cloud.google.com/kms/docs/locations) must match the [location](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations) of the instance that you encrypt.

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

     3. Create a key using the [`projects.locations.keyRings.cryptoKeys`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method.

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

  2. If you have not created an AML AI instance in the AML AI project, then the AML AI service account doesn't exist yet. Create the service account.

Before using any of the command data below, make the following replacements: 

     * `PROJECT_ID`: the Google Cloud project ID for the project where AML AI is running 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta services identity create --service=financialservices.googleapis.com --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta services identity create --service=financialservices.googleapis.com --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta services identity create --service=financialservices.googleapis.com --project=PROJECT_ID

You should receive a response similar to the following:
    
    Service identity created: service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com

  3. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the AML AI service account. Grant this permission on the key you created.

Before using any of the command data below, make the following replacements: 

     * `PROJECT_ID`: the Google Cloud project ID for the project where AML AI is running 
     * `KEY_ID`: the user-defined identifier for the key
     * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

       * `us-central1`
       * `us-east1`
       * `europe-west2`
       * `europe-west6`
     * `KEY_RING_ID`: a user-defined identifier for the key ring
     * `PROJECT_NUMBER`: the Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for the project where AML AI is running 

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud kms keys add-iam-policy-binding KEY_ID --project=PROJECT_ID \
      --location LOCATION --keyring=KEY_RING_ID \
      --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com \
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud kms keys add-iam-policy-binding KEY_ID --project=PROJECT_ID `
      --location LOCATION --keyring=KEY_RING_ID `
      --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com `
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud kms keys add-iam-policy-binding KEY_ID --project=PROJECT_ID ^
      --location LOCATION --keyring=KEY_RING_ID ^
      --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com ^
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter

You should receive a response similar to the following:
    
    Updated IAM policy for key KEY_ID.
    bindings:
    - members:
      - serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com
      role: roles/cloudkms.cryptoKeyEncrypterDecrypter
    etag: BwYCq0Sq4Ho=
    version: 1
    

For more information about this command see the [gcloud kms keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) documentation.




You can now [create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances) and specify the key to use for encryption.

## Removing access

There are several ways to remove access to the key from the CMEK-encrypted instance:

  * Revoke the Cloud KMS CryptoKey Encrypter/Decrypter [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) from the **AML AI service account** using the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-gcloud-manual)
  * [Temporarily disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) the CMEK key
  * [Permanently destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) the CMEK key



We recommend that you revoke the permissions from the AML AI service account before disabling or destroying a key. Changes to permissions are propagated within seconds, so you can observe the impacts of disabling or destroying a key.

When you disable or destroy the encryption key for an instance, you lose the ability to use or retrieve customer data associated with the instance. All customer data stored in the instance becomes inaccessible, including models, engine configs, backtest results, and prediction results. Users with any AML AI viewer [role](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control#roles) can still view fields such as the instance name or the other resource fields returned by retrieving AML AI resources.

Any operations which use or export customer data, for example exporting `backtestResults` metadata, will fail.

Users with the AML AI Administrator [role](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control#roles) or Owner role can delete the instance.

## CMEK organization policies

AML AI does not support [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy). However, AML AI always requires the use of CMEK, regardless of the `constraints/gcp.restrictNonCmekServices` organization policy.

## Interaction with VPC-SC

If you have configured AML AI inside a VPC-SC perimeter, the CMEK key must still be accessible to the service account. If the key is not inside the same VPC-SC perimeter, there are multiple ways to achieve this, including:

  * Use an egress rule to allowlist the resource
  * Use VPC perimeter peering



## What's next?

  * [Create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance)
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
