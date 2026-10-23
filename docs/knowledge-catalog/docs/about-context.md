---
url: https://docs.cloud.google.com/knowledge-catalog/docs/about-context/
title: About data context in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:01.543921+00:00
---

# About data context in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/about-context/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data context in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Data context in Knowledge Catalog lets you unify technical structures, business rules, and real-world usage patterns into an active context layer. With Knowledge Catalog, you and your AI applications can discover, evaluate, and interpret data assets accurately and securely without manual validation or hallucinations.

## What is context?

_Context_ is the rich fabric of structural, operational, and semantic details that describes a data asset. Instead of representing a table as a standalone schema of names and data types, context provides the complete story of your data.

Knowledge Catalog organizes context into the following layers:

  * **Technical metadata**. The structural details ingested directly from source systems, including database schemas, field types, partitioning keys, and security tags (such as Identity and Access Management (IAM) policies).

  * **Semantic metadata**. The business meaning of the data, which includes business glossaries, metric relationships, classifications, domain terminology, and _golden queries_ (verified natural-language questions mapped to correct SQL code statements).

  * **Operational metadata**. The data's behavior and health over time, including execution profiles, profiling statistics, and data quality scores.

  * **Relationships**. The inferred or defined links between underlying storage tables and conceptual business indicators.

  * **Trust signals**. Indicators of verification, such as stamps of ownership and certification, that verify if an asset is an authoritative source.

  * **Agent guidance**. Unstructured descriptions (such as README files, usage notes, and execution logs) that guide autonomous tools on how and when to query a resource.




By unifying these layers, Knowledge Catalog helps ensure that your data is fully understood, helping you avoid the operational bottlenecks and uncertainty associated with siloed and undocumented data.

## How data context differs from metadata

While metadata provides the foundational building blocks, **metadata** and **context** aren't interchangeable:

  * **Metadata**. Descriptive attributes that define the underlying structure, location, and technical properties of an isolated data asset (for example, column names, data types, partition keys, and table sizes).
  * **Context**. The synthesized, multi-dimensional knowledge graph that combines technical schemas, business semantics, data relationships, operational behavior, and trust signals to give data meaning and guide reasoning.



Knowledge Catalog transitions metadata management from a passive catalog into a dynamic control plane of active context. The following table highlights the key differences between passive metadata and active data context:

Dimension | Technical metadata | Active data context  
---|---|---  
**Core focus** | Underlying specifications and storage format. | Business meaning, operational behavior, and relationships.  
**State** | **Passive** : Stored in catalog registries for manual lookup by engineers. | **Active** : Continuously enriched by AI, mined from query histories, and assembled dynamically for LLM prompts.  
**Primary consumers** | Database engines, data engineers, and compliance auditors. | AI agents, Large Language Models (LLMs), business analysts, and conversational interfaces.  
**Primary purpose** | Storage management, indexing, and compliance verification. | Grounding agent reasoning, resolving joins, and preventing hallucinations.  
  
### Example: Metadata compared to context

To understand how context expands upon technical metadata, consider how Knowledge Catalog represents a transaction column:

#### Technical metadata alone

Technical metadata provides structural information, but lacks business logic and operational guidelines:

  * **Table** : `fact_orders`
  * **Column** : `disc_val`
  * **Data type** : `NUMERIC`
  * **Storage properties** : Partitioned by `order_date`



An AI agent using only this technical metadata might guess that `disc_val` represents total customer discounts, but it can't determine whether that value includes tax, manufacturer rebates, or promotional coupons.

#### Enriched data context

Knowledge Catalog enriches the technical metadata with semantic, relational, and operational layers into a unified context payload:

  * **Technical schema** : `fact_orders.disc_val` (`NUMERIC`).
  * **Semantic definition** : Mapped to the business glossary term _"Promotional Discount"_ , defined as customer discounts applied at checkout, excluding manufacturer rebates and shipping allowances.
  * **Discovered relationships** : Automatically links `fact_orders.customer_id` to `dim_customers.id` and `fact_orders.promo_id` to `dim_promotions.id`.
  * **Operational usage** : Query history reveals that 90% of business queries filter this table by `status = 'COMPLETED'` and join it with `dim_promotions`.
  * **Trust and quality** : Scored with a 99.8% validity rating by automated data quality scans, with verified data freshness within the last 2 hours.
  * **Golden query** : Includes a verified SQL template demonstrating how to calculate net recognized revenue using `disc_val`.



