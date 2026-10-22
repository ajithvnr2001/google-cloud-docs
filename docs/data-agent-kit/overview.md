---
url: https://docs.cloud.google.com/data-agent-kit/overview/
title: Data Agent Kit overview \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:16.675102+00:00
---

# Data Agent Kit overview  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Data Agent Kit overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Data Agent Kit is built for data scientists, engineers, and data app developers. Data Agent Kit lets you manage your entire data workload lifecycle directly within your preferred development environment. You can use Data Agent Kit to build and oversee workloads or data apps without the need to context switch between the Google Cloud console, command-line tools, and your IDE.

Data Agent Kit offers two interfaces that integrate core Google Cloud services directly into your development environment:

  * **IDE extension**. The Data Agent Kit extension for VS Code and VS Code-compatible IDEs includes a UI component that provides a unified view of your data assets and data workloads within your IDE. This extension is installed by default in Cloud Workstations, and it's integrated into Cloud Code.
  * **Plugin**. The Data Agent Kit plugin lets you use natural language prompts in your preferred coding agent to work with your Google Cloud data. Supported agents include Antigravity CLI, Claude Code, Codex CLI, and Gemini CLI.



## Core capabilities

The extension streamlines complex data workflows through several key functional areas:

  * **Data discovery and exploration**. Connect to Google Cloud and explore your data. Query and analyze your data in Python and SQL. Ask questions about your data in natural language.
  * **Data pipeline development**. Build, test, and deploy data engineering pipelines on Managed Service for Apache Spark or BigQuery.
  * **AI and machine learning**. Explore and clean up your data, and use your data to train and deploy ML models.
  * **Agentic skills and tools**. Use built-in AI skills and tools to automate repetitive tasks and accelerate development.



## Main benefits

  * **Unified workflow**. Work with BigQuery, Dataflow, Managed Service for Apache Spark, Cloud Storage, Spanner, AlloyDB for PostgreSQL, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL all within a single IDE or coding agent.
  * **Task automation**. Leave writing boilerplate code and manual tasks to the agents. Focus on getting your workload to production and delivering business value.
  * **Best practices**. Develop and deploy your data apps and workloads with the built-in best practices.



## Supported services

Data Agent Kit provides a centralized interface for the following Google Cloud services:

**Technology area** | **Supported services**  
---|---  
**Analytics and governance** | BigQuery, Dataflow, Managed Service for Apache Spark, Managed Service for Apache Airflow, Knowledge Catalog  
**Databases** | AlloyDB, Bigtable, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, Spanner  
**Storage** | Cloud Storage  
  
## Limitations

The following limitations apply:

  * **Google Cloud databases**. For AlloyDB, only Identity and Access Management (IAM) database authentication is supported. For Cloud SQL, both IAM database authentication and built-in database authentication are supported.
  * **Data engineering pipelines**. Automated deployment of orchestration pipelines only works with GitHub Actions.



## What's next

  * [Install the extension](https://docs.cloud.google.com/data-agent-kit/install)
  * [Install the coding agent plugin](https://docs.cloud.google.com/data-agent-kit/install-plugin)
  * [Try a codelab that uses Data Agent Kit](https://codelabs.developers.google.com/next26/gen-keynote/raw-data-forecasting#0)
  * [Codelab: Analytics with the Data Agent Kit and Antigravity](https://codelabs.developers.google.com/dak-analytics-eng-antigravity-ide#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
