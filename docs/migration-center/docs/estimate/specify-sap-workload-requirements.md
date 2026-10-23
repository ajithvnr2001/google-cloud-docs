---
url: https://docs.cloud.google.com/migration-center/docs/estimate/specify-sap-workload-requirements/
title: Specify SAP workload requirements \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:42.781523+00:00
---

# Specify SAP workload requirements  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/specify-sap-workload-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Specify SAP workload requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to specify your requirements for evaluating the cost of hosting your SAP workloads on Google Cloud.

To learn more about SAP on Google Cloud, see [SAP on Google Cloud overview](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).

## Before you begin

Complete the steps to [start a cost estimate](https://docs.cloud.google.com/migration-center/docs/estimate/start-estimation).

## Specify SAP workload requirements

  1. On the **Start your estimate** page, in the **SAP** card, click **Start**.

If you have completed estimation for another environment and want to start specifying details in the SAP cost calculator, on the results page, click **Start** in the **SAP** card.

  2. Choose a pricing track. By default, the **3-year committed use discount** is selected.

  3. From the **Primary location** list, select the primary location to run the SAP workload.

  4. Click **Add a deployment** and specify the following details for the deployment:

     1. Select the timeline start and end period for migrating the deployment.
     2. Choose which of the following application suites you want to include in your estimate:

        * **BO** \- SAP BusinessObjects
        * **BODS** \- SAP BusinessObjects Data Services
        * **BW/4HANA** \- SAP BW/4HANA
        * **Fiori** \- SAP Fiori
        * **PO** \- SAP Process Orchestration
        * **S/4HANA** \- SAP S/4HANA
        * **SAP NW ABAP** \- SAP NetWeaver Application Server for ABAP
     3. In the **Application details** section, for each application that you've selected, perform the following steps:

        1. Select a size for each application you've included in your estimate. To know more about application sizes, see the [application sizing guidance](https://docs.cloud.google.com/migration-center/docs/estimate/sap-sizing-guidance).

        2. If you want redundant instances of your application, select **HA** for high-availability. If you select this option, in case one instance stops functioning, all the traffic is directed to another instance.

        3. If you want a backup data center that can take over running the application in case a disaster renders the applications' data center non-operational, select **DR** for disaster recovery.

     4. If you require storage in addition to the storage that comes with each application, select **Additional storage**. Then, specify the units of additional storage required. One unit of additional storage includes 100 GB of block storage and 49 GB of Cloud Storage.

Optionally, you can select **HA** to include high-availability and **DR** to include disaster recovery for the additional storage in your estimate.

     5. To include the SAP Solution Manager in your estimate, select **SAP Solution Manager (SolMan)**.

Optionally, you can select **HA** to include high-availability and **DR** to include disaster recovery for SAP Solution Manager in your estimate.

     6. To save the specified deployment details, click **Done**.

  5. Repeat the previous step to add more deployments. You can specify a different migration timeline for each deployment.

A cost estimate is displayed for each deployment you add. If you want to view the cost breakdown for the deployments, click **View details**.

To view the cost breakdown for each application, click the application name. And to further view the cost breakdown for each environment, click the arrow next to the environment name. To view the configuration details for each system within the environment, click the arrow next to the system name.

  6. From the currency drop-down list, select the currency in which you want to see the estimate. By default, the estimate is displayed in US dollars.

  7. To review the estimate for SAP workloads, click **Submit**.




You can see the SAP cost estimate on the results page.

## What's next

  * See the [SAP application sizing guidance](https://docs.cloud.google.com/migration-center/docs/estimate/sap-sizing-guidance).
  * See how to [review and export the estimate results](https://docs.cloud.google.com/migration-center/docs/estimate/review-and-export-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
