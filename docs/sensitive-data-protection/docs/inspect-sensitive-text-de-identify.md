---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify/
title: De-identify and re-identify sensitive data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:43.481471+00:00
---

# De-identify and re-identify sensitive data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# De-identify and re-identify sensitive data

This document shows you how to use Sensitive Data Protection to de-identify and re-identify sensitive data in text content. In the process, it guides you through creating a wrapped key using Cloud Key Management Service. You need this key in your de-identify and re-identify requests. 

The process described in this document is called _pseudonymization_ (or _tokenization_). In this process, Sensitive Data Protection uses a cryptographic key to convert (de-identify) sensitive text into a token. To restore (re-identify) that text, you need the cryptographic key used during de-identification and the token.

Sensitive Data Protection supports both reversible and non-reversible cryptographic methods. To re-identify content, you need to choose a reversible method.

The cryptographic method described here is called [deterministic encryption using AES-SIV](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#aes-siv) (Advanced Encryption Standard in Synthetic Initialization Vector mode). We recommend this method, because it provides the highest level of security among all the reversible cryptographic methods that Sensitive Data Protection [supports](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#supported-methods).

You can complete the steps in this document in 10 to 20 minutes, excluding the [Before you begin](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#before-you-begin) steps.

**Note:** When you use Cloud KMS for cryptographic operations, [charges apply](https://cloud.google.com/kms/pricing). In addition, when you use a [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) key or a [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) key, you consume Cloud KMS quota on the project that contains the key. In contrast, if you're using a software Cloud KMS key with Sensitive Data Protection, no quota values apply. For more information, see [Quotas](https://docs.cloud.google.com/kms/quotas) in the Cloud KMS documentation.

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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Sensitive Data Protection and Cloud KMS APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dlp.googleapis.com cloudkms.googleapis.com

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

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Sensitive Data Protection and Cloud KMS APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dlp.googleapis.com cloudkms.googleapis.com




### Required roles

To get the permissions that you need to create a wrapped AES key, de-identify sensitive data, and re-identify it, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`)
  * [Cloud KMS CryptoKey Encrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypter) (`roles/cloudkms.cryptoKeyEncrypter`)
  * [DLP User ](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.user) (`roles/dlp.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a key ring and a key

Before you start this procedure, decide where you want Sensitive Data Protection to process your de-identification and re-identification requests. When you create a Cloud KMS key, you must store it in either `global` or in the same region that you will use for your Sensitive Data Protection requests. Otherwise, the Sensitive Data Protection requests will fail.

You can find a list of supported locations in [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). Note the name of your chosen region (for example, `us-west1`).

This procedure uses `global` as the location for all API requests. If you want to use a different region, replace `global` with the region name.

  1. Create a key ring:
         
         gcloud kms keyrings create "dlp-keyring" \
             --location "global"
         

  2. Create a key:
         
         gcloud kms keys create "dlp-key" \
             --location "global" \
             --keyring "dlp-keyring" \
             --purpose "encryption"
         

  3. List your key ring and key:
         
         gcloud kms keys list \
             --location "global" \
             --keyring "dlp-keyring"
         

You get the following output:
         
         NAME: projects/<var>PROJECT_ID</var>/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key
         PURPOSE: ENCRYPT_DECRYPT
         ALGORITHM: GOOGLE_SYMMETRIC_ENCRYPTION
         PROTECTION_LEVEL: SOFTWARE
         LABELS:
         PRIMARY_ID: 1
         PRIMARY_STATE: ENABLED
         

In this output, `PROJECT_ID` is the ID of your project.

The value of `NAME` is the full resource name of your Cloud KMS key. Note this value because the de-identify and re-identify requests require it.




## Create a base64-encoded AES key

This section describes how to create an Advanced Encryption Standard (AES) key and encode it in base64 format.

**Note:** These steps use the `openssl` and `base64` commands, but there are [many other ways](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys#generate-csek) to perform this task.

  1. Create a 128-, 192-, or 256-bit AES key. The following command uses `openssl` to create a 256-bit key in the current directory:
         
         openssl rand -out "./aes_key.bin" 32
         

The file `aes_key.bin` is added to your current directory.

  2. Encode the AES key as a base64 string:
         
         base64 -i ./aes_key.bin
         

You get an output similar to the following:
         
         uEDo6/yKx+zCg2cZ1DBwpwvzMVNk/c+jWs7OwpkMc/s=
         

**Warning:** Don't use this example key to protect actual sensitive workloads. This key is provided only to serve as an example. Because it's shared here, this key is not safe to use.



## Wrap the AES key using the Cloud KMS key

This section describes how to use the Cloud KMS key that you created in Create a key ring and a key to wrap the base64-encoded AES key that you created in Create a base64-encoded AES key.

To wrap the AES key, use `curl` to send the following request to the Cloud KMS API [`projects.locations.keyRings.cryptoKeys.encrypt`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key:encrypt" \
        --request "POST" \
        --header "Authorization:Bearer $(gcloud auth application-default print-access-token)" \
        --header "content-type: application/json" \
        --data "{\"plaintext\": \"BASE64_ENCODED_AES_KEY\"}"
    

Replace the following:

  * `PROJECT_ID`: the [ID of your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
  * `BASE64_ENCODED_AES_KEY`: the base64-encoded string returned in Create a base64-encoded AES key.



The response that you get from Cloud KMS is similar to the following JSON:
    
    
    {
      "name": "projects/<var>PROJECT_ID</var>/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key/cryptoKeyVersions/1",
      "ciphertext": "CiQAYuuIGo5DVaqdE0YLioWxEhC8LbTmq7Uy2G3qOJlZB7WXBw0SSQAjdwP8ZusZJ3Kr8GD9W0vaFPMDksmHEo6nTDaW/j5sSYpHa1ym2JHk+lUgkC3Zw5bXhfCNOkpXUdHGZKou1893O8BDby/82HY=",
      "ciphertextCrc32c": "901327763",
      "protectionLevel": "SOFTWARE"
    }
    

In this output, `PROJECT_ID` is the ID of your project.

Note the value of `ciphertext` in the response. That is your wrapped key.

## Send a de-identify request to the DLP API

This section describes how to de-identify sensitive data in text content.

To complete this task, you need the following:

  * The full resource name of the Cloud KMS key that you created in [Create a key ring and a key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#create-kms-key).
  * The wrapped key that you created in [Wrap the AES key using the Cloud KMS key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#wrap-aes-key).



You must save the sample request in a JSON file. If you use Cloud Shell, use the Cloud Shell Editor to create the file. To launch the editor, click  edit **Open Editor** launch on the Cloud Shell toolbar.

To de-identify sensitive data in text content, follow these steps:

  1. Create a JSON request file called `deidentify-request.json` with the following text.
         
         {
           "item": {
             "value": "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
           },
           "deidentifyConfig": {
             "infoTypeTransformations": {
               "transformations": [
                 {
                   "infoTypes": [
                     {
                       "name": "EMAIL_ADDRESS"
                     }
                   ],
                   "primitiveTransformation": {
                     "cryptoDeterministicConfig": {
                       "cryptoKey": {
                         "kmsWrapped": {
                           "cryptoKeyName": "projects/PROJECT_ID/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key",
                           "wrappedKey": "WRAPPED_KEY"
                         }
                       },
                       "surrogateInfoType": {
                         "name": "EMAIL_ADDRESS_TOKEN"
                       }
                     }
                   }
                 }
               ]
             }
           },
           "inspectConfig": {
             "infoTypes": [
               {
                 "name": "EMAIL_ADDRESS"
               }
             ]
           }
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `WRAPPED_KEY`: the wrapped key that you created in [Wrap the AES key using the Cloud KMS key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#wrap-aes-key).

Make sure that the resulting value of `cryptoKeyName` forms the full resource name of your Cloud KMS key.

For more information about the components of this JSON request, see [`projects.locations.content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/deidentify). After you complete this task, experiment with different inputs for this request. You can use `curl` as described here. Alternatively, use the API Explorer on that API reference page under **Try this method**.

  2. Use `curl` to make a `projects.locations.content.deidentify` request:
         
         curl -s \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/global/content:deidentify \
             -d @deidentify-request.json
         

Replace `PROJECT_ID` with the ID of your project.

To pass a filename to `curl`, use the `-d` option (for data) and precede the filename with an `@` sign. This file must be in the same directory where you run the `curl` command.

**Note:** This example request explicitly targets the `global` location. Making this request is the same as calling the [`projects.content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify) API, which defaults to the `global` location.

The response that you get from Sensitive Data Protection is similar to the following JSON:
         
         {
           "item": {
             "value": "My name is Alicia Abernathy, and my email address is EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q."
           },
           "overview": {
             "transformedBytes": "22",
             "transformationSummaries": [
               {
                 "infoType": {
                   "name": "EMAIL_ADDRESS"
                 },
                 "transformation": {
                   "cryptoDeterministicConfig": {
                     "cryptoKey": {
                       "kmsWrapped": {
                         "wrappedKey": "CiQAYuuIGo5DVaqdE0YLioWxEhC8LbTmq7Uy2G3qOJlZB7WXBw0SSQAjdwP8ZusZJ3Kr8GD9W0vaFPMDksmHEo6nTDaW/j5sSYpHa1ym2JHk+lUgkC3Zw5bXhfCNOkpXUdHGZKou1893O8BDby/82HY=",
                         "cryptoKeyName": "projects/<var>PROJECT_ID</var>/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key"
                       }
                     },
                     "surrogateInfoType": {
                       "name": "EMAIL_ADDRESS_TOKEN"
                     }
                   }
                 },
                 "results": [
                   {
                     "count": "1",
                     "code": "SUCCESS"
                   }
                 ],
                 "transformedBytes": "22"
               }
             ]
           }
         }
         

In the `item` field, the email address is replaced with a token like `EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q`. Note the value of the token in the response. To re-identify the de-identified content, you pass the entire token in the re-identify request.




## Send a re-identify request to the DLP API

This section describes how to re-identify tokenized data in text content.

To complete this task, you need the following:

  * The full resource name of the Cloud KMS key that you created in [Create a key ring and a key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#create-kms-key).
  * The wrapped key that you created in [Wrap the AES key using the Cloud KMS key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#wrap-aes-key).
  * The token that you received in Send a de-identify request to the DLP API.



To re-identify tokenized content, follow these steps:

  1. Create a JSON request file called `reidentify-request.json` with the following text.
         
         {
           "reidentifyConfig":{
             "infoTypeTransformations":{
               "transformations":[
                 {
                   "infoTypes":[
                     {
                       "name":"EMAIL_ADDRESS_TOKEN"
                     }
                   ],
                   "primitiveTransformation":{
                     "cryptoDeterministicConfig":{
                       "cryptoKey":{
                       "kmsWrapped": {
                         "cryptoKeyName": "projects/PROJECT_ID/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key",
                         "wrappedKey": "WRAPPED_KEY"
                       }
                     },
                       "surrogateInfoType":{
                         "name":"EMAIL_ADDRESS_TOKEN"
                       }
                     }
                   }
                 }
               ]
             }
           },
           "inspectConfig":{
             "customInfoTypes":[
               {
                 "infoType":{
                   "name":"EMAIL_ADDRESS_TOKEN"
                 },
                 "surrogateType":{
         
                 }
               }
             ]
           },
           "item":{
             "value": "My name is Alicia Abernathy, and my email address is TOKEN."
           }
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `WRAPPED_KEY`: the wrapped key that you created in [Wrap the AES key using the Cloud KMS key](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify#wrap-aes-key).
     * `TOKEN`: the token that you received in Send a de-identify request to the DLP API—for example, `EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q`.

Make sure that the resulting value of `cryptoKeyName` forms the full resource name of your Cloud KMS key.

For more information about the components of this JSON request, see [`projects.locations.content.reidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/reidentify). After you complete this task, experiment with different inputs for this request. You can use `curl` as described here. Alternatively, use the API Explorer on that API reference page under **Try this method**.

  2. Use `curl` to make a `projects.locations.content.reidentify` request:
         
         curl -s \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "Content-Type: application/json" \
             https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/global/content:reidentify \
             -d @reidentify-request.json
         

Replace `PROJECT_ID` with the ID of your project.

To pass a filename to `curl`, use the `-d` option (for data) and precede the filename with an `@` sign. This file must be in the same directory where you run the `curl` command.

**Note:** This example request explicitly targets the `global` location. Making this request is the same as calling the [`projects.content.reidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify) API, which defaults to the `global` location.

The response that you get from Sensitive Data Protection is similar to the following JSON:
         
         {
           "item": {
             "value": "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
           },
           "overview": {
             "transformedBytes": "70",
             "transformationSummaries": [
               {
                 "infoType": {
                   "name": "EMAIL_ADDRESS"
                 },
                 "transformation": {
                   "cryptoDeterministicConfig": {
                     "cryptoKey": {
                       "kmsWrapped": {
                         "wrappedKey": "CiQAYuuIGo5DVaqdE0YLioWxEhC8LbTmq7Uy2G3qOJlZB7WXBw0SSQAjdwP8ZusZJ3Kr8GD9W0vaFPMDksmHEo6nTDaW/j5sSYpHa1ym2JHk+lUgkC3Zw5bXhfCNOkpXUdHGZKou1893O8BDby/82HY=",
                         "cryptoKeyName": "projects/<var>PROJECT_ID</var>/locations/global/keyRings/dlp-keyring/cryptoKeys/dlp-key"
                       }
                     },
                     "surrogateInfoType": {
                       "name": "EMAIL_ADDRESS_TOKEN"
                     }
                   }
                 },
                 "results": [
                   {
                     "count": "1",
                     "code": "SUCCESS"
                   }
                 ],
                 "transformedBytes": "70"
               }
             ]
           }
         }
         

In the `item` field, the email address token is replaced with the actual email address from the original text.

You have now de-identified and re-identified sensitive data in text content using deterministic encryption.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Destroy your key version

If you no longer want to use the key you created in this task, destroy its version.

**Warning:** When you destroy a key version, you can no longer decrypt content that was encrypted using that version of the key. Make sure that you no longer need a key version before you destroy it.

List the versions available for your key:
    
    
    gcloud kms keys versions list \
        --location "global" \
        --keyring "dlp-keyring" \
        --key "dlp-key"
    

To destroy a version, run the following command:
    
    
    gcloud kms keys versions destroy KEY_VERSION \
        --location "global" \
        --keyring "dlp-keyring" \
        --key "dlp-key"
    

Replace `KEY_VERSION` with the number of the version to be destroyed—for example, `1`.

### Delete the project

If you created a new project for this task, the easiest way to prevent additional charges is to delete the project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Revoke your credentials

Optional: Revoke credentials from the gcloud CLI. 
    
    
    gcloud auth revoke

## What's next

  * For more information about de-identifying sensitive content, see [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data).
  * For information about how a de-identification workflow fits into real-life deployments, see [De-identification and re-identification of PII in large-scale datasets using Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp).
  * For conceptual information about tokenizing data with a cryptographic key, see [Pseudonymization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
