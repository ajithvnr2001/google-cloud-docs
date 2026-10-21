---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-capacity-allocations/
title: Manage capacity allocations \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:15.867690+00:00
---

# Manage capacity allocations  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-capacity-allocations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage capacity allocations

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A capacity allocation is a global reservation of physical nodes for your Cloud Billing account. Your reserved nodes are organized into placement groups (PGs), which represent the specific physical hardware and location of your reserved capacity.

You can view all allocated capacity for your billing account on the **Capacity allocations** page in the Google Cloud console. From this page, you can filter allocations by region and zone to understand your available capacity in specific locations.

Each capacity allocation entry displays the following information:

  * The associated PG
  * The total capacity allocated within that PG
  * The current usage of that capacity
  * The number of provisioned private clouds using that capacity



Additionally, you can view the assigned PG for the clusters on the details page for private clouds.

**Note:** The total allocated capacity and current usage values reflect the entire Cloud Billing account. However, the listed private clouds show only those within the context of your selected project.

If you require new or additional capacity allocations, contact your Google Cloud account team.

## Use a capacity allocation during private cloud creation

When you create a new private cloud, you can select a capacity allocation for your primary cluster by selecting a PG after defining the basic private cloud details. Selecting a PG lets you deploy your cluster on specific physical hardware where you have globally allocated capacity.

To use your capacity allocation during private cloud creation, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Create private cloud**.

  3. Provide the basic private cloud details, including the private cloud name and the region and zone.

  4. For the private cloud type, select **Standard private cloud** or **Stretched private cloud**.

  5. In the **Primary cluster** section, specify the node type and the number of nodes.

  6. In the **Placement group** list, select a PG to choose your capacity allocation:

     * **Standard private cloud:** Select an available PG for your selected zone.
     * **Stretched private cloud:** You must select a PG for _each_ zone to choose your capacity allocation.
     * **No PG selection:** Only select the **No PG selection** option if Google Cloud specifically allocated capacity to this private cloud. If you select this option when Google Cloud has not allocated specific capacity to the private cloud, the creation attempt fails.
  7. Complete the remaining networking configurations and click **Create** to provision your private cloud.




## Use a capacity allocation when adding a cluster

You can select a capacity allocation when expanding an existing private cloud by adding a new cluster. Selecting a PG ensures that Google Cloud provisions the new cluster's nodes from your designated capacity reservation.

To use your capacity allocation when adding a cluster, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the name of the private cloud that you want to expand.

  3. Click the **Clusters** tab.

  4. Click **Add cluster**.

  5. Provide a name for the new cluster, and select the node type and the number of nodes.

  6. In the **Placement group** list, select the specific PG from which you want to provision the new nodes to choose your capacity allocation.

  7. Click **Create** to provision the new cluster by using your allocated capacity.




## Configure a hybrid private cloud across multiple placement groups

A hybrid private cloud is a deployment model that lets you scale consumption or transition from retiring `ve1` hardware by adding clusters in a different PG. This self-service approach eliminates the need for manual support tickets.

To configure a hybrid private cloud, do the following:

  1. Create a standard private cloud with a primary cluster in your initial PG. For instructions, see Use a capacity allocation during private cloud creation.
  2. Add a new cluster to the private cloud and select a different PG where you have capacity allocated. For instructions, see Use a capacity allocation when adding a cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
