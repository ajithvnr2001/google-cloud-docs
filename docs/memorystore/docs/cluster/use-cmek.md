---
url: https://docs.cloud.google.com/memorystore/docs/cluster/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:56.603421+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By using customer-managed encryption keys (CMEK), you have control over your keys. This gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Instead of Google owning and managing the symmetric key encryption keys (KEKs) that protect your data, you control and manage these keys in [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs).

**Note:** You can use CMEK on new Memorystore for Redis Cluster deployments only. You can't enable CMEK on existing clusters in Memorystore for Redis Cluster. Also, for more information about CMEK for Memorystore for Redis Cluster, see [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek).

## Before you begin

  1. Make sure that you have the Redis Admin [role](https://docs.cloud.google.com/memorystore/docs/cluster/access-control) on your user account.

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




## Workflow to create a cluster that uses CMEK

  1. Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key) in the location where you want the cluster in Memorystore for Redis Cluster to be.

  2. Copy or write down the key name (`KEY_NAME`), the location of the key, and the name of the key ring (`KEY_RING`). You need this information when granting the service account access to the key.

  3. Grant the Memorystore for Redis Cluster service account access to the key.

  4. Go to a project and create a cluster in Memorystore for Redis Cluster with CMEK enabled in the same region as the key ring and key.




Your cluster is now enabled with CMEK.

## Create a key ring and key

Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key). Both must be in the same region as your cluster in Memorystore for Redis Cluster. The key can be from a different project, as long as the key is in the same region. Also, the key must use the [symmetric encryption algorithm](https://docs.cloud.google.com/kms/docs/algorithms#symmetric).

After you create the key ring and key, copy or write down the `KEY_NAME`, the key location, and the `KEY_RING`. You need this information when you grant the service account access to the key.

## Grant the Memorystore for Redis Cluster service account access to the key

Before you can create a cluster in Memorystore for Redis Cluster that uses CMEK, you must grant a specific Memorystore for Redis Cluster service account access to the key.

You can grant the service account access to the key by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To grant access to the service account, use the following format:
    
    
      service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
      

### gcloud

To grant the service account access to the key, use the [`gcloud kms keys add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command.
    
    
    gcloud kms keys add-iam-policy-binding  \
    projects/PROJECT_ID/locations/REGION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
    --member=serviceAccount:service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Make the following replacements:

  * PROJECT_ID: the ID or number of the project that contains the key ring
  * REGION_ID: the region where the key ring is located
  * KEY_RING: the name of the key ring that contains the key
  * KEY_NAME: the name of the key that you're granting access to the service account
  * PROJECT_NUMBER: the ID or number of the project that contains the service account



## Create a cluster that uses CMEK

You can create a cluster that uses CMEK by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

**Note:** You can't enable CMEK on existing clusters. Also, this operation takes several minutes to complete.

### gcloud

To create a cluster that uses CMEK, use the [`gcloud redis clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/create) command.
    
    
    gcloud redis clusters create CLUSTER_ID \
    --project=PROJECT_NAME \
    --region=REGION_ID \
    --network=NETWORK_ID \
    --kms-key=projects/PROJECT_NAME/locations/REGION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
    --shard-count=SHARD_NUMBER \
    --persistence-mode=PERSISTENCE_MODE
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster that you're creating.
  * PROJECT_NAME: the name of the project where you want to create the cluster.
  * REGION_ID: the ID of the region where you want the cluster to be located.
  * NETWORK_ID: the ID of the network that you want to use to create the cluster.
  * KEY_RING: the name of the key ring that contains the key.
  * KEY_NAME: the name of the key.
  * SHARD_NUMBER: the number of shards that you want to have for the cluster.
  * PERSISTENCE_MODE: the persistence mode for the cluster. You can set this mode to one of the following values: 
    * `aof`: you enable Append-Only File (AOF)-based persistence for the cluster.
    * `disabled`: you deactivate persistence for the cluster.
    * `rdb`: you enable Redis Database (RDB)-based persistence for the cluster.

**Note:** For more information about persistence, including the types of persistence that Memorystore for Redis Cluster supports, see [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).

## View key information for a CMEK-enabled cluster

You can view information about your CMEK-enabled cluster by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). This information includes whether CMEK is enabled for your cluster and the active key.

### gcloud

To verify if CMEK is enabled and to see the key reference, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command to view the `encryptionInfo` and `kmsKey` fields.
    
    
    gcloud redis clusters describe CLUSTER_ID \
    --project=PROJECT_NAME \
    --region=REGION_ID
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster about which you want to view information
  * PROJECT_NAME: the name of the project that contains the cluster
  * REGION_ID: the ID of the region where the cluster is located



## Manage key versions

For information about what happens when you disable, destroy, rotate, enable, and restore a key version, see [Behavior of a CMEK key version](https://docs.cloud.google.com/memorystore/docs/cluster/about-cmek#behavior-of-a-cmek-key-version).

For instructions on how to disable and re-enable key versions, see [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable).

For instructions on how to destroy and restore key versions, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

## What's next

  * Learn more about [backups](https://docs.cloud.google.com/memorystore/docs/cluster/backups).
  * Learn more about [persistence](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
