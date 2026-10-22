---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits/
title: Quotas and limits for Workflow Builder \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:37.390340+00:00
---

# Quotas and limits for Workflow Builder  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Quotas and limits for Workflow Builder Stay organized with collections  Save and categorize content based on your preferences. 

A _quota_ is a configurable or allocated limit on the amount of a resource you can use, such as daily agent creations or queries. For seat-based subscriptions, quotas are automatically adjusted based on the number of licenses your organization purchases. A _limit_ is a system constraint or capacity threshold, such as subagent depth, file upload size, or the number of individuals an agent can be shared with. System limits are fixed constraints, unless explicitly noted as an adjustable administrative setting.

For information on overall Gemini Enterprise quotas, pooling across editions, and overage pricing, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages).

**Workflow Builder limits at a glance:**

  * **Creation quotas:** Frontline (0), Standard (1/user/day pooled), Plus (10/user/day pooled), Pay-as-you-go (unlimited).
  * **Agent capacity:** 1,000 agents per user; 10,000 agents per app instance (configurable by administrators).
  * **Sharing limits:** 1,500 individual accounts per agent (IAM policy cap). Use Google Groups for larger audiences.
  * **Flow complexity:** Single-level subagent depth (1); maximum 50 subagents routed by chat root; maximum 100 nodes per flow.
  * **Knowledge base:** 20 MB max file size; 100 files max per agent; 10 files per upload batch; 800,000 combined context tokens.
  * **Schedules:** Multi-region only; 14-day credential validity; up to 5-minute execution latency.



## Feature and edition-based quotas

Creating and running agents in Workflow Builder depends on your Gemini Enterprise edition.

### Daily creation quotas

Creating, drafting, and registering agents consumes a daily creation quota allocated by edition (`discoveryengine.googleapis.com/agents_tier_enterprise_regional`). Daily creation quotas are pooled across all users with licenses for that edition within a specific project and location, and reset daily at midnight Pacific Time (PT).

This daily creation quota applies to both:

  * Creating and drafting custom agents in Workflow Builder.
  * Registering external, custom, or partner agents (such as [A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent), [ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent), or [Dialogflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent)) with an app instance or engine using the Google Cloud console or the [`agents.create`](https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.agents/create) API.

Edition | Daily creation quota | Description  
---|---|---  
Frontline Worker / Starter | 0 | Cannot create or register custom agents. Frontline licenses provide 0 creation quota and don't contribute to the project's pooled creation quota. Users can only run agents shared with them.  
Standard | 1 agent per user per day (pooled) | Pooled across all Standard edition licensed seats in the project and location. For example, 100 licenses provide 100 creation and registration operations per day for the project.  
Plus | 10 agents per user per day (pooled) | Pooled across all Plus edition licensed seats in the project and location. For example, 100 licenses provide 1,000 creation and registration operations per day for the project.  
Pay-as-you-go | Unlimited | No daily creation limits. Usage is billed according to underlying resource consumption and query volume.  
  
**Important: Agent registration across multiple engines or apps**

Agent registrations are scoped to an application instance (engine). If your architecture deploys a centralized or horizontally scaled agent backend registered across multiple Gemini Enterprise engines or apps in a project, each registration API call (`agents.create`) counts as an agent creation against the project's daily quota.

If the number of registration calls in a day exceeds the number of distributed Standard licenses in the project, subsequent calls fail with `HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded`.

**Deployment recommendation:** If automated deployment scripts or CI/CD pipelines need to register an agent across many apps in a single project (for example, 60+ apps), ensure that an equivalent number of Standard licenses (for example, 60+ seats) are temporarily distributed to the project before initiating the rollout. Alternatively, pace automated registrations across daily quota reset windows.

For more information about how quotas are pooled, calculated, and billed for overages across editions, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#edition-quotas).

### Agent capacity limits

The following limits govern the number of active agents that can exist in an application instance:

Resource | Default limit | Scope | Description  
---|---|---|---  
Agents per user | 1,000 | Per user account | The maximum number of agents that a single user can create and own.  
Agents per application instance | 10,000 | Per application instance | The total maximum number of agents that can exist across all users within an application instance.  
**Note:** App administrators can adjust the per-user and per-instance agent limits in the application's [feature control configurations](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls). 

## Sharing limits

When sharing an agent with colleagues in your organization, the following limits apply:

Setting | Limit | Description  
---|---|---  
Maximum individual members per agent | 1,500 individual accounts | The maximum number of individual user accounts that can be added directly to an agent's access list. Enforced by Google Cloud IAM allow policies.  
Google Groups support | Unlimited total members (1 group = 1 policy member) | Sharing with a Google Group counts as a single member toward the 1,500-member policy limit.  
  
### Sharing limit error behavior

If you attempt to share an agent with more than 1,500 individual user accounts, the operation fails and returns the following error:
    
    
    The number of members in the policy (1,501) is larger than the maximum allowed size 1,500.
    

### Best practices for sharing at scale

To share an agent with large audiences (such as team-wide, department-wide, or organization-wide distributions) without encountering the 1,500-member IAM limit:

  1. Request that your app administrator [enable group sharing](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls) in feature controls.
  2. In the agent sharing dialog, enter the email address of a Google Group or Workspace group (for example, `support-team@example.com`) rather than individual user accounts.
  3. Manage audience membership dynamically within the Google Group; all group members automatically inherit access without modifying the agent's IAM policy.



For step-by-step sharing instructions and permission levels, see [Share a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent) and [Share a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows).

## Flow builder complexity limits

