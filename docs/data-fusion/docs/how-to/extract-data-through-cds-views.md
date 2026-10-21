---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/extract-data-through-cds-views/
title: Extract data through CDS views \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:25.916950+00:00
---

# Extract data through CDS views  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/extract-data-through-cds-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Extract data through CDS views Stay organized with collections  Save and categorize content based on your preferences. 

This page describes data extraction through [_core data services (CDS) views_](https://help.sap.com/docs/SAP_NETWEAVER_750/f2e545608079437ab165c105649b89db/7c078765ec6d4e6b88b71bdaf8a2bd9f.html) when using the SAP ODP plugin in Cloud Data Fusion. A CDS view defines the structure of a SQL view and it applies the structure to one or more database tables or views. The view is part of the ABAP Core Data Services framework, which lets you push down data-intensive logic to the database layer.

## Before you begin

To extract data through CDS views, check the following requirements:

  * Cloud Data Fusion is compatible with SAP ODP CDS views in SAP S/4HANA 2021 (​ _​S4HANA ON PREMISE 2021 Stack - 01 (02/2022) FPS_) or later.
  * CDS view must have delta enabled in SAP.



### Transport request details and ABAP version

Transport request: DS4K901591

**Component** | **Release** | **SP Stack** | **Short description**  
---|---|---|---  
S4HANA ON PREMISE | 2021 | 01 (02/2022) FPS | SAP S/4HANA 2021  
  
## Configure the ODP plugin to use CDS views

  1. Follow the steps to [set up the SAP ODP plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin).
  2. When you [configure the plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin#plugin-configuration), in the **Object Type** field, select **ABAP Core Data Services**.



## What's next

  * Learn how to [use the SAP ODP connector in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
