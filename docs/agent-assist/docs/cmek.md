---
url: https://docs.cloud.google.com/agent-assist/docs/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:35:20.655568+00:00
---

# Customer-managed encryption keys (CMEK)  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Agent Assist encrypts customer content at rest. Agent Assist handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Agent Assist. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Agent Assist resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Protected data

Only Conversation data [at-rest](https://en.wikipedia.org/wiki/Data_at_rest) in a supported location can be protected with CMEKs.

## Supported locations and features

CMEK is available in all Agent Assist [locations](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization#available_regions) and for all Agent Assist [features](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization#available_features_for_regional_serving) in supported locations, including generative AI features.

## Limitations

CMEK is not available for features that are disabled in Agent Assist locations and smart reply.

## Create keys

To create keys, you use the KMS service. For instructions, see [Creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys). When creating or choosing a key, you must configure the following:

  * Be sure to select the [location](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization#available_regions) that you use for your Agent Assist data, otherwise, requests will fail.



## Enable CMEK in Agent Assist

Before you create any Agent Assist data in a specific location, you can specify whether the data in this location will be protected by a customer-managed key. Configure your key at this time.

**Warning:** You **cannot change** encryption key settings for a location once it has been specified. If you already have Agent Assist data for a Google Cloud project in a location, you won't be be able to add a CMEK key given this location.

### Prerequisites

  1. Create the CCAI CMEK Service account for your project with Google Cloud CLI. For more information, see [gcloud services identity documentation](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).
         
         gcloud beta services identity create --service=dialogflow.googleapis.com --project=PROJECT_ID

The service account will be created. It won't be returned in the create response, but will have the following format:
         
         service-PROJECT_NUMBER@gcp-sa-ccai-cmek.iam.gserviceaccount.com

  2. Grant the CCAI CMEK Service account the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role to ensure that the service has permissions to encrypt and decrypt with your key.
         
         gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
         --project=PROJECT_ID \
         --location=LOCATION_ID \
         --keyring=KMS_KEY_RING \
         --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-ccai-cmek.iam.gserviceaccount.com \
         --role=roles/cloudkms.cryptoKeyEncrypterDecrypter




### Configure a key for an Agent Assist location

  1. Use InitializeEncryptionSpec API to configure the key.

You will need to provide the following variables:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `LOCATION_ID`: The location you chose to enable CMEK in Agent Assist.
     * `KMS_KEY_RING`: The key ring your KMS key was created in. (The location in the key ring, like `projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING`, must match the location where you're enabling CMEK.)
     * `KMS_KEY_ID`: The name of your KMS key that will be used to encrypt and decrypt Agent Assist data in the selected location.

For example:
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "{ encryption_spec: { kms_key: 'projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING/cryptoKeys/KMS_KEY_ID' } }" \
        "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec:initialize"

You should receive a JSON response similar to the following:
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
    }

  2. Use GetOperation API to check the long-running operation result.

For example: 
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"




## Check CMEK Settings

Use GetEncryptionSpec API to check the encryption key configured for a location.

For example:
    
    
        curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec"
      

## Revoke keys

To revoke Agent Assist access to the key, you could [disable the KMS key version](https://docs.cloud.google.com/kms/docs/iam#revoking_access_to_a_resource) or [remove](https://docs.cloud.google.com/kms/docs/iam#revoking_access_to_a_resource) the service account's [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role from the KMS key.

After key revocation the encrypted data will become inaccessible to Agent Assist and the service will no longer be in an operational state until the key permissions are reinstated.

**Warning:** If you have revoked the key for more than 30 days, the Agent Assist data encrypted by that key will be lost.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
