---
url: https://docs.cloud.google.com/oracle/database/docs/manage-exascale-clusters/
title: Manage Exascale VM Clusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:00.752161+00:00
---

# Manage Exascale VM Clusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/manage-exascale-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Manage Exascale VM Clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage an Exascale VM Cluster.

After you've provisioned an Exascale VM Cluster, Oracle Database@Google Cloud lets you add or delete VMs.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to modify an Exascale VM Cluster:

    * `roles/oracledatabase.exadbVmClusterAdmin`

For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

  * Make sure that you have the required OCI permissions necessary to manage an Exascale VM Cluster. Refer to the Oracle documentation.




## Add a VM to an Exascale VM Cluster

To add a VM to an Exascale VM Cluster, do the following:

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the Exascale VM Cluster to which you want to add a VM.

  4. On the **Exascale VM Cluster details** page, go to the **Virtual machines** section.

  5. Click **Add**.

  6. In the **Add virtual machines** dialog, enter the number of VMs you want to add to the cluster.

A cluster can have a maximum of 10 VMs.

  7. Click **Add**.




You can view the newly added VM in the list of the VMs.

## Delete a VM from an Exascale VM Cluster

Before deleting a VM, make sure that there is no single instance database running on that VM.

To delete a VM from an Exascale VM Cluster, do the following:

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the Exascale VM Cluster from which you want to delete a VM.

  4. On the **Exascale VM Cluster details** page, go to the **Virtual machines** section.

  5. For the VM which you want to delete, click more_vert **View actions** , and then click **Delete**.

  6. In the **Delete virtual machine?** dialog, type the VM name to confirm the deletion of the VM.

  7. Click **Confirm**.




To further manage an Exascale VM Cluster, you can use the OCI console. On the **Exascale VM Cluster details** page, click **Manage in OCI**. You're redirected to the OCI page to modify your Exascale VM Cluster settings.

## What's next

  * Learn more about [Exadata Database Service on Exascale Infrastructure](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/exadb-xs/doc/overview-exadb-xs-service.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
