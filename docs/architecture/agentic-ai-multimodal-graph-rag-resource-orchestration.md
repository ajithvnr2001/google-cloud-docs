---
url: https://docs.cloud.google.com/architecture/agentic-ai-multimodal-graph-rag-resource-orchestration/
title: Agentic AI use case: Multimodal GraphRAG resource orchestration \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:14.387582+00:00
---

# Agentic AI use case: Multimodal GraphRAG resource orchestration  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-multimodal-graph-rag-resource-orchestration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Multimodal GraphRAG resource orchestration Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-13 UTC

This document provides a high-level architecture for a multi-agent AI system that consolidates fragmented multimodal data into a searchable knowledge graph. The system enables users to upload data and then use the knowledge graph to identify potential issues or systemic risks. The architecture lets agents navigate complex data webs and maintain long-term personalization. It ensures that distributed resources are matched to search requirements with continuity.

_GraphRAG_ is a graph-based approach to retrieval augmented generation (RAG). RAG helps to ground AI-generated responses by augmenting prompts with contextually relevant data that's retrieved using vector search. GraphRAG combines vector search with a knowledge-graph query to retrieve contextual data that better reflects the interconnectedness of data from diverse sources. Prompts that are augmented using GraphRAG can generate more detailed and relevant AI responses.

The intended audience for this document includes architects, developers, and administrators who build and manage AI infrastructure and applications in the cloud. This document assumes that you have a foundational understanding of AI agents and models. The document doesn't provide specific guidance for designing and coding AI agents.

The deployment section of this document provides a code sample that demonstrates how to define a Spanner Graph schema and link multimodal entities for agentic retrieval.

## Architecture

The following shows a high-level view of an architecture of a multi-agent AI system that enables multimodal GraphRAG resource orchestration:

![High-level architecture of a multi-agent AI system that enables multimodal GraphRAG resource orchestration.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-high-level.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-high-level.svg)

The architecture in the preceding diagram has two workflows: data ingestion and search.

  * The **data ingestion** workflow consolidates fragmented multimodal records into the unified knowledge graph. This workflow uses a sequential multi-agent pattern to upload raw data to Cloud Storage, extract complex relationships using Gemini, and update the Spanner Graph knowledge graph to ensure that the data is available for retrieval.
  * The **search** workflow lets you retrieve insights and ground responses through a GraphRAG process. This workflow uses Gemini and specialized subagents to navigate the knowledge graph and consolidate findings based on previous session data.



The following tabs provide architecture diagrams that show the data ingestion and search workflows: 

### Data ingestion workflow

The following diagram shows a detailed architecture for a data ingestion workflow.

![Architecture that shows the data ingestion workflow.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-data-ingestion.svg)

![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-data-ingestion.svg)

