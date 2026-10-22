---
url: https://docs.cloud.google.com/composer/docs/composer-3/agentic-capabilities-overview/
title: Overview of agentic capabilities in Managed Airflow \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:11.273278+00:00
---

# Overview of agentic capabilities in Managed Airflow  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/agentic-capabilities-overview/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Overview of agentic capabilities in Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/agentic-capabilities-overview "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

Agentic capabilities in Managed Airflow let you get insight into environment health and metrics, diagnose and resolve failed workflows, connect external developer agents to environments by using the Model Context Protocol (MCP), and apply automated telemetry recommendations and migrations.

## Managed Airflow Agent

[ ![The Ask Agent dialog shows the Managed Airflow Agent
    responding to the question 'Why my environment isn't healthy?' The response
    is that the environment creation failed.](https://docs.cloud.google.com/static/composer/docs/images/managed-airflow-agent-environment-health-chat.png)](https://docs.cloud.google.com/static/composer/docs/images/managed-airflow-agent-environment-health-chat.png) **Figure 1.** Conversation with the Managed Airflow Agent (click to enlarge) 

The Managed Airflow Agent can help you to:

  * Identify existing or potential issues or bottlenecks and optimize your environment's performance.
  * Understand, diagnose, and resolve issues with failed Airflow tasks and DAG runs. Analyze task execution.
  * Gain insight into environment's metrics and monitoring information.



To investigate failed DAG runs and task instances, start a conversation with the [Managed Airflow Agent](https://docs.cloud.google.com/composer/docs/composer-3/troubleshoot-tasks-and-dag-runs-with-agent) in the Google Cloud console. You can start a direct root-cause investigation by clicking the **Investigate** button for failed DAG runs and task instances.

The Managed Airflow Agent provides structured diagnostic reports, which include:

  * A problem statement
  * Evidence with log excerpts and timestamps
  * Actionable remediation recommendations



## Remote Model Context Protocol (MCP) server

The [Model Context Protocol (MCP) server](https://docs.cloud.google.com/composer/docs/composer-3/use-composer-mcp) provides an open standard JSON-RPC interface that allows external developer agents, such as Gemini Code Assist, Gemini CLI, ChatGPT, Claude, Cursor, Goose, or custom tools, to interact with Managed Airflow environments.

The remote MCP server provides the following capabilities and tools:

  * Environment lifecycle operations: Create and delete environments, list environments, get environment details, and install PyPI packages.
  * DAG operations: List DAGs, trigger DAG runs, and check DAG and task execution state.
  * Diagnostic retrieval: Fetch task logs and inspect execution errors.



You might want to only allow read-only tools in certain environments through your organization policy. MCP tools that are read-only have the MCP attribute `mcp.tool.isReadOnly` set to true.

## Telemetry-driven environment optimization

To optimize environments based on telemetry data, use the [Data Agent Kit recommendations skill](https://github.com/gemini-cli-extensions/data-agent-kit-starter-pack/blob/main/skills/gcp-managed-airflow-recommendations/SKILL.md) (`gcp-managed-airflow-recommendations`).

The recommendations skill provides automated telemetry analysis of the following metrics:

  * Workload CPU and memory utilization.
  * Worker and scheduler restart frequencies.
  * DAG parsing latency.
  * Cloud Storage bucket hygiene.



Based on the telemetry analysis, the skill offers prescriptive guidance for tuning Airflow configuration options, optimizing worker and scheduler autoscaling, and addressing resource bottlenecks.

## DAG migration assistance

To automate workflow migrations and upgrades, use the [Data Agent Kit migrations skill](https://github.com/gemini-cli-extensions/data-agent-kit-starter-pack/blob/main/skills/gcp-managed-airflow-migrations/SKILL.md) (`gcp-managed-airflow-migrations`).

The migrations skill executes a four-phase upgrade workflow:

  1. Static dependency analysis and compatibility checks: Analyze code using tools like Ruff linting rules for Airflow.
  2. Automated remediation recipes: Generate fixes for deprecations and provider updates, such as Google provider package updates.
  3. DAG code refactoring: Automatically refactor DAG code.
  4. Verification and validation: Verify the correctness of the migrated workflows.



## Limitations

Agentic capabilities in Managed Airflow have the following limitations.

Data residency and conversational processing:

  * The in-console Managed Airflow Agent is powered by the Conversational Analytics API, which operates under its own [data residency policy](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).
  * Chat conversations and prompts can be processed in a different geographic region or multi-region than where your Managed Airflow environment and data reside.



IAM roles and authentication:

  * Using the remote MCP server requires explicit IAM roles: `roles/serviceusage.serviceUsageAdmin` to enable the service and `roles/mcp.toolUser` to execute tool calls.

  * We recommend to use dedicated service identities for external agents ( such as Gemini Code Assist, Gemini CLI, ChatGPT, Claude, Cursor, Goose) to audit and constrain actions.

  * Access is scoped by OAuth credentials distinguishing full access (`https://www.googleapis.com/auth/composer`) from read-only access (`https://www.googleapis.com/auth/composer.readonly`).




MCP operational scope and security guardrails:

  * Mutating and destructive operations are subject to Organization Policy constraints and IAM deny policies.



Telemetry recommendations and migration skills:

  * The recommendations skill (`gcp-managed-airflow-recommendations`) analyzes telemetry (CPU and memory utilization, worker and scheduler restarts, DAG parsing latency, and Cloud Storage bucket hygiene) and provides tuning advice, but doesn't apply infrastructure changes automatically.
  * The migrations skill (`gcp-managed-airflow-migrations`) automates dependency analysis and code refactoring for Airflow 2.11.1 and Airflow 3, but breaking changes require manual verification and test validation.



Preview terms and SLAs:

  * Capabilities in Preview or using preview model parameters operate under Pre-GA Offerings Terms and don't carry GA service level agreements ( SLAs).



## What's next

  * [Troubleshoot Airflow tasks and DAG runs with Managed Airflow Agent](https://docs.cloud.google.com/composer/docs/composer-3/troubleshoot-tasks-and-dag-runs-with-agent)
  * [Using Managed Airflow remote MCP server](https://docs.cloud.google.com/composer/docs/composer-3/use-composer-mcp).
  * Explore the [Data Agent Kit GitHub repository](https://github.com/gemini-cli-extensions/data-agent-kit-starter-pack).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
