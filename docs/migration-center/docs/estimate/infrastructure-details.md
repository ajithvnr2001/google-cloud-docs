---
url: https://docs.cloud.google.com/migration-center/docs/estimate/infrastructure-details/
title: Specify infrastructure details \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:37.548934+00:00
---

# Specify infrastructure details  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/infrastructure-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Specify infrastructure details Stay organized with collections  Save and categorize content based on your preferences. 

Based on the infrastructure data that you have about your current on-premises environment, enter your best estimates for CPU, memory, and storage. Enter the total aggregate count of memory across all systems in the data center. Also, specify the total aggregate storage footprint, including all [direct-attached storage (DAS)](https://en.wikipedia.org/wiki/Direct-attached_storage) and [network-attached storage (NAS)](https://en.wikipedia.org/wiki/Network-attached_storage).

## Before you begin

  * Complete the steps to [start a cost estimate](https://docs.cloud.google.com/migration-center/docs/estimate/start-estimation).



## Specify basic estimate details

  1. On the **Start your estimate** page, in the **On-premise** card, click **Start**.

If you've completed estimation for another environment and want to start specifying details in the **On-premise** cost calculator, then on the results page, click **Start** in the **On-premise** card.

  2. On the **Estimate basics** tab, from the **Location** list, choose a location where you want your workloads to be located.

  3. To specify infrastructure details, click **Next**.




## Specify infrastructure details

On the **Infrastructure** tab, follow these steps:

  1. In the **Total vCPUs to be migrated** section, in the **Number of vCPUs** field, enter the number of x86 vCPUs you want to migrate to Google Cloud.

The **Data center memory required** field is automatically updated based on the default memory to compute ratio, which is 4:1.

  2. Optional: To edit the [compute sizing default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults#compute_sizing_default_assumptions) used for this estimate click **Edit compute sizing details**.

  3. If you're migrating non-x86 infrastructure and want to include it in your cost estimate, then in the **Total vCPUs to be migrated** section, select **Include non-x86 infrastructure**. Then, specify non-x86 infrastructure details in the additional fields that appear.

  4. In the **Storage currently in use in your data center(s)** section, follow these steps:

     1. In the **Total storage (TB)** field, enter the total storage, in TB, that you have in your data center.

     2. In the **% File Storage** , **% Block Storage** , and **% Object Storage** fields, enter the percentage of total storage used by file, block, and object storage respectively.

     3. Under **Storage location** , select the locations where you want your storage to be located. If you select multiple locations, then new fields appear where you need to specify the percentage distribution of storage for every location.

     4. Optional: To edit the [storage sizing default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults#storage_sizing_default_assumptions) used for this estimate, click **Edit storage sizing details**.

  5. In the **Networking** section, follow these steps:

     1. In the **CDN data transfer out bandwidth** field, enter the amount of data transfer out bandwidth used for Google Cloud Content Delivery Network, in GB.

     2. Select how you want to calculate your networking costs:

        * If you select **Percentage of total compute cost** , then specify the networking costs you expect to have as a percentage of your compute costs.
        * If you select **Monthly network bandwidth** , then specify your estimated networking bandwidth per month in TB, and the percentage of the external network traffic, excluding the data center traffic.
  6. From the currency list on the right, choose the currency you want to use for your cloud cost estimate.

  7. To specify enterprise workload details, click **Next**.




### Specify non-x86 infrastructure details

  1. If you're migrating mainframes, then in the **Mainframe** section, select **I am migrating mainframes** and follow these steps:

     1. In the **Mainframe MIPS #** field, enter the mainframe million instructions per second capacity.

     2. Under **Mainframe Colocation or Rehosting (Emulation)** , choose whether you want to use **Colocation** or **Rehosting** for your mainframes.

  2. If you're migrating Unix cores, then follow these steps:

     1. In the **Number of UNIX vCPUs** field, enter the number of Unix vCPUs you want to migrate.

     2. In the **UNIX vCPU distribution** section, specify the percentage distribution of the Unix cores.

     3. In the **Unix infrastructure type** field, choose if you want a **Managed Service Provider** for your Unix vCPUs or you want them to be **Emulated**.

  3. Optional: To edit the [non-x86 sizing default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults#non-x86_sizing_default_assumptions) used for this estimate, click **Edit non-x86 sizing details**.




## What's next

  * To continue with your estimate, see how to [specify workload and license details](https://docs.cloud.google.com/migration-center/docs/estimate/enterprise-workloads).
  * Optional: To review the default assumptions that are used to calculate your cloud cost estimate, see how to [review the default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
