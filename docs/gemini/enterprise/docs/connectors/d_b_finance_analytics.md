---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_finance_analytics/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:02.762737+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_finance_analytics/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The D&B Finance Analytics connector for Gemini Enterprise lets you run credit and portfolio workflows against your D&B Finance Analytics account using natural language. You can look up company and credit reports, financial summaries, payment and delinquency scores, UCC filings, tax liens, judgments, and corporate ownership and family trees, and you can search, filter, count, and compare the companies in your portfolios, folders, and watchlists.

The connector can also carry out authorized write operations, such as creating and processing credit applications, running credit decisioning, and managing folders and the companies in them.

## Limitations

The D&B Finance Analytics connector for Gemini Enterprise has the following limitations:

  * Gemini Enterprise does not ingest or index your D&B Finance Analytics data. Queries are answered live through your D&B Finance Analytics account, so results reflect your D&B Finance Analytics permissions at query time rather than a crawled copy.

  * When a report request asks for a billing endorsement, Gemini Enterprise uses the current default endorsement on your D&B Finance Analytics account.




  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing D&B Finance Analytics data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The D&B Finance Analytics data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with D&B Finance Analytics, see [Set up a D&B Finance Analytics data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/d_b_finance_analytics/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
