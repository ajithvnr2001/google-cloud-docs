---
url: https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances/
title: MCP Tools Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:58:00.218863+00:00
---

# MCP Tools Reference: cloud-sql  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  MCP Tools Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_instances`

List all Cloud SQL instances in the project.

The following code sample shows how to use `curl` to call the `list_instances` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_instances",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Instance list request.

### SqlInstancesListRequest

JSON representation  
---  
      
    
    {
      "filter": string,
      "maxResults": integer,
      "pageToken": string,
      "project": string,
      "location": string
    }  
  
Fields  
---  
`filter` |  `string` A filter expression that filters resources listed in the response. The expression is in the form of field:value. For example, 'instanceType:CLOUD_SQL_INSTANCE'. Fields can be nested as needed as per their JSON representation, such as 'settings.userLabels.auto_start:true'.Multiple filter queries are space-separated. For example. 'state:RUNNABLE instanceType:CLOUD_SQL_INSTANCE'. By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of instances to return. The service may return fewer than this value. If unspecified, at most 500 instances are returned. The maximum value is 1000; values above 1000 are coerced to 1000.  
`pageToken` |  `string` A previously-returned page token representing part of the larger set of results to view.  
`project` |  `string` Project ID of the project for which to list Cloud SQL instances.  
`location` |  `string` Optional. Region of the Cloud SQL instance.  
  
## Output Schema

Instance list response for MCP.

### SqlInstancesListMcpResponse

JSON representation  
---  
      
    
    {
      "kind": string,
      "warnings": [
        {
          object ([ApiWarning](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.ApiWarning))
        }
      ],
      "items": [
        {
          object ([McpDatabaseInstance](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.McpDatabaseInstance))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`kind` |  `string` This is always sql#instancesList.  
`warnings[]` |  `object (`[ApiWarning](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.ApiWarning)`)` List of warnings that occurred while handling the request.  
`items[]` |  `object (`[McpDatabaseInstance](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.McpDatabaseInstance)`)` List of mcp instance resources.  
`nextPageToken` |  `string` The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results.  
  
### ApiWarning

JSON representation  
---  
      
    
    {
      "code": enum ([SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlApiWarningCode)),
      "message": string,
      "region": string
    }  
  
Fields  
---  
`code` |  `enum (`[SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlApiWarningCode)`)` Code to uniquely identify the warning type.  
`message` |  `string` The warning message.  
`region` |  `string` The region name for REGION_UNREACHABLE warning.  
  
### McpDatabaseInstance

JSON representation  
---  
      
    
    {
      "project": string,
      "name": string,
      "databaseVersion": string,
      "region": string,
      "edition": string,
      "tier": string,
      "dataDiskSizeGb": string,
      "availabilityType": string,
      "tags": {
        string: string,
        ...
      },
      "state": enum ([SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState))
    }  
  
Fields  
---  
`project` |  `string` Required. Project ID of the project for which to list Cloud SQL instances.  
`name` |  `string` Required. Name of the Cloud SQL instance. This does not include the project ID.  
`databaseVersion` |  `string`  
`region` |  `string` Optional. The geographical region of the Cloud SQL instance. For example, `us-central1`, `europe-west1`, and `asia-east1`.  
`edition` |  `string` Optional. The edition of the instance, can be ENTERPRISE or ENTERPRISE_PLUS.  
`tier` |  `string` Optional. The tier (or machine type) for this instance.  
`dataDiskSizeGb` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Optional. Data disk size in GB. Default value is 100.  
`availabilityType` |  `string` Optional. Availability type. Potential values: * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data accessibility. This is the default value. * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available).  
`tags` |  `map (key: string, value: string)` Optional. Input only. Tag keys and tag values that are bound to this instance.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState)`)` Output only. State of the Cloud SQL instance.  
  
### Int64Value

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The int64 value.  
  
### TagsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### SqlApiWarningCode

Enums  
---  
`SQL_API_WARNING_CODE_UNSPECIFIED` | An unknown or unset warning type from Cloud SQL API.  
`REGION_UNREACHABLE` | Warning when one or more regions are not reachable. The returned result set may be incomplete.  
`MAX_RESULTS_EXCEEDS_LIMIT` | Warning when user provided maxResults parameter exceeds the limit. The returned result set may be incomplete.  
`COMPROMISED_CREDENTIALS` | Warning when user tries to create/update a user with credentials that have previously been compromised by a public data breach.  
`INTERNAL_STATE_FAILURE` | Warning when the operation succeeds but some non-critical workflow state failed.  
  
### SqlInstanceState

The current serving state of the database instance.

Enums  
---  
`SQL_INSTANCE_STATE_UNSPECIFIED` | The state of the instance is unknown.  
`RUNNABLE` | The instance is running, or has been stopped by owner.  
`SUSPENDED` | The instance is not available, for example due to problems with billing.  
`PENDING_DELETE` | The instance is being deleted.  
`PENDING_CREATE` | The instance is being created.  
`MAINTENANCE` | The instance is down for maintenance.  
`FAILED` | The creation of the instance failed or a fatal error occurred during maintenance.  
`ONLINE_MAINTENANCE` | Deprecated  
`REPAIRING` | (Applicable to read pool nodes only.) The read pool node needs to be repaired. The database might be unavailable.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