The flow builder canvas enforces structural and routing constraints to maintain low execution latency, ensure deterministic orchestration, and prevent circular call graphs:

Constraint | Limit | Description  
---|---|---  
Subagent depth | 1 level | Single-level flow depth only. Subagents cannot call additional subagents. Nested multi-level hierarchies are not supported.  
Subagents routed by chat root | 50 subagents | The maximum number of subagents that a single chat root agent can evaluate and route requests to.  
Nodes per flow | 100 nodes | The maximum total number of nodes (including trigger, condition, action, subagent, and human-in-the-loop nodes) allowed in a single workflow.  
Skills per node | 20 skills | The maximum number of tool skills or actions that can be attached to a single flow node.  
Simultaneous subagent execution | 1 subagent at a time | Workflow executions evaluate and run subagents sequentially; parallel branch execution across multiple subagents is not supported.  
  
## Knowledge base and file upload limits

The following limits apply to documents uploaded directly to an agent's knowledge base:

Resource | Limit | Description  
---|---|---  
Maximum file size | 20 MB per file | The maximum size for an individual file uploaded directly to an agent's knowledge base.  
Maximum files per agent | 100 files | The maximum total number of files that can be attached to a single agent.  
Maximum files per upload batch | 10 files | The maximum number of files that can be selected and uploaded in a single operation.  
Maximum combined context tokens | 800,000 tokens |  The maximum total token count across all static knowledge files attached to an agent, files uploaded directly within a chat session, and conversation history. Exceeding this token limit returns a `FILE_SIZE_TOO_LARGE` or `Input too long` error, even if individual files are under the 20 MB size limit.   
Supported document types | PDF, DOCX, TXT, PPTX, CSV, XLSX, HTML, and Markdown (.md).  
  
### Best practices for large documents and multi-sheet spreadsheets

When configuring knowledge sources or analyzing complex files in your agent, follow these guidelines to avoid context token limits and processing timeouts:

  * **Use a connected data store (RAG) for large static document libraries** : Gemini Enterprise loads files that you upload to an agent's **Knowledge** section in full into the model's prompt context on every turn. If you attach many files or dense PDFs (such as manuals over 100 pages), the combined token count can exceed the 800,000-token context limit or cause generation timeouts. Instead, ingest large static reference libraries into a connected Gemini Enterprise data store, which automatically chunks and indexes documents, and reserve direct file uploads for smaller, session-specific files.
  * **Split dense PDFs for direct uploads** : Because Gemini Enterprise tokenizes each page of a PDF alongside its text and visual layout, a single multi-hundred-page PDF can consume a large portion of the session token budget and increase reasoning latency. When uploading PDFs directly to an agent or chat session, split large documents into smaller, topic-specific files.
  * **Multi-sheet Excel (`.xlsx`) workbooks**: When you upload a multi-sheet `.xlsx` workbook to an agent's **Knowledge** section or in a chat session, Gemini Enterprise automatically converts each worksheet into an individual CSV table for Python code execution so the agent can query, join, and analyze data across all sheets in the workbook.



### Storage capacity

Uploaded files and indexed documents consume storage from your organization's storage capacity pool. Storage is pooled across all users in a project and location, regardless of edition:

  * **Frontline Worker / Starter:** 2 GiB per user.
  * **Standard:** 30 GiB per user.
  * **Plus:** 75 GiB per user.



If total stored content exceeds the combined pool for your licensed seats, Google bills overages at $5 per GiB per month. For more details, see [Storage and data indexing quota](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#storage-quotas).

## Execution schedule limits

The following limits and operational constraints apply to automated agent schedules:

Setting | Limit or constraint | Description  
---|---|---  
Location support | Multi-region only | Agent execution schedules are supported only in multi-region deployments (such as `us` or `eu`).  
Recurrence frequencies | Hourly, Daily, Weekly, Monthly, Annually | Configurable intervals for automated execution triggers.  
Credential validity window | 14 days | Scheduled agents execute using the author's delegated user credentials. Credentials expire every 14 days and must be manually refreshed in Gemini Enterprise to prevent schedules from pausing.  
Execution timing latency | Up to 5 minutes delay | Scheduled runs may experience a scheduling delay of up to 5 minutes depending on system queue load.  
Approval pausing (HITL) | Mandatory pause on external actions | Scheduled runs that perform actions affecting other individuals (such as sending emails or scheduling meetings) automatically pause for review and require user approval in chat history.  
  
For instructions on configuring or refreshing schedules, see [Schedule a chat agent run](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent).

## Connected data sources and integration limits

The following limits apply to connected data stores and third-party integrations:

Resource | Default limit | Description  
---|---|---  
Data stores per application | 100 data stores | The maximum number of connected enterprise data stores per application instance. Can be increased up to 500 by submitting a [quota increase request](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).  
Connectors per agent | 100 connectors | The maximum number of third-party data connectors attached to a single agent.  
MCP servers per agent | 100 servers | The maximum number of Model Context Protocol (MCP) servers linked to an agent.  
Skill agents per agent | 100 skills | The maximum number of modular skill agents referenced by an agent.  
  
## What's next

  * [Create a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows): Build custom workflows using the flow builder canvas.
  * [Share a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent) and [Share a workflow](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows): Manage access permissions and share agents with team members or Google Groups.
  * [Schedule a chat agent run](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent): Configure automated hourly, daily, or weekly recurrence triggers.
  * [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages): Review organization-wide pooled query quotas, storage indexing limits, and overage billing for Gemini Enterprise.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
