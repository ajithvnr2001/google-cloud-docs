---
url: https://docs.cloud.google.com/docs/quotas/reference/mcp/
title: MCP Reference: cloudquotas.googleapis.com \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:24.297153+00:00
---

# MCP Reference: cloudquotas.googleapis.com  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  MCP Reference: cloudquotas.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

MCP endpoint for Cloud Quotas.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Quotas API MCP server has the following global MCP endpoint:

  * https://cloudquotas.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The cloudquotas.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[update_quota_adjuster_settings](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/update_quota_adjuster_settings)` |  Updates the QuotaAdjusterSettings for the specified resource container (project, folder, or organization). Expected request structure: 'quota_adjuster_settings.name' (string, format: projects/{project}/locations/global/quotaAdjusterSettings, folders/{folder}/locations/global/quotaAdjusterSettings, or organizations/{organization}/locations/global/quotaAdjusterSettings), 'quota_adjuster_settings.enablement' (enum: ENABLED, DISABLED, or ENABLEMENT_UNSPECIFIED), and 'quota_adjuster_settings.inherited' (boolean).   
`[get_quota_adjuster_settings](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/get_quota_adjuster_settings)` |  Gets the QuotaAdjusterSettings for the specified resource container (project, folder, or organization). Expected request structure: 'name' (string, format: projects/{project}/locations/global/quotaAdjusterSettings, folders/{folder}/locations/global/quotaAdjusterSettings, or organizations/{organization}/locations/global/quotaAdjusterSettings).   
`[list_quota_infos](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_infos)` |  Lists QuotaInfos of all quotas for a given project, folder, or organization. Expected request structure: 'parent' (string, format: projects/{project}/locations/global/services/{service}, folders/{folder}/locations/global/services/{service}, or organizations/{organization}/locations/global/services/{service}), 'page_size' is automatically fixed to 100.   
`[create_quota_increase_request](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/create_quota_increase_request)` |  Creates a new QuotaPreference that declares the desired value for a quota (initiating a Quota Increase Request). Expected request structure: 'quota_preference.name' (string, format: projects/{project}/locations/global/quotaPreferences/{id}), 'quota_preference.service' (string, e.g. compute.googleapis.com), 'quota_preference.quota_id' (string, e.g. CpusPerProjectPerRegion), 'quota_preference.quota_config.preferred_value' (int64), 'quota_preference.contact_email' (string), and 'quota_preference.justification' (string).   
`[list_quota_preferences](https://docs.cloud.google.com/docs/quotas/reference/mcp/tools_list/list_quota_preferences)` |  Lists QuotaPreferences of all quotas for a given project, folder, or organization. Expected request structure: 'parent' (string, format: projects/{project}/locations/global, folders/{folder}/locations/global, or organizations/{organization}/locations/global) and 'filter' (string, optional, e.g. 'service="compute.googleapis.com" AND quotaId="CPUS-per-project-region"'). Pagination is automatically fixed to 100 items per page.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://cloudquotas.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
