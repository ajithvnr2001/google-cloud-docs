---
url: https://docs.cloud.google.com/oracle/database/docs/delete-exascale-clusters/
title: Delete Exascale VM Clusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:03.542817+00:00
---

# Delete Exascale VM Clusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/delete-exascale-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Delete Exascale VM Clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete an Exascale VM Cluster in Google Cloud.

Deleting an Exascale VM Cluster doesn't delete its associated Exascale Storage Vault. To delete an Exascale Storage Vault, see [Delete Exascale Storage Vaults](https://docs.cloud.google.com/oracle/database/docs/delete-exascale-vaults). This action is irreversible.

## Before you begin

Make sure that you have the required Identity and Access Management (IAM) roles and permissions to delete an Exascale VM Cluster:

  * `roles/oracledatabase.exadbVmClusterAdmin`



For information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## Delete an Exascale VM Cluster

To delete an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. For the Exascale VM Cluster that you want to delete, click more_vert **View actions** , and then click **Delete**.

  4. In the **Delete Exascale VM Cluster?** dialog, type the cluster name to confirm deletion.

  5. Click **Confirm**.




###  API 

To delete an Exascale VM Cluster, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project which contains the Exascale VM Cluster. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your Exascale VM Cluster.
  * CLUSTER_ID: the ID of your Exascale VM Cluster.



## What's next

  * Learn more about [Exadata Database Service on Exascale Infrastructure](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/exadb-xs/doc/overview-exadb-xs-service.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
