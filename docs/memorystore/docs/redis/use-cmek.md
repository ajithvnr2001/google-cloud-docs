---
url: https://docs.cloud.google.com/memorystore/docs/redis/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.779114+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By using customer-managed encryption keys (CMEK), you have control over your keys. This gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Instead of Google owning and managing the symmetric key encryption keys (KEKs) that protect your data, you control and manage these keys in [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs).

**Note:** You can use CMEK on new Memorystore for Redis deployments only. You can't enable CMEK on existing Memorystore for Redis instances. Also, for more information about CMEK for Memorystore for Redis, see [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/redis/about-cmek).

If your instance uses CMEK and the [Cloud Key Management Service API](https://docs.cloud.google.com/kms/docs/reference/rest) is unavailable because of an outage, then when you [reconnect to your instance](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance), you might need to use a different IP address.

## Before you begin

  1. Make sure that you have the Redis Admin [role](https://docs.cloud.google.com/memorystore/docs/redis/access-control) on your user account.

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




## Workflow to create an instance that uses CMEK

  1. Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key) in the location where you want the Memorystore for Redis instance to be.

  2. Copy or write down the key name (`KEY_NAME`), the location of the key, and the name of the key ring (`KEY_RING`). You need this information when granting the service account access to the key.

  3. Grant the Memorystore for Redis service account access to the key.

  4. Go to a project and create a Memorystore for Redis instance with CMEK enabled in the same region as the key ring and key.




Your Memorystore for Redis instance is now enabled with CMEK.

## Create a key ring and key

Create a [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key). Both must be in the same region as your Memorystore for Redis instance. The key can be from a different project, as long as the key is in the same region. Also, the key must use the [symmetric encryption algorithm](https://docs.cloud.google.com/kms/docs/algorithms#symmetric).

After you create the key ring and key, copy or write down the `KEY_NAME`, the key location, and the `KEY_RING`. You need this information when you grant the service account access to the key.

## Grant the Memorystore for Redis service account access to the key

Before you can create a Memorystore for Redis instance that uses CMEK, you must grant a specific Memorystore for Redis service account access to the key. You can grant the service account access to the key by using the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To grant access to the service account, use the following format:
    
    
    service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
    

### Console

You grant the service account access to the key as part of the steps for creating a Memorystore for Redis instance that uses CMEK.

### gcloud

To grant the service account access to the key, use the [`gcloud kms keys add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command.
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
    --location=REGION_ID \
    --keyring=KEY_RING \
    --member=serviceAccount:service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Make the following replacements:

  * KEY_NAME: the name of the key that you're granting access to the service account
  * REGION_ID: the region where the key ring is located
  * KEY_RING: the name of the key ring that contains the key
  * PROJECT_NUMBER: the ID or number of the project that contains the service account



## Create a Memorystore for Redis instance that uses CMEK

**Note:** You can't enable CMEK on existing instances. Also, this operation takes several minutes to complete.

You can create an instance that uses CMEK by using the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. Make sure that you create a key ring and key in the same region where you want to create your instance.

  2. Follow the instructions at [Create a Redis instance on a VPC network](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_on_a_vpc_network) until you reach the step to enable CMEK. Then, return to these instructions.

  3. Select **Use a customer-managed encryption key (CMEK)**.

  4. To select your key, use the menu.

**Note** : If you haven't granted the service account the permissions that it needs to access the key, then the following message appears:

`The service-PROJECT-NUMBER@cloud-redis.iam.gserviceaccount.com service account does not have the "cloudkms.cryptoKeyEncrypterDecrypter" role. Verify the service account has permission to encrypt/decrypt with the selected key.`

If this occurs, then click **Grant** to grant the permissions to the service account.

  5. Select your remaining configurations for the instance, and then click **Create**.




### gcloud

To create an instance that uses CMEK, use the [`gcloud redis instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/create) command.
    
    
    gcloud redis instances create INSTANCE_ID \
    --size=SIZE \
    --region=REGION_ID \
    --customer-managed-key=projects/PROJECT_NAME/locations/REGION_ID/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you're creating
  * SIZE: the size of the instance that you want to create, in gibibytes (GiB)
  * REGION_ID: the ID of the region where you want the instance to be located
  * PROJECT_NAME: the name of the project where you want to create the instance
  * KEY_RING: the name of the key ring that contains the key
  * KEY_NAME: the name of the key



## View key information for a CMEK-enabled instance

You can view key information for a CMEK-enabled instance by using the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). This information includes the active key and whether CMEK is enabled for your instance.

### Console

  1. In the Google Cloud console, go to the **Instances** page.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. Click the ID of your instance.

  3. In the left-hand pane, click the **Security** tab. The **Security** page contains a link to the active key and shows the key reference path. If this information doesn't appear, then you didn't enable CMEK for your instance.




### gcloud

To verify if CMEK is enabled and to see the key reference, use the [`gcloud redis instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/describe) command to view the `customerManagedKey` field.
    
    
    gcloud redis instances describe INSTANCE_ID \
    --project=PROJECT_NAME \
    --region=REGION_ID
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance about which you want to view information
  * PROJECT_NAME: the name of the project that contains the instance
  * REGION_ID: the ID of the region where the instance is located



## Manage key versions

For information about what happens when you disable, destroy, rotate, enable, and restore a key version, see [Behavior of a CMEK key version](https://docs.cloud.google.com/memorystore/docs/redis/about-cmek#behavior-of-a-cmek-key-version).

For instructions on how to disable and re-enable key versions, see [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable).

For instructions on how to destroy and restore key versions, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

## What's next

  * Learn more about [Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview).
  * Learn more about [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/in-transit-encryption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
