---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices/
title: Best practices for Data Cloud connectors that use conversational analytics \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:15.728682+00:00
---

# Best practices for Data Cloud connectors that use conversational analytics  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Best practices for Data Cloud connectors that use conversational analytics Stay organized with collections  Save and categorize content based on your preferences. 

When you connect [Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud) in federated query mode, Gemini Enterprise uses the Model Context Protocol (MCP) to query your data sources in place. While MCP tool definitions give the assistant the mechanics to execute SQL, answering natural-language business questions with high accuracy and low latency requires two additional layers of guidance:

  * **A default analytical harness** : Engine-specific procedural skills that teach the Gemini Enterprise assistant how to plan queries, resolve filter values, use advanced analytical functions, and handle errors like an expert data analyst.
  * **Organizational context** : Domain-specific skills, custom instructions, and [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) metadata that map your company's business vocabulary, KPI definitions, and governance guardrails to the right underlying tables and models.



This document describes how Data Cloud connectors use built-in analytical skills managed by Google, and how you can use [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog), custom [skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills), and assistant instructions to provide organizational context for your data.

## Understand the default analytical harness

Out-of-the-box MCP tools expose low-level operations (such as listing tables or running a SQL string), which by themselves are often insufficient for complex multi-step data analysis. First-party Data Cloud connectors bridge this gap by bundling a **default analytical harness** —a set of built-in, Google-managed skills derived from the conversational analytics agent harness. These built-in skills automatically handle core analytical tasks—such as generating read-only `SELECT` queries, recovering from SQL compiler errors, and invoking built-in BigQuery AI, ML, and graph functions (such as `AI.FORECAST`, `AI.DETECT_ANOMALIES`, `AI.CLASSIFY`, `AI.AGG`, `AI.GENERATE`, and `GRAPH_TABLE`)—without requiring any configuration or action from you.

Because Google controls these built-in connector skills, you can't modify or add context to the connectors directly. Instead, you can resolve common query execution, search latency, and metric accuracy problems by configuring connector settings, curating metadata in [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog), or [creating and using custom skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) in your Gemini Enterprise app.

The following table describes common problems that you might encounter when using Data Cloud connectors and options to resolve them:

