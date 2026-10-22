---
url: https://docs.cloud.google.com/datastream/docs/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:01.953337+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Datastream encrypts customer content at rest. Datastream handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Datastream. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Datastream resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

This page describes how customer-managed encryption keys (CMEK) work with Datastream. 

To use this feature, see Use CMEK. Also, for more information about CMEK, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Is CMEK right for you?

CMEK is intended for organizations that have sensitive or regulated data that requires them to manage their encryption keys.

## Google-managed encryption versus customer-managed encryption

The CMEK feature lets you use your own cryptographic keys for data at rest in Datastream. After adding CMEK, whenever an API call is made, Datastream uses your key to access data.

Datastream uses Google-managed data encryption keys (DEK) and key encryption keys (KEK) to encrypt Datastream. There are two levels of encryption:

  1. The DEK encrypts data.
  2. The KEK encrypts the DEK.



Datastream stores the encrypted DEK alongside the encrypted data, and Google manages the Google KEK. With CMEK, you create a key that wraps the Google KEK. CMEK lets you create, revoke, and delete the KEK.

CMEK, including software, hardware, and external keys, are all managed through the [Cloud Key Management Service (KMS) API](https://docs.cloud.google.com/kms/docs/reference/rest).

## Which locations support CMEK-enabled Datastream streams?

CMEK is available in all Datastream [locations](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).

The Cloud Key Management Service key ring location must match the region where you want to create a stream in Datastream. A multi-region or global region key **won't** work. If the regions don't match, then a request for creating the stream fails.

## Understand service accounts

When your Datastream streams have CMEK enabled, you need to use a service account to request key access from Cloud Key Management Service.

To use a CMEK on a project, you must have a service account and you must grant the key access to the service account. The service account must exist inside of the project. The service account is visible in all regions.

If you use the Console to create a stream, Datastream creates the service account automatically when you first choose the **Customer-managed key** option (if a service account doesn't exist already). You don't need to have special permissions on your user account when Datastream creates the service account automatically.

## Understand keys

In [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs), you need to create a key ring with a cryptographic key, set with a location. When you create a new stream in Datastream, you select this key to encrypt the stream.

You need to know the key ID and key region when you create new streams that use CMEK. You must put new streams in the same region as the CMEK associated with the streams. You can create one project for both keys and streams, or different projects for each.

CMEK uses the following format:

`projects/[CMEK_ENABLED_PROJECT]/locations/[REGION]/keyRings/[RING_NAME]/cryptoKeys/[KEYNAME]`

If Datastream can't access the key (for example, you disable the key version), then Datastream changes the state of the stream to `FAILED` and an associated error message appears. After troubleshooting any issues associated with the errors message so that the key becomes accessible again, Datastream resumes the stream automatically.

If you disable the primary version of the CMEK, then Datastream won't be able to use the key. As a result, Datastream will change the state of the stream to `FAILED`.

### External key managers

You can use keys stored in external key managers, such as Fortanix, Ionic, or Thales, as your CMEK. To learn how to use external keys with Cloud Key Management Service, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## How do you make CMEK-encrypted data inaccessible permanently?

You have complete control over keys and data access. If you destroy a key version that's associated with a stream in Datastream, then Google can't get the data back. However, if you disable the key version, you can re-enable it to get the data back.

You might have situations where you want to permanently destroy data encrypted with CMEK. To do this, you destroy the CMEK version. You can't destroy the key ring or key, but you can destroy key versions of the key.

## Restrictions

The following restrictions apply when using CMEK:

  * You can't update CMEK on a running stream.

  * Although you can use CMEK to encrypt rows from the source database, you can't use these keys to encrypt stream metadata, such as the stream ID, IP address of the source database or the names of the source database tables.




## Use CMEK

Now that you understand CMEK, you're ready to set up a service account and keys for CMEK. In addition, you'll learn how to set up Datastream to use CMEK.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Install and initialize the Cloud SDK.](https://docs.cloud.google.com/sdk/docs/install)
  7. Make sure that you have the Datastream Admin role assigned to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  8. Enable the Cloud Key Management Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  9. Enable the Datastream API. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)




## Workflow to create a stream in Datastream with CMEK

  1. _gcloud and API users only:_ Make sure that you have a service account for each project that requires CMEK. If you don't, then here's how to create a service account.
  2. Create a key ring and key, and set the location for each key. The location is the Google Cloud region.
  3. _gcloud and API users only:_ Grant the key access to the service account.
  4. Copy or write down the key ID (`KMS_KEY_ID`) and location for the key, and the ID (`KMS_KEYRING_ID`) for the key ring. You need this information when granting the key access to the service account.
  5. Go to a project and [create a stream in Datastream](https://docs.cloud.google.com/datastream/docs/create-a-stream) with the following options: 
     1. The same location as the CMEK
     2. The CMEK configuration
     3. The CMEK ID



Your stream in Datastream is now enabled with CMEK.

## Create a service account

You need to create a service account for each project that requires CMEK.

To allow a user to manage service accounts, grant one of the following roles:

  * Service Account User (`roles/iam.serviceAccountUser`): Includes permissions to list service accounts, get details about a service account, and impersonate a service account.
  * Service Account Admin (`roles/iam.serviceAccountAdmin`): Includes permissions to list service accounts and get details about a service account. Also includes permissions to create, update, and delete service accounts, and to view or change the Datastream policy on a service account.



You can use only `gcloud` commands to create the type of service account that you need for CMEK. If you're using the Console, then Datastream creates this service account for you automatically.

To create a service account with `gcloud`, run the following command:
    
    
    gcloud beta services identity create \
    --service=datastream.googleapis.com \
    --project=PROJECT_ID

The previous command returns a service account name. You use this service account name during the procedure in Grant the key access to the service account.

## Create a key

You can use an externally managed key with CMEK using the Cloud EKM service to make the key available through Cloud KMS. To learn more, see [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key).

You can create the key in the same Google Cloud project as the stream in Datastream, or in a separate user project. The Cloud KMS key ring location must match the region where you want to create the stream. A multi-region or global region key **won't** work. If the regions don't match, then you can't create the stream.

If you destroy the key version that Datastream uses to encrypt data, but the data is still in the stream, then the stream won't be usable, and Datastream changes the state of the stream to `PERMANENTLY FAILED`. If this occurs, then delete and recreate the stream. When you use CMEK in Datastream, your projects can consume Cloud KMS cryptographic requests quotas. Confirm that you have enough quota to enable application-layer secrets encryption for your application. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas). 

To create a Cloud KMS key:

### Console

  1. In the Google Cloud console, go to the **[Cryptographic keys](https://console.cloud.google.com/security/kms/keyrings)** page.
  2. Click **Create key ring**.
  3. Add a **Key ring name**. Note this name because you need it when granting the key access to the service account.
  4. Add a **Key ring location**.
  5. Click **Create**. The **Create key** page opens.
  6. Add a **Key name**.
  7. Select a **Purpose** (symmetric or asymmetric).
  8. Select a **Rotation period** and **Starting on date**.
  9. Click **Create**.
  10. On the **Keys** table, click the three dots in the last column, and select **Copy Resource ID** or write it down. This is the `KMS_KEY_ID`. You need the `KMS_KEY_ID` when granting the key access to the service account.



### gcloud

  1. Create a new key ring. 
         
         gcloud kms keyrings create KMS_KEYRING_ID \
         --location=GCP_REGION
           

Write down this name because you need it when granting the key access to the service account.
  2. Create a key on the key ring. 
         
         gcloud kms keys create KMS_KEY_ID \
         --location=GCP_REGION \
         --keyring=KMS_KEYRING_ID \
         --purpose=encryption
           

Write down this name because you need it when granting the key access to the service account.



## Grant the key access to the service account

You only need to perform this procedure if you're using `gcloud` or the API.

To grant access to the service account, use the following code:
    
    
    gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
    --location=GCP_REGION \
    --keyring=KMS_KEYRING_ID \
    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-datastream.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

## Create a stream in Datastream with CMEK

As part of [creating a stream in Datastream](https://docs.cloud.google.com/datastream/docs/create-a-stream), you can use your CMEK to manage the encryption of your data.

## What's next

  * To learn how to disable a key version, see [Disable an enabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable).
  * To learn how to re-enable a key version, see [Enable a disabled key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
