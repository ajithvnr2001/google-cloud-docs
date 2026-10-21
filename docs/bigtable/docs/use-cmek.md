---
url: https://docs.cloud.google.com/bigtable/docs/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:13.362773+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use customer-managed encryption keys (CMEK)

This page describes how to perform tasks related to [customer-managed encryption keys (CMEK) for Bigtable](https://docs.cloud.google.com/bigtable/docs/cmek). For more information about CMEK in general, including when and why to enable it, see the [Cloud KMS documentation](https://docs.cloud.google.com/kms/docs/cmek).

We recommend that you use the Google Cloud console for all key management tasks. If you plan to use the Google Cloud CLI, [install the gcloud CLI for Bigtable](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk).

## Prepare your CMEK keys

Before you can create a CMEK-protected Bigtable resource, you need to complete the following steps to create a CMEK key for each region that the instance's clusters will be in:

  1. Create (or retrieve) a Bigtable service agent.
  2. Create a CMEK key.
  3. Configure IAM settings for that key.

**Note:** The `gcloud` commands on this page show placeholders for two Google Cloud projects: the project that contains Bigtable resources, `CBT_PROJECT`, and the project that contains your CMEK key(s), `KMS_PROJECT`. However, you can use the same project for your Bigtable resources and CMEK keys.

### Create a Bigtable service agent

Before you create a CMEK key, you must have a Bigtable [service agent](https://docs.cloud.google.com/iam/docs/service-agents), which Bigtable uses to access the key.

###  Console 

You can't create a service agent in the Google Cloud console. Bigtable might automatically provision a service agent during the instance creation workflow when you create or select your key. Additionally, when you select a customer-managed key, the console checks for the service agent. One of the following results might happen:

  * If the service agent exists, you are prompted to grant it the [ Cloud KMS Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles) role.
  * If the service agent is not automatically provisioned or you encounter errors during key selection, use the **gcloud** tab to manually create the agent and grant the necessary permissions.



###  gcloud 

  1. Run the [gcloud services identity create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command to view the service agent that Bigtable uses to access the CMEK key on your behalf. This command creates the service account if it does not already exist, then displays it.
         
         gcloud beta services identity create \
             --service=bigtableadmin.googleapis.com \
             --project CBT_PROJECT
         

Replace `CBT_PROJECT` with the project that contains your Bigtable resources.

The command displays the service agent ID, which is formatted like an email address. Record the output email string, because you'll use it in a later step.
         
         Service identity created:
         service-xxx@gcp-sa-bigtable.iam.gserviceaccount.com
         




### Create a key

You can use a key created directly in Cloud KMS or an externally managed key that you make available with [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

  1. In the Google Cloud project where you want to manage your keys:

     1. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

     2. Create a key ring and a key using one of the following options:

        * [Create the key ring and key directly in Cloud KMS](https://docs.cloud.google.com/kms/docs/creating-keys).
        * Use an externally-managed key. [Create the external key](https://docs.cloud.google.com/kms/docs/ekm-internet#create_external_key) and then [create an Cloud EKM key](https://docs.cloud.google.com/kms/docs/ekm-internet#create_ekm_key) to make the key available through Cloud KMS.

The Cloud KMS [key location](https://docs.cloud.google.com/kms/docs/locations) must be the same as the Bigtable cluster that it will be used with. For example, if you create a key ring and key in `us-central1` (Iowa), then clusters in `us-central1-a`, `us-central1-b`, and `us-central1-c` can be protected by keys from that key ring.




### Configure IAM settings for the key

###  Console 

To grant an Cloud KMS role to your service agent, do the following. You are also able to grant permission at the key or key-ring level if you want lower granularity.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Add**.

  3. Enter the email-formatted ID for your Bigtable service agent.

  4. Select the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

  5. Click **Save**.




###  gcloud 

  1. Grant the `cloudkms.cryptoKeyEncrypterDecrypter` role to your service agent:
         
         gcloud kms keys add-iam-policy-binding KMS_KEY \
             --keyring KMS_KEYRING\
             --location KMS_LOCATION \
             --member serviceAccount:SERVICE_ACCOUNT_EMAIL \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
             --project KMS_PROJECT
         

Provide the following: 

     * `KMS_KEY`: the name you assigned to the key
     * `KMS_KEYRING`: the KMS key ring that contains the key
     * `KMS_LOCATION` : the region that contains the key ring
     * `SERVICE_ACCOUNT_EMAIL`: the email-formatted identifier for the service agent that you are granting access to
     * `KMS_PROJECT`: the project that contains the key



## Create a CMEK-enabled instance

After your CMEK keys are created and configured, you can create a CMEK-protected instance. Existing Bigtable instances that are protected by Google default encryption cannot be converted to use CMEK; you can only choose an encryption type and key at the time of creation.

Follow the steps on [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) to create your CMEK-protected instance.

## View the key in use

Information on key versions comes from the `encryption_info` field.

**Note:** When an instance's key version changes, the change is not immediately propagated to the table's encryption information. There might be a delay from when the change occurs to when the change appears.

To view the CMEK key version information for a table, complete the following steps:

###  Console 

  1. Go to the Bigtable instances page in the Google Cloud console.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the name of the instance that contains the table to open the **Instance Details** page and view the list of clusters in the instance.

  3. Next to a cluster ID, click the _key name_ under **Encryption key** to view the **Versions** page for the cluster's key.




###  gcloud 

For each cluster, you can confirm its CMEK configuration as follows:
    
    
        gcloud bigtable clusters describe CLUSTER_ID \
            --instance INSTANCE_ID --project CBT_PROJECT
    

Provide the following: 

  * `CLUSTER_ID`: the permanent identifier for the cluster
  * `INSTANCE_ID`: the permanent identifier for the instance
  * `CBT_PROJECT`: the project that contains your Bigtable resources



The command displays output similar to the following:
    
    
        defaultStorageType: SSD
        encryptionConfig:
          kmsKeyName: projects/cloud-kms-project/locations/us-central1/keyRings/cloud-bigtable-keys/cryptoKeys/my-cmek-key
        location: projects/cloud-bigtable-project/locations/us-central1-a
        name: projects/cloud-bigtable-project/instances/cmek-test-instance/clusters/my-cluster
        serveNodes: 1
        state: READY
    

## Disable a key

Disabling a CMEK key version suspends access to all data protected by that key version. [Destroying a key version](https://docs.cloud.google.com/kms/docs/destroy-restore) is the permanent (after 24 hours) counterpart of this action. Always disable _all_ of the keys for an instance rather than disabling only the keys for one or some clusters.

**Note:** Bigtable resources that are protected by a key version that you or another administrator have made inaccessible are automatically deleted after 30 consecutive days. Destroying a key or revoking the Encrypter/Decrypter role also triggers this 30-day time to live (TTL).**Important:** Always disable **all key versions** , not just the current primary version, when disabling a key. Because Bigtable is a distributed system, multiple key versions may be in use at any time, including while a key rotation process is underway. For this reason, disabling the current primary key version may not prevent access to all the data that you intend to restrict.

###  Console 

**This is the recommended method.** Using the Google Cloud console lets you disable all versions of a key at once.

Follow [these instructions](https://docs.cloud.google.com/kms/docs/enable-disable) for each key version.

###  gcloud 

We recommend that you **use the Google Cloud console to disable keys.** If you wish to use the Google Cloud CLI instead, run the following commands.

  1. List all versions of the CMEK key:
         
         gcloud kms keys versions list --key KMS_KEY \
             --keyring KMS_KEYRING --location KMS_LOCATION \
             --project KMS_PROJECT
         

Provide the following: 

     * `KMS_KEY`: the name of the CMEK key
     * `KMS_KEYRING`: the KMS key ring that contains the key
     * `KMS_LOCATION`: the region that contains the key ring
     * `KMS_PROJECT`: the project that contains the key

The output is similar to the following:
    
    NAME                                  STATE
    KMS_KEY_NAME/cryptoKeyVersions/1      ENABLED
    KMS_KEY_NAME/cryptoKeyVersions/2      ENABLED
    KMS_KEY_NAME/cryptoKeyVersions/3      ENABLED
    KMS_KEY_NAME/cryptoKeyVersions/4      ENABLED
    

  2. Disable **all** versions:
         
         for $KV in 1 2 3 4;
         do
         gcloud kms keys versions disable KV --key KMS_KEY \
             --keyring KMS_KEYRING --location KMS_LOCATION \
             --project KMS_PROJECT;
         done
         

Provide the following: 

     * `1 2 3 4`: the versions that you are disabling
     * `KMS_KEY`: the name of the CMEK key
     * `KMS_KEYRING`: the KMS key ring that contains the key
     * `KMS_LOCATION`: the region that contains the key ring
     * `KMS_PROJECT`: the project that contains the key

Listing all key versions again will show their state flipped to `DISABLED`, though it may take up to 4 hours for Bigtable to act on this state change.

  3. [Optional] To confirm the status of a disabled CMEK after you've waited 4 hours, run the following command:
         
         gcloud bigtable instances tables describe TABLE_ID \
              --instance INSTANCE_ID --view ENCRYPTION \
              --project CBT_PROJECT
         

Provide the following: 

     * `TABLE_ID`: the permanent identifier for the table
     * `INSTANCE_ID`: the permanent identifier for the instance
     * `CBT_PROJECT`: the project that contains your Bigtable resources

The command displays output similar to the following:
    
    clusterStates:
      CLUSTER:
        encryptionInfo:
        - encryptionStatus:
            code: 9
            details:
            - '@type': type.googleapis.com/google.rpc.PreconditionFailure
              violations:
              - subject: KMS_KEY_NAME/cryptoKeyVersions/<int>
                type: KEY_DISABLED
            message: KMS_KEY_NAME is not enabled, current state is: DISABLED.
          encryptionType: CUSTOMER_MANAGED_ENCRYPTION
          kmsKeyVersion: KMS_KEY_NAME/cryptoKeyVersions/<int>
    name: projects/CBT_PROJECT/instances/INSTANCE/tables/TABLE
    

  4. [Optional] To verify that the clusters in the instance are disabled, run the following command:
         
         gcloud bigtable clusters list --instances INSTANCE_ID
             --project CBT_PROJECT
         

Provide the following: 

     * `INSTANCE_ID`: the permanent identifier for the instance
     * `CBT_PROJECT`: the project that contains your Bigtable resources

The command displays output similar to the following:
    
    NAME              ZONE           NODES  STORAGE    STATE
    my-cluster        us-central1-a  1      SSD        DISABLED
    my-other-cluster  us-central1-b  1      SSD        DISABLED
    




## Enable a key

If a key version has been disabled, you can re-enable it to regain access to your Bigtable resources. This option is available for 30 days from the time the key version is disabled.

**Important:** Because Bigtable is a distributed system, multiple key versions might be in use at any time, such as when a key is automatically rotated to a new version. To avoid unexpected or unintended behavior and ensure that all resources are correctly enabled, **always enable all key versions** , not just the current primary version, when enabling a key.

###  Console 

**This is the recommended method.** Using the Google Cloud console lets you enable all versions of a key at once.

Follow [these instructions](https://docs.cloud.google.com/kms/docs/enable-disable) for each key version.

###  gcloud 

We recommend that you **use the Google Cloud console to enable keys**. If you wish to use the Google Cloud CLI instead, run the following commands.

  1. View the versions list to identify all the versions of the key:
         
         gcloud kms keys versions list --key KMS_KEY \
             --keyring KMS_KEYRING --location KMS_LOCATION \
             --project KMS_PROJECT
         

Provide the following: 

     * `KMS_KEY`: the name of the CMEK key
     * `KMS_KEYRING`: the KMS key ring that contains the key
     * `KMS_LOCATION`: the region that contains the key ring
     * `KMS_PROJECT`: the project that contains the key

The command displays output similar to the following:
    
    NAME                                  STATE
    KMS_KEY_NAME/cryptoKeyVersions/1      DISABLED
    KMS_KEY_NAME/cryptoKeyVersions/2      DISABLED
    KMS_KEY_NAME/cryptoKeyVersions/3      DISABLED
    KMS_KEY_NAME/cryptoKeyVersions/4      DISABLED
    

Run the `kms keys versions enable` command, providing **all versions** that are listed. Using the example output, the command looks similar to the following:
    
    for $KV in 1 2 3 4;
    do
    gcloud kms keys versions enable KV --key KMS_KEY \
        --keyring KMS_KEYRING --location KMS_LOCATION \
        --project KMS_PROJECT;
    done
    

Provide the following: 

     * `1 2 3 4`: the versions that you are disabling
     * `KMS_KEY`: the name of the CMEK key
     * `KMS_KEYRING`: the KMS key ring that contains the key
     * `KMS_LOCATION`: the region that contains the key ring
     * `KMS_PROJECT`: the project that contains the key

Listing the key versions again shows their state flipped to `ENABLED`.




## View audit logs for a Cloud KMS key

Before you enable Cloud KMS Data Access audit logs, you should be familiar with [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

[Cloud KMS Data Access audit logs](https://docs.cloud.google.com/kms/docs/audit-logging) show you when Bigtable or any other products that are configured to use your CMEK key make encrypt/decrypt calls to Cloud KMS. Bigtable does not issue an encrypt/decrypt call on every data request, but instead maintains a poller that checks the key periodically. The polling results appear in the audit logs.

You can set up and interact with the audit logs in the [Google Cloud console](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console):

  1. Make sure that [logging is enabled](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project.

  2. Go to **Cloud Logging** in the Google Cloud console.

[Go to Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary)

  3. Limit the log entries to your Cloud KMS key by adding the following lines to the Query builder:
         
         resource.type="cloudkms_cryptokey"
         resource.labels.key_ring_id = KMS_KEYRING
         resource.labels.crypto_key_id = KMS_KEY
         

Provide the following: 

     * `KMS_KEY`: the name of the CMEK key
     * `KMS_KEYRING`: the KMS key ring that contains the key

The log shows a couple log entries about every five minutes per table in each cluster. The log entries look similar to these examples:
    
    Info 2021-03-20 08:02:24.869 EDT Cloudkms.googleapis.com Decrypt projects/cloud-kms-project/locations/us-central1/keyRings/cloud-bigtable-keys/cryptoKeys/my-cmek-key service-123456789123@gcp-sa-bigtable.iam.gserviceaccount.com
    audit_log, method: "Decrypt", principal_email: "service-1234567891011@gcp-sa-bigtable.iam.gserviceaccount.com"
    
    Info 2021-03-20 08:02:24.913 EDT Cloudkms.googleapis.com Encrypt projects/cloud-kms-project/locations/us-central1/keyRings/cloud-bigtable-keys/cryptoKeys/my-cmek-key service-123456789123@gcp-sa-bigtable.iam.gserviceaccount.com
    audit_log, method: "Encrypt", principal_email: "service-123456789123@gcp-sa-bigtable.iam.gserviceaccount.com"
    




See [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs) for details about interpreting audit logs.

## View key usage

Cloud KMS lets you view the following information about the Bigtable resources that your keys protect.

  * **Key usage summary** : Includes information about the number of protected resources and projects that use the key.
  * **Key usage detail** : Identifies the resources that a key protects and the resources that depend on the key.



The following Bigtable resources are supported:

  * `bigtableadmin.googleapis.com/Backup`
  * `bigtableadmin.googleapis.com/Cluster`
  * `bigtableadmin.googleapis.com/Table`
  * `bigtableadmin.googleapis.com/AuthorizedView`



The following Bigtable resources are supported as **Preview** :

  * `bigtableadmin.googleapis.com/LogicalView`
  * `bigtableadmin.googleapis.com/MaterializedView`



For more information about viewing key usage, see [View key usage information](https://docs.cloud.google.com/kms/docs/view-key-usage#view-usage).

## View the encryption status of a table

###  Console 

You are not able to view the encryption status of a table in the Google Cloud console.

###  gcloud 

To view the CMEK details on a table, set `view` to `ENCRYPTION` or `FULL`. The response includes the in-use key version and its status as seen by Bigtable.
    
    
        gcloud alpha bigtable instances tables describe TABLE_ID \
            --instance INSTANCE_ID --view ENCRYPTION \
            --project CBT_PROJECT
    

Provide the following: 

  * `TABLE_ID`: the permanent identifier for the cluster
  * `INSTANCE_ID`: the permanent identifier for the instance that contains the backup
  * `CBT_PROJECT`: the project that contains your Bigtable resources



The command displays output similar to the following:
    
    
        clusterStates:
          my-cluster:
            encryptionInfo:
            - encryptionStatus: {}
              encryptionType: CUSTOMER_MANAGED_ENCRYPTION
              kmsKeyVersion: KMS_KEY_NAME/cryptoKeyVersions/4
          my-other-cluster:
            encryptionInfo:
            - encryptionStatus: {}
              encryptionType: CUSTOMER_MANAGED_ENCRYPTION
              kmsKeyVersion: KMS_KEY_NAME/cryptoKeyVersions/4
          name: projects/cloud-bigtable-project/instances/cmek-test-instance/tables/my-table
    

## View the encryption details for a backup

A backup stays pinned to its original key version. [Key version rotations](https://docs.cloud.google.com/kms/docs/key-rotation) in Cloud KMS don't rotate the versions used to decrypt backups.

###  Console 

  1. Go to the Bigtable instances page in the Google Cloud console.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance name to open the **Instance Details** page.

  3. In the left navigation pane, click **Backups**.




The key name and key version for each backup are listed under **Customer managed key**.

###  gcloud 

Run the following command to view encryption info for a backup.
    
    
        gcloud alpha bigtable backups describe BACKUP_ID \
            --instance INSTANCE_ID --cluster CLUSTER_ID \
            --project CBT_PROJECT
    

Provide the following: 

  * `BACKUP_ID`: the ID assigned to the backup
  * `CLUSTER_ID`: the permanent identifier for the cluster
  * `INSTANCE_ID`: the permanent identifier for the instance that contains the backup
  * `CBT_PROJECT`: the project that contains your Bigtable resources



The command returns output similar to the following. The `kmsKeyVersion` is the CMEK key version that the backup is pinned to. The status of the key version is not reported.
    
    
        encryptionInfo:
          encryptionStatus:
            code: 2
            message: Status of the associated key version is not tracked.
          encryptionType: CUSTOMER_MANAGED_ENCRYPTION
          kmsKeyVersion: KMS_KEY_NAME/cryptoKeyVersions/3
        endTime: '2020-09-01T00:03:26.568600Z'
        expireTime: '2020-09-02T00:03:25.436473Z'
        name: projects/cloud-bigtable-project/instances/cmek-test-instance/clusters/my-cluster/backups/my-backup
        sizeBytes: '3780'
    

## What's next

  * [Read the overview of Bigtable CMEK.](https://docs.cloud.google.com/bigtable/docs/cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
