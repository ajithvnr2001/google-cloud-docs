---
url: https://docs.cloud.google.com/memorystore/docs/valkey/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:38.458792+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By using customer-managed encryption keys (CMEK), you have control over your keys. This gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Instead of Google owning and managing the symmetric key encryption keys (KEKs) that protect your data, you control and manage these keys in [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs).

**Note:** You can use CMEK on new Memorystore for Valkey deployments only. You can't enable CMEK on existing Memorystore for Valkey instances. Also, for more information about CMEK for Memorystore for Valkey, see [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek).

## Before you begin

  1. Make sure that you have the Memorystore Admin [role](https://docs.cloud.google.com/memorystore/docs/valkey/access-control) on your user account.

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




## Workflow to create an instance that uses CMEK

  1. Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key) in the location where you want the Memorystore for Valkey instance to be.

  2. Copy or write down the key name (`KEY_NAME`), the location of the key, and the name of the key ring (`KEY_RING`). You need this information when granting the service account access to the key.

  3. Grant the Memorystore for Valkey service account access to the key.

  4. Go to a project and create a Memorystore for Valkey instance with CMEK enabled in the same region as the key ring and key.




Your Memorystore for Valkey instance is now enabled with CMEK.

## Create a key ring and key

Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key). Both must be in the same region as your Memorystore for Valkey instance. The key can be from a different project, as long as the key is in the same region. Also, the key must use the [symmetric encryption algorithm](https://docs.cloud.google.com/kms/docs/algorithms#symmetric).

After you create the key ring and key, copy or write down the `KEY_NAME`, the key location, and the `KEY_RING`. You need this information when you grant the service account access to the key.

## Grant the Memorystore for Valkey service account access to the key

Before you can create a Memorystore for Valkey instance that uses CMEK, you must grant a specific Memorystore for Valkey service account access to the key.

You can grant the service account access to the key by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To grant access to the service account, use the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com
    

### gcloud

To grant the service account access to the key, use the [`gcloud kms keys add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command.
    
    
    gcloud kms keys add-iam-policy-binding  \
    projects/PROJECT_ID/locations/REGION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
    --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-memorystore.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Make the following replacements:

  * PROJECT_ID: the ID or number of the project that contains the key ring
  * REGION_ID: the region where the key ring is located
  * KEY_RING: the name of the key ring that contains the key
  * KEY_NAME: the name of the key that you're granting access to the service account
  * PROJECT_NUMBER: the ID or number of the project that contains the service account



## Create a Memorystore for Valkey instance that uses CMEK

You can create an instance that uses CMEK by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** You can't enable CMEK on existing instances. Also, this operation takes several minutes to complete.

### gcloud

To create an instance that uses CMEK, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --project=PROJECT_NAME \
    --location=REGION_ID \
    --endpoints='[{"connections": [{"pscAutoConnection": {"network": "projects/PROJECT_NAME/global/networks/NETWORK_ID", "projectId": "PROJECT_NAME"}}]}]' \
    --kms-key=projects/PROJECT_NAME/locations/REGION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
    --shard-count=SHARD_NUMBER \
    --persistence-config-mode=PERSISTENCE_CONFIG_MODE
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you're creating.
  * PROJECT_NAME: the name of the project where you want to create the instance.
  * REGION_ID: the ID of the region where you want the instance to be located.
  * NETWORK_ID: the ID of the network that you want to use to create the instance.
  * KEY_RING: the name of the key ring that contains the key.
  * KEY_NAME: the name of the key.
  * SHARD_NUMBER: the number of shards that you want to have for the instance.
  * PERSISTENCE_CONFIG_MODE: the persistence mode for the instance. You can set this mode to one of the following values: 
    * `aof`: you enable Append-Only File (AOF)-based persistence for the instance.
    * `disabled`: you deactivate persistence for the instance.
    * `rdb`: you enable Redis Database (RDB)-based persistence for the instance.

**Note:** For more information about persistence, including the types of persistence that Memorystore for Valkey supports, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).

## View key information for a CMEK-enabled instance

You can view information about your CMEK-enabled instance by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). This information includes whether CMEK is enabled for your instance and the active key.

### gcloud

To verify if CMEK is enabled and to see the key reference, use the [`gcloud memorystore instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/describe) command to view the `encryptionInfo` and `kmsKey` fields.
    
    
    gcloud memorystore instances describe INSTANCE_ID \
    --project=PROJECT_NAME \
    --location=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance about which you want to view information
  * PROJECT_NAME: the name of the project that contains the instance
  * REGION_ID: the ID of the region where the instance is located



## Manage key versions

For information about what happens when you disable, destroy, rotate, enable, and restore a key version, see [Behavior of a CMEK key version](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek#behavior-of-a-cmek-key-version).

For instructions on how to disable and re-enable key versions, see [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable).

For instructions on how to destroy and restore key versions, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

## What's next

  * Learn more about [backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups).
  * Learn more about [persistence](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
