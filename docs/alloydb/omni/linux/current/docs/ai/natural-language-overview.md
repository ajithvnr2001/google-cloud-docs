---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/natural-language-overview/
title: AlloyDB AI natural language overview \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:02.507256+00:00
---

# AlloyDB AI natural language overview  |  AlloyDB Omni using RPM: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/natural-language-overview/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  AlloyDB AI natural language overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/natural-language-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/ai/natural-language-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/ai/natural-language-overview)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/ai/natural-language-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/natural-language-overview)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This experimental launch is a Pre-GA offering.

This page describes AlloyDB AI natural language, which lets you create user-facing generative AI applications using natural language to query databases.

AlloyDB AI natural language generates context-aware SQL queries for application end users' natural language questions, and it provides a security API to execute these queries. Natural language streamlines the development of generative AI applications by transferring the complexity of converting natural language to SQL from the application layer to the database layer. Natural language-to-SQL (NL2SQL) orchestration is embedded in the database. You can query structured and unstructured data.

AlloyDB AI natural language also provides an intuitive interface to SQL developers that translates natural language to SQL, as shown in the following example:
    
    
    SELECT
      alloydb_ai_nl.get_sql(
        ...,
        'What is the sum that client number 4''s account has following transaction 851?'
      );
    

AlloyDB AI natural language support is provided through `alloydb_ai_nl`, which is an AlloyDB Omni extension. The extension has a dependency on PostgreSQL extensions like `google_ml_integration`, `vector`, and `pg_trgm`.

The `alloydb_ai_nl` extension issues prediction requests to Vertex AI models. For more information, see [Install AlloyDB AI in AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/install-with-alloydb-ai). **Note:** To provide feedback about your experiences using AlloyDB AI natural language, [submit the User Experience Research: AlloyDB AI Natural Language form](https://docs.google.com/forms/d/e/1FAIpQLSfksRzklOU_T1aMVbI0tb0O5ZNpnone7XiD_KCBW2GWHo9uqA/viewform).

## Use cases

AlloyDB AI natural language is well-suited for developers who want to do the following:

  * Rapidly build a customer chat interface by using query generation from natural language.
  * Refine automatically generated queries and perform thorough testing to provide accurate responses.
  * Tune generated results by adding templates and context information.
  * Deploy an intuitive, accurate chat experience that lets customers ask natural language questions about their relational data.



## Key capabilities

Key capability | Description  
---|---  
Semantic layer | 

  * Maintains rich schema and application context for enhanced accuracy.


  * Stores the meaning of your database—schemas, tables, columns, and relationships.


  * Enables AlloyDB Omni to understand the context of user questions.

  
Concept search | 

  * Intelligently parses user questions to identify key value phrases.


  * Maps these values to your data with disambiguation based on concept types, improving accuracy.

  
Query store | 

  * Supports accurate query generation for a wide variety of common natural language questions.


  * Uses templates and query fragments (manual and auto generated) for faster, more accurate SQL construction.

  
  
## Limitations

AlloyDB AI natural language objects created on the primary instance are propagated to read-only replicas. However, the `alloydb_ai_nl.enabled` flag setting isn't replicated automatically, so you must replicate it manually on each instance. For more information, see [Generate SQL queries that answer natural language questions](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/generate-sql-queries-natural-language#before-you-begin). 

## What's next

  * [Generate SQL queries that answer natural language questions](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/generate-sql-queries-natural-language).
  * [Use AlloyDB AI natural language to generate SQL](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/use-natural-language-generate-sql-queries).
  * Learn how to [search your relational data stored in AlloyDB Omni in Gemini Enterprise using AlloyDB AI natural language](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data#alloydb-ai-nl-setup) ([Preview](https://cloud.google.com/products#product-launch-stages)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