With this complete context, an AI agent or data analyst can accurately generate queries and interpret data without manual human validation or hallucinations.

## The challenges of using data without context

In a distributed data estate, raw data without context is rarely enough to solve a business problem. When structured databases, unstructured logs, and analytical metrics lack business meaning, users and autonomous systems face a _context ceiling_ that makes data difficult to discover, trust, or operationalize for AI. Human analysts must perform manual validation to verify data sources, while AI agents often generate inaccurate answers (hallucinations) or fail to run actions.

Without structured context, organizations face several operational bottlenecks:

  * **Collaboration toil**. A lack of clear business definitions forces analytics and AI teams into continuous, manual coordination cycles with subject matter experts (SMEs) to build basic understanding of tables.

  * **Context drift**. Standard documentation remains static and decays over time. Without continuous monitoring, outdated metadata leads to incorrect assumptions and broken AI agent workflows.

  * **Reasoning failures**. AI agents and large language models might generate syntactically correct SQL queries but fail to respect the underlying enterprise logic, yielding calculations that are incorrect from a business perspective.

  * **Siloed information**. Internal knowledge regarding how to correctly filter or join datasets remains trapped in undocumented scripts or dashboard setups rather than being registered in a centralized inventory.




To overcome these operational bottlenecks and make data actionable, organizations require a reliable context engine across their data estate.

## Core pillars of context management

To maintain this reliable context engine across your data estate, Knowledge Catalog operates on three pillars:

### Aggregation

Knowledge Catalog automatically gathers metadata from across your built-in databases, Iceberg REST catalogs, and third-party platforms. It consolidates these fragmented inputs into a single, unified zone of governance, helping ensure that security policies and classification definitions inherit consistently.

### Enrichment

Using Knowledge Studio interfaces, data stewards and context engineers can continually update and curate specific context sets within the overall context graph. Knowledge Catalog automatically mines transaction logs, database schemas, and business intelligence models to discover column descriptions and table relations. Through the Knowledge Studio interface, this continuous learning lets human reviewers capture their institutional knowledge and apply it to your assets dynamically.

### Search and retrieval

Knowledge Catalog provides high-precision semantic search that lets you query your data estate in natural language. Because Knowledge Catalog understands permission groups (ACLs) and business terminology, both users and autonomous agents can locate relevant data context with low latency.

## How metadata and context are fed into Knowledge Catalog

To build a reliable context engine, Knowledge Catalog ingests and curates information through automated platform connectors, continuous AI enrichment, and extensible custom interfaces.

### First-party data sources and automated harvesting

Knowledge Catalog automatically harvests structural and operational metadata from core Google Cloud services without requiring manual configuration:

  * **Databases and analytical warehouses**. Services like BigQuery, Spanner, Cloud SQL, and AlloyDB for PostgreSQL continuously sync technical metadata, including table schemas, field data types, partitioning keys, clustering specifications, and dataset boundaries.



  * **Out-of-the-box BI semantic sync**. For Looker ( Google Cloud core), Knowledge Catalog automatically synchronizes business intelligence assets:

    * **LookML semantic definitions**. Models, Explores, views, dimensions, and measures.
    * **BI dashboard assets**. Dashboards, dashboard elements, and Looks.
  * **Data integration and transformations**. Services like Datastream capture change data capture (CDC) stream metadata, Dataform pushes table definitions and SQL transformations, and Cortex Framework publishes registered data products.




### Continuous AI-driven context curation

Beyond static technical schemas, Knowledge Catalog dynamically updates its context graph using built-in intelligence engines:

  * **Data insights**. Powered by Gemini in BigQuery, data insights mines historical query logs, user transactions, and schema patterns to generate natural-language column descriptions, discover table relationships (such as join keys), and propose verified _example queries_ ("golden queries") that capture enterprise logic. For more information, see [About data insights for structured data](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data).
  * **Automated data profiling and data quality**. Scans compute statistical distributions (such as distinct counts, null ratios, and sample values) and evaluate data against rule-based data quality checks, attaching live health scores to catalog entries. For more information, see [About auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).



