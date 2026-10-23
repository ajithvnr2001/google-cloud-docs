---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/access-report/
title: Access reports from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:36.539542+00:00
---

# Access reports from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/access-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Access reports from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page provides instructions on how to access the appliance management console's built-in historical reports in CSV format that are exported to a Cloud Storage bucket. It also provides instructions on how to modify the data retention period of the reporting data.

## Modify data retention period

By default, the reporting data for your reports is retained as per the existing retention period defined in the report manager. By default, the retention period is set to one year. With **Modify data retention period** , you can extend the retention period up to 10 years and modify the retention period between 1 day and 10 years.

If you reduce the data retention period, you won't be able to retrieve the data for the period that has been reduced. For example, changing the data retention period from 10 years to 8 years results in the loss of reporting data for the oldest 2 years.

**Note:** Only a Backup and DR administrator can modify the data retention period. To modify the data retention period, ask your administrator to grant you the Backup and DR Admin (`roles/backupdr.admin`) IAM role.

Use the following instructions to modify the data retention period:

  1. Click the **Reports** tab and select **Export historical reports** from the drop-down menu.
  2. Click **Modify data retention period**.
  3. In the **Retain data for** the field, enter the retention period and select **Year** , **Month** , **Week** , or **Day** from the drop-down.
  4. Select the **Select to confirm that you would like to modify the data retention period** checkbox.
  5. Click **Save**.

It can take one day for the modified retention period to take effect.




## Export historical reports

To export historical reports, you need the following:

  * A Cloud Storage bucket. This bucket serves as the destination for the exported report. You can [Create a new Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) or use an existing bucket.
  * Assign the Storage Object Creator (`roles/storage.objectCreator`) IAM role to the bucket. This role provides permissions to access to the Cloud Storage bucket where the report is to be exported. Assigning the role to the bucket is a one-time activity.
  * Be assigned with the Backup and DR Backup User (`roles/backupdr.backupUser`) IAM role to export reports.



Use the following instructions to export historical reports to a Cloud Storage bucket:

  1. Click the **Reports** tab and select **Export historical reports** from the drop-down menu.
  2. Click the calendar_month icon and select **From** and **To** dates. The selectable **From** date is limited based on the retention period configured for your reports. The maximum **To** date that you can select is yesterday.

**Note:** You can only export two years of data at a time. To export more than two years of data, perform multiple export operations.
  3. From the **Report to export** section, select reports from one of the following categories that you want to export.

     * Audit
     * Jobs
     * Protection
     * Backup plan compliance
     * Summary
     * Utilization
  4. In the **Bucket name** field, enter the bucket name that you created to export the built-in reports. If you didn't export a report in the last 90 days, you'll need to re-enter the bucket name.

  5. To assign the permissions to the Cloud Storage bucket, do the following. This role provides access to the Cloud Storage bucket where the report is to be exported.

     1. Go to the Google Cloud console and click **Activate cloud shell**.
     2. Copy and paste the command that is displayed in the appliance management console. This role provides permissions to access the Cloud Storage bucket where the report is to be exported.
            
            gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member=SERVICE_ACCOUNT --role=roles/storage.objectCreator
            

Replace the following:

        * `BUCKET_NAME`: the name that is given to storage bucket.
        * `SERVICE_ACCOUNT`: the service account associated with storage bucket. For example, my-service-account@my-project.iam.gserviceaccount.com.
  6. After assigning the permissions, go to the appliance management console and select the **Prerequisites** checkbox.

  7. Click **Export**.

  8. Optional: Click **View details** to view the detailed export status of reports.

The reports are exported to a Cloud Storage **Buckets** in a CSV format.

**Note:** You cannot run more than one export at a time. If you attempt to initiate an export while an export is already in progress, it displays an error message.



## Access the exported reports in Cloud Storage bucket

Use the following instructions to access the exported reports in a Cloud Storage bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Select the bucket that you have used to export reports.
  3. Select a report and click **Download**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
