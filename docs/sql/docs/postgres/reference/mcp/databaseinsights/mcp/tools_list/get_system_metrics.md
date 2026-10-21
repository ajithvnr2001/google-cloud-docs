---
url: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/databaseinsights/mcp/tools_list/get_system_metrics/
title: MCP Tools Reference: databaseinsights.googleapis.com \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:44.450304+00:00
---

# MCP Tools Reference: databaseinsights.googleapis.com  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/databaseinsights/mcp/tools_list/get_system_metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  MCP Tools Reference: databaseinsights.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_system_metrics`

Fetches system related telemetry data for a given database instance using a PromQL query from cloud monitoring.

The following sample demonstrate how to use `curl` to invoke the `get_system_metrics` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://databaseinsights.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_system_metrics",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request of the FetchSystemMetrics RPC.

### FetchSystemMetricsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "resource": string,
      "promqlQuery": string,
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The name of the location where we request metrics. Format: `projects/{project}/locations/{location}`  
`resource` |  `string` Required. The resource name used for system metrics. It is the project ID in this case.  
`promqlQuery` |  `string` Required. The promql_query to fetch the system metrics.  
`startTime` |  `string` Optional. The start_time of the metrics in RFC3339 format.  
`endTime` |  `string` Optional. The end_time of the metrics in RFC3339 format.  
  
## Output Schema

The response of the FetchSystemMetrics RPC.

### FetchSystemMetricsResponse

JSON representation  
---  
      
    
    {
      "promqlResult": string
    }  
  
Fields  
---  
`promqlResult` |  `string` The result of the fetch system metrics.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
