---
url: https://docs.cloud.google.com/kms/docs/getting-resource-ids/
title: Getting a Cloud KMS resource ID \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:20.092134+00:00
---

# Getting a Cloud KMS resource ID  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/getting-resource-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Getting a Cloud KMS resource ID Stay organized with collections  Save and categorize content based on your preferences. 

When you refer to a Cloud Key Management Service resource using the Cloud KMS API or Google Cloud CLI, you use the resource ID. For example, you can use the resource ID of a key ring to grant an [Identity and Access Management (IAM) role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) on that key ring. This topic shows how to get the ID for a key ring, a key, and a key version.

## Getting the resource ID for a key ring

###  Console 

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click **More** _more_vert_ for the key ring.

  3. Click **Copy resource name**. The resource ID for the key ring is copied to your clipboard.




###  gcloud 

List all key rings in a location:
    
    
    gcloud kms keyrings list --location LOCATION
    

The **Name** column of the output includes the resource ID for each key ring. For example:
    
    
    projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING
    

## Getting the ID for a key and version

###  Console 

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring that contains the key.

  3. For the key whose resource ID you are retrieving, click **More** _more_vert_.

  4. Click **Copy resource name**. The resource ID for the key is copied to your clipboard. Its format is similar to the following:
         
         projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
         

  5. A key contains zero or more key versions. The resource ID for a key version is the key ID, plus a slash (`/`), plus the version ID. To list all versions for a key, click the key's name. Click the **More** icon for the version, and click **Copy resource name**.




###  gcloud 

List all keys on a given key ring:
    
    
    gcloud kms keys list --keyring KEY_RING --location LOCATION
    

The **Name** column of the output includes the resource ID for each key. For example:
    
    
    projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

A key has zero or more key versions. The resource ID for a key version is the key ID, plus a slash (`/`), plus the version ID. To list all versions for a key:
    
    
    gcloud kms keys versions list --location LOCATION --keyring KEY_RING --key KEY_NAME
    

The **Name** column of the output includes the resource ID for each key version. For example:
    
    
    projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/2
    

## What's next

  * Learn more about [permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) in Cloud KMS.
  * [Manage access to Cloud KMS resources](https://docs.cloud.google.com/kms/docs/iam).
  * [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
