---
url: https://docs.cloud.google.com/architecture/agentic-ai-cross-cloud-analytics/
title: Implement agentic analytics workflows for distributed data \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:25.531800+00:00
---

# Implement agentic analytics workflows for distributed data  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-cross-cloud-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement agentic analytics workflows for distributed data Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-16 UTC

This document provides a high-level architecture for implementing cross-cloud analytics workflows that use AI agents. The document is intended for cloud architects, data engineers, and data scientists who want to use agentic AI for analytics workflows across multi-cloud data lakes, structured data warehouses, and unstructured data stores. The document assumes that you have a foundational understanding of agentic AI concepts, data analytics, and cloud architecture.

The Deployment section of this document provides a codelab that you can use to learn how to build an agentic analytics solution.

## Architecture

The following diagram shows an architecture for an agentic analytics solution that derives business insights from structured and unstructured data that's distributed across multiple data stores and cloud service providers.

![An architecture that uses an agentic development environment and an AI model to analyze data that's distributed across Google Cloud and other cloud service providers.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-cross-cloud-analytics-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-cross-cloud-analytics-architecture.svg)

The components in this architecture are organized into the following layers:

  * **User and agentic actions**

    * **Agentic development environment** : Data practitioners, like data engineers and data scientists, submit natural-language requests by using one of the following methods: 
      * An agentic development environment like [Google Antigravity IDE](https://antigravity.google/) or Microsoft Visual Studio Code.
      * A CLI agent like Gemini CLI, Claude Code, or Codex.
    * **[Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit)** : Data Agent Kit lets agents access trusted data in Google Cloud by loading appropriate skills and connecting to remote MCP servers for Google Cloud services.
    * **Foundation model** : To generate business insights from trusted context and data, the agentic development environment uses a foundation model, such as a [model from the Gemini family](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#generally-available-gemini-models). The model uses appropriate skills from Data Agent Kit and it uses the required MCP server tools to implement complex analytics workflows.
  * **Analytics workflows**

    * **[Borderless Lakehouse](https://docs.cloud.google.com/lakehouse/docs/introduction)** : Lakehouse provides a high-performance, unified metadata catalog that integrates the Apache Iceberg open table format with enterprise-grade storage in Google Cloud. With [cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access), Lakehouse lets you federate external catalogs like Databricks Unity Catalog without moving or copying data.
    * **[Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)** : This is the core data processing component in the architecture. The [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless) feature of Managed Service for Apache Spark supports high-performance, serverless data processing in batch and interactive modes. The Spark data-processing jobs use metadata from the Iceberg catalog in Lakehouse, read structured data from [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), and perform zero-copy reads from external sources like Amazon S3.
    * **[Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)** : The agent uses Knowledge Catalog to perform intelligent scans of unstructured data in [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction), extracts semantic metadata, and builds a context graph.
  * **Trusted data stores**

    * **Data in Google Cloud** : BigQuery serves as the central warehouse for structured data, including structured extracts from unstructured data in Cloud Storage.
    * **Data from external sources** : The architecture shows external data sources, such as data in Amazon S3 buckets and metadata in Databricks Unity Catalog. [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) provides high-bandwidth dedicated connectivity between Google Cloud and other cloud service providers.



## Products used

The architecture uses the following Google Cloud products and tools:

  * [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit): Agent extensions to let data scientists, data engineers, and data app developers manage the entire data lifecycle from within their preferred agentic development environments. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ Managed Service for Apache Spark](https://cloud.google.com/dataproc): A managed service that runs Apache Spark batch workloads on a managed compute infrastructure. 
  * [ Lakehouse](https://cloud.google.com/products/lakehouse): A high-performance storage engine that lets you build open data lakehouses and provides a unified interface for advanced analytics and AI. 
  * [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/introduction): An AI-powered service that provides a unified catalog of data assets with intelligent metadata and governance capabilities. 
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview): A service that provides high-bandwidth, low-latency, dedicated connectivity between Google Cloud and other cloud service providers. 
  * [ Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview): Google-managed remote services that implement the [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) to provide AI applications access to Google and Google Cloud products and services. 



## Use cases

The architecture that this document describes is suitable for the following use cases:

  * **Multi-cloud data analysis** : Efficiently query and analyze data that's distributed across Google Cloud and other cloud service providers without moving files or building complex [extract, transform, load (ETL)](https://en.wikipedia.org/wiki/Extract,_transform,_load) pipelines. For example, a marketing manager at a global retailer can analyze the effectiveness of marketing campaigns by joining customer loyalty data in Amazon S3 with marketing operations data in BigQuery.
  * **Intelligent data discovery** : Use natural language prompts and AI agents to discover, query, and process federated datasets across multiple environments. For example, a procurements specialist can determine common causes for supply chain disruptions based on structured data in a supply chain management (SCM) system combined with insights from unstructured email communications and damage-assessment reports.
  * **Structured data extraction from unstructured sources** : Scan large volumes of unstructured data, derive semantic metadata, and store structured data extracts in BigQuery for downstream analysis. For example, an operations controller can efficiently analyze expenses by extracting structured data from thousands of invoices that are stored in an unstructured format, such as PDF files.



## Security considerations

To help address the unique security risks of AI agents, Google recommends an [approach](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines deterministic security controls with dynamic, reasoning-based defenses:

  * **Human oversight** : Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions.
  * **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** : Assign each agent a workload-bound identity to enforce least-privilege access control and centrally manage credentials for external tools.
  * **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** : Enforce ingress and egress traffic governance, default-deny access policies, and inline prompt and tool inspection with [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
  * **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** : Verify that agents only connect to approved subagents and MCP tools.



The guidance in this section isn't exhaustive. For more information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

## Deployment

To learn how to build an agentic analytics solution by using Data Agent Kit, see the codelab, [Raw data to forecasting in seconds with AI agents](https://codelabs.developers.google.com/next26/gen-keynote/raw-data-forecasting#0). The codelab shows how Data Agent Kit lets you efficiently analyze data from within your preferred agentic development environment. All of the sample data that the codelab uses is stored in Google Cloud.

## What's next

  * Learn how Data Agent Kit lets you [use notebooks for data transformation and analysis](https://docs.cloud.google.com/data-agent-kit/transform-data).
  * Explore [use cases for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).
  * Learn more about [cross-cloud data access with Lakehouse](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access).
  * Learn how to accelerate Apache Spark workloads by using [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine).
  * Learn how you can use [Knowledge Catalog as a governance and agentic layer for BigQuery](https://docs.cloud.google.com/bigquery/docs/use-knowledge-catalog).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Abirami Sukumaran](https://www.linkedin.com/in/abiramisukumaran) | Staff Developer Advocate
  * [Arti Prasad](https://www.linkedin.com/in/arti-prasad) | Technical Writer
  * [Brad Miro](https://www.linkedin.com/in/bradmiro/) | Senior Developer Advocate
  * [Matthew Rahmann](https://www.linkedin.com/in/mrahmann) | Senior Product Manager
  * [Ranadip Chatterjee](https://www.linkedin.com/in/ranadipchatterjee) | Solutions Engineer
  * [Remigiusz Samborski](https://www.linkedin.com/in/remigiusz-samborski) | Lead Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
