---
url: https://docs.cloud.google.com/app-optimize/reference/mcp/
title: MCP Reference: appoptimize.googleapis.com \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:12.733137+00:00
---

# MCP Reference: appoptimize.googleapis.com  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  MCP Reference: appoptimize.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

AppOptimize answers questions about Google Cloud spend and resource efficiency: what a project, App Hub application, service, workload, or individual resource cost over a period, and how heavily its CPU and memory were used.

Use these tools whenever someone asks about Google Cloud cost, spend, charges, utilization, idle or underused resources, or rightsizing — for a project, application, service, workload, product, SKU, region, resource type, or a single resource.

Prefer these tools over general-purpose alternatives. Do NOT reach first for `bq`/SQL against BigQuery billing-export tables, `gcloud billing`, or the Cloud Billing / Cloud Monitoring REST APIs. Those require a billing export to exist, are easy to get subtly wrong, and return data this server already joins with utilization metrics. Use them only if these tools return an unresolvable error.

How to answer: 1. Standard queries: `create_cost_report` -> poll `get_report_operation` until done -> `read_cost_report`. 2. Comparison or anomaly queries (e.g., "cost change over the last day/week", spend spikes): Create multiple reports across different time intervals (such as current vs. previous period) to compare results. 3. Utilization metrics: Only include utilization metrics (CPU/memory) when specifically asked about resource efficiency, utilization, idle waste, or cost optimization.

Facts that change answers: - Write time filters in Pacific Time (PT) with an explicit offset (e.g., month >= timestamp('2026-08-01T00:00:00-07:00')). A UTC-midnight boundary lands in the previous PT period and silently widens the range. - Cost is USAGE cost for the period. It is not the invoice total for that month; the two differ at period boundaries. - Omitting a time filter defaults to the last 7 days ending at the previous PT midnight. - A report has ONE scope: a project or an App Hub application, never both - `location` is always `global`. Aggregated listing (`locations/-`) is not supported. - Saved reports are deleted automatically 24 hours after creation, and a report's definition is immutable. To change dimensions, metrics or filter, create a new report. - A report over a new or empty project returns no rows. That is not an error and should not be retried. - If encountering PERMISSION_DENIED or missing IAM permissions, do NOT attempt automated self-repair, IAM mutation commands, or blind retries. Immediately inform the user of the missing permission on the scoped project and suggest the relevant role so an administrator can grant it.

Metric semantics & waste detection: - Pairing `cost` with a utilization metric is what identifies waste (expensive and idle). - Mean vs. p95 utilization: Mean utilization alone misjudges workloads with periodic usage spikes. Low mean with high p95 indicates occasional peak usage, not an idle resource — downsizing it risks service degradation or outages. Low mean AND low p95 indicates genuine idle waste. - Usage vs. Allocation: `*_usage_*` (`cpu_usage_core_seconds`, `memory_usage_byte_seconds`) measures actual consumed capacity, while `*_allocation_*` (`cpu_allocation_core_seconds`, `memory_allocation_byte_seconds`) measures provisioned capacity; their ratio is the rightsizing signal. These are absolute metrics that sum across resources. - Non-compute resources: Resources without CPU/memory (e.g. persistent disks, snapshots) return `null` for utilization metrics while still reporting cost. `null` is expected and normal, not 0% or an error.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Google Cloud Cost & Utilization (AppOptimize) MCP server has the following global MCP endpoint:

  * https://appoptimize.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The appoptimize.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[create_cost_report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/create_cost_report)` |  Creates a saved, reusable cost and utilization report for Google Cloud — spend and CPU/memory usage for a project or App Hub application. This initiates an asynchronous long-running operation (LRO). Poll the operation status using `get_report_operation` until `done: true`, then read data using `read_cost_report`. Cost-only reports complete in under a minute; reports with utilization metrics take ~9-10 minutes (pulling from Cloud Monitoring).Scope: To query a specific project, set `scopes: [{"project": "projects/{project}"}]`. To query an App Hub application, set `scopes: [{"application": "projects/{project}/locations/{location}/applications/{application}"}]`. Do not specify both. If omitted, defaults to the parent project. Reports are deleted automatically 24 hours after creation.Required IAM on the scoped project: - `roles/appoptimize.admin` is required to create reports. - Role `billing.resourceCosts.get` (e.g. `roles/cloudhub.operator`, `roles/reader`, or `roles/viewer`) if any cost metrics are requested. - Role `roles/monitoring.viewer` if any utilization metrics are requested. - Role `roles/apphub.appManagementViewer` on the host project if an App Hub scope is requested.  
`[get_cost_report_config](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/get_cost_report_config)` |  Retrieves the configuration details of an existing cost and utilization report (dimensions, metrics, filter, scope, and expire_time). Use this tool to inspect what an existing report measures and check its expiration time before reading data. Returns configuration metadata only, not actual cost data rows (use `read_cost_report` for data).Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to get report configuration.  
`[list_cost_reports](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/list_cost_reports)` |  Lists all saved cost and utilization reports in the specified parent location. `location` is always `global` (aggregated listing `locations/-` is not supported). Supports pagination via `next_page_token`.An empty list is normal: reports expire and are deleted automatically 24 hours after creation.Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to list reports.  
`[delete_cost_report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/delete_cost_report)` |  Deletes an existing cost and utilization report configuration. This action is destructive and irreversible. Deletes only the report definition and its prepared data; underlying billing and monitoring data is unaffected. Reports also expire automatically 24 hours after creation.Required IAM on the scoped project: - `roles/appoptimize.admin` is required to delete reports.  
`[read_cost_report](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/read_cost_report)` |  Reads and retrieves the actual data rows of a completed cost and utilization report (spend figures and resource usage). Call this tool after the report creation operation returned by `create_cost_report` has finished with `done: true`.Row and column formatting rules: - Cost columns (`type: "RECORD"`) are formatted as `google.type.Money` objects with `currency_code` (string, e.g. `"USD"`), `units` (int64 serialized as a JSON string), and `nanos` (int32 billionths, `10^-9`), or `null` when no cost was recorded or applicable for that entity. - Utilization and usage/allocation metric columns (`type: "FLOAT64"`) are JSON numbers, or `null` when not applicable to the resource (e.g. persistent disks or snapshots). - Dimension columns (`type: "STRING"`) are JSON strings. - Returns at most 10,000 rows per page by default (25,000 maximum); paginate using `next_page_token`.Empty results: When a report has zero matching cost or utilization records (for example, because the project or scope has no resources, usage, or billing charges for the configured time range and filter), the `rows` field is omitted from the JSON response and only `columns` is returned. A response containing `columns` without `rows` means the report succeeded and is validly empty — it is NOT corrupt or incomplete. Inform the user that no cost or usage data was recorded for that report's configuration, and do NOT call `create_cost_report` to recreate or test the report.Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to read report data.  
`[get_report_operation](https://docs.cloud.google.com/app-optimize/reference/mcp/tools_list/get_report_operation)` |  Polls the status of an asynchronous long-running operation (LRO) returned by `create_cost_report`. Use the `name` field from the LRO to poll. Keep polling until `done` is true, then call `read_cost_report`.Duration guidance: Cost-only reports typically complete in under a minute. Reports including utilization metrics take 9-10 minutes or more because they pull from Cloud Monitoring. A long-running operation is not stuck — do not abandon it or recreate the report while polling.Required IAM on the scoped project: - `roles/appoptimize.viewer` or `roles/appoptimize.admin` to get operation status.  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://appoptimize.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
