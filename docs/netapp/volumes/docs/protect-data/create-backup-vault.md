---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-vault/
title: Create a backup vault \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:05.205415+00:00
---

# Create a backup vault  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a backup vault.

## Create a backup vault

Use the following instructions to create a backup vault using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backup vaults**.

  3. In the **Backup vaults** page, click **Create**.

  4. In the **Name** field, enter a name for the backup vault. Your backup vault name must be unique to the region, use lowercase letters, numbers, hyphens, and start with a letter. Your choice is permanent.

  5. Optional: in the **Description** field, enter a description for the backup vault.

  6. Use the **Region** drop-down menu to select a location for the backup vault. Make sure that the location you choose is the same region where the volumes you want to back up are located.

  7. Under **Type** , select one of the following:

     * Select **In-region** to store backups in the same region as the volume.

     * Select **Cross-region** to specify a different region for storing the backups. From the **Destination region** drop-down menu, select your destination region.

**Note:** Cross-region backup vaults are supported for the Flex Unified, Standard, Premium, and Extreme service levels and aren't available for the Flex File service level.

To view details about the types, click **Compare the backup vault types**.

  8. Optional: under **Prevent backup deletion** , complete the following steps:

     1. Select the **Enable minimum enforced retention** checkbox.

**Important:** Your selection is permanent.
     2. Enter the minimum number of days the backups in the vault are retained in the **Minimum enforced retention days** field. The value must be between 2 to 5475 days. This value can only be increased, but can't be decreased.

     3. Under **Types of backups to retain** , select the backup types you want to retain from the following. You must select at least one backup type.

        * **Daily**

        * **Weekly**

        * **Monthly**

        * **Manual**

**Important:** Your selection is permanent.
  9. Optional: in the **Encryption** section, choose one of the following encryption key options:

     * **Google-managed encryption key**. This is the default option.

     * **Customer-managed encryption key (CMEK)**

       * For **In-region** backup, select a CMEK policy located in the same region as the backup.

       * For **Cross-region** backup, select a CMEK policy located in the destination region of the backup.

  10. Optional: in the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.

  11. Click **Create**.




### gcloud

Create an in-region backup vault:
    
    
    gcloud netapp backup-vaults create BACKUP_VAULT \
      --location=LOCATION \
      --backup-vault-type=IN_REGION \
      --description=DESCRIPTION \
      --labels=foo=bar

Create an in-region backup vault with customer-managed encryption key (CMEK):
    
    
    gcloud netapp backup-vaults create BACKUP_VAULT \
      --location=LOCATION \
      --backup-vault-type=IN_REGION \
      --kms-config=projects/PROJECT_ID/locations/LOCATION/kmsConfigs/KMS_NAME \
      --description=DESCRIPTION \
      --labels=foo=bar

Create a cross-region backup vault:
    
    
    gcloud beta netapp backup-vaults create BACKUP_VAULT \
      --location=LOCATION \
      --backup-vault-type=CROSS_REGION \
      --backup-region=REMOTE_LOCATION \
      --description=DESCRIPTION \
      --labels=foo=bar

Create a cross-region backup vault with customer-managed encryption key (CMEK):
    
    
    gcloud netapp backup-vaults create BACKUP_VAULT \
      --location=LOCATION \
      --backup-vault-type=CROSS_REGION \
      --backup-region=REMOTE_LOCATION \
      --kms-config=projects/PROJECT_ID/locations/REMOTE_LOCATION/kmsConfigs/KMS_NAME \
      --description=DESCRIPTION \
      --labels=foo=bar

Create a backup vault with deletion prevention:
    
    
    gcloud beta netapp backup-vaults create BACKUP_VAULT \
      --location=LOCATION \
      --backup-region=REMOTE_LOCATION \
      --backup-retention-policy=\
       backup-minimum-enforced-retention-days=DAYS, \
       daily-backup-immutable=FALSE, \
       weekly-backup-immutable=TRUE, \
       monthly-backup-immutable=FALSE, \
       manual-backup-immutable=FALSE, \
      --description=DESCRIPTION \
      --labels=foo=bar

Replace the following information:

  * `BACKUP-VAULT`: the name of the backup vault.

  * `LOCATION`: the location in which you want to create the vault.

  * `REMOTE_LOCATION`: the location of the cross-region destination backup vault.

  * `BACKUP_RETENTION_POLICY`: a parameter block describing the details of the configuration:

    * Backup-minimum-enforced-retention-days: number of days to retain the specified backup types.

    * Available backup types are: **daily-backup-immutable** , **weekly-backup-immutable** , **monthly-backup-immutable** , and **manual-backup-immutable**. To enable the retention period for a specific type, set its value to **true**. Note that at least one backup type must have its retention period enabled. When you enable a backup type, you can't disable it.

  * `KMS_NAME`: the name of the CMEK policy.

  * `DESCRIPTION`: the description for the backup vault.




For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults).

## What's next

[Create a backup policy](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