### Human-in-the-loop curation with Knowledge Studio

To govern and orchestrate the active context graph, users operate within the Knowledge Studio. This interface provides the primary center for:

  * **Context sets**. Grouping related tables, unstructured documents, and glossaries into unified bundles that are ready for AI agent consumption.
  * **Enrichment workflows**. Reviewing AI-suggested column descriptions, applying business glossary mappings, and manually certifying assets as authoritative. For more information, see [Manage enrichment runs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).
  * **Environment organization**. Ensuring different domain teams (like Finance or Engineering) have their own isolated areas to manage semantic rules.



For more information, see [Enrich context with Knowledge Studio](https://docs.cloud.google.com/knowledge-catalog/docs/knowledge-studio).

### Custom metadata ingestion and third-party systems

For organizations with bespoke knowledge bases, third-party governance tools, or on-premises systems, Knowledge Catalog provides flexible ingestion mechanisms:

  * **Knowledge Catalog APIs (CRUD operations)**. Use the `CreateEntry`, `UpdateEntry`, and `CreateAspectType` API methods to programmatically register external assets and attach custom metadata aspects (such as compliance ratings or system documentation).
  * **Custom enrichment agents**. Use agent frameworks such as the Agent Development Kit (ADK) or LangChain to build custom enrichment agents. For example, an ADK agent can ingest technical documentation from internal wikis or Git repositories, use an LLM to parse them into standardized business glossary terms, and attach them to catalog entries. For more information, see [Build an AI agent to enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/build-agent-to-enrich-metadata).
  * **Export and import operations**. Use file-based (JSON or CSV) bulk export and import workflows to review AI-generated business definitions, collaborate with data stewards, and batch-update metadata. For more information, see [Export metadata](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata).



## How context is consumed across 1P and 3P services

Services and applications interact with Knowledge Catalog in two distinct roles:

  * **Metadata providers**. Services that send technical metadata, schemas, and LookML definitions into Knowledge Catalog (for example, Looker, Cloud SQL, and Spanner). Metadata providers push metadata into the catalog but don't necessarily consume business glossary definitions into their own user interfaces.
  * **Context consumers**. Services, developer tools, and AI agents that retrieve business definitions, operational profiles, and governance rules from Knowledge Catalog to ground their reasoning and execution.



Before applications and agents can consume context, you need to establish foundational business terms and quality rules. For more information, see [Establish foundational data context](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context) and [Build a policy-as-code data quality workflow](https://docs.cloud.google.com/knowledge-catalog/docs/build-policy-as-code-data-quality-workflow).

AI applications and services consume context from Knowledge Catalog through the following mechanisms:

### Built-in first-party (1P) integrations

Several Google Cloud services natively query Knowledge Catalog to provide context-aware AI experiences:

  * **Gemini in BigQuery (Conversational Agent)**. When you enter natural-language prompts in BigQuery Studio, Gemini automatically queries Knowledge Catalog business glossary definitions, column descriptions, and historical query relationships in the background. This grounds Gemini in enterprise business terminology, ensuring that generated SQL queries use the correct table joins and metric definitions.
  * **Data Engineering Agent in BigQuery**. Discovers and queries Apache Iceberg and BigQuery tables, automatically invokes semantic catalog searches to resolve asset dependencies, and generates catalog metadata during pipeline execution.
  * **Gemini and Agent Builder**. Custom GenAI agents and search applications built on Gemini use catalog metadata and business rules to ground model reasoning in verified enterprise facts.
  * **Google Cloud console and Business UI**. End users and data stewards explore assets using natural-language semantic search, view interactive data relationship graphs, and manage business glossaries.



### Third-party applications and AI agent ecosystems

Services and autonomous systems without built-in integrations consume context through open protocols and dedicated retrieval APIs:

#### Model Context Protocol (MCP)

Model Context Protocol (MCP) is an open standard that lets AI agents, developer tools, and IDEs connect directly to Knowledge Catalog tools. MCP provides a standardized interface to inspect table schemas, look up glossary definitions, and verify data quality scores.

Knowledge Catalog supports two MCP deployment options:

  * **Remote MCP Server**. A managed endpoint hosted by Google Cloud (or deployed on Cloud Run) for cloud-native agents, serverless workflows, and multi-agent platforms. For more information, see [Use the Knowledge Catalog remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp).
  * **Local MCP Toolbox**. A local CLI proxy that integrates with developer IDEs (such as VS Code and Cursor) and local development workflows. For more information, see [Use Knowledge Catalog with a local MCP Toolbox server](https://docs.cloud.google.com/knowledge-catalog/docs/pre-built-tools-with-mcp-toolbox).



#### Retrieve pre-formatted context with the LookupContext API

For custom AI pipelines and LLM applications, Knowledge Catalog provides the [`LookupContext` API method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext).

Instead of requiring an agent to make multiple sequential calls to inspect schemas, look up glossary terms, fetch data quality scores, and inspect query logs, the `LookupContext` method retrieves a unified, pre-formatted bundle of rich metadata in a single request.

Key capabilities of the `LookupContext` method include the following:

  * **LLM-ready formats**. Returns context formatted as `yaml` (default), `json`, or `xml`, designed for direct insertion into LLM system prompts.
  * **Token budgeting (`context_budget`)**. Lets you specify a target character budget. This is a soft budget, meaning the API intelligently truncates and prioritizes metadata to try to fit within your model's context window, but it does not guarantee staying strictly under the limit.
  * **Configurable context views**. 
    * **BASIC**. Returns fundamental entry metadata, schemas, column descriptions, overview text, and agent guidelines.
    * **STANDARD**. In addition to basic metadata, traverses the context graph to include multi-table join relationships, attached business glossary terms and synonyms, and verified sample queries.
  * **Discovered joins and golden queries**. Includes inferred table join conditions (for example, `orders.customer_id = customers.id`) and verified example SQL queries.



For more information, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context) and the [`lookupContext` REST reference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext).

## How context helps end users and AI agents

Knowledge Catalog provides universal context within its agentic data cloud by unifying technical schemas, business semantics, and quality metrics into an active context layer. By exposing this metadata through open interfaces like the Model Context Protocol (MCP), context retrieval APIs, and semantic search, Knowledge Catalog assists both users and autonomous systems.

### Eliminate manual trust work for users

Without a centralized semantic layer, you must investigate underlying databases and query histories to answer basic business questions. Standard catalogs act as passive inventories of schemas, which requires you to manually look up metric definitions or verify table cleanliness.

Knowledge Catalog converts this passive governance into active intelligence. By presenting quality scores, semantic descriptions, and usage warnings directly alongside data assets, Knowledge Catalog lets you trust and use data without waiting for engineering reviews.

### Ground autonomous agents and enable dynamic governance

AI agents and Large Language Models (LLMs) require strict, deterministic rules to interact with databases. Without explicit semantic context, agents make incorrect assumptions about column names or generate faulty SQL queries.

Additionally, active context transitions metadata management from a passive registry into an active governance layer. By defining verified business rules, metrics, and agent instructions directly within Knowledge Catalog, organizations can govern how agents retrieve, evaluate, and act upon corporate data.

Knowledge Catalog solves this gap. It exports unified active context profiles to your AI applications through standard interfaces like the Model Context Protocol (MCP) or the `LookupContext` API. Grounding your models in this metadata minimizes hallucinations, enforces governance rules, and helps ensure that autonomous actions are based on verified organizational truth.

### How AI applications consume context sets

Gemini Enterprise and other AI applications consume context sets through two primary patterns:

  * **Dynamic context discovery using semantic search:** In conversational or self-service analytics environments, users ask ad hoc questions in natural language (for example, _What was our quarterly net retention rate across enterprise accounts?_). When a user submits a prompt, the agent issues a semantic search query against Knowledge Catalog to locate the most relevant context set matching the question's domain. The agent injects the retrieved context into the active prompt, allowing it to generate accurate SQL queries against the underlying data warehouse.

  * **Preconfigured context sets for dedicated applications:** You can preconfigure an agent with an explicit context set reference by supplying its resource URI during setup. Binding a dedicated context set provides deterministic grounding, ensuring that all future interactions consistently use certified business definitions, without runtime search overhead. Because recurring enrichment tasks refine the context set over time, the downstream application automatically inherits these quality improvements without requiring manual reprompts or application redeployments.




Knowledge Catalog minimizes hallucinations and enforces governance rules by exporting unified active context profiles to your AI applications through standard interfaces like the Model Context Protocol (MCP) or the `LookupContext` API.

### Coordinate multi-agent workflows with shared context

In a multi-agent framework (or swarm), separate specialized agents collaborate to run complex workflows. When these agents operate across siloed environments without a shared context plane, they face a _context ceiling_ —they might use conflicting business rules, fail to locate relevant dependencies, or duplicate retrieval effort.

Using Knowledge Catalog as a centralized context registry helps you coordinate and scale multi-agent swarms. Grounding your swarm in Knowledge Catalog provides the following benefits:

  * **Shared business semantics**. All agents reference the same business meanings and definitions. For example, if a data analysis agent and a reporting agent both retrieve a table containing sales figures, they use the same glossary definition of a metric like `Gross Merchandise Value (GMV)` to help ensure consistency.

  * **Dynamic dependency resolution**. Agents can use context relationships to discover upstream and downstream resources programmatically. This lets a pipeline troubleshooting agent trace a data failure to its source table and hand off the task to a repair agent without hardcoding dependency rules.

  * **Unified connection interface**. By using Model Context Protocol (MCP), you expose a single semantic endpoint to the entire swarm. This eliminates the need to configure custom API integrations for each individual agent.

  * **Perimeter-level security governance**. Knowledge Catalog checks agent queries against preconfigured IAM roles. This helps ensure that agents retrieve only the resource context that they are explicitly authorized to access, preventing accidental data exposure across the swarm.




## Use cases for using data context

To understand how data context resolves complex inquiries, consider how Knowledge Catalog applies technical, semantic, and operational layers in practice:

### Ecommerce: Personalize search recommendations

To align seasonal marketing campaigns with product inventories, search agents must understand how unstructured promotional emails relate to structured product catalogs and user transaction tables. Knowledge Catalog maps these entities, letting recommendation models suggest relevant products in real time.

### Manufacturing: Optimize machinery maintenance

Predictive maintenance models require integrating structured parts logs with unstructured technician repair guides and live sensor feeds. By mapping relations between part numbers and manual chapters, Knowledge Catalog lets analytical systems predict equipment fatigue and schedule repairs before failures occur.

### Healthcare: Validate clinical trial data

Clinical research centers must verify that patient statistics conform to strict study rules, and that patient consent records map directly to trial result datasets. Knowledge Catalog maps context relationships to audit consent pipelines and alerts researchers to data profile anomalies, helping preserve trial integrity.

### Financial services: Evaluate credit risk

Loan underwriting models use customer credit scores, transaction histories, and active debt balances across separate source systems. Knowledge Catalog provides a unified graph of loan metrics, letting underwriting tools confirm that risk assessments use certified, compliant assets.

### Telecommunications: Diagnose network operations

Autonomous network management systems and agents analyze real-time signal behaviors, detect performance degradations, and apply self-healing corrective actions. By grounding these agents in Knowledge Catalog context, the systems can safely map relationships between technical logs and business service areas.

## What's next

Concept 

###  [ Knowledge Studio overview ](https://docs.cloud.google.com/knowledge-catalog/docs/knowledge-studio)

Learn how to orchestrate rich data context, build context sets, and ground AI agents using Knowledge Studio interfaces. 

Concept 

###  [ Context sets overview ](https://docs.cloud.google.com/knowledge-catalog/docs/context-sets)

Learn about Knowledge Studio's packaged context containers used to safely ground your downstream AI agents. 

Concept 

###  [ About enrichment tasks ](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks)

Learn how to configure AI-driven metadata extraction workflows to build data context automatically. 

Tutorial 

###  [ Establish foundational data context ](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context)

Build a business glossary, define custom aspect types, and enrich assets in BigQuery. 

Ai integration 

###  [ Ground agents with MCP ](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview)

Learn how Model Context Protocol connects agents to Knowledge Catalog tools and resources. 

Api 

###  [ Retrieve context with LookupContext ](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context)

Extract pre-formatted, token-budgeted YAML or JSON context for direct LLM prompt injection. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
