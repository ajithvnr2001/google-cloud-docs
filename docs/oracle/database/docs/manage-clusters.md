---
url: https://docs.cloud.google.com/oracle/database/docs/manage-clusters/
title: Manage VM clusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:46.235173+00:00
---

# Manage VM clusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage VM clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage a Exadata VM Cluster in Google Cloud.

In Oracle Database@Google Cloud, you can modify a Exadata VM Cluster using Oracle Cloud Infrastructure (OCI). To create a Exadata VM Cluster, see [Create clusters](https://docs.cloud.google.com/oracle/database/docs/create-clusters).

To learn more about Oracle Database@Google Cloud, see [Product overview](https://docs.cloud.google.com/oracle/database/docs/overview).

## Before you begin

  * [Set up gcloud CLI and enable the API](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * Confirm that you have the required roles necessary to create a cluster: `cloudVmClusterViewer`.

For more information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

  * Confirm you have the required [Oracle Cloud Infrastructure (OCI) permissions](https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/exadatacloud/exacs/ecs-policy-details.html#ECSCM-GUID-5CA6A297-F583-4A60-A781-C0A3934760FA) to manage a cluster.




## Manage clusters

### Console

  1. Go to the **Exadata Database Service** page in the Google Cloud console.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. Click **Exadata VM Clusters**.

  3. In the **Exadata VM Clusters** section, click the name of the cluster you want to modify.

  4. Click **Manage in OCI**.

You're redirected to the [OCI](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/manage-vm-clusters.html#GUID-292097D6-2F40-44AF-9228-A10E615F9638) page to modify your cluster. Modifying a cluster isn't supported in Google Cloud console.

For more information on how to manage a VM Cluster in OCI, see [Manage VM Clusters](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/manage-vm-clusters.html#GUID-A24799BF-0D41-4F58-B54C-AF7D0C3DF31C).




## What's next

  * [Create an Exadata database](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/manage-databases.html#GUID-E322F1CC-46C9-47A1-8A4E-921432B25287)
  * Learn how to [create](https://docs.cloud.google.com/oracle/database/docs/create-clusters) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-clusters) a Exadata VM Cluster.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
