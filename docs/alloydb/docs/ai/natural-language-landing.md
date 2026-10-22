---
url: https://docs.cloud.google.com/alloydb/docs/ai/natural-language-landing/
title: AlloyDB AI natural language overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:11.381916+00:00
---

# AlloyDB AI natural language overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/natural-language-landing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB AI natural language overview Stay organized with collections  Save and categorize content based on your preferences. 

The AlloyDB AI natural language feature ([Preview](https://cloud.google.com/products#product-launch-stages)) lets you translate natural language questions into schema-aware SQL queries, helping developers and analysts retrieve insights from AlloyDB for PostgreSQL databases faster. 

**Important:** For next-generation text-to-SQL workflows with superior accuracy, multi-database-engine support, and seamless AI agent integration, we recommend that you use [QueryData](https://docs.cloud.google.com/alloydb/docs/ai/querydata) instead of the `alloydb_ai_nl` AI extension.**Note:** This experimental launch is a Pre-GA offering.

![AI-powered filtering thumbnail](https://docs.cloud.google.com/static/alloydb/images/nl-semantic-layer.png)

###  [ Build a context layer ](https://docs.cloud.google.com/alloydb/docs/ai/generate-sql-queries-natural-language)

Create a rich **context layer** by understanding your tables, columns, and relationships to generate accurate, context-aware queries. 

![In-database text generation thumbnail](https://docs.cloud.google.com/static/alloydb/images/nl-intelligentsql.png)

###  [ Intelligent SQL generation ](https://docs.cloud.google.com/alloydb/docs/ai/use-natural-language-generate-sql-queries)

Intelligently parse intent using **concept search** and leverages a **template store** of templates to rapidly and reliably construct SQL queries. 

![Direct model integration thumbnail](https://docs.cloud.google.com/static/alloydb/images/nl-psv.png)

###  [ Parameterized secure views ](https://docs.cloud.google.com/alloydb/docs/parameterized-secure-views-overview)

Provide **fine-grained access control** , ensuring that end users only see data they're authorized to access, which is critical for applications executing AI-generated queries. 

## How it works

AlloyDB AI natural language ([Preview](https://cloud.google.com/products#product-launch-stages)) feature is designed to work securely with your database schema. After registering your schema objects with a natural language configuration, you can call the `alloydb_ai_nl.get_sql()` function from your application to translate plain English questions into SQL queries, or use `explain_sql` to understand a query. The feature integrates with standard PostgreSQL roles and IAM for security, and you can use [parameterized secure views](https://docs.cloud.google.com/alloydb/docs/parameterized-secure-views-overview) for fine—grained access control. 

To accelerate setup and ensure accuracy, AlloyDB includes **productivity tools for automatic context generation** from your schema. These tools automatically generate schema context and suggest query templates, reducing the manual effort required to get started. You can further refine results by adding business—specific query templates to the **template store**. The underlying model can generate complex SQL—including multi—table joins, aggregations, and window functions—based on user intent and schema context, with accuracy improving as more context and templates are provided.

**Note:** To provide feedback about your experiences using AlloyDB AI natural language, [submit the User Experience Research: AlloyDB AI Natural Language form](https://docs.google.com/forms/d/e/1FAIpQLSfksRzklOU_T1aMVbI0tb0O5ZNpnone7XiD_KCBW2GWHo9uqA/viewform).

![Visual overview of AlloyDB AI natural language](https://docs.cloud.google.com/static/alloydb/images/natural-language-landing.png)

## Use cases

Explore how you can apply AlloyDB AI natural language queries can be applied to common business scenarios.

Use Case | Business Goal | Sample Question | Business Impact  
---|---|---|---  
trending_up Sales Analytics | Track sales performance and identify top reps | `"Who were our top 3 sales reps by revenue in Austin for the last quarter?"` | \- Accelerated Decisions   
\- Immediate, self-service sales analytics.  
explore Product Adoption | Understand user behavior and feature adoption | `"How many users on our 'Pro' plan used the new reporting feature last week?"` | \- Faster Iteration   
\- Quickly validate hypotheses and build better products.  
local_shipping Supply Chain | Monitor supply chain and identify bottlenecks | `"Show me all shipments from the Reno warehouse that are delayed by more than 3 days."` | \- Improved Efficiency   
\- Proactively solve operational issues.  
support_agent Customer Support | Analyze support tickets to find trends | `"What is the most common complaint category for tickets created in the last 7 days?"` | \- Better Service   
\- Identify and resolve customer issues faster.  
  
## Learn more

Explore Google developer resources to build your natural language query applications with AlloyDB.

Tutorial 

###  [ Conversational app tutorial ](https://medium.com/google-cloud/alloydb-powered-conversational-commerce-using-natural-language-to-sql-google-cloud-serverless-38773a2f7eac)

Learn to build a conversational commerce app with AlloyDB AI and Serverless. 

Guide 

###  [ How-to guide ](https://docs.cloud.google.com/alloydb/docs/ai/generate-sql-queries-natural-language)

A step-by-step technical guide on setting up, configuring, and using the `get_sql()` function. 

Codelab 

###  [ Generate SQL using AlloyDB AI natural language ](https://codelabs.developers.google.com/alloydb-ai-nl-sql)

Get practical experience with a guided tutorial on generating SQL from natural language. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
