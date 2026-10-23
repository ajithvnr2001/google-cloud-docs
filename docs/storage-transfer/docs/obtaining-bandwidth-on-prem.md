---
url: https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem/
title: Manage network bandwidth \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:49.949902+00:00
---

# Manage network bandwidth  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Manage network bandwidth Stay organized with collections  Save and categorize content based on your preferences. 

This article discusses options for obtaining more network bandwidth for agent-driven transfers. Increasing your network bandwidth helps decrease transfer times, especially for large data sets.

## Control bandwidth usage for agent-driven transfers

Bandwidth limits are helpful if you need to limit how much data Storage Transfer Service uses to transfer data. Using a bandwidth limit helps ensure that:

  * Your network is not saturated as a result of using Storage Transfer Service.

  * Your organization's existing application behavior doesn't degrade during the transfer.

  * You don't cause a sudden price increase if you're on a network connection that charges by peak bandwidth usage.




Bandwidth limits are applied at an agent pool level and are divided by all agents in the pool. Bandwidth limits are enforced as an average value over one minute, so you may still experience short bursts that exceed the per-second limit that you specify.

### Set a bandwidth limit

To set a bandwidth limit:

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

  2. Select the agent pool to update.

  3. Click **Set bandwidth limit**.

  4. Enter the desired network limit in megabytes per second (MB/s) and click **Set limit**.




### Edit a bandwidth limit

To edit an existing bandwidth limit:

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

  2. Select the agent pool to update.

  3. Click **Edit limit**.

  4. Enter the desired network limit in megabytes per second (MB/s) and click **Set limit**.




To remove a limit, click **Use all bandwidth**.

## Options for obtaining more network bandwidth

There are several options for obtaining more network bandwidth for agent-driven transfers:

  * **Peering with Google** —Peering is where you directly interconnect with Google to support traffic exchange. We have [direct peering locations](https://docs.cloud.google.com/vpc/docs/edge-locations) world-wide. To learn about the benefits and our policies, see [Peering](https://peering.google.com/#/options/peering).

  * **Cloud Interconnect** —Cloud Interconnect is similar to peering, but you'll use an interconnect to connect to Google. There are two types of [interconnects to choose from](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect):

    * **Dedicated Interconnect** — You connect directly from your data center to a Google data center via a private, dedicated connection. For more information, see [Dedicated Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

    * **Partner Interconnect** —You work with a service provider to establish a connection to a Google data center via a service partner's network. For more information, see [Partner Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

  * **Obtain bandwidth from your ISP** —Your internet service provider (ISP) may be able to offer more bandwidth for your needs. Consider contacting them to ask what options they have available.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
