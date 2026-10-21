---
url: https://docs.cloud.google.com/bare-metal/docs/order-bms-resources/
title: Order Bare Metal Solution resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:36.670514+00:00
---

# Order Bare Metal Solution resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/order-bms-resources/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Order Bare Metal Solution resources

This document explains how to create, view, and track procurements.

After you've executed a simplified, one-time Bare Metal Solution Order Form, you can order your Bare Metal Solution resources online by creating procurements through the Google Cloud console. Procurements let you order resources as you scale, without having to execute a new Bare Metal Solution Order Form every time.

Procurements are enabled for you in the Google Cloud console only after you've signed the Order Form. Contact [Google Cloud Sales](https://cloud.google.com/contact) to get started on the Order Form.

**Important:** The procurements are billed as per the terms agreed upon in the Order Form.

You can use procurements to order the following Bare Metal Solution resources:

  * Servers ([available server configurations](https://docs.cloud.google.com/bare-metal/docs/bms-planning#server_configurations))
  * Storage ([available storage choices](https://docs.cloud.google.com/bare-metal/docs/bms-planning#storage_choices))
  * Partner Interconnect bandwidth



To procure any other Bare Metal Solution resource, contact [Google Cloud sales](https://cloud.google.com/contact).

## Before you begin

  * Grant Identity and Access Management (IAM) roles that give users the necessary permissions to create procurements.

The predefined IAM role [`roles/baremetalsolution.procurementseditor`](https://docs.cloud.google.com/iam/docs/roles-permissions/baremetalsolution#baremetalsolution.procurementseditor) includes all the permissions that you need to create and view a procurement.

For more information about IAM roles in Bare Metal Solution, see [Configure IAM for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-iam).

  * Ensure that the Bare Metal Solution API is enabled in your Google Cloud project. For instructions, see [Set up your Google Cloud project to use the Bare Metal Solution API](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#set_up_the_bms_api).




## Create a procurement

To create a procurement, follow these steps:

  1. In the Google Cloud console, go to the **Procurements** page.

[Go to Procurements](https://console.cloud.google.com/compute/bareMetalSolution/procurements)

  2. Click **Create**.

  3. Enter a name for your procurement.

  4. Select a location where your Bare Metal Solution environment is located.

  5. From the **Pod** drop-down list, select a pod in which you want to create your resources.

A pod is a unit of isolation that contains your Bare Metal Solution resources. A region can have multiple pods.

**Note:** Resources in different pods cannot be connected.

The **Pod** drop-down list also shows the number of your existing Bare Metal Solution resources in each pod of the selected location.

The following pages show you the pods that contain your existing resources:

     * [Servers](https://console.cloud.google.com/compute/bareMetalSolution/servers)
     * [Networks](https://console.cloud.google.com/compute/bareMetalSolution/networks)
     * [Volumes](https://console.cloud.google.com/compute/bareMetalSolution/volumes)
     * [NFS Shares](https://console.cloud.google.com/compute/bareMetalSolution/nfsShares)

If you're unsure about which pod to select, contact [Google Cloud Sales](https://cloud.google.com/contact).

  6. Select a commitment term:

     * 1 month (Applicable only to storage and Partner Interconnect.)
     * 1 year
     * 3 years
  7. Add a server:

     1. Click **Add servers**.

     2. Select the type of the server.

For information about the types of servers available, see [Server configurations](https://docs.cloud.google.com/bare-metal/docs/bms-planning#server_configurations).

     3. Enter the quantity of the servers.

  8. Add storage:

     1. Click **Add storage**.

     2. Select the type of storage:

        * HDD
        * Performance SSD
        * SSD
     3. Enter the quantity of storage.

You can add storage in increments of 1 TiB only. For example, to order 10 TiB of storage, enter `10` in the **Quantity** field.

  9. Add Partner Interconnect bandwidth:

     1. Click **Add bandwidth**.

     2. Enter the quantity of interconnect bandwidth.

You can add bandwidth in increments of 1 Gbps only. For example, to order 10 Gbps of bandwidth, enter `10` in the **Quantity** field.

When you add a resource, the page shows the monthly unit price, capacity of resource, and its total price.

  10. Click **Done**.

  11. In the **Procurement summary** section, review the total monthly cost of your procurement.

  12. Click **Submit**.

  13. Click **Confirm**.




## View and track procurements

The time to fulfill an order might vary depending on the availability, type, and quantity of the resources that you want to procure. Some procurements might require evaluation (two business days) or additional processing (four to six weeks). You can check the status of your procurement for detailed information.

To view details and track your procurements, follow these steps:

  1. In the Google Cloud console, go to the **Procurements** page.

[Go to Procurements](https://console.cloud.google.com/compute/bareMetalSolution/procurements)

The **Procurements** page shows the following details for the procurements:

     * **Status:** The status of the procurement. A procurement can be in one of the following states:

       * **Pending:** The procurement request is pending for evaluation or requires additional processing. 
       * **In progress:** The procurement fulfillment is in progress.
       * **Completed:** All resources are procured and fulfillment is complete.
     * **Name:** The name of the procurement.

     * **Location:** The location of your Bare Metal Solution environment.

     * **Created:** The date of creation of the procurement.

  2. To view more details and status of a procurement, click the name of the procurement.

The **Procurement details** page shows the following information for the selected procurement:

     * **Name:** The name of the procurement.
     * **Status:** The status of the procurement. A procurement can be in one of the following states: 
       * **Pending:** The procurement request is pending for evaluation or requires additional processing.
       * **In progress:** The procurement fulfillment is in progress.
       * **Completed:** All resources are procured and fulfillment is complete.
     * **Location:** The location of your Bare Metal Solution environment.
     * **Pod:** The pod in which your resources are procured.
     * **Procurement details:** The details of the procurement.

To view the status of individual resources, click the commitment. You can view the following details:

     * **Requested:** The number of ordered resources.
     * **Procured:** The number of procured resources.
     * **Billed:** The number of billed resources.



You need not wait for the whole procurement to complete in order to start using the resources that are procured. As your resources are procured, you can provision them through the following options and start using them:

  * [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections)
  * [Create a network UI](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#add-attach-network)
  * [Create a storage volume UI](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#provision-storage-volume-in-your-bare-metal-solution-environment)
  * [Create an NFS volume UI](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#create-nfs-volume)



## What's next

  * [Deploy your Bare Metal Solution environment](https://docs.cloud.google.com/bare-metal/docs/bms-deploy).
  * [Configure IAM for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-iam).
  * [Maintain the Bare Metal Solution environment](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
