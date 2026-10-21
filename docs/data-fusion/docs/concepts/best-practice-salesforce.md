---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/best-practice-salesforce/
title: Best practices for the Salesforce batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.230584+00:00
---

# Best practices for the Salesforce batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/best-practice-salesforce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Best practices for the Salesforce batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for improving performance when you use a [Salesforce batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) in Cloud Data Fusion.

## Improve performance with PK chunking

PK chunking breaks up large datasets into smaller datasets, or _chunks_.

Enabling PK chunking in the Salesforce batch source plugin has the following benefits:

  * It improves performance, especially for large datasets
  * It reduces the load on the server
  * It increases scalability

**Note:** Before enabling PK chunking, check that you're using an sObject that supports it. For more information about PK chunking and the supported sObjects, see the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.234.0.api_asynch.meta/api_asynch/async_api_headers_enable_pk_chunking.htm).

To use PK chunking, follow these steps:

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and open your pipeline on the **Studio** page.
  2. Optional: If you haven't added a Salesforce node in your pipeline, add one: 
     1. In the **Source** menu, click **Salesforce**. The Salesforce node appears in your pipeline. If you don't see the Salesforce source on the **Studio** page, [deploy the Salesforce plugins from the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).
  3. To configure the source, go to the Salesforce node and click **Properties**.
  4. Turn on **Enable PK chunking**.
  5. In the **Chunk size** field, enter the number of records per chunk. The default value is `100000` records. The maximum is `250000` records.
  6. Click **Validate**.



## Use SObject query filters or SOQL queries

To reduce the number of API calls in Salesforce, retrieve records with SObject query filters or SOQL queries.

  * **SObject query filters** : configure the filter in the Salesforce plugin properties in the **SObject name** field. For more information, see [Configure the plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source).

  * **SOQL queries** : configure the queries in the Salesforce plugin properties in the **SOQL query** field. For more information, see [SOQL queries for the Salesforce source](https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries).




## What's next

  * Learn about configuring the [Salesforce batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#properties) in Cloud Data Fusion.
  * Work through a [Salesforce plugin tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/connect-salesforce-to-bq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