The preceding diagram shows the following data flow:

  1. The user interacts with the web application to upload new data. For example, a financial analyst might upload an earnings PDF, a recording of a shareholder meeting, or a market performance chart.
  2. The web application forwards the request to the root agent. The root agent is a [coordinator agent](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#coordinator-pattern) that receives requests and is deployed on a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service.
  3. The root agent retrieves persistent session data from [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) to personalize the search results based on the user's preferences from past sessions.
  4. The root agent uses Gemini on Gemini Enterprise Agent Platform to interpret the request and it delegates the task to the multimedia agent to execute the data ingestion pipeline.
  5. The multimedia agent initiates the [ sequential pattern](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#sequential-pattern) and it forwards the raw input to the upload agent.
  6. The upload agent performs the following tasks: 
     1. Stores the raw file in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects) and detects the media type.
     2. Forwards an intermediate summary of the actions that it performed to the extraction agent.

  7. The extraction agent performs the following tasks: 
     1. Fetches the data URI from the storage bucket and uses Gemini to parse the data and identify structured entities. For example, the entities of financial data can include corporate subsidiaries, fiscal quarters, and revenue sentiment.
     2. Forwards the structured entities and intermediate summary of the actions that it performed to the graph agent.
  8. The graph agent performs the following tasks: 
     1. Receives the structured entities and uploads the data to the knowledge graph. [Spanner Graph](https://docs.cloud.google.com/spanner/docs/graph/overview) creates or links nodes that represent issuers, stakeholders, and market instruments.
     2. Forwards an intermediate summary of the actions that it performed to the summary agent.
  9. The summary agent produces a response that contains a text summary of the ingestion results and the actions that were conducted by all subagents. The summary agent sends the response to the multimedia agent.
  10. The multimedia agent forwards the summary response back to the root agent.
  11. The root agent triggers a [ callback function](https://adk.dev/callbacks/types-of-callbacks/#after-agent-callback) to save session data to [Gemini Enterprise Agent Platform Sessions ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions). The root agent extracts custom [ memory topics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories#memory-topics) from the session to save information about critical focus areas. For example, a financial analyst might create a memory topic to track regulatory flags or sectoral trends.
  12. The root agent forwards the summary response to the web application.
  13. The web application forwards the response back to the user.



### Search workflow

The following diagram shows a detailed architecture for a search workflow.

![Architecture that shows the search workflow.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-search.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-multimodal-graph-rag-resource-orchestration-search.svg)

The preceding diagram shows the following data flow:

  1. A user initiates a search request to the web application. For example, a portfolio manager submits a request to detect any circular transaction patterns that involve more than three entities where the total volume exceeds $1 million within a 24-hour window.
  2. The web application forwards the request to the root agent. The root agent is a [ coordinator agent](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#coordinator-pattern) that receives requests and is deployed on a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) service.
  3. The root agent retrieves persistent session data from [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) to personalize the search results based on the portfolio manager's historical preferences and context.
  4. The root agent uses Gemini on Agent Platform to determine the optimal search strategy: 
     * **Keyword search** : Uses SQL `LIKE` clauses to match exact categories or locations.
     * **Semantic RAG search** : Uses the [ embedding model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings) and [cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance) to find semantically similar data entries.
     * **Hybrid search** : Executes keyword search and semantic RAG search and merges the results using [Reciprocal Rank Fusion (RRF)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/about-hybrid-search#rrf) to ensure high relevance and coverage.
  5. The root agent performs the appropriate search strategy on the knowledge graph, which is stored in [Spanner Graph](https://docs.cloud.google.com/spanner/docs/graph/overview), and retrieves the search results.
  6. The root agent triggers a [ callback function](https://adk.dev/callbacks/types-of-callbacks/#after-agent-callback) to save session data to [Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions). The root agent extracts custom [memory topics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/generate-memories#memory-topics) from the session. For example, a portfolio manager might create a memory topic to track regulatory flags or emerging sectoral trends.
  7. The root agent forwards the summary response to the web application.
  8. The web application forwards the response back to the user.



## Products used

This reference architecture uses the following Google Cloud products and features:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Spanner Graph](https://docs.cloud.google.com/spanner/docs/graph/overview): A graph database that provides the scalability, availability, and consistency features of Spanner.
  * [ Gemini Enterprise Agent Platform Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions): A persistent storage service that saves and retrieves the history of interactions between a user and agents. 
  * [ Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank): A persistent storage service that generates, refines, manages, and retrieves long-term memories based on a user's conversations with an agent. 



For information about selecting alternative components for your agentic AI system including framework, agent runtime, tools, memory, and design patterns, see [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).

## Use case

The architecture is designed for use cases that consolidate and analyze fragmented multimodal data to optimize resource allocation and information retrieval. By maintaining independent subagents, the system supports modular updates and ensures that distributed resources are matched to search requirements with high continuity. The integration of Spanner Graph as a knowledge graph enables the agentic AI system to model complex, interconnected data. This integration facilitates rich contextual understanding and sophisticated query capabilities that can be challenging or inefficient with relational or NoSQL databases.

For the following use cases, a graph database excels at representing the arbitrary and evolving connections that are derived from multimodal data. These connections would otherwise require complex and rigid schema management in a relational database.

The following are examples of use cases for the architecture that's described in this document:

  * **Enterprise HR talent mobility** : Improve keyword search for large-scale recruitment search by identifying qualified internal candidates through semantic expansion. The architecture extracts technical skills and soft-skill assessments from multimodal portfolios and video introductions to build a comprehensive talent graph. The Spanner knowledge graph traces relationships between employees, competencies, and project history. The trace results identify experts based on conceptual depth and flag understaffed projects.
  * **Social media content analysis** : Identify specific memories or trends by performing advanced content discovery and network analysis on social media platforms. The system processes uploads like videos, voice memos, and vlogs, and then it extracts entities, topics, sentiment, and mentions. The Spanner knowledge graph traces relationships between users, their connections (friends and followers), posts, likes, comments, shared topics, and trends.



## Design considerations

The following sections provide general recommendations for designing the AI agents and implementing this architecture for production.

The guidance in this section isn't exhaustive. For more information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

### AI agent design

To improve the cost and performance of your agents, consider the following recommendations:

  * **Agent system design** : Deconstruct complex workflows into multiple specialized agents with well-defined responsibilities instead of a monolithic agent. This separation of concerns simplifies prompt engineering, minimizes instruction drift, and enables granular model scaling. The architecture routes high-volume, well-defined tasks to smaller, faster models while reserving complex reasoning for high-capacity models.
  * **Tool design** : Segregate tools into multiple, focused methods instead of using a single monolithic method. This approach ensures consistency across the codebase, reduces logic branching, and enables specific optimization paths, such as skipping query analysis when a direct search method is invoked.
  * **Agent context** : To prevent downstream agents from repeating queries against upstream data in a sequential pipeline, pass sufficient context through the agent state. Use well-defined JSON structures for shared state so that each agent can parse data reliably.
  * **Session state storage** : Use session state for immediate conversation history and use Memory Bank for distilled facts across sessions. Inject memory context at the start of a session so that the agent can reference preferences without reprocessing long conversation histories.
  * **Memory quality** : Let users [clear or update stale memories](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/revisions#memory-deletion) if their preferences or roles change over time.



### Security, privacy, and compliance

To help address the unique security risks of AI agents, Google recommends an [approach](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines deterministic security controls with dynamic, reasoning-based defenses:

  * **Human oversight** : Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions.
  * **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** : Assign each agent a workload-bound identity to enforce least-privilege access control and centrally manage credentials for external tools.
  * **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** : Enforce ingress and egress traffic governance, default-deny access policies, and inline prompt and tool inspection with [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
  * **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** : Verify that agents only connect to approved subagents and MCP tools.

  * **Implement fine-grained access control** : Use [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) to authorize access at the table and column level. Restrict the Cloud Storage bucket policy so that only the Cloud Run service account has access.

  * **Sanitize inference and responses** : Use [Model Armor](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) to inspect and sanitize both inference requests and model responses. This sanitization mitigates prompt injection risks from multimodal content that users upload. It also helps prevent the accidental exfiltration of personally identifiable information (PII) or sensitive data in agent outputs.




### Reliability

To help ensure that your agent configurations meet your reliability requirements, consider the following recommendations:

  * **Implement agent retry logic** : To handle transient errors like quota limits, implement [retry logic](https://docs.cloud.google.com/run/docs/jobs-retries) with exponential backoff for calls to Agent Platform endpoints and Spanner.
  * **Set file limits** : To avoid API timeouts from large files, set explicit [upload size limits](https://docs.cloud.google.com/storage/quotas) and separate large videos into [chunks](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/fine-tune-rag-transformations) before data entities are extracted. For more information, see [Customize video processing](https://ai.google.dev/gemini-api/docs/video-understanding#customize-video-processing).



### Operational efficiency

To help ensure that your agent configurations meet your operational efficiency requirements, consider the following recommendations:

  * **Use structured logging** : Log all agent tool invocations and pipeline outcomes with [structured metadata](https://docs.cloud.google.com/logging/docs/structured-logging). Structured logs let you query logs and dashboards in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).
  * **Implement tracing** : To diagnose latency hotspots, use [Cloud Trace](https://docs.cloud.google.com/trace/docs) to capture end-to-end request traces across the agent runner and tool execution.
  * **Evaluate agent quality** : Periodically [evaluate agent output quality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents) using the Gen AI evaluation service to verify tool selection trajectories and response quality.



### Cost optimization

To help ensure that your agent configurations meet your cost requirements, consider the following recommendations:

  * **Storage costs** : To reduce storage costs, use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to move files to Nearline or Coldline [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes) after a defined retention period.
  * **Cost analysis and management** : To analyze and manage Agent Platform costs, we recommend that you create baseline metrics for queries per second (QPS) and tokens per second (TPS). Then monitor these metrics after deployment. The baseline that you create as part of cost management can help you determine capacity planning. For example, the baseline helps you determine when [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput) might be necessary.



### Performance optimization

To help ensure that your agent configurations meet your performance requirements, consider the following recommendations:

  * **Root agent routing** : To minimize latency and avoid unnecessary sub-agent invocations, clearly define routing logic in the agent instructions. Ensure each tool's purpose, input parameters, and expected outputs are documented in string literals to help the model select the correct tool.
  * **In-database AI models** : To reduce latency, use the Spanner [`ML.PREDICT`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/ml-functions#mlpredict) function to call models inline within SQL queries. Monitor Agent Platform quota usage, because hybrid search workloads can trigger multiple model calls per query.
  * **Resource allocation** : Depending on your performance requirements, configure the [memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) to be allocated to the Cloud Run service.



## Deployment

To deploy a sample implementation of this architecture, try the [Way Back Home Level 2 codelab](https://codelabs.developers.google.com/codelabs/survivor-network/instructions#0).

## What's next

  * Learn about how to [host AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn how to build a [GraphRAG infrastructure for generative AI using Agent Platform and Spanner Graph](https://docs.cloud.google.com/architecture/gen-ai-graphrag-spanner).
  * Learn [best practices for designing Spanner Graph schema](https://docs.cloud.google.com/spanner/docs/graph/best-practices-designing-schema).
  * Learn how to [get multimodal embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings).
  * Learn how to build a [multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system).
  * Explore learning resources to build and deploy enterprise-grade agents with [Gemini Enterprise Agent Ready (GEAR)](https://developers.google.com/program/gear).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Annie Wang](https://www.linkedin.com/in/anniewangtech/) | Software Engineer
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer



Other contributors: 

  * [Christina Lin](https://www.linkedin.com/in/weimeilin/) | Developer Relations Engineer Manager
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Olivier Bourgeois](https://www.linkedin.com/in/olivi-eh/) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
