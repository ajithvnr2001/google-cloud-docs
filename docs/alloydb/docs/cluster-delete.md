---
url: https://docs.cloud.google.com/alloydb/docs/cluster-delete/
title: Delete a cluster \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:52.513018+00:00
---

# Delete a cluster  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cluster-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Delete a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an AlloyDB for PostgreSQL cluster. Deleting a cluster that you no longer need stops compute and storage charges for the cluster and all of its instances.

**Caution:** If there is a cluster backup operation on the cluster that you want to delete, then the cluster deletion is queued until the backup operation completes. The cluster continues to be billed until the cluster status changes from `ready` to `deleting`.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Procedure

### Console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.
  3. In the **Overview** page of your cluster, click **Delete cluster**.
  4. In the **Delete cluster** dialog that appears, enter your cluster ID.
  5. Click **Delete**.



You can't delete an AlloyDB cluster that contains any instances using the Google Cloud console. To override this default behavior, use the gcloud CLI to specify the [`--force` option](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/delete) in the `clusters delete` command.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `clusters delete` command to delete a cluster.
    
    
    gcloud alloydb clusters delete CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

  * `CLUSTER_ID`: The ID of the cluster.
  * `REGION_ID`: The region where the cluster is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



#### Deleting a cluster that contains instances

Attempts to delete an AlloyDB cluster that contains any instances will fail. To override this behavior, specify the `--force` option in the `clusters delete` command to direct AlloyDB to delete all instances in the cluster and then delete the cluster itself; for example:
    
    
    gcloud alloydb clusters delete CLUSTER_ID \
        --force \
        --region=REGION_ID \
        --project=PROJECT_ID

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
