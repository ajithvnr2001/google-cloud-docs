---
url: https://docs.cloud.google.com/alloydb/docs/instance-delete/
title: Delete an instance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:38.495033+00:00
---

# Delete an instance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Delete an instance Stay organized with collections  Save and categorize content based on your preferences. 

To stop compute billing for an unused instance while retaining your underlying cluster storage, you can delete a primary instance or a read pool instance from an AlloyDB for PostgreSQL cluster.

Points to remember when you delete an AlloyDB instance:

  * When you delete an AlloyDB instance, it does not automatically delete the data in the storage layer.
  * After you delete the AlloyDB primary instance, you continue to incur the cost of the AlloyDB storage.
  * If you create the primary instance in the same cluster from which you deleted the primary instance, the data becomes readily available and accessible from the primary instance, without any need to restore.

**Note:** You cannot delete the primary instance if the cluster contains any read pool instances.

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
  3. In the **Overview** page, go to the **Instances in your cluster** section, choose the instance that you want to delete, and click **Delete**.
  4. In the dialog that appears, enter the instance's ID, and click **Delete**.



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `instances delete` command to delete an instance.
    
    
    gcloud alloydb instances delete INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The region where the instance is placed.
  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
