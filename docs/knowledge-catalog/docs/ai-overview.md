---
url: https://docs.cloud.google.com/knowledge-catalog/docs/ai-overview/
title: Knowledge Catalog for AI agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:06:10.886200+00:00
---

# Knowledge Catalog for AI agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/ai-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)



Send feedback 

#  Knowledge Catalog for AI agents Stay organized with collections  Save and categorize content based on your preferences. 

As data ecosystems grow increasingly complex, AI applications require more than just raw data access. They need business context. Knowledge Catalog represents an evolution from Dataplex, shifting the focus toward empowering AI and agentic systems.

At the core of this platform, a unified map links your physical data assets with business semantics, governance rules, and usage relationships. By integrating Knowledge Catalog into your AI workflows, you can achieve the following:

  * Ground AI agents to provide reliable, up-to-date, and contextual metadata to guide agent reasoning.

  * Reduce hallucinations and ensure generative models base their answers on established enterprise truths.

  * Provide a unified context—a single, governed view of your data landscape—to AI agents.




## Use cases

Knowledge Catalog serves distinct roles across the data and AI lifecycle:

  * **AI developers and agent builders.** Developers building custom bots or agents (for example, using LangChain or the Agent Development Kit (ADK)) that must query and understand enterprise data.

    * _Use cases:_ Natural language search and retrieval of context to enable agents to work with enterprise data; agentic data discovery.
  * **Data analysts.** Users who use AI-assisted tools such as Gemini in BigQuery or Looker to find data and understand its business meaning.

    * _Use cases:_ Natural language querying and conversational data exploration.
  * **Data stewards.** Domain experts who oversee AI-driven metadata enrichment and ensure the quality of the catalog's context.

    * _Use cases:_ Reviewing, curating, and promoting AI-generated metadata and descriptions.



## Access Knowledge Catalog context with MCP

Model Context Protocol (MCP) is a standardized bridge that lets AI agents and tools seamlessly connect to data sources like Knowledge Catalog.

To accommodate different deployment workflows, Knowledge Catalog offers two types of MCP implementations. Understanding when to use each is key to setting up your environment:

  * **Remote MCP Server:** when building cloud-native applications, deploying agents to serverless environments (like Cloud Run), or integrating with external managed services where you want to avoid managing local infrastructure.

  * **Local MCP Toolbox:** during local agent development, rapid prototyping, or when you need direct integration with local desktop IDEs such as VS Code or Cursor.




### Remote MCP Server

A Google-hosted endpoint that enables direct access to Knowledge Catalog tools for AI applications and services (for example, agents running on Cloud Run or external services like Claude).

  * **Endpoint:** `https://dataplex.googleapis.com/mcp`
  * **Benefits:** No need to run a local MCP server; suitable for serverless environments.
  * **Reference:** [Use a remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp)



### Local MCP Toolbox

A command-line tool that acts as a local proxy between your IDE (for example, VS Code, Cursor) or local tools and Knowledge Catalog.

  * **Installation:** Downloadable binary.
  * **Configuration:** Typically involves a `.mcp.json` or settings file in your project or IDE configuration.
  * **Benefits:** Ideal for locally secure development environments and integration with various IDEs.
  * **Reference:** [Use a local MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox)



## Enrich the context for Knowledge Catalog

To maximize the value of Knowledge Catalog for AI, the underlying graph must be rich with business context. You can achieve this through out-of-the-box features or custom agentic enrichment.

### Out-of-the-box enrichment with data insights

Data insights (powered by Gemini in BigQuery) automatically enriches your catalog, reducing the "cold start" problem for new data platforms. When enabled, it automatically generates the following:

  * Dataset and column-level descriptions.
  * Relationship graphs between tables.
  * Example queries based on historical usage patterns.



This provides immediate semantic understanding to downstream agents without requiring manual data stewardship.

For example, for a table named `telco_churn`, data insights can automatically generate descriptions for fields like `Tenure` and `MonthlyCharges`, infer relationships to customer tables, and publish an example query such as finding churn rates by segment to the catalog.

For more information, see [About data insights for structured data](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data).

### Custom context enrichment with agents

For organizations with specialized knowledge bases, you can build custom enrichment agents to ingest metadata from bespoke sources like internal wikis, code repositories, or proprietary systems.

  * **Knowledge Catalog APIs (CRUD operations):** use to add or update metadata in the catalog.

    * For example, call the `UpdateEntry` API method to programmatically attach an overview aspect to a table using documentation extracted from an internal system.
  * **Tools like the ADK:** use to build your enrichment agents.

    * For example, build a Java-based ADK agent that uses internal tools to extract technical wiki pages, uses an LLM to parse them into glossary terms, and syncs the terms to Knowledge Catalog.
  * **Export and import operations:** use for bulk metadata updates with review.

    * For example, export an AI-generated business glossary to a file, have data stewards review and refine the definitions collaboratively, and import the finalized file back into the catalog.



## What's next

  * [Use the Knowledge Catalog remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp).
  * [Use the Knowledge Catalog local MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox).
  * [Build a data discovery agent](https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent).
  * [Implement agentic analytics workflows for distributed data](https://docs.cloud.google.com/architecture/agentic-ai-cross-cloud-analytics).
  * [Manage data workloads in your IDE using the Data Agent Kit](https://docs.cloud.google.com/data-cloud-extension/vs-code/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
