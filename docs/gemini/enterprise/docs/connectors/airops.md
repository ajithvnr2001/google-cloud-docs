---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:40.233643+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Private preview:** The federated search and actions features are in private preview. You need to be on the allowlist to use these features. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

The AirOps connector for Gemini Enterprise lets you search, read, and perform write operations on your AirOps workspaces, grids, reports, and knowledge bases using natural language.

## Supported actions

When the AirOps connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Add grid column | Add a new column to a grid table.  
Add URLs to knowledge base | Add one or more URLs to a knowledge base for indexing.  
Create action grid | Create a grid with power agents for taking action on AEO insights.  
Create grid | Create a new grid (spreadsheet-like table for organizing and processing data).  
Create grid sheet | Create a new sheet (table) within an existing grid.  
Create knowledge base direct upload | Initiate a direct file upload to a knowledge base.  
Create report | Create a new analytics report for a Brand Kit.  
Manage knowledge base | Create or update a knowledge base.  
Suggest Brand Kit edits | Suggest edits to a Brand Kit's fields without applying them.  
Update knowledge base document metadata | Update metadata for a document in a knowledge base.  
Write grid | Create or update rows in a grid table.  
**Note:** Additional read-only actions are also available.

## Limitations

The AirOps data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing AirOps data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The AirOps data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with AirOps, see [Set up a AirOps data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
