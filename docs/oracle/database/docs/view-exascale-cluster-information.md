---
url: https://docs.cloud.google.com/oracle/database/docs/view-exascale-cluster-information/
title: View Exascale VM Cluster information \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:55.421595+00:00
---

# View Exascale VM Cluster information  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-exascale-cluster-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View Exascale VM Cluster information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view details for an Exascale VM Cluster in Google Cloud.

## Before you begin

Make sure that you have the required Identity and Access Management (IAM) roles and permissions to view details of an Exascale VM Cluster:

  * `roles/oracledatabase.exadbVmClusterViewer`



For information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## View Exascale VM Cluster details

To view details of an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the cluster.

The **VM Cluster details** page shows Exascale VM Cluster details.

  4. To view change logs, select the **Operations** tab.

  5. To view the VM details, go to the **Virtual machines** section.




###  API 

  * **List Exascale VM Clusters**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your Exascale VM Clusters.
  * **View Exascale VM Cluster details**
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then this project ID is the ID of your host project.
    * REGION: the region of your Exascale VM Cluster.
    * CLUSTER_ID: the ID of your Exascale VM Cluster.



## What's next

  * Learn more about [Exadata Database Service on Exascale Infrastructure](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/exadb-xs/doc/overview-exadb-xs-service.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
