---
url: https://docs.cloud.google.com/service-extensions/docs/cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:04.349755+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to encrypt content stored in Service Extensions plugins with customer-managed encryption keys (CMEK).

**Note:** CMEK for Service Extensions is supported only for regional plugins.

## Overview

By default, Service Extensions encrypts customer content at rest. Service Extensions handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Service Extensions. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Service Extensions resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

All cryptographic operations are billed to the Google Cloud project that owns the key, regardless of the key type. For pricing information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Create a key and grant permissions

The following instructions explain how to create a key for a plugin and grant permissions to encrypt and decrypt plugin data with the key.

  1. In the Google Cloud project where you want to manage your keys, do the following:

     1. To be able to create a key, [enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

     2. Create a key ring and a key by using one of the following options:

        * [Create a Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and then [create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key).
        * [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key).

The Cloud KMS [key location](https://docs.cloud.google.com/kms/docs/locations) must match the location of the plugin that you want to encrypt.

  2. The Service Extensions service account must exist in your Service Extensions project. The service account name is `service-PROJECT_NUMBER@gcp-sa-networkactions.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Service Extensions is running.

The service account is created automatically when you create your first plugin in your Service Extensions project. If you haven't yet created a plugin in your project, create the service account by running the following command:
         
         gcloud beta services identity create \
             --service=networkactions.googleapis.com \
             --project=PROJECT
         

Replace PROJECT with the ID of the project where Service Extensions is running.

  3. Grant the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/understanding-roles#cloud-kms-roles) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Service Extensions service account on the key that you created.

###  Console 

     1. In the Google Cloud console, go to the **Key management** page.

[Go to Key management](https://console.cloud.google.com/security/kms)

     2. Select the key that you created.

     3. Grant access to the Service Extensions service account:

        1. Select **Show info panel**.
        2. Click **Add member**.
        3. Add the Service Extensions service account. The service account is `service-PROJECT_NUMBER@gcp-sa-networkactions.iam.gserviceaccount.com`.
        4. In **Select a role** , select **Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter**
        5. Click **Save**.
     4. Repeat the previous step to grant access to the account of the plugin creator.

     5. Return to the **[Key management](https://console.cloud.google.com/security/kms)** page and select the key again.

     6. Select **Show info panel**. You see roles in the **Role/Member** column.

###  gcloud 

     1. Grant access to the Service Extensions service account by running the [`gcloud kms keys add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding):
            
            gcloud kms keys add-iam-policy-binding [--project=PROJECT] KEY_NAME \
                --location LOCATION
                --keyring=KEYRING_NAME \
                --member=serviceAccount:service-PROJECT-NUMBER@gcp-sa-networkactions.iam.gserviceaccount.com \
                --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
            

Replace the following:

        * `PROJECT`: the ID of the project that contains the key
        * `KEY_NAME`: the key name
        * `LOCATION`: the location of the key
        * `KEYRING_NAME`: the key ring name
        * `PROJECT-NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project
     2. Repeat the previous step with `member` set to the account of the plugin creator.




When [creating a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) or updating it, specify the CMEK key. The key provides encryption for the plugin image and configuration data. Other plugin data is protected by Google default encryption.

## Automatic re-encryption

When the primary version of the KMS key changes (either by a manual user change or by [automatic rotation](https://docs.cloud.google.com/kms/docs/rotate-key#automatic)), the plugin data that is protected by the key is automatically re-encrypted with the new key version.

## Key tracking

You can use key tracking to list the plugin resources that a key protects. For more information, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

## Cloud Key Management Service quotas and Service Extensions

When you use CMEK keys in Service Extensions, such as in the following operations, your projects can consume [Cloud KMS cryptographic request quotas](https://cloud.google.com/kms/quotas#cryptographic_requests):

  * Creating or updating a CMEK-protected plugin
  * Adding new versions or changing the main version of CMEK-protected plugins
  * Listing versions of CMEK-protected plugins that have the `plugin_config_data` field set
  * Attaching a plugin to the extension



Attached plugins additionally incur decrypt operations over time.

If you use hardware (Cloud HSM) or external (Cloud EKM) keys, encryption and decryption operations using CMEK keys affect Cloud KMS quotas.

## Remove access to a CMEK-encrypted plugin

**Warning:** Disabling or destroying the encryption key for a plugin renders plugin data irretrievable.

There are several ways to remove access to a CMEK-encrypted plugin:

  * Revoke the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) from the Service Extensions service account by using either the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-revoke-single-role-console) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-revoke-single-role-gcloud). Changes to permissions take effect within seconds, but it might take tens of minutes until all serving replicas of a plugin stop serving traffic after its key is revoked.
  * Temporarily [disable the customer-managed encryption key](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version).
  * [Permanently destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) the CMEK key.



We recommend that you revoke the permissions from the Service Extensions service account before disabling or destroying a key.

### Implications of removing access

CMEK-protected data consists of images downloaded from Artifact Registry as well as any plugin configuration data provided directly (through the `plugin_config_data` field).

After you disable or destroy the encryption key for a plugin, all plugin data protected by CMEK becomes inaccessible within minutes. It might take tens of minutes until all serving replicas of a plugin stop serving traffic after its key is revoked.

Plugin metadata, such as the plugin name, description, labels, or logging configuration, remains accessible.

As a consequence, removing access to a key protecting an active plugin (that is, a plugin that's attached to an extension), causes the plugin to become unable to serve traffic. All requests to the plugin fail.

When plugin invocation fails, the behavior of the extension depends on the `fail_open` field:

  * If the field is set to `true`, the request proceeds to the target service, without providing any indication that plugin invocation has failed.
  * If the field is set to `false`, the request doesn't reach the target service.



## Limitations

  * CMEK protection set on a plugin is confined to Service Extensions.

To protect plugin resources on other Google products, enable CMEK through them. For the plugin images uploaded to Artifact Registry, set up [CMEK for Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/cmek). To protect the logs generated by your plugin, configure [CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

  * You can't change encryption mode (Google-managed or CMEK) of a plugin. However, you can update the plugin to use a different KMS key.

  * Only regional plugins are supported. Additionally, plugins can be encrypted only by a key in the same region as the plugin.




## What's next?

  * Learn more about [creating a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin).
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn more about [default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
