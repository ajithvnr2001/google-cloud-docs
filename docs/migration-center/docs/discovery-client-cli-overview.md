---
url: https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview/
title: Migration Center discovery client CLI overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:48.482287+00:00
---

# Migration Center discovery client CLI overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Migration Center discovery client CLI overview Stay organized with collections  Save and categorize content based on your preferences. 

The Migration Center discovery client CLI (`mcdc` CLI) is an offline tool that lets you run different types of asset discoveries on your infrastructure. These asset discoveries scan the physical servers, virtual machine (VM) instances, and databases in your infrastructure to collect the necessary information for a successful migration assessment to Google Cloud.

Migration Center provides advanced migration recommendations and planning capabilities, however, if you're working with sensitive data and don't want to upload it to Google Cloud, you can choose to [run an offline assessment](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment) instead.

The `mcdc` CLI has the following advantages:

  * It doesn't require installation.
  * It runs on Linux and Windows host machines.
  * It creates offline assessment reports.



You can use the data collected by running a `mcdc` CLI discovery to perform the following actions:

  * [Run an offline assessment](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment).
  * [Export this data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data) where you can perform these actions: 
    * [View and understand insights](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights)
    * [Group assets](https://docs.cloud.google.com/migration-center/docs/create-groups).
    * [Generate total cost of ownership (TCO) reports](https://docs.cloud.google.com/migration-center/docs/generate-tco-report)

**Note:** The `mcdc` CLI doesn't upload the collected data to Google Cloud until you choose to export it to Migration Center.

## Available collection methods

Using the `mcdc` CLI, you can run the following collection methods:

  * **Inventory discovery** scans and lists all of the VMware VM instances, Amazon Elastic Compute Cloud (EC2) instances, Amazon Relational Database Service (RDS) and Azure Virtual Machine instances ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * **Guest discovery** scans VM instances and physical servers, collecting data about the running applications. This data includes information about machine configurations, hardware, network, open files, services, and processes. Guest discovery also scans and lists Microsoft SQL Server, PostgreSQL, and MySQL databases that are running on-premises and on AWS.
  * **IP range scan** detects all assets in your network, verifies credentials, and scans the detected assets. It collects data using guest discovery. Use IP range scan when you have several machines in an IP address range or when you are unfamiliar with the infrastructure that you want to scan.



## Limitations

  * The `mcdc` CLI can export data of only up to 10,000 machines to Migration Center.



## What's next

  * Review the [requirements for downloading and running `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  * Learn more about the following discovery methods:

    * [Inventory discovery](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery)
    * [Guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery)
    * [IP range scan](https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
