---
url: https://docs.cloud.google.com/bigtable/docs/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:05.727208+00:00
---

# Customer-managed encryption keys (CMEK)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customer-managed encryption keys (CMEK)

By default, Bigtable encrypts customer content at rest. Bigtable handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Bigtable. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Bigtable resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Bigtable clusters or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Bigtable. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

Autokey creates a default key when you create Bigtable clusters.

To set up CMEK manually, see [Use CMEK](https://docs.cloud.google.com/bigtable/docs/use-cmek).

## Features

  * **Security** : CMEK provides the same level of security as Google's default encryption but provides more administrative control.

  * **Data access control** : Administrators can rotate, manage access to, and disable or destroy the key used to protect [data at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) in Bigtable.

  * **Auditability:** All actions on your CMEK keys are logged and viewable in [Cloud Logging](https://docs.cloud.google.com/kms/docs/audit-logging). Cloud EKM keys support [Key Access Justification](https://docs.cloud.google.com/kms/docs/ekm-access-justification), which adds a justification field to all key requests. With select external key management partners, you can automatically approve or deny these requests, based on the justification.

  * **Comparable performance:** Bigtable CMEK-protected instances offer comparable performance to Bigtable instances that use Google default encryption.

  * **Flexibility:** You can use the same CMEK key in multiple projects, instances, or clusters, or you can use separate keys, depending on your business needs.

  * **Cross-region protection:** You can enable CMEK in instances that have clusters in any region where Bigtable is available. Each cluster is protected by a CMEK key in that cluster's region.




## Pricing

Cloud KMS charges for the cost of the key and any cryptographic operations performed using that key. See [Cloud KMS pricing](https://docs.cloud.google.com/kms/pricing) for details.

You're billed for the operation costs when Bigtable asks the Cloud KMS key to perform an encryption or decryption operation. Each encryption or decryption request is sent from every table on every cluster in the instance. Because Bigtable uses [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption), these costs per table are generally low, given the small number of expected cryptographic operations. If you store many tables in a CMEK-protected instance, your costs are higher.

There are no additional Bigtable costs for using CMEK-enabled instances.

## What is protected with CMEK

In a CMEK-protected instance, Bigtable uses your CMEK key to protect your data at rest. This includes data in all tables in the cluster. Data stored on both [HDD and SSD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd) is protected.

Some data is protected by Google default encryption at rest and not by the CMEK key:

  * A subset of row keys that mark range boundaries and are used for routing
  * Debugging data including core dumps and operational logs
  * Data in transit or in memory
  * A subset of timestamp values used for garbage collection



Bigtable uses [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption) for data at rest. The CMEK key is used as a key encryption key (KEK) to encrypt other keys used by Bigtable. When you rotate the CMEK key, Bigtable only needs to re-encrypt the intermediate keys.

## Enabling CMEK

At a high level, to use CMEK with Bigtable, you follow these steps:

  1. Create and configure a CMEK key in each region where your instance's clusters are going to be.
  2. Create a new Bigtable instance, selecting a CMEK key for each cluster in the instance. A cluster's CMEK key must be in the same region as the cluster.
  3. Schedule a [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) for each key.



Applications that use Bigtable do not need to specify a key or encryption config when reading, writing, or deleting data. Bigtable is able to access the key on your behalf after you grant the [Cloud KMS Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) role to the Bigtable [service agent](https://docs.cloud.google.com/iam/docs/service-agents).

For detailed instructions, see [Use CMEK](https://docs.cloud.google.com/bigtable/docs/use-cmek).

You can use the following when you work with CMEK for Bigtable.

  * [Google Cloud console](https://console.cloud.google.com/)
  * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs)
  * All generally available (GA) [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) that call the Cloud Bigtable APIs.



You can also access the [Cloud Bigtable Admin API](https://docs.cloud.google.com/bigtable/docs/reference/service-apis-overview) directly, but we strongly recommend that you do so only if you cannot use a Bigtable client library that makes CMEK calls to the API.

## Key management

Key management operations are performed using Cloud KMS. Bigtable cannot detect or act upon any key changes until they are propagated by Cloud KMS. Some operations, such as disabling or destroying a key, can take up to 4 hours to propagate; changes to a key's permissions usually propagate more quickly.

After you create at least one table in a CMEK-protected instance, Bigtable validates the key for each table in each cluster every 5 minutes.

If Bigtable detects a disabled key, **it disables one cluster at a time in a cascading fashion until all clusters in the instance are disabled.** After the first cluster reports a key is disabled or destroyed and until the instance is disabled, some data requests might succeed and others return an error. Any data operations that are sent to a cluster that has been disabled return a `FAILED_PRECONDITION` or `NOT_FOUND` error.

Additionally, because Bigtable replication is eventually consistent, it's possible that a cluster might have acknowledged a write request but not yet replicated it to the other clusters in the instance before it was disabled.

The Bigtable process of automatically disabling all clusters in an instance after one key is disabled can take up to several hours. To avoid this state, we recommend that you always disable all of an instance's keys at the same time.

**Key Point:** Always disable the keys for every cluster in the instance at the same time. Don't disable one and wait for Bigtable to disable the rest.

When a Bigtable cluster is disabled, the following administrator operations are restricted for the entire instance:

  * Creating a cluster
  * Deleting a cluster
  * Creating a table
  * Modifying a column family
  * Restoring a table



You are still able to delete the instance, delete a table, and delete a backup.

If Bigtable's calls to Cloud KMS detect that a formerly disabled key has been re-enabled, Cloud KMS restores access to the Bigtable cluster automatically.

If a Cloud KMS key has been destroyed, then any Bigtable instance that has a cluster that was encrypted with that key becomes permanently inaccessible.

**Caution:** If a Cloud KMS key becomes inaccessible due to configuration changes such as IAM policy or VPC-SC setting, the cluster will be disabled. Read and write requests will be blocked until the key becomes accessible again after fixing the configuration.**Caution:** If a cluster remains disabled for more than 30 consecutive days, Bigtable automatically deletes it. To avoid permanent data loss, don't leave CMEK keys in an inaccessible state for an extended time.**Warning:** If a Cloud KMS key is destroyed and cannot be recovered, any Bigtable cluster encrypted with that key becomes permanently inaccessible.

## How an unavailable key status is handled

In rare scenarios, such as during periods when Cloud KMS is unavailable, Bigtable may be unable to retrieve the status of a key from Cloud KMS.

If a Bigtable cluster is protected by a key that is enabled at the time at which Bigtable is first unable to communicate with Cloud KMS, Bigtable continues to support full instance operations on a best-effort basis for up to one hour, to minimize the impact of any such incident on your workload.

After an hour, if Bigtable is still unable to connect with Cloud KMS, Bigtable begins taking the instance offline as a protective measure. The data in your Bigtable instance remains inaccessible until your instance can reconnect with Cloud KMS and Cloud KMS responds that the key is active.

Conversely, if a cluster in your Bigtable instance is protected by a key that was disabled prior to the point at which Bigtable is first unable to communicate with Cloud KMS, your instance remains inaccessible until it is able to reconnect to Cloud KMS and you have re-enabled your key.

## External key considerations

When you use a Cloud EKM, Google has no control over the availability of your externally managed key in the external key management partner system.

If the externally managed key is unavailable, Bigtable continues to support cluster operations on a best-effort basis for up to one hour.

After an hour, if Bigtable is still unable to connect with Cloud KMS, it begins taking the instance offline as a protective measure. The data in your Bigtable instance remains inaccessible until the instance can reconnect with Cloud KMS and Cloud KMS responds that the external key is active.

If you plan to use an external key for a Bigtable instance that has clusters in more than one region, make sure your key is supported in those regions. For details, see [External key managers and regions](https://docs.cloud.google.com/kms/docs/ekm#regions). Additionally, you should not use a combination of external and non-external keys in the same instance.

To learn more about using external keys with Cloud Key Management Service, see [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm).

## Organization policies

Bigtable supports organization policy constraints to help ensure CMEK usage across an organization. For details on how to use organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## Backups

Like other data, a backup is protected by the CMEK key for the cluster that the backup is stored on. New tables that are restored from a backup are protected by the CMEK key or keys for the cluster where they are restored. For further details about how CMEK affects backups and restore operations, see [Backups](https://docs.cloud.google.com/bigtable/docs/backups). To learn how to create or restore from a backup, see [Manage backups](https://docs.cloud.google.com/bigtable/docs/managing-backups).

## Logging

You can audit the requests that Bigtable sends to Cloud KMS on your behalf in [Cloud Logging](https://docs.cloud.google.com/kms/docs/audit-logging), if you have [enabled Cloud KMS audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project. You can expect a few log entries every 5 minutes or so per table in each cluster.

## Limitations

  * CMEK can only be configured at the cluster level. You cannot configure CMEK on backups, tables, or app profiles.

  * A cluster's CMEK key must be in the same region as the cluster. When you create a [Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings), be sure to select the region that corresponds with your planned Bigtable [zonal configuration](https://docs.cloud.google.com/bigtable/docs/locations).

  * The encryption configuration of a Bigtable resource (an instance, cluster, table or backup) is immutable.

    * Non-CMEK instances cannot be converted to use CMEK.
    * CMEK instances cannot be converted to use Google default encryption.
    * Clusters created with a CMEK key cannot be reconfigured to use a different key.
  * CMEK-protected Bigtable resources (instances, clusters, tables, or backups) tied to a key that has been made inaccessible as the result of a user-triggered action (such as disabling or destroying a key, or by revoking the Encrypter/Decrypter role) for more than 30 consecutive days are **automatically deleted**.

  * If you re-enable a disabled CMEK key to restore access to Bigtable instances protected by that key, some Data API requests might time out while your data is brought back online.

  * For up to five minutes after a table is created in a CMEK-protected instance, the key version and key status might be reported as unknown. However, any data written to the table is still protected with the CMEK key during that time.

  * Disabling or deleting only one version instead of all versions of a key that Bigtable uses can result in unpredictable behavior. Always disable or delete **all versions** of a CMEK key.




## What's next

  * [Learn how to use CMEK with Bigtable.](https://docs.cloud.google.com/bigtable/docs/use-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
