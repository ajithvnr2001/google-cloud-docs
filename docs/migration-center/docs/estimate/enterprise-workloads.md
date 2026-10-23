---
url: https://docs.cloud.google.com/migration-center/docs/estimate/enterprise-workloads/
title: Specify workload and license details \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:44.298212+00:00
---

# Specify workload and license details  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/enterprise-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Specify workload and license details Stay organized with collections  Save and categorize content based on your preferences. 

On the **Workloads and licenses** tab, you can select the applications that you run in your infrastructure, such as Oracle, SAP, or Microsoft SQL Server, and add the details. Also, select which OS platforms you use and provide the additional details.

## Before you begin

  * Complete the steps to [specify infrastructure details](https://docs.cloud.google.com/migration-center/docs/estimate/infrastructure-details).



## Specify workload and license details

  1. In the **Oracle and SAP workloads** section, select the workloads you want to include in your cloud estimate calculation:

     * **Oracle.** After you select this workload, additional options appear for different Oracle workload types. In the **Oracle vCPUs** section, follow these steps:

       1. For each workload type, specify what percentage of the total number of x86 vCPUs you want to migrate as that workload.

       2. Specify the total storage, in GB, to use for the Oracle database.

       3. Optional: To edit the [Oracle sizing default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults#oracle_sizing_default_assumptions) used for this estimate, click **Edit Oracle sizing details**.

     * **SAP.** After you select this workload, additional options appear for different SAP workload types. In the **SAP vCPUs** section, follow these steps:

       1. For each workload type, specify what percentage of the total number of x86 vCPUs you want to migrate as that workload.

       2. Optional: To edit the [SAP sizing default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults#sap_sizing_default_assumptions) used for this estimate, click **Edit SAP sizing details**.

  2. In the **Licenses for all other workloads** section, select the operating systems for your remaining vCPUs after excluding the Oracle and SAP vCPUs. For the additional options that appear in this section, follow these steps:

     1. For all the selected operating systems, specify the percentage distribution of your remaining vCPUs.

     2. In the related license sections, choose the licensing model for all the operating systems you selected. For all the operating systems, **Pay as you go (PAYG)** is the default licensing model.

If you've selected Windows Server, then to determine which licensing model you're eligible for, you can do the following:

        1. In the **Windows Server licenses** section, click **Determine your license eligibility**.

        2. In the **Windows Server license eligibility** pane that appears, select the appropriate options about your licenses, and then click **Next**.

The licensing model that you're eligible for is displayed.

        3. To apply the displayed licensing model to your estimate, click **Accept**.

For more information about licensing, see the following:

        * [Microsoft licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)
        * [Ubuntu Pro FAQ](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq)
        * [Red Hat Enterprise Linux FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq)
        * [SUSE Linux Enterprise Server FAQ](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq)
     3. If you've selected Red Hat Enterprise Linux or SUSE Linux Enterprise Server, then choose a pricing track for these Linux operating systems. The default pricing track is 3-year committed use discount. For more information about the pricing tracks, see [Disk image and pricing](https://cloud.google.com/compute/disks-image-pricing).

  3. If you're migrating Microsoft SQL server, then in the **Microsoft SQL server licenses** section, select the **Microsoft SQL server** checkbox. For the additional options that appear in this section, follow these steps:

     1. To determine which licensing model you're eligible for, do the following:

        1. Click **Determine your license eligibility**.

        2. In the **Microsoft SQL Server license eligibility** pane that appears, select the appropriate options about your licenses, and then click **Next**.

The licensing model you're eligible for is displayed.

        3. To apply the displayed licensing model to your estimate, click **Accept**.

Alternatively, you can manually choose the licensing model. The default model is **Pay as you go (PAYG)**.

     2. For each SQL license type, specify the percentage distribution.

     3. Specify what percentages of vCPUs with the operating systems you selected are running Microsoft SQL Server.

  4. To set up the migration timeline, click **Next**.




## What's next

  * To continue with your estimate, see how to [set up the migration timeline and apply discounts](https://docs.cloud.google.com/migration-center/docs/estimate/migration-timeline).
  * Optional: To review the default assumptions that are used to calculate your cloud cost estimate, see how to [review the default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
