---
url: https://docs.cloud.google.com/kms/docs/create-encryption-keys/
title: Quickstart: Create encryption keys with Cloud KMS \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:36.108127+00:00
---

# Quickstart: Create encryption keys with Cloud KMS  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/create-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create encryption keys with Cloud KMS

This quickstart shows you how to create and use encryption keys with Cloud Key Management Service in a project you own. These instructions use the Google Cloud console to create key rings, keys, and key versions in Cloud KMS. For instructions that use other methods, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview), [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring), and [Create a key](https://docs.cloud.google.com/kms/docs/create-key).

This quickstart uses the command line to send requests to the Cloud KMS API. For programming examples that use the client libraries to send requests to the Cloud KMS API, see [Encrypting and Decrypting](https://docs.cloud.google.com/kms/docs/encrypt-decrypt).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud KMS API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudkms.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/cloudkms.admin, roles/cloudkms.cryptoKeyEncrypterDecrypter`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud KMS API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudkms.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/cloudkms.admin, roles/cloudkms.cryptoKeyEncrypterDecrypter`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.


**Note:** This quickstart creates Cloud KMS resources such as key rings and keys. Key rings and keys can't be renamed after they're created, and you can't reuse the names of deleted keys.

## Key rings and keys

To encrypt and decrypt content you will need a Cloud KMS key, which is part of a key ring.

Create a key ring named `test`, and a key named `quickstart`. Refer to the [object hierarchy overview](https://docs.cloud.google.com/kms/docs/object-hierarchy) for more information about these objects and how they are related.
    
    
    gcloud kms keyrings create "test" \
        --location "global"
    
    
    gcloud kms keys create "quickstart" \
        --location "global" \
        --keyring "test" \
        --purpose "encryption"

You can use the `list` option to view the name and metadata for the key that you just created.
    
    
    gcloud kms keys list \
        --location "global" \
        --keyring "test"

You should see:
    
    
    NAME                                                                      PURPOSE          PRIMARY_STATE
    projects/PROJECT_ID/locations/global/keyRings/test/cryptoKeys/quickstart  ENCRYPT_DECRYPT  ENABLED
    

## Encrypt data

Now that you have a key, you can use that key to encrypt text or binary content.

Store some text to be encrypted in a file called "mysecret.txt".
    
    
    echo -n "Some text to be encrypted" > mysecret.txt

To encrypt the data with `gcloud kms encrypt`, provide your key information, specify the name of the plaintext file to encrypt, and specify the name of the file that will contain the encrypted content:
    
    
    gcloud kms encrypt \
        --location "global" \
        --keyring "test" \
        --key "quickstart" \
        --plaintext-file ./mysecret.txt \
        --ciphertext-file ./mysecret.txt.encrypted

The `encrypt` method saves your encrypted content in the file specified by the `--ciphertext-file` flag.

## Decrypt ciphertext

To decrypt the data with `gcloud kms decrypt`, provide your key information, specify the name of the encrypted file (ciphertext file) to decrypt, and specify the name of the file that will contain the decrypted content:
    
    
    gcloud kms decrypt \
        --location "global" \
        --keyring "test" \
        --key "quickstart" \
        --ciphertext-file ./mysecret.txt.encrypted \
        --plaintext-file ./mysecret.txt.decrypted

The `decrypt` method saves your decrypted content in the file specified by the `--plaintext-file` flag.

To decrypt encrypted content, you must use the same key that was used to encrypt the content.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

List the versions available for your key:
    
    
    gcloud kms keys versions list \
        --location "global" \
        --keyring "test" \
        --key "quickstart"

To destroy a version, run the following command, where `1` is the number of the key version that you want to destroy:

**Important:** When you destroy a key version, you can no longer decrypt content that was encrypted using that version of the key. Make sure that you no longer need a key version before you destroy it.
    
    
    gcloud kms keys versions destroy 1 \
        --location "global" \
        --keyring "test" \
        --key "quickstart"
    

## What's next

  * Start [using the API](https://docs.cloud.google.com/kms/docs/accessing-the-api).
  * Take a look at the [API Reference](https://docs.cloud.google.com/kms/docs/reference/rest).
  * Learn more about how to [encrypt data at rest](https://codelabs.developers.google.com/codelabs/encrypt-and-decrypt-data-with-cloud-kms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
