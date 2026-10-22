---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/configure-and-manage-trial/
title: Configure and manage the 30-day introductory trial for Storage Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:26.044502+00:00
---

# Configure and manage the 30-day introductory trial for Storage Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/configure-and-manage-trial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Configure and manage the 30-day introductory trial for Storage Intelligence Stay organized with collections  Save and categorize content based on your preferences. 

To gain insights into your Cloud Storage usage and costs, you can start a [30-day introductory trial for Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview). This document explains how you can configure and disable this trial. Starting the trial activates Storage Intelligence and automatically creates a [Storage Insights dataset configuration](https://docs.cloud.google.com/storage/docs/insights/datasets). You can use this configuration to analyze your storage data. To learn how to use these datasets, see [Use Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/configure-datasets). You can configure or disable this trial at any time during the 30-day period.

## Required roles

The following table shows the required IAM roles and permissions for configuring the 30-day introductory trial for Storage Intelligence operations:

Roles required | Permissions required  
---|---  
Ask your administrator to grant you _any_ of the following IAM roles on either a project, a folder, or an organization within the [Google Cloud Resource Hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy):

  * Owner `(roles/owner)`
  * Storage Admin `(roles/storage.admin)`

| `storage.intelligenceConfigs.update`  
Ask your administrator to grant you the following IAM role on your source project:

  * Storage Insights Admin `(roles/storageinsights.admin)`

| `storageinsights.datasetConfigs.create`  
  
You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

To grant, change, or revoke access to projects, folders, and organizations, see [Manage access to projects, folders, and organizations.](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)

## Configure the 30-day introductory trial for Storage Intelligence

### Console

  1. In the Google Cloud console, go to the Storage Intelligence **Configuration** page.

[Go to Configuration](https://console.cloud.google.com/storage/storage-intelligence/configuration)

  2. Click **Start 30-day introductory trial**.

**Note:** If you've already started the 30-day trial, the **Start 30-day introductory trial** button is disabled.
  3. In the **Configure Storage Intelligence 30-day introductory trial** dialog, select the [resource](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) where you want to enable the Storage Intelligence 30-day introductory trial.

  4. Click **Continue** , and then complete the steps in the following sections.




### Configure the trial settings

On the **Storage Intelligence trial configuration** page, do the following:

  1. Optional: To include or exclude specific buckets in your Storage Intelligence configuration, click the expand_more expander arrow to expand the **Apply trial only to certain buckets** section, and then do the following:

     1. To [filter buckets by location](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-location), do the following:

        1. To either include or exclude buckets, use the **Select filter type** menu.

        2. Select the location from the **location** menu.

     2. To [filter buckets by name](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-name), do the following:

        1. To either include or exclude buckets, use the **Select filter type** menu.

        2. In the **Regular expression 1** field, enter the regular expression.

        3. Optionally, to add multiple regular expressions, click **\+ Add regular expression**.

  2. In the **Name your dataset** field, enter a name for your dataset. Names identify dataset configurations and are immutable. The name can contain up to 128 characters, including letters, numbers, and underscores, and must start with a letter.

  3. In the **Specify project to store dataset** field, click **Browse** , and then select the project where you want to store your dataset.

  4. Click **Next**.




### Complete the configuration

To complete the configuration, do the following:

  1. To enable the Storage Insights API, click **Next**.
  2. To select the [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations) to store the configured dataset, use the **Select the BigQuery location to store the configured dataset** drop-down menu.
  3. Click **Next**.
  4. To grant IAM role to service agent, click **Next**.
  5. Click **Enable trial**.



### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To configure the 30-day introductory trial for Storage Intelligence, run the [`gcloud storage intelligence-configs enable --trial-edition`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/enable) command:
         
         gcloud storage intelligence-configs enable RESOURCE_FLAG --trial-edition

Where:

`RESOURCE_FLAG` is one of the following flags, depending on the [resource](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) for which you are configuring the Storage Intelligence 30-day introductory trial:

     * `--project=``PROJECT_ID`: Where PROJECT_ID is a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). For example, `my-project`.

     * `--sub-folder=``FOLDER_ID`: Where FOLDER_ID is a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For example, `1234567890`.

     * `--organization=``ORGANIZATION_ID`: Where ORGANIZATION_ID is an [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). For example, `9876546738`.

For example, the following command configures the Storage Intelligence 30-day introductory trial for a project called `my-project`:
    
    gcloud storage intelligence-configs enable --project=my-project --trial-edition

For a complete list of settings to configure the Storage Intelligence 30-day introductory trial, see [Storage Intelligence configuration settings](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/enable#SETTINGS-FLAGS).




### REST APIs

### JSON API

To configure the Storage Intelligence 30-day introductory trial, see [Configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#json-api).

## Disable the 30-day introductory trial for Storage Intelligence

You can disable the 30-day introductory trial for Storage Intelligence at any time during the 30-day period. For instructions, see [Disable Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#disable-storage-intelligence).

## End of the 30-day introductory trial

After the 30-day introductory trial period ends, Storage Intelligence automatically upgrades to the `STANDARD` edition. Following the automatic upgrade to the `STANDARD` edition, you can continue using all the Storage Intelligence features. For detailed information about pricing of the `STANDARD` edition, see [Storage Intelligence pricing](https://docs.cloud.google.com/storage/pricing#storage-intelligence).

## What's next

  * [View a Storage Intelligence configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#view-storage-intelligence-configuration).
  * Learn about: 
    * [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets)
    * [Bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
