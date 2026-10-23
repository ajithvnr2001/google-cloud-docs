---
url: https://docs.cloud.google.com/alloydb/docs/backup/list/
title: View a list of backups \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:15.858018+00:00
---

# View a list of backups  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  View a list of backups Stay organized with collections  Save and categorize content based on your preferences. 

To audit available recovery points, verify backup completion, or find a backup ID for a restore operation, you can view a list of AlloyDB for PostgreSQL backups in your project.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### Console

In the Google Cloud console, go to the **Backups** page.

[Go to Backups](https://console.cloud.google.com/alloydb/backups)

This displays a list of all AlloyDB backups within your project.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To view a list of backups, use the [`gcloud alloydb backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/backups/list) command.
    
    
    gcloud alloydb backups list \
    --region=REGION_ID \
    --filter=clusters/CLUSTER_ID \
    --project=PROJECT_ID

Replace the following:

  * `REGION_ID`: The region whose backups you want listed. For example, `us-central1`.

To list backups in all regions, omit this argument.

  * `CLUSTER_ID`: The ID of the cluster whose backups you want listed.

To list backups in all your clusters within the specified regions, omit this argument.

  * `PROJECT_ID`: The ID of the project whose backups you want listed.




Note that the `NAME` column in the output table displays the full name of each backup, which includes its project ID and location. The backup's ID is the substring following `/backups/` in its name.

For example, if a backup has a name of `/projects/myproject/locations/us-central1/backups/bkp-1`, the backup's ID is `bkp-1`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
