---
url: https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery/
title: Asset inventory discovery overview \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:59.489740+00:00
---

# Asset inventory discovery overview  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Asset inventory discovery overview Stay organized with collections  Save and categorize content based on your preferences. 

Inventory discovery lets you scan and list VMware virtual machine (VM) instances, AWS assets, and Azure VM instances by using the Migration Center discovery client CLI. To discover VM instances and databases in your on-premises environment, use [guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery) or an [IP range scan](https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan).

For VMware VM instances and Azure VM instances, the `mcdc` CLI collects data such as the operating system, storage configuration, the number of cores, and performance data.

For AWS assets, the `mcdc` CLI collects data based on the AWS service. For more information, see [Data collected during inventory discovery](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets#inventory-discovery-info).

## Before you begin

  1. Review the [requirements for downloading and running the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  2. Complete the steps to [download `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



## What's next

  * Learn how to [discover VM instances on VMware](https://docs.cloud.google.com/migration-center/docs/discover-vmware-vms).
  * Learn how to [discover assets on AWS](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets).
  * Learn how to [discover Azure VM instances](https://docs.cloud.google.com/migration-center/docs/discover-azure-vms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
