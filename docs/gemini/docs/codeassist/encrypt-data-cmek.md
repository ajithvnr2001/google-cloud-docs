---
url: https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek/
title: Encrypt data with customer-managed encryption keys \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:48.240027+00:00
---

# Encrypt data with customer-managed encryption keys  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/encrypt-data-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Encrypt data with customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to use customer-managed encryption keys (CMEK) to encrypt and control data-at-rest in a cloud service through [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). CMEK is integrated with [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) for Gemini Code Assist. Gemini Code Assist doesn't support the use of [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) keys.

In this document, you do the following:

  * Learn how to create a CMEK.
  * Grant permissions to the Gemini Code Assist service account.
  * Create a code repository index with a CMEK.
  * Remove access to a CMEK repository.



By default, code customization for Gemini Code Assist encrypts customer content at rest. code customization handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including code customization. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your code customization resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Before you begin

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In the development environment where you set up the gcloud CLI, run the [`gcloud components update` command](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) to make sure that you have updated all installed components of the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to the latest version.
         
         gcloud components update
         




## Create a CMEK and grant permissions

To create a CMEK and grant the Gemini Code Assist service account permissions on the key, perform the following tasks:

  1. In the Google Cloud project where you want to manage your keys, do the following:

     1. [Enable the Cloud Key Management Service API](https://console.cloud.google.com/flows/enableapi?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

     2. Create the [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key) directly in Cloud KMS.

  2. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Gemini Code Assist service account. Grant this permission on the key that you created.

###  Console 

     1. Go to **Key management**.

[Go to Key management](https://console.cloud.google.com/security/kms)

     2. Select the key that you created.

     3. Grant access to the Gemini Code Assist service account:

        1. Click **Add principal**.
        2. Add the Gemini Code Assist service account. The service account is `service-PROJECT_NUMBER@gcp-sa-cloudaicompanions.iam.gserviceaccount.com`, where PROJECT_NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Gemini Code Assist is enabled.
        3. In **Select a role** , select **Cloud KMS** > **Cloud KMS CryptoKey Encrypter/Decrypter**.
        4. Click **Save**.
     4. Repeat the previous step to grant access to the account that will create the code repository index with a CMEK.

     5. Return to the **[Key management](https://console.cloud.google.com/security/kms)** page and select the key again.

     6. Select **Show info panel**. You should see roles in the **Role/Member** column.

###  gcloud CLI 

     1. To grant access to the Gemini Code Assist service account, in a shell environment, use the [`kms keys add-iam-policy-binding`command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
                --project=PROJECT_ID \
                --location=LOCATION \
                --keyring=KEYRING_NAME \
                --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudaicompanion.iam.gserviceaccount.com" \
                --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
            

Replace the following:

        * KEY_NAME: the key name.
        * PROJECT_ID: the ID of the project that contains the key.
        * LOCATION: the key location.
        * KEYRING_NAME: the key ring name.
        * PROJECT_NUMBER: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project with Gemini Code Assist enabled.
     2. Repeat the previous step to grant access to the account that will create the code repository index with a CMEK.

For more information about this command, see the [`gcloud kms keys add-iam-policy-binding` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding).




You can now create a code repository index with a CMEK using the API, and specify the key to use for encryption.

## Create a code repository index with a CMEK

To create a new repository that has CMEK protection, do one of the following:

###  gcloud CLI 

Use the [`gemini code-repository-indexes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/create):
    
    
    gcloud gemini code-repository-indexes create CODE_REPOSITORY_INDEX_NAME \
        --location=LOCATION \
        --kms-key="projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME"
    

Replace the following:

  * CODE_REPOSITORY_INDEX_NAME: the name of the new code repository index that you'll create.
  * LOCATION: the key location.
  * KEY_PROJECT_ID: the key project ID.
  * KEYRING_NAME: the key ring name.
  * KEY_NAME: the key name.



###  API 

  1. Create a JSON file that contains the following information:
         
         {
             "kmsKey": "projects/KEY_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME"
           }
         

Replace the following:

     * `KEY_PROJECT_ID`: the key project ID
     * `KEY_LOCATION`: the key location
     * `KEYRING_NAME`: the key ring name
     * `KEY_NAME`: the key name
  2. Use a [`cURL`](http://curl.haxx.se/) command to call the [`projects.locations.codeRepositoryIndexes.create` method](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes/create):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://cloudaicompanion.googleapis.com/v1/projects/PROJECT_ID/locations/KEY_LOCATION/codeRepositoryIndexes?codeRepositoryIndexId=CODE_REPOSITORY_INDEX_NAME"

Replace the following:

     * `JSON_FILE_NAME`: the path for the JSON file that you created in the preceding step.
     * `PROJECT_ID`: the ID of the project to create the repository in.
     * `KEY_LOCATION`: the location to create the repository in, which must match the location where the CMEK exists.
     * `CODE_REPOSITORY_INDEX_NAME`: the name of the new code repository index that you'll create. For example, `zg-btf-0001`.



The response returns a set of log entries.

## Remove access to a CMEK repository

**Warning:** If you disable the CMEK, Google Cloud removes the instance and the service will no longer be available, even if you re-enable the key.

There are several ways to remove access to a CMEK-encrypted repository:

  * Revoke the Cloud KMS CryptoKey Encrypter/Decrypter [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) from the Gemini Code Assist service account using the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-gcloud-manual).
  * [Temporarily disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) the CMEK.
  * [Permanently destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) the CMEK.



We recommend that you revoke the permissions from the Gemini Code Assist service account before disabling or destroying a key. Changes to permissions are consistent within seconds, so you can observe the impacts of disabling or destroying a key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
