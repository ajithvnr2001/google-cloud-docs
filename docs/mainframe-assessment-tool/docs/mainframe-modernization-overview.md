---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mainframe-modernization-overview/
title: Mainframe modernization overview \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:08.809146+00:00
---

# Mainframe modernization overview  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/mainframe-modernization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Mainframe modernization overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the mainframe modernization products available in Google Cloud to help you choose a path for modernizing and migrating your mainframe applications to Google Cloud.

You can use the tools and processes described here to assess, augment, rewrite, reduce migration risks, and test your mainframe applications in Google Cloud before you deploy them in production. The information on this page can help you to do the following:

  * Understand the Google Cloud products and tools that facilitate mainframe modernization, including Mainframe Assessment Tool, Antigravity, Mainframe Connector, and Dual Run.
  * Learn about the typical phases of a mainframe modernization journey: assessment, modernization, and validation.
  * Identify how these tools can accelerate your mainframe modernization process and reduce risk.



This page is intended for IT professionals, architects, and decision-makers who are planning or in the process of modernizing their mainframe applications by migrating to Google Cloud.

Before reading this page, make sure that you're familiar with the following:

  * [Understanding mainframe modernization products in Google Cloud](https://cloud.google.com/solutions/mainframe-modernization).
  * [General understanding of Google Cloud fundamentals](https://docs.cloud.google.com/docs/overview).
  * [Overview of Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview).



By using these tools, you can accelerate and reduce risk when migrating your applications to Google Cloud.

## Building a mainframe modernization strategy

Google Cloud provides a phased approach and tools to guide your mainframe modernization journey. The following are the products used in mainframe modernization:

  * **[Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview):** analyze your existing mainframe environment.
  * **[Antigravity](https://antigravity.google/):** assists in code transformation and generation.
  * **[Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview):** facilitates data conversion and migration.
  * **[Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview):** enables parallel testing for validation.



The following diagram shows a high-level overview of the mainframe modernization process:

![Diagram showing the three phases of mainframe modernization: Assess, Modernize, and Validate, with the Google Cloud tools used in each phase.](https://docs.cloud.google.com/static/mainframe-assessment-tool/docs/images/mainframe-modernization-overview.png)

## Key modernization activities

Successful mainframe modernization involves several key activities, supported by Google Cloud tools. The following diagram illustrates these activities:

![Diagram illustrating the key activities in mainframe modernization: Assess, Generate and Transform, Modernize Data, and Reduce Risks, each associated with specific Google Cloud tools.](https://docs.cloud.google.com/static/mainframe-assessment-tool/docs/images/mainframe-modernization-activities.png)

  1. **Assess mainframe applications:** Use Mainframe Assessment Tool to assess your mainframe applications. Mainframe Assessment Tool helps you understand the existing codebase, application and data dependencies, and extract business rules. This automated assessment and extracted business rules help you plan your migration to Google Cloud. In the modernization workflow, this process is referred to as reverse engineering.

  2. **Generate and transform code:** Use Antigravity to convert your mainframe application to modernized application code that can be migrated to Google Cloud. The extracted business rules from Mainframe Assessment Tool help you migrate only those business rules that are valid. Antigravity helps you generate your cloud-native code and transform existing code through natural language prompts and automated workflows. In the modernization workflow, this process is referred to as forward engineering.

  3. **Modernize and migrate mainframe data:** Use Mainframe Connector to migrate and convert data from mainframe-specific formats such as `EBCDIC` into formats which are compatible with Google Cloud services. This process lets you use your mainframe data with cloud services such as Cloud Storage and BigQuery.

  4. **Reduce migration risks with parallel testing:** Use Dual Run to run your workloads on both your mainframe and Google Cloud simultaneously. This parallel execution lets you check for consistency and functional validation, making sure that the modernized code is functionally equivalent to your mainframe applications system and ready to be deployed in production.




## Modernization phases

The modernization process has three phases to guide you from initial discovery all the way to final production deployment and cutover.

The following diagram shows the three key phases of the mainframe modernization journey:

![Mainframe modernization phases.](https://docs.cloud.google.com/static/mainframe-assessment-tool/docs/images/mainframe-modernization-phases.png)

### Phase 1: Assess your mainframe application (reverse engineering)

Analyze your existing mainframe applications, understand dependencies, extract business logic, and define the scope of your mainframe modernization project.

In this phase, you use [Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview) to analyze your existing mainframe applications and define the scope of your modernization project. Mainframe Assessment Tool uses [Gemini](https://docs.cloud.google.com/gemini/docs/overview) to generate natural language summaries, technical specifications, and business rules from your mainframe application source code. You can validate the extracted business rules and only export the valid business rules to use for application modernization.

Use Mainframe Assessment Tool to perform the following tasks:

  * [Create a mainframe application assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment): create an assessment to analyze your mainframe application, including source code in supported [languages](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#languages), [database schemas](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#database_schemas), [transaction monitors](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#transaction_monitors), and [scheduler configurations](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview#scheduler_configurations).
  * [Upload your mainframe application files and define business domains](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment#upload-data): define domains when you create an assessment to break down and map your mainframe application into logical business domains and smaller, migratable units to prioritize your migration strategy.
  * [Review and understand assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results): review reports to understand dependencies, databases, and call trees. For more information about the available report types, see [Discover and analyze source code](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results#discover-analyze). 
    * Review migratable units to prepare a migration plan: the **migratable units** report partitions assets into migration units to generate a preliminary migration plan.
  * [Extract business rules](https://docs.cloud.google.com/mainframe-assessment-tool/docs/business-rules-extraction): isolate and verify the core business logic within your mainframe application code. This ensures that only valid and critical rules are preserved during the modernization process. This process lets you review and validate the business rules.



### Phase 2: Modernize (forward engineering)

In this phase, you'll transform the insights from the assessment phase into modern, cloud-native applications and components. Use the outputs from Mainframe Assessment Tool, such as extracted business rules, to guide the modernization process.

You can also use the exported assessment results for further analysis:

  * **Export Assessment HTML or JSON reports:** export HTML or JSON reports for review and sharing. 
    * [Export HTML report](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results#export-report)
    * [Export JSON report](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results#export-json)
  * **Export Neo4j Assessment data from the asset relations:** export data to a Neo4j database to visualize and analyze complex relationships within your mainframe applications. 
    * [Export assessment data to your Neo4j database](https://docs.cloud.google.com/mainframe-assessment-tool/docs/export-results#export-to-neo4j)
  * **Mainframe Assessment Tool MCP server** : use natural language prompts with the Mainframe Assessment Tool MCP server to get further insights into your mainframe assessments. 
    * [Enable Mainframe Assessment Tool MCP server](https://docs.cloud.google.com/mainframe-assessment-tool/docs/mcp-server#enable_the_mcp_server)



Use [Antigravity](https://antigravity.google/) to perform the following tasks:

  * **Define target architecture and data models** : analyze your extracted business rules with Antigravity prompts to generate proposals for your target architecture. Design optimized data models (files, relational data), select appropriate data services (BigQuery, Spanner, AlloyDB for PostgreSQL), and choose ideal Google Cloud compute services (Spanner, Cloud SQL, Compute Engine, Cloud Run, or Google Kubernetes Engine (GKE)).
  * **Create AI-optimized implementation plans** : break down complex architectural requirements into a sequenced "forward-engineering" plan. This plan ensures tasks are appropriately sized and optimized for Antigravity-assisted code generation.
  * **Automate code generation** : generate new, modern, cloud-ready, and high-performance code that implements the extracted business rules and aligns with the target data models.

For more information, see [Modernize your mainframe application code with Antigravity](https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate#modernize-with-antigravity).




Use [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview) to perform the following task:

  * **Migrate and modernize mainframe data:** convert and migrate your legacy mainframe data to Google Cloud by using Mainframe Connector. This process ensures high data availability and consistency for both testing and production environments.

For more information, see [Choose your data migration journey](https://docs.cloud.google.com/mainframe-connector/docs/configurations).




### Phase 3: Validate

After deploying the modernized application, validate that it is functionally equivalent to your legacy mainframe application and ensure a reduced-risk transition to production.

This phase focuses on performing functional equivalence testing to ensure the modernized environment matches the legacy system's business logic.

Use [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview) to perform the following tasks:

  * **Test for functional parity by using Dual Run:** validate the modernized application by using Dual Run. By comparing real-world mainframe transactions and data with the Google Cloud environment in parallel, you can ensure functional parity, certify the modern application, and reduce regression risks before deployment. This activity is an important step for reducing risk in your migration project.
  * **Deploy and monitor** : deploy the modernized workload to production with confidence. Use Google Cloud observability products for ongoing monitoring and performance management.



For more information, see [Get started with Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/get-started).

## What's next

  * Learn how to [modernize and validate](https://docs.cloud.google.com/mainframe-assessment-tool/docs/modernize-validate).
  * Learn more about [Mainframe Connector](https://docs.cloud.google.com/mainframe-connector/docs/overview).
  * Learn more about [Dual Run](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
