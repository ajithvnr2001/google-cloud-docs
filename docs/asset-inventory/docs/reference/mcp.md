---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/
title: MCP Reference: cloudasset.googleapis.com \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:12.920094+00:00
---

# MCP Reference: cloudasset.googleapis.com  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  MCP Reference: cloudasset.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Asset API MCP server has the following global MCP endpoint:

  * https://cloudasset.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The cloudasset.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_assets](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/list_assets)` |  List assets from Cloud Asset Inventory   
`[analyze_iam_policy](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/analyze_iam_policy)` |  Analyzes Google Cloud IAM allow policies to determine who can do what on which resources. It can perform policy analysis such as finding resources accessible to a principal, finding principals with access to a resource, or checking access paths.This tool requires the `analysis_query` parameter, which specifies the root container where policies are analyzed (`scope`) and offers optional selectors for resource names, principal identifiers, and applicable roles and permissions.

  * Folder and Organization scopes are _not_ supported. `scope` must be a project scope (`projects/PROJECT_ID`).
  * When analyzing policies in a specific project (for example, 'in `PROJECT_ID`'), set `scope` to `projects/PROJECT_ID` and do _not_ set `resource_selector`.
  * Only set `resource_selector.full_resource_name` (for example, `//storage.googleapis.com/BUCKET_NAME`) if the user specifically asks for access to a particular resource within that scope.
  * If a project scope is not specified in the request, confirm the scope before calling this tool.
  * If `execution_timeout` is not specified in the request, set `execution_timeout` to `60s` as a string with suffix 's'.

You can also provide `options` to `expand_groups`, `expand_roles`, `expand_resources` (default `false`), and `analyze_service_account_impersonation` (default `false`). For supported policy types, see <https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview#supported-policy-types>. For BYOID support, see <https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#policy-intelligence>.  
`[export_iam_analysis_results](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/export_iam_analysis_results)` |  Analyzes Google Cloud IAM policies asynchronously and exports the results to a BigQuery dataset or Google Cloud Storage bucket. Use this for large-scale analysis (for example, expanding resources or impersonation).This tool requires the `analysis_query` parameter, which specifies the root container where policies are analyzed (`scope`) and offers optional selectors for resource names, principal identifiers, and applicable roles and permissions.

  * Folder and Organization scopes are _not_ supported; `scope` must be a project scope (for example, `projects/PROJECT_ID`).
  * When analyzing policies in a specific project (for example, 'in `PROJECT_ID`'), set `scope` to `projects/PROJECT_ID` and do _not_ set `resource_selector`.
  * Only set `resource_selector.full_resource_name` (for example, `//storage.googleapis.com/BUCKET_NAME`) when a request is made specifically for access to a particular resource within that scope.

This tool returns a long-running operation object containing an operation `name`. You must subsequently use the `get_iam_policy_analysis_status` tool with this `name` to poll the status until the `done` field is `true`.  
`[get_iam_policy_analysis_status](https://docs.cloud.google.com/asset-inventory/docs/reference/mcp/tools_list/get_iam_policy_analysis_status)` |  Polls the status of a long-running IAM Policy Analyzer operation. Use this _only_ to pass the operation `name` returned by the `export_iam_analysis_results` tool. If the operation is finished, the `done` field will be `true`.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://cloudasset.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
