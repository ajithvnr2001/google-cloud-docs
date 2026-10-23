---
url: https://docs.cloud.google.com/vpc/docs/connect-vpc-networks-spokes/
title: Connect VPC networks by using VPC spokes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:19.220089+00:00
---

# Connect VPC networks by using VPC spokes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/connect-vpc-networks-spokes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect VPC networks by using VPC spokes

This page describes how to connect VPC networks by using VPC spokes that are attached to the same Network Connectivity Center (NCC) hub.

For more information about Network Connectivity Center (NCC) hubs and spokes, including instructions for managing VPC spokes by using the gcloud CLI or the API, see the [NCC documentation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

## Before you begin

Ensure that you have the required roles and permissions to work with NCC spokes. For more information, see [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control).

## Create a VPC spoke

This section describes how to add a VPC spoke to an NCC hub. To connect multiple VPC networks to each other, add each network to the same hub as a VPC spoke.

  1. In the Google Cloud console, go to the **VPC connectivity** page.

[Go to VPC connectivity](https://console.cloud.google.com/networking/vpc-connectivity/spokes)

  2. Click **Connect VPC networks**.

  3. In the **Select hub** section, choose one of the following options:

     * Select **Create a new hub** , and enter a name for the hub.
     * Select **Use an existing hub in project`PROJECT_NAME`** and select a hub from the list.
     * Select **Use an existing hub in another project** and enter the **Project ID** , then enter the name of the hub. When a VPC network and the NCC hub are located in different projects, the hub administrator must approve the spoke before it can become active. See [Spoke administration overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin).
  4. Click **Next step**.

  5. In the **New spoke** section, enter a **Spoke name** and an optional **Description**.

     1. Select the **Associated VPC network** from the list.
     2. Optional: Configure **VPC spoke filters** to include or exclude specific IP address ranges from being exported to the hub. For more information about spoke filters, see [Spoke filters overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview).
     3. When you are finished entering the details of the spoke, click **Done**.
  6. To add another spoke, click **Add a spoke** and complete the form.

  7. When you are finished adding spokes, click **Create**.




## View VPC spokes

  1. In the Google Cloud console, go to the **VPC connectivity** page.

[Go to VPC connectivity](https://console.cloud.google.com/networking/vpc-connectivity/spokes)

  2. The **VPC spokes** table displays information for each spoke, including VPC spokes and [producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview). To view a list that includes other [spoke types](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#supported-spoke-resources), see [List spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#list-spokes) in the NCC documentation.




## What's next

  * For more information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).
  * For more information about using hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
