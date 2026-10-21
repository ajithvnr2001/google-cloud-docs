---
url: https://docs.cloud.google.com/channel/docs/rebilling/repricing-configurations-example/
title: Repricing Configurations examples \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:34.803669+00:00
---

# Repricing Configurations examples  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/rebilling/repricing-configurations-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Repricing Configurations examples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples of repricing configurations with Overrides and how the repricing config is evaluated for each SKU. 

### Example 1: Configuration with higher priority on Google Cloud Reseller SKU group

![Repricing configuration
1](https://docs.cloud.google.com/static/channel/docs/images/repricing-configuration-example-1.png)

**Note:** The override rules are evaluated in a top-down approach. SKUs could be in multiple SKU groups. Overlapping configurations on the same SKU on lower ranked SKU group will be ignored.

This configuration leads to repricing of SKUs as the following:

  * **Override 1 (Google Cloud Reseller):** SKUs in Google Cloud reseller SKU group will be marked up by 5% on Direct Customer Cost.
  * **Override 2 and 3 (On-Demand Compute and Cloud Storage):** The following 2 rules on Compute and Storage SKU groups will be ignored as On-demand Compute and Cloud Storage are subsets of Google Cloud Reseller.
  * **Base rule:** All the other remaining SKUs (not part of the 3 configured SKU groups) will be marked up by 20% on Direct Customer Cost due to the Base rule.



### Example 2: Configuration with lower priority on Google Cloud Reseller SKU group

![Repricing configuration
2](https://docs.cloud.google.com/static/channel/docs/images/repricing-configuration-example-2.png) This configuration leads to repricing of SKUs as the following:

  * **Override 1 (On-Demand Compute):** SKUs in On-demand Compute SKU group will be marked up by 10% on Direct Customer Cost.
  * **Override 2 (Cloud Storage):** SKUs in Cloud Storage SKU group will be marked up by 15% on Direct Customer Cost.
  * **Override 3 (Google Cloud Reseller):** SKUs in Google Cloud Reseller SKU Group, except SKUs in On-demand Compute and Cloud Storage SKU groups will be marked up by 5% on Direct Customer Cost.
  * **Base rule:** All the other remaining SKUs (not part of the 3 configured SKU groups) will be marked up by 20% on Direct Customer Cost due to the Base rule.



### Example 3: Configuration with higher priority on Third party Marketplace SKU group

![Repricing configuration with Marketplace SKU
groups](https://docs.cloud.google.com/static/channel/docs/images/repricing-configuration-example-3.png)

**Note:** The override rules are evaluated in a top-down approach. SKUs could be in multiple SKU groups. Overlapping configurations on the same SKU on lower ranked SKU group will be ignored.

This configuration leads to repricing of SKUs as the following:

  * **Override 1 (Third party Marketplace):** SKUs in Third party Marketplace SKU group will be marked up by 10% on Direct Customer Cost.
  * **Override 2, 3 and 4 (Itopia, Splunk and MongoDB Marketplace SKUs):** The following 3 rules on Itopia, Splunk and MongoDB Marketplace SKU groups will be ignored as these SKU groups are subsets of Third party Marketplace SKU group.
  * **Base rule:** All the other remaining SKUs (not part of the 4 configured SKU groups) will be marked up by 5% on List Price due to the Base rule.



### Example 4: Configuration with lower priority on Third party Marketplace SKU group

![Repricing configuration with Marketplace SKU
groups](https://docs.cloud.google.com/static/channel/docs/images/repricing-configuration-example-4.png) This configuration leads to repricing of SKUs as the following:

  * **Override 1 (Itopia Marketplace SKUs):** SKUs in Itopia Marketplace SKU group will be marked up by 15% on List Price.
  * **Override 2 (Splunk party Marketplace):** SKUs in Splunk Marketplace SKU group, except SKUs in Itopia Marketplace SKU group, will be marked up by 20% on Direct Customer Cost.
  * **Override 3 (MongoDB party Marketplace):** SKUs in MongoDB Marketplace SKU group, except SKUs in Itopia and Splunk Marketplace SKU group, will be marked up by 15% on List Price.
  * **Override 4 (Third party Marketplace):** SKUs in Third party Marketplace SKU group, except SKUs in Itopia, Splunk and MongoDB Marketplace SKU group, will be marked up by 10% on Direct Customer Cost.
  * **Base rule:** The other remaining SKUs (not part of the 3 configured SKU groups) will be marked up by 5% on List Price due to the Base rule.



To view list of SKUs in a SKU group, see [Export SKU Groups](https://docs.cloud.google.com/channel/docs/rebilling/manage-repricing-configurations#export-SKU-groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
