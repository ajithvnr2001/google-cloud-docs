---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-policy/
title: Create a backup policy \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:33.385763+00:00
---

# Create a backup policy  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a backup policy Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions about how to create a backup policy.

## Considerations

  * Each backup policy must retain a minimum of two daily backups.



## Create a new backup policy

Use the following instructions to create a backup policy using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Policies** , click **Backup policies**.

  3. In the **Backup policies** page, click **Create**.

  4. In the **Name** field, enter a name for the backup policy. The name must be unique to the project.

  5. Optional: in the **Description** field, enter a description for the backup policy.

  6. Click the **Region** drop-down, select the region of the backup vault storing your backups. Your choice is permanent.

  7. Using the **Daily, Weekly, and Monthly** tabs, configure your backup schedule:

For each interval (daily, weekly, and monthly), use the **Backups to keep** field to enter the amount of backups you want to keep.

  8. Optional: under the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.

  9. Click **Create**.




### gcloud
    
    
    gcloud netapp backup-policies create BACKUP_POLICY \
      --location=LOCATION \
      --description=DESCRIPTION \
      --enabled=TRUE_OR_FALSE \
      --daily-backup-limit=DAILY_BACKUP_LIMIT \
      --weekly-backup-limit=WEEKLY_BACKUP_LIMIT \
      --monthly_backup_limit=MONTHLY_BACKUP_LIMIT \
      --labels=foo=bar

Replace the following information:

  * `BACKUP_POLICY`: the name of the backup policy.

  * `LOCATION`: the location in which you want to create the backup policy.

  * `DESCRIPTION`: the description for the backup policy.

  * `TRUE_OR_FALSE`: mark as `TRUE` to enable backups or `FALSE` to disable backups.

  * `DAILY_BACKUP_LIMIT`: the number of daily backups in the backup policy.

  * `WEEKLY_BACKUP_LIMIT`: the number of weekly backups in the backup policy.

  * `MONTHLY_BACKUP_LIMIT`: the number of monthly backups in the backup policy.




For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-policies).

## What's next

[Create a backup](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
