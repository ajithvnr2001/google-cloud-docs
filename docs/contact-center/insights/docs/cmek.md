---
url: https://docs.cloud.google.com/contact-center/insights/docs/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:38:00.697663+00:00
---

# Customer-managed encryption keys (CMEK)  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Customer Experience Insights encrypts customer content at rest. CX Insights handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including CX Insights. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your CX Insights resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Protected data

All Insights [at-rest](https://en.wikipedia.org/wiki/Data_at_rest) data in a supported location can be protected with CMEKs.

You must enable CMEK for your project before you add Customer Experience Agent Studio conversations. To enable CMEK for a project with existing conversations, you must delete both the CX Agent Studio apps and the conversations. CX Insights retains deleted conversations for 7 days, before you can enable CMEK on your existing project.

## Supported Locations

CMEK is available in all Insights [locations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization#available_regions) except `global`.

## Limitations

For features involving data egress to customer-owned instances of another Google Cloud product, configure CMEK in the corresponding Google Cloud products.

  * Upload audio with transcription: enable CMEK in [Cloud Speech-to-Text](https://docs.cloud.google.com/speech-to-text/v2/docs/encryption#cmek-supported_resources)
  * Export conversation to BigQuery: enable CMEK on BigQuery table [BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption)



## Create keys

To create keys, you use the KMS service. For instructions, see [Creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys). When creating or choosing a key, you must configure the following:

  * Be sure to select the [location](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization#available_regions) that you use for your Insights data, otherwise, requests will fail.



## Enable CMEK in Insights

Before you create any Insights data in a specific location, you can specify whether the data in this location will be protected by a customer-managed key (i.e. enable CMEK). Configure your key at this time. 

**Warning:** You **cannot change** encryption key settings for a location after that location has been enabled for CMEK. If you already have CX Insights data for a Google Cloud project, then you cannot configure a customer-managed key for that project.

### Prerequisites

  1. Create an Insights service account for your project with Google Cloud. For more information, see [Google Cloud services identity documentation](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).
         
         gcloud beta services identity create --service=contactcenterinsights.googleapis.com --project=PROJECT_ID
         

  2. Grant the CCAI CMEK service agent the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role for your encryption key to ensure that the service agent will have permissions to encrypt and decrypt with your key. The email address for the service agent is: 
         
         service-PROJECT_NUMBER@gcp-sa-ccai-cmek.iam.gserviceaccount.com




### Configure a key for an Insights location

  1. Use InitializeEncryptionSpec API to configure the key.

You will need to provide the following variables:

     * `PROJECT_ID`: your Google Cloud project ID
     * `LOCATION_ID`: the location you chose to enable CMEK in Insights.
     * `KMS_KEY_NAME`: the name of your KMS key that will be used to encrypt or decrypt Insights data in the selected location. 
       * The location in the KMS key name (e.g. `projects/<project_id>/locations/<location_id>/keyRings/<key_ring>/cryptoKeys/<key_name>`) has to match the selected location that you want to enable CMEK.
       * You need to grant the access to this key in [prerequisites](https://docs.cloud.google.com/gemini-enterprise-cx/insights/cmek#prerequisites) step 2.

For example:
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d '{ encryption_spec: { kms_key: "KMS_KEY_NAME" } }' \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec:initialize"
    

You should receive a JSON response similar to the following:
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

  2. Use GetOperation API to check the long-running operation result.

For example:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \ 
             "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
         




## Check CMEK Settings

Use GetEncryptionSpec API to check the encryption key configured for a location.

For example:
    
    
      curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec"
    

## Revoke keys

To revoke Insights access to the key, you could [disable the KMS key version](https://docs.cloud.google.com/kms/docs/iam#revoking_access_to_a_resource) or [remove](https://docs.cloud.google.com/kms/docs/iam#revoking_access_to_a_resource) the service account's [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role from the KMS key.

**Warning:** If you have revoked the key for more than 30 days, the Insights data encrypted by that key will be lost.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
