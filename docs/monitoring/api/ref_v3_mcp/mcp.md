---
url: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/
title: MCP Reference: monitoring.googleapis.com \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:06:38.790664+00:00
---

# MCP Reference: monitoring.googleapis.com  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MCP Reference: monitoring.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

An MCP server that provides tools for Cloud Monitoring

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Monitoring API MCP server has the following global MCP endpoint:

  * https://monitoring.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The monitoring.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_timeseries](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries)` |  Lists time series data from the Google Cloud Monitoring API   
`[query_range](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/query_range)` |  Evaluate a PromQL query in a range of time   
`[get_alert_policy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy)` |  Use this as the primary tool to get information about a specific alerting policy. Alerting policies define the conditions under which you want to be notified about issues with your services. This is useful for understanding the details of a specific alert configuration.   
`[list_alert_policies](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_alert_policies)` |  Use this as the primary tool to list the alerting policies in a Google Cloud project. Alerting policies define the conditions under which you want to be notified about issues with your services. This is useful for understanding what alerts are currently configured.   
`[get_alert](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert)` |  Use this as the primary tool to get information about a specific alert. An alert is the representation of a violation of an alert policy. This is useful for understanding the details of a specific alert.   
`[list_alerts](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_alerts)` |  Use this as the primary tool to list the alerts in a Google Cloud project. An alert is the representation of a violation of an alert policy. This is useful for understanding current and past violations of an alert policy.   
`[list_metric_descriptors](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors)` |  Use this as the primary tool to discover the types of metrics available in a Google Cloud project. This is a good first step to understanding what data is available for monitoring and building dashboards or alerts.   
`[list_dashboards](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_dashboards)` |  Use this as the primary tool to retrieve a list of existing custom monitoring dashboards in a Google Cloud project. Custom monitoring dashboards let users view and analyze data from different sources in the same context. This is useful for understanding what custom dashboards are currently configured and available in a given project.   
`[get_dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_dashboard)` |  Use this as the primary tool to retrieve a single specific custom monitoring dashboard from a Google Cloud project using the resource name of the requested dashboard. Custom monitoring dashboards let users view and analyze data from different sources in the same context. This is often used as a follow on to list_dashboards to get full details on a specific dashboard.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://monitoring.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-07 UTC."],[],[]] 
