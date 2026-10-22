---
url: https://docs.cloud.google.com/data-agent-kit/reference-resources/
title: Reference resources \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:15.256197+00:00
---

# Reference resources  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/reference-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Reference resources Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to reference Google Cloud data resources when working with Google Cloud Data Agent Kit. You can reference resources in your development environment or supported coding agent using explicit or implicit referencing, depending on the environment and agent that you use.

  * **Explicit referencing**. You explicitly identify a resource in chat or the user interface, such as by typing `@RESOURCE_NAME`, selecting a resource from the Model Context Protocol (MCP) resource menu, or using drag-and-drop.
  * **Implicit referencing**. You refer to a resource through natural language context in chat, such as typing `"this table"` or `"this dataset"`, referring to the open or selected resource.



## Referencing methods

If your development environment and coding agent support referencing, you can reference data resources in the following ways:

  * **Chat mentions** : In supported chat interfaces, type `@` followed by the resource name or ID (for example, `@DATASET_NAME`) to explicitly attach the resource context to your prompt.
  * **MCP resource menu** : Select a resource directly from the Model Context Protocol (MCP) resource picker in your IDE.
  * **Drag-and-drop** : Drag a data asset from the explorer tree directly into the chat or editor window.
  * **Natural language reference** : In environments that support implicit referencing, use contextual phrases like `"this table"` or `"this dataset"` to have the agent automatically infer the active resource.



The following table describes the supported referencing methods for each development environment and coding agent.

Development environment or agent | Chat mention (@) | MCP resource menu | Drag-and-drop | Natural language  
---|---|---|---|---  
VS Code (GitHub Copilot), Cursor, Antigravity IDE | Supported | Supported | Supported | Supported  
Claude Code CLI (standalone) | Supported | Not supported | Not supported | Supported  
Antigravity 2.0, Antigravity CLI, Claude Code (VS Code extension) | Not supported | Not supported | Not supported | Supported  
  
## Supported resources

The following table describes the referencing syntax and natural language phrases for supported Google Cloud resources across services.

  1. Partial table name is also supported. 
  2. In Claude Code CLI, use `@SESSION_ID`. 
  3. In Claude Code CLI, use `@BATCH_ID`. Implicit referencing is not supported. 

  
---  
Service | Resource | Chat mention syntax (@) | Natural language reference  
BigQuery | Dataset1 | `@DATASET_NAME` | `"this dataset"`  
| Table | `@TABLE_NAME` | `"this table"`  
| View | `@VIEW_NAME` | `"this view"`  
AlloyDB for PostgreSQL, Cloud SQL, Spanner | Table | `@TABLE_NAME` | `"this table"`  
| View | `@VIEW_NAME` | `"this view"`  
Spark | Cluster | `@CLUSTER_NAME` | `"this cluster"`  
| Serverless runtime | `@RUNTIME_NAME` | `"this runtime"`  
| Job | `@JOB_NAME` | `"this job"`  
| Interactive session2 | `@SESSION_NAME` | `"this session"`  
| Batch3 | `@BATCH_NAME` | Not supported  
  
## What's next

  * [Find and explore data](https://docs.cloud.google.com/data-agent-kit/find-explore-data)
  * [Query your data](https://docs.cloud.google.com/data-agent-kit/query-data)
  * [Use MCP servers](https://docs.cloud.google.com/data-agent-kit/use-mcp-servers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
