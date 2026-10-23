---
url: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-hsm/
title: Configure Key Access Justifications with Cloud HSM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:16.146638+00:00
---

# Configure Key Access Justifications with Cloud HSM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-hsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management)
  * [ Key Access Justifications ](https://docs.cloud.google.com/assured-workloads/key-access-justifications)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Key Access Justifications with Cloud HSM

This page describes how to configure Key Access Justifications with Cloud HSM for Assured Workloads' [Japan Regions control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages#jp-regions).

During the steps to [create a new Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) for Japan Regions, you have the option of creating a new project and a key ring for your cryptographic keys. [Cloud HSM keys](https://docs.cloud.google.com/kms/docs/hsm) keys can be added to this key ring, and you can also configure a Key Access Justifications policy to control access to each key.

## Before you begin

  * The ability to use Key Access Justifications with Cloud HSM keys is only available for the Japan Regions control package in Assured Workloads.
  * Ensure that your administrator has granted you one of the required Identity and Access Management (IAM) roles to create and manage both your Key Access Justifications policies and the Cloud HSM keys themselves.



### Required IAM permissions

To get the permissions that you need to create and manage Cloud HSM keys and their Key Access Justifications policies, ask your administrator to grant you the [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on the project containing the key ring. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage Cloud HSM keys and their Key Access Justifications policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage Cloud HSM keys and their Key Access Justifications policies:

  * `cloudkms.cryptoKeys.create`
  * `cloudkms.cryptoKeys.update`
  * `cloudkms.cryptoKeys.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** The **Cloud KMS Admin** role contains permissions for key maintenance and key version destruction. To protect your Cloud KMS resources, this role should only be assigned to individuals responsible for key administration.

## Configure a Cloud HSM key with Key Access Justifications

To configure Key Access Justifications with a Cloud HSM key, you can either include the key access policy as a parameter when you create the key, or you can update the key with the policy after the key has been created.

### Create a new key and policy

### REST

Create a new key and policy using the [`cryptoKeys.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method:
    
    
    POST https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys?crypto_key_id=KEY_NAME

In the request, replace the following placeholder values:

  * PROJECT_ID: The project ID that contains the key ring on which you want to add a key—for example, `919698201234`.
  * LOCATION: The location of the key ring—for example, `us-west1`.
  * KEY_RING: The name of the key ring that you specified when you created your Assured Workloads folder's key management project and key ring—for example, `my-key-ring`.
  * KEY_NAME: The name of the HSM key you want to create—for example, `my-hsm-key`.



Request body: 
    
    
    {
      "purpose": "PURPOSE",
      "versionTemplate": {
        "protectionLevel": "HSM",
        "algorithm": "ALGORITHM"
      },
      "keyAccessJustificationsPolicy": {
        "allowedAccessReasons": [
          ALLOWED_ACCESS_REASONS
        ]
      }
    }

In the request body, replace the following placeholder values:

  * PURPOSE: The purpose for the key. For a list of different key purposes, see [Key purposes](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes)—for example, `ENCRYPT_DECRYPT`.
  * ALGORITHM: The cryptographic algorithm to use. For a list of available algorithms, see [Cloud KMS algorithms](https://docs.cloud.google.com/kms/docs/algorithms)—for example, `GOOGLE_SYMMETRIC_ENCRYPTION`.
  * ALLOWED_ACCESS_REASONS: The Key Access Justifications policy that defines zero or more allowed [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes) for accessing the encryption key—for example, `["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]`.



The following example request and request body only allows access justifications for a few reasons:
    
    
    POST https://cloudkms.googleapis.com/v1/projects/919698201234/locations/us-west1/keyRings/my-key-ring/cryptoKeys?crypto_key_id=my-hsm-key
    
    
    {
      "purpose": "ENCRYPT_DECRYPT",
      "versionTemplate": {
        "protectionLevel": "HSM",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION"
      },
      "keyAccessJustificationsPolicy": {
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }

### Update an existing key's policy

### REST

Update an existing key in Cloud KMS using the [`cryptoKeys.patch`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch) method:
    
    
    PATCH https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME?update_mask=keyAccessJustificationsPolicy

In the request, replace the following placeholder values:

  * PROJECT_ID: The project ID of the project that contains the key ring for the key—for example, `919698201234`.
  * LOCATION: The location of the key ring—for example, `us-west1`.
  * KEY_RING: The name of the key ring that you specified when you created your Assured Workloads folder's key management project and key ring—for example, `my-key-ring`.
  * KEY_NAME: The name of the HSM key you want to update—for example, `my-hsm-key`.



Request body: 
    
    
    {
      "purpose": "PURPOSE",
      "versionTemplate": {
        "protectionLevel": "HSM",
        "algorithm": "ALGORITHM"
      },
      "keyAccessJustificationsPolicy": {
        "allowedAccessReasons": [
          ALLOWED_ACCESS_REASONS
        ]
      }
    }

In the request body, replace the following placeholder values:

  * PURPOSE: The purpose for the key. For a list of different key purposes, see [Key purposes](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes)—for example, `ENCRYPT_DECRYPT`.
  * ALGORITHM: The cryptographic algorithm to use. For a list of available algorithms, see [Cloud KMS algorithms](https://docs.cloud.google.com/kms/docs/algorithms)—for example, `GOOGLE_SYMMETRIC_ENCRYPTION`.
  * ALLOWED_ACCESS_REASONS: The Key Access Justifications policy that defines zero or more allowed [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes) for accessing the encryption key—for example, `["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]`.



The following example request and request body only allows access justifications for a few reasons:
    
    
    PATCH https://cloudkms.googleapis.com/v1/projects/919698201234/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-hsm-key?keyAccessJustificationsPolicy
    
    
    {
      "purpose": "ENCRYPT_DECRYPT",
      "versionTemplate": {
        "protectionLevel": "HSM",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION"
      },
      "keyAccessJustificationsPolicy": {
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }

### Get the Key Access Justifications policy for a key

### REST

Get metadata about an existing key in Cloud KMS using the [`cryptoKeys.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/get) method:
    
    
    GET https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME

In the request parameters, replace the following placeholder values with your own:

  * PROJECT_ID: The project ID that contains the key ring for the key—for example, `919698201234`.
  * LOCATION: The location of the key ring—for example, `us-west1`.
  * KEY_RING: The name of the key ring that you specified when you created your Assured Workloads folder's key management project and key ring—for example, `my-key-ring`.
  * KEY_NAME: The name of the HSM key you want to get—for example, `my-hsm-key`.



The following example request gets metadata about a key in Cloud KMS: 
    
    
    GET https://cloudkms.googleapis.com/v1/projects/919698201234/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-hsm-key

The response body contains metadata about your key, including the [`keyAccessJustificationsPolicy`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys). For example:
    
    
    {
      "purpose": "ENCRYPT_DECRYPT",
      "versionTemplate": {
        "protectionLevel": "HSM",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION"
      },
      "keyAccessJustificationsPolicy": {
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }

## What's next

  * You can also [Set default Key Access Justifications policy](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/set-default-policy) ([Preview](https://cloud.google.com/products#product-launch-stages)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
