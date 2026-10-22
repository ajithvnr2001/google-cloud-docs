---
url: https://docs.cloud.google.com/migration-center/docs/estimate/specify-vmware-engine-requirements/
title: Specify VMware Engine requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:14.187338+00:00
---

# Specify VMware Engine requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/specify-vmware-engine-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Specify VMware Engine requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to specify your requirements for evaluating the cost of running your VMware platform as a fully managed service in Google Cloud.

To learn more about Google Cloud VMware Engine, see [VMware Engine](https://docs.cloud.google.com/vmware-engine).

## Before you begin

Complete the steps to [start a cost estimate](https://docs.cloud.google.com/migration-center/docs/estimate/start-estimation).

## Specify your VMware Engine workloads requirements

To estimate the cost of hosting your VMware environment in VMware Engine, follow these steps:

  1. On the **Estimate cost** page, click **Start** in the **Google Cloud VMware Engine** card.
  2. Choose a pricing track. By default, the **3-year committed use discount** with monthly payment is selected.
  3. In the **Workloads** section, click **Add a workload**.
  4. Enter the name of your workload and select the **Workload type**.
  5. In the **GCVE service type** section, select one of the available options: 
     * **Fully licensed:** Purchase your VMware Cloud Foundation licenses from Google, as part of your VMware Engine nodes.
     * **Portable license:** Use your VMware Cloud Foundation licenses on VMware Engine.
  6. In the **GCVE protected** section, select if you want to enable backup and disaster recovery on your VMware Engine nodes, if available, or if you don't want to enable this option.
  7. In the **Location** section, select the region where you want to host your environment. The available VMware nodes depend on the region that you select.
  8. In the **Basic workload requirements** section, enter the following details: 
     1. Optional: The number of VMs in your environment
     2. The number of vCPUs
     3. The total memory
     4. The total storage
  9. Optional: In the **Advanced Google Cloud VMware Engine sizing** section, specify the sizing of your environment. For more information, see Specify optional sizing details.
  10. To confirm the configuration of your workload, click **Done**.
  11. If you have multiple workloads, click **Add a workload** and repeat the previous steps.
  12. In the **Node configuration** section, review the recommended configuration. To change the vSAN policy of the node, click **Change**.
  13. To review the estimate for VMware Engine workloads, click **Submit**. The VMware Engine cost estimate is displayed on the results page.



## Specify optional sizing details

This section describes how to specify the optional details in the **Google Cloud VMware Engine sizing** section.

  1. In the **CPU Overcommit** field, enter the overcommit factor for the CPU. Use the following values according to your workload type:

     1. `1-3` for low overcommit
     2. `4-6` for moderate
     3. `7-12` for high

The default value is `6`.

  2. In the **RAM Overcommit field** , enter the overcommit factor for the RAM. The default value is `1`.

  3. In the **vSAN settings section** , specify the following details:

     1. **Optimization:** select one of the available optimization types:

        1. **None**
        2. **Compression**
        3. **Deduplication and compression**

The default value is **Compression**.

     2. **Optimization factor:** select the ratio between the allocated storage and the actual amount written to the vSAN. The default value is `1.7`.

     3. **SLA threshold:** specify the reserved vSAN storage capacity, in %, to perform updates, upgrades and other operational tasks. The default value is `20%`.

     4. To support VMs with VMDKs larger than 8 TB, select **Use large VMDKs**.

     5. To enable vSAN Operations Reserve, select **Use OR buffer**.

  4. In the **Advanced Google Cloud VMware Engine settings** section, specify the following details:

     1. **System CPU:** specify the maximum amount of system CPU consumption, in %. The default value is `15%`.
     2. **System RAM:** specify the default system RAM reservation, in %. The default value is `5%`.
     3. **HT Weight:** specify the amount of hyperthreading boost effect, in %. The default value is `25%`.
     4. To host management appliances in the cluster, such as vCSA, NSX-T Manager, NSX-T Edge Node, select **Management Cluster**.
     5. If you want to reserve capacity for HCX Mesh components, select **HCX Mesh Deployed**.
     6. **NSX-T Edge Size:** select one of the available sizes for NSX-T Edge: 
        1. **Large**
        2. **Extra Large**



To reset the default values of the sizing configuration, click **Reset to defaults**.

## Review and export estimation results

The steps to review and export estimate results are [common for all](https://docs.cloud.google.com/migration-center/docs/estimate/review-and-export-results) calculators.

In addition, the overall estimate for VMware Engine is displayed in a separate result card as well. This cost estimate is based on the default assumption and the inputs you've provided. By default, the calculator recommends the node configuration with the lowest total cost of ownership (TCO). To edit the node configuration, including the vSAN policy, in the total estimate page, click **Edit**.

To view the details of this cost estimate and the breakdown of the costs for each workload, click **View details**.

## What's next

  * See how to [review and export the estimate results](https://docs.cloud.google.com/migration-center/docs/estimate/review-and-export-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
