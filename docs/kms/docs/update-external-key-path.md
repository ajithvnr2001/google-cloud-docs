---
url: https://docs.cloud.google.com/kms/docs/update-external-key-path/
title: Update external key reference \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:22.069431+00:00
---

# Update external key reference  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/update-external-key-path/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Update external key reference Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to update the external key reference for a Cloud EKM key without rotating the key. The new key reference must point to the same key material as the current key reference. If the key material has been rotated in the external key management partner system, you must rotate the key instead.

Use the instructions on this page if your external key management partner system has changed the key reference for an existing key. For example, the key reference can change as a result of a change to the hostname of the external key management partner or a change in their key reference structure.

## Required roles

To get the permission that you need to update an external key reference, ask your administrator to grant you the [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on your key. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `cloudkms.cryptoKeyVersions.update` permission, which is required to update an external key reference. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update the URI for a key version without rotation

To update the key reference for a Cloud EKM key that you use over the internet, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring, and then select the key and version.

  3. Click _more_vert_ **More** , and then click **View key URI**.

  4. Click **Update key URI**.

  5. Enter the new key URI, and then click **Save**.




###  gcloud 

To update the URI for the key version, use the `gcloud kms versions update` command:
    
    
    gcloud kms keys versions update KEY_VERSION \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION \
      --external-key-uri NEW_KEY_URI
    

Replace the following:

  * `KEY_VERSION`: the key version number.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `NEW_KEY_URI`: the new URI for the existing external key material.



## Update the key path for a key version without rotation

To update the key reference for a Cloud EKM key that you use over a VPC network, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring, and then select the key and version.

  3. Click **More** _more_vert_ then **View key path**.

  4. Click **Update key path**.

  5. Enter the new key path, then click **Save**.




###  gcloud 

To update the key path of the key version, use the `gcloud kms versions update` command:
    
    
    gcloud kms keys versions update KEY_VERSION \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION \
      --ekm-connection-key-path NEW_KEY_PATH
    

Replace the following:

  * `KEY_VERSION`: the key version number.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `NEW_KEY_PATH`: the new path for the existing external key material.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
