---
url: https://docs.cloud.google.com/artifact-registry/docs/cmek/
title: Enabling customer-managed encryption keys \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:26.704634+00:00
---

# Enabling customer-managed encryption keys  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Enabling customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

Customer-managed encryption keys (CMEK) let you encrypt repository content using keys that you manage in Cloud Key Management Service. This encryption process helps you maintain direct control over key rotation and lifecycle policies while meeting regulatory compliance requirements.

## Overview

By default, Artifact Registry encrypts customer content at rest. Artifact Registry handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Artifact Registry. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Artifact Registry resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Artifact Registry resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Artifact Registry. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

To set up CMEK manually, see [Creating a key and granting permissions](https://docs.cloud.google.com/artifact-registry/docs/cmek#create)

To set up CMEK using Autokey, see Use Autokey to create keys on this page.

You assign a CMEK key when you create a repository. You cannot change the encryption mechanism of an existing repository. If you have a CMEK-encrypted repository, then you cannot change the encryption mechanism to use a Google-owned and Google-managed encryption key or assign a different Cloud KMS key for encryption.

For more information about CMEK in general, including when and why to enable it, see the [CMEK overview](https://docs.cloud.google.com/kms/docs/cmek).

## Creating a key and granting permissions

The following instructions explain how to create a key for a repository and grant permissions to encrypt and decrypt repository data with the key. You can use a key created directly in Cloud KMS or an externally-managed key that you make available with [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

  1. In the Google Cloud project where you want to manage your keys:

     1. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

     2. Create a key ring and a key using one of the following options:

        * [Create a Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and then [create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key).
        * [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key).

The Cloud KMS [key location](https://docs.cloud.google.com/kms/docs/locations) must match the [repository location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository you will encrypt. 

  2. If you have not created a repository in the Artifact Registry project, the Artifact Registry service account doesn't exist. To create the service account, run the following command:
         
         gcloud beta services identity create --service=artifactregistry.googleapis.com --project=PROJECT
         

Replace PROJECT with the ID of the project where Artifact Registry is running.

  3. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Artifact Registry service account. Grant this permission on the key you created.

###  Console 

     1. Go to the **Cryptographic keys** page.

[Open the Cloud KMS page](https://console.cloud.google.com/security/kms)

     2. Select the key you created.

     3. Grant access to the Artifact Registry service account:

        1. If the info panel is hidden, click **Show info panel**.
        2. Click **Grant access**.
        3. In the **New principals** field, add the Artifact Registry service account. The service account is **service- PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com**, where PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) of the Google Cloud project where Artifact Registry is running.
        4. In **Select a role** , select **Cloud KMS** > **Cloud KMS CryptoKey Encrypter/Decrypter**.
        5. Click **Save**.
     4. Repeat the previous step to grant access to the account that will create repositories.

     5. Return to the **[Key management](https://console.cloud.google.com/security/kms)** page and select the key again.

     6. If the info panel is hidden, click **Show info panel**. You should see roles in the **Role/Principal** section.

###  gcloud 

     1. Run the following command to grant access to the Artifact Registry service account:
            
            gcloud kms keys add-iam-policy-binding [--project=PROJECT] \
                   KEY --location LOCATION --keyring=KEYRING \
                   --member serviceAccount:service-PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com \
                   --role roles/cloudkms.cryptoKeyEncrypterDecrypter
            

Where

        * PROJECT is the ID of the project that contains the key.
        * KEY is the key name.
        * LOCATION is the key location. The [key location](https://docs.cloud.google.com/kms/docs/locations) must match the [repository location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository you will encrypt.
        * KEYRING is the key ring name.
        * PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects) of the Google Cloud project that is running Artifact Registry.
     2. Repeat the previous step to grant access to the account that will create repositories.

For more information about this command see the [gcloud kms keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) documentation.




Next, [create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) and specify the key to use for encryption.

## Use Autokey to create keys

Autokey creates a new key in the same location as the repository.

### Required roles

To get the permissions that you need to use Autokey to create protected repositories, ask your administrator to grant you the following IAM roles on the folder or project: 

  * [Cloud KMS Autokey User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.autokeyUser) (`roles/cloudkms.autokeyUser`)
  * [Artifact Registry Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create keys

Before you create keys with Autokey, you must [enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click **Create Repository**.

  3. Fill out the required and optional fields for your [standard](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#create-console), [remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#create), or [virtual](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo#create) repository.

  4. In the **Encryption** section, choose **Cloud KMS with Autokey automated management**.

  5. Click **Create**.




## Removing access

There are several ways to remove access to a CMEK-encrypted repository:

  * Revoke the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) from the **Artifact Registry service account** using one of the following methods: 
    * [Revoke access in the Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-revoke-single-role-console)
    * [Revoke access by using the gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-revoke-single-role-gcloud)
  * Temporarily [disable the Customer-managed encryption key](https://docs.cloud.google.com/kms/docs/enable-disable#disable)
  * [Permanently destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) the CMEK key



We recommend that you revoke the permissions from the Artifact Registry service account before disabling or destroying a key. Changes to permissions are consistent within seconds, so you can observe the impacts of disabling or destroying a key.

When you disable or destroy the encryption key for a repository, you lose the ability to view or retrieve artifact data. All artifact data stored in the repository becomes inaccessible, including built artifacts, arbitrary binary data (blobs), and manifests such as a Docker manifest or an npm packument file. Users with the Artifact Registry Reader role (`roles/artifactregistry.reader`) or Viewer role (`roles/artifactregistry.viewer`) can still view artifact metadata such as the artifact name, version, or tag.

Users with the Artifact Registry Administrator role (`roles/artifactregistry.admin`) or Owner role (`roles/owner`) can delete the repository.

## CMEK organization policies

Artifact Registry supports [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that can require CMEK protection.

Policies can limit which Cloud KMS CryptoKeys can be used for CMEK protection.

  * When Artifact Registry API is in the `Deny` policy list of services of constraint `constraints/gcp.restrictNonCmekServices`, Artifact Registry refuses to create new repositories that aren't CMEK-protected.

  * When `constraints/gcp.restrictCmekCryptoKeyProjects` is configured, Artifact Registry creates CMEK-protected repositories that are protected by a CryptoKey from an allowed project, folder, or organization.




Pub/Sub supports the same constraints. When you activate the Artifact Registry API in a Google Cloud project, Artifact Registry tries to automatically create a Pub/Sub topic with the topic ID `gcr` using Google-owned and Google-managed encryption keys. However, if the Pub/Sub API is in the `Deny` policy list for the constraint `constraints/gcp.restrictNonCmekServices`, then Pub/Sub won't create the topic. In this scenario, you must create the `gcr` topic with CMEK encryption. For more information, see the Pub/Sub [instructions for encrypting topics](https://docs.cloud.google.com/pubsub/docs/encryption#using-cmek).

For more about configuring organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## What's next?

  * [Create a repository encrypted with CMEK](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#create)
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek)
  * Learn more about [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
