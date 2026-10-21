---
url: https://docs.cloud.google.com/looker/docs/looker-core-scheduled-export/
title: Create a scheduled export job for a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:05.589599+00:00
---

# Create a scheduled export job for a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-scheduled-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a scheduled export job for a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

You can configure a scheduled export job for your Looker (Google Cloud core) instance to regularly back up its data, configurations, and content. Scheduled exports run every 24 hours, beginning at a start time that you set, store the exported data in a Cloud Storage bucket, and don't create downtime for your Looker (Google Cloud core) instance during the process.

A scheduled export includes all data, configurations, and content from an instance, with the following exceptions:

  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) data isn't exported.
  * [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) data isn't exported.

  * [Data Studio](https://docs.cloud.google.com/looker/docs/bi-connectors#looker_studio) reports are not exported.

  * Any Google Cloud console settings, which must be made in the Google Cloud console for each instance, are not exported. However, settings in the Looker **Admin** panel within the Looker (Google Cloud core) application are exported.

  * Any OAuth tokens that are stored in an instance are not exported. If OAuth is used for individual database connections, after import each user will have to log in again and refresh their tokens for any database connections that use OAuth.

  * If you export and import into a Looker (Google Cloud core) instance that uses a different [networking setup](https://docs.cloud.google.com/looker/docs/looker-core-networking-options) than the instance that created the export, you may need to configure your connections to external services differently.

  * If an export from an instance in one Google Cloud project is moved to an instance in a different project, [IAM permissions](https://docs.cloud.google.com/looker/docs/looker-core-access-control) to provide users with access to the instance need to be set in the new project.




The scheduled export process takes minutes to hours, depending on the size of the instance. While a scheduled export process is running, [import operations](https://docs.cloud.google.com/looker/docs/looker-core-import-export#importing) and [one-time exports](https://docs.cloud.google.com/looker/docs/looker-core-import-export#exporting) aren't available.

Once a scheduled export job is set up, you can set up a script to [import](https://docs.cloud.google.com/looker/docs/looker-core-import-export#importing) the exported data to a backup instance on a daily basis.

## Required role

To get the permissions that you need to create a scheduled export job for Looker (Google Cloud core), ask your administrator to grant you the following IAM roles on the project in which the instance was created: 

  * All: [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Before you begin

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the export artifact.
  2. [Create a customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/creating-keys) in Cloud Key Management Service. This is required to encrypt the data for the scheduled export, even if your instance does not use CMEK. The CMEK key must be in a different region from your Looker (Google Cloud core) instance, or it must be a global key.
  3. [Identify the service account](https://docs.cloud.google.com/looker/docs/looker-core-service-account) for your Looker (Google Cloud core) instance.
  4. Grant the following required Identity and Access Management (IAM) roles and permissions to the instance's service account: 
     * Grant the [`roles/storage.objectAdmin` role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectAdmin) on the Cloud Storage bucket that stores your export.
     * Grant the [`roles/cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) on the CMEK key that you use to encrypt your data.
     * Alternatively, you can create a custom role with the following permissions: 
       * `storage.objects.create`
       * `storage.objects.delete`
       * `cloudkms.cryptoKeyVersions.useToEncrypt`
       * `cloudkms.cryptoKeyVersions.useToDecrypt`



## Configure a scheduled export job

You can configure a scheduled export job using the Google Cloud console or `gcloud`.

### console

  1. In the Google Cloud console, go to the Looker (Google Cloud core) **Instances** page.

[ Go to Looker instances](https://console.cloud.google.com/looker/instances?mods=monitoring_api_prod)

  2. Click the name of the instance for which you want to schedule an export job.

  3. Click the **Export** tab.

  4. Expand the **Schedule export job** section and enter the following information:

     1. **Start time** : The time of day in local time (HH:MM) to perform the daily export.
     2. **Cloud Storage bucket** : The URI of your Cloud Storage bucket, for example: `gs://bucket-name/export-path`.
     3. **Cloud KMS key** : Select the Cloud Key Management Service key that will be used to encrypt the instance data.
  5. Click **Set schedule**.




### gcloud

  1. To configure a periodic export, run the following `gcloud` command:


    
    
    gcloud looker instances update INSTANCE_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --periodic-export-gcs-uri="gs://BUCKET_NAME/EXPORT_PATH" \
        --periodic-export-kms-key="KMS_KEY_NAME" \
        --periodic-export-start-time="TIME"
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/docs/overview#projects).
  * `REGION`: the region where your instance is located.
  * `BUCKET_NAME`: the name of your Cloud Storage bucket.
  * `EXPORT_PATH`: the path within the bucket for the export artifact.
  * `KMS_KEY_NAME`: the [full resource name](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) of your CMEK key.
  * `TIME`: the time of day in UTC (HH:MM) to perform the daily export.



## Verify the export configuration

After you set a schedule, you can view the scheduled export job configuration on the **Instance details** page.

  1. In the Google Cloud console, go to the Looker (Google Cloud core) **Instances** page.

[ Go to Looker instances](https://console.cloud.google.com/looker/instances?mods=monitoring_api_prod)

  2. Click the name of your instance.

  3. On the **Instance details** page, view the **Export schedule** configuration, which includes the scheduled start time each day in local time. The start time includes a link to the instance's **Export** page.




## Stop a periodic export

To stop a periodic export from occurring, clear the configuration fields.

### console

  1. In the Google Cloud console, go to the **Instances** page.

[ Go to Looker instances](https://console.cloud.google.com/looker/instances?mods=monitoring_api_prod)

  2. Click the name of the instance.

  3. Click the **Export** tab.

  4. In the **Set schedule for periodic export** section, clear the values for the **Cloud Storage bucket** , **Customer-managed encryption key** , and **Time** fields.

  5. Click **Clear schedule**.




### gcloud

  1. To stop a periodic export, run the following `gcloud` command:


    
    
    gcloud looker instances update INSTANCE_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --clear-periodic-export-config
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/docs/overview#projects).
  * `REGION`: the region where your instance is located.



## What's next

  * Learn how to [import Looker (Google Cloud core) instance data from Cloud Storage](https://docs.cloud.google.com/looker/docs/looker-core-import-export#importing).
  * [Troubleshoot](https://docs.cloud.google.com/looker/docs/looker-core-import-export#troubleshooting) export or import errors. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