Problem | Options to resolve  
---|---  
Ensuring that all BigQuery queries run in a single project |  Configure the **Billing Project ID** (under **Advanced options**) when you [create the BigQuery data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery#create-data-store). Setting a billing project ensures that all BigQuery query jobs executed through the connector run and are billed in that designated Google Cloud project.  
Reducing search latency or prioritizing specific data |  Use one or both of the following options to narrow where the agent searches and queries data:

  * **Create a custom skill** : [Create and share a skill](https://docs.cloud.google.com/gemini/enterprise/docs/skills) in your Gemini Enterprise app that guides the agent to only search for or query data in specific Google Cloud projects, datasets, or tables. For example, include the following instructions in your skill: _"When answering questions about sales, revenue, or customer activity, only search for metadata and run SQL queries against tables in the`analytics-prod.sales_mart` dataset. Don't scan staging, sandbox, or archive datasets."_
  * **Create a Knowledge Catalog data product** : Curate high-priority tables into a [Knowledge Catalog data product](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview) (see [Create data products](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products)) so the agent can discover authoritative assets directly.

  
Agent using the wrong definition of a metric or joining on incorrect keys |  Use one or more of the following options to standardize definitions and join logic:

  * **Create custom skills** : [Create and share custom skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) (and [manage shared skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills)) in your Gemini Enterprise app that tell the agent how to define and calculate your metrics (see Choose where to define business metrics: Custom skills versus Knowledge Catalog for an example).
  * **Curate glossaries and golden queries in Knowledge Catalog** : Ensure that metric definitions, business glossaries, and pre-verified sample queries (golden queries) are curated and surfaced in Knowledge Catalog. Golden queries provide certified SQL join syntax that helps prevent the agent from hallucinating table joins on complex schemas. For best practices on structuring metadata for AI agents, see [Establish foundational data context with Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context) and [Manage glossaries on Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).

  
  
To compare the advantages of using Knowledge Catalog versus custom skills, see Choose where to define business metrics: Custom skills versus Knowledge Catalog. For step-by-step instructions on creating and enabling skills in your app, see [Create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) and [Manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills).

## Provide organizational context with skills and Knowledge Catalog

Because Data Cloud connectors are not restricted to a single dataset or table—they can access all resources in the connected data source that the authenticated user has permission to query—the assistant needs organizational context to know which assets are authoritative and how your business calculates key metrics.

Use a layered approach that combines **Knowledge Catalog** , **organization-wide custom skills** , and **user personalization** :

### 1\. Ground data discovery with Knowledge Catalog

When you connect a BigQuery or database connector in federated query mode, [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app. Rather than making sequential exploratory calls across raw database schemas, the agent uses Knowledge Catalog tools to search for data that the user has access to and look up rich metadata context in a single workflow.

If your organization curates metadata in third-party catalogs (such as DataHub) or internal documentation wikis, sync those descriptions into Knowledge Catalog or capture essential business rules in organization-wide custom skills so the agent can discover them.

### 2\. Choose where to define business metrics: Custom skills versus Knowledge Catalog

To codify organization-specific analytical rules and standardize business metric definitions and SQL formulas across conversations, you can either:

  * [Create, upload, and share custom skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) (and [manage shared skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills)) directly in Gemini Enterprise.
  * Work with your data stewards to curate enterprise metric definitions, business glossaries, and pre-verified example queries in [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context) (see [Manage glossaries on Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries) and [Data products overview](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview)).



Defining exact calculation logic and filter rules for company KPIs ensures that the assistant doesn't have to guess. For example, you can define that **"Active Customer"** strictly means an account in `analytics_prod.crm.user_events_log` with more than 10 platform logins in the past 30 days (`event_type = 'LOGIN'` and `is_test_account = FALSE`), or that **"Net Contribution Margin"** must exclude promotional giveaways (`order_type != 'PROMO'`) and inventory shrinkage (`status != 'SHRINKAGE'`).

When choosing whether to implement metric definitions in custom skills within Gemini Enterprise or in Knowledge Catalog, consider the following trade-offs:

  * **Knowledge Catalog** : 
    * **Advantages** :
    * Enforces Identity and Access Management (IAM) access controls so users and agents only discover metadata and definitions that they have permission to view.
    * Can be reused across other agent harnesses, tools, and platforms outside of Gemini Enterprise (such as BigQuery Studio and MCP clients).
    * Centrally maintained by data governance teams without requiring individual app users to enable a skill.
    * **Disadvantages** :
    * Provides descriptive metadata context and sample queries rather than strict procedural instructions, so the agent might need additional prompting for complex, multi-step calculation flows.
  * **Organization-wide custom skills in Gemini Enterprise** : 
    * **Advantages** :
    * Provides specific, prescriptive procedural instructions and exact SQL formulas that the agent adheres to deterministically within the app.
    * Can be rapidly created and updated by Gemini Enterprise app administrators without modifying corporate catalog resources.
    * **Disadvantages** :
    * Must be [shared with users](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills) and enabled in Gemini Enterprise, and applies only within Gemini Enterprise rather than across other harnesses or platforms.



### 3\. Tailor analysis with user skills and personalization

Individual analysts and business users can layer personal context on top of organization-wide skills:

  * **User-created skills** : End users can [create personal skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) for recurring analytical tasks or team-specific defaults—for example, a skill stating that whenever the user asks for "weekly product performance," the assistant should automatically filter for their product line, exclude QA traffic, and group results by fiscal week.
  * **Gemini Enterprise memory and personalization** : When [personalization](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization) is enabled, the assistant can retain user-specific preferences and clarifications across sessions, reducing repeated disambiguation prompts over time.



## Choose where to configure each type of context

Because Google controls the built-in skills attached to Data Cloud connectors, you can't add custom context directly to a connector. Instead, use the following table to decide where to configure your analytical rules and business context:

Context layer | Managed by | Best used for | Example  
---|---|---|---  
[Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) metadata | Data stewards and catalog administrators | Dynamic asset discovery across large data estates, table and column descriptions, data quality signals, dataset glossaries, and verified sample SQL queries. | Curating certified Data Products and business glossary terms in `analytics_prod` so the agent can discover authoritative tables and metric definitions.  
[Organization-wide custom skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) and [assistant instructions](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant) | Gemini Enterprise administrators and data operators | Deterministic project and dataset scoping, company-wide KPI definitions, disambiguation rules, and response conventions. | Restricting queries to specific production datasets; defining the exact SQL calculation for "Weighted Net ARR".  
User skills and [personalization](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization) | Individual end users and analysts | Role-specific default filters, preferred metric layouts, and recurring team workflows. | Automatically applying EMEA region and active QA filters when a user asks for "monthly pipeline metrics".  
  
## What's next

  * Learn how to [create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) and [manage shared skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills) in Gemini Enterprise.
  * Review [Data Cloud connectors overview](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud) and [Secure Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
