---
url: https://docs.cloud.google.com/alloydb/docs/use-cmek/
title: Secure data with encryption keys \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:52.119718+00:00
---

# Secure data with encryption keys  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Secure data with encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, configure, and apply customer-managed encryption keys (CMEK) for AlloyDB for PostgreSQL.

For more information about CMEK, see [About CMEK](https://docs.cloud.google.com/alloydb/docs/cmek).

## Create and authorize a CMEK key for AlloyDB

  1. Create a key in Cloud Key Management Service (Cloud KMS). AlloyDB supports the following kinds of keys:

     * [Symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys)
     * [Cloud HSM keys](https://docs.cloud.google.com/kms/docs/hsm#create-a-key)
     * [Cloud External Key Manager (Cloud EKM) keys](https://docs.cloud.google.com/kms/docs/ekm#overview)

The key must be in the same location as your AlloyDB cluster. For example, a AlloyDB cluster located in `us-west1` can use only keys in `us-west1`.

If you already have a Cloud KMS key in the correct location, you can skip this step.

  2. Grant AlloyDB access to the key.

     1. Using the Google Cloud CLI, create and display the service agent, or display it if the account already exists:
    
    gcloud beta services identity create --service=alloydb.googleapis.com \
            --project=PROJECT

The [gcloud services identity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command creates or gets the [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) that AlloyDB can use to access the Cloud KMS key on your behalf.

The service account ID resembles an email address:
    
    Service identity created: service-xxx@gcp-sa-alloydb.iam.gserviceaccount.com
    

     1. Grant the `cloudkms.cryptoKeyEncrypterDecrypter` role to the service account:
    
    gcloud kms keys add-iam-policy-binding KEY \
            --location REGION \
            --keyring KEYRING \
            --project=PROJECT \
            --member serviceAccount:service-xxx@gcp-sa-alloydb.iam.gserviceaccount.com \
            --role roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

     * KEY: the Cloud KMS ID of the key
     * REGION: the key's region—for example, `us-central1`
     * PROJECT: the ID of the key's project
     * KEYRING: the ID of the key's Cloud KMS key ring

This role grants the service account permission to encrypt and decrypt using the Cloud KMS key. For more information, see [ Cloud KMS Permissions and Roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).




## Create a CMEK-encrypted cluster

When you create a new cluster, you can choose whether to encrypt the cluster with the default Google-managed encryption or use a CMEK key instead. For more information, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

## View a cluster's encryption method and CMEK key

### Console

The **Encryption** column of the **Clusters** page displays whether each cluster in your project uses Google-managed encryption or CMEK.

[Go to the Clusters page](https://console.cloud.google.com/alloydb/clusters)

To view the key details of a cluster using CMEK, click its name in the **Resource name** column. The resulting detail page's **Encryption key** field contains a description of the key, including a link to its own Cloud KMS detail page.

### gcloud

Call the [`gcloud alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/describe) command:
    
    
    gcloud alloydb clusters describe CLUSTER \
    --project=PROJECT \
    --region=REGION

Replace the following:

  * CLUSTER: the ID of the cluster to describe
  * PROJECT: the ID of the cluster's project
  * REGION: the cluster's region—for example, `us-central1`



The output includes an `encryptionInfo` field with a summary of the cluster's encryption.

## Apply CMEK to backups

When you create a new backup, you can choose whether to encrypt it using the default Google-managed encryption or a CMEK key. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand) or [Schedule automatic backups](https://docs.cloud.google.com/alloydb/docs/backup/schedule).

You also have the option to apply a CMEK key to the cluster created when restoring from a backup, regardless of that backup's encryption method. For more information, see [Restore a cluster](https://docs.cloud.google.com/alloydb/docs/backup/restore).

## Rotate keys using CMEK encryption

It's important to understand the implications of rotating your customer-managed encryption keys (CMEK) in Cloud Key Management Service (Cloud KMS) when used with AlloyDB clusters.

When you rotate a CMEK key, the following happens to your existing AlloyDB data:

  * Immediate access continues: the data remains encrypted with its original Data Encryption Key (DEK) version, as long as the earlier version of the key is still available in KMS, neither disabled nor deleted.

  * Full data re-encryption is manual: to get all your AlloyDB data on the latest primary key version, you must re-encrypt it.




To re-encrypt your existing cluster with a new CMEK key version, you must perform a backup and restore operation:

  1. Create a backup of your existing cluster.

  2. Restore the backup into a new cluster, specifying the new CMEK primary key version during the restore process.




For more information, see [Cluster restoration](https://docs.cloud.google.com/alloydb/docs/backup/overview#restoring).

Frequent CMEK key rotation with AlloyDB requires significant operational overhead. Because existing data doesn't automatically re-encrypt, and because manual re-encryption involves a full backup and restore to a new cluster, frequent rotations can be cumbersome and can impact availability or management complexity.

You can safely delete old CMEK key versions in Cloud KMS only after you confirm that all relevant AlloyDB data is manually re-encrypted and that the data uses a newer key version.

**Warning:** Before deleting any old key versions in Cloud KMS, you must verify that all relevant AlloyDB data is fully re-encrypted with a new key version. Destroying a key version that is still in use by any data leads to permanent data loss, rendering that data unrecoverable. This happens because the keys that are used to encrypt the data remain associated with the older CMEK key version.

## View a backup's encryption method and CMEK key

### Console

The **Encryption** column of the **Backups** page displays whether each backup in your project uses Google-managed encryption or Cloud Key Management Service (CMEK).

[Go to the Backups page](https://console.cloud.google.com/alloydb/backups)

To see the key details of a backup using CMEK, click **Restore**. The subsequent detail panel's **Encryption key** field contains a description of the key, including a link to its own Cloud KMS detail page.

### gcloud

Call the [`gcloud alloydb backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/describe) command:
    
    
    gcloud alloydb backups describe CLUSTER \
    --project=PROJECT \
    --region=REGION

Replace the following:

  * CLUSTER: the ID of the backup to describe
  * PROJECT: the ID of the backup's project
  * REGION: the backup's region—for example, `us-central1`



The output includes an `encryptionInfo` field with a summary of the backup's encryption.

## Disable a key

Disabling a cluster's CMEK key makes that cluster's data inaccessible until you enable the key again.

However, disabling a key can take [up to three hours to propagate](https://docs.cloud.google.com/kms/docs/consistency) to your AlloyDB cluster. To disable a key while preventing access to your data immediately, follow these steps:

  1. [Delete your cluster's primary instance.](https://docs.cloud.google.com/alloydb/docs/instance-delete) This does not affect your cluster's data. You can create a new primary instance after re-enabling the key, as described in the following section.

  2. [Use Cloud KMS to disable the key.](https://docs.cloud.google.com/kms/docs/enable-disable#disable)




## Enable a key

To enable a key, follow these steps:

  1. [Use Cloud KMS to enable the key](https://docs.cloud.google.com/kms/docs/enable-disable#enable).

  2. If you deleted your cluster's primary instance before disabling your key, [create a new primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create).




Enabling a key can take up to three hours to propagate to your cluster. The cluster's data becomes accessible as soon as this propagation happens.

## View audit logs for a Cloud KMS key

To view audit logs associated with a particular CMEK key, follow these steps:

  1. Make sure that [logging is enabled ](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project.

  2. Go to the **Logs Explorer** in the Google Cloud console.

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  3. Limit the log entries to your Cloud KMS key by adding the following lines to the query builder:
         
         resource.type="cloudkms_cryptokey"
         resource.labels.location="REGION"
         resource.labels.key_ring_id="KEYRING"
         resource.labels.crypto_key_id="KEY"
         

Replace the following:

     * REGION: the key's region—for example, `us-central1`
     * KEYRING: the ID of the key's Cloud KMS key ring
     * KEY: the Cloud KMS ID of the key
  4. Under normal operations, encrypt and decrypt operations are logged with `INFO` severity. These entries are logged when the instances in your AlloyDB cluster validate the Cloud KMS key, which occurs about every five minutes.

  5. If AlloyDB fails to access the key, the operations are logged as `ERROR`.




## View access justifications for a Cloud EKM key

If you [use a Cloud EKM key](https://docs.cloud.google.com/alloydb/docs/cmek#ekm), then you can use Key Access Justifications to view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For more information, see [View and act on justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/view-justifications).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
