---
url: https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats/
title: MCP Tools Reference: databaseinsights.googleapis.com \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:13.578165+00:00
---

# MCP Tools Reference: databaseinsights.googleapis.com  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Reference ](https://docs.cloud.google.com/alloydb/docs/reference/rest)



Send feedback 

#  MCP Tools Reference: databaseinsights.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_advanced_aggregated_query_stats`

Fetches aggregated query execution statistics for a requested AlloyDB instance within a specified time period. Supports filtering by database name, database user, and a specific query ID, as well as pagination. Returns statistics including query ID, database name, total execution time (sum(execution_time)), average execution time (avg(execution_time)), total execution count (sum(count)), total wait time (sum(wait_time)), and normalized query text. Requires advanced query insights to be enabled.

The following sample demonstrate how to use `curl` to invoke the `get_advanced_aggregated_query_stats` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://LOCATION-databaseinsights.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_advanced_aggregated_query_stats",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
Replace `LOCATION` with the location of your AlloyDB instance (for example, if your instance is in `us-east7`, use `https://us-east7-databaseinsights.googleapis.com/mcp`).

## Input Schema

Message for fetching query execution statistics (including execution times, count, wait times, and normalized query text) for the requested instance.

### FetchQueryStatsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "fullResourceName": string,
      "startTime": string,
      "endTime": string,
      "database": string,
      "username": string,
      "queryId": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The name of the location where we request stats. Format: `projects/{project}/locations/{location}`  
`fullResourceName` |  `string` Required. Identifies the AlloyDB instance. `//alloydb.googleapis.com/clusters/{cluster}/instances/{instance}`  
`startTime` |  `string` Optional. The beginning of the interval for fetching stats in RFC3339 format.  
`endTime` |  `string` Optional. The end of the interval for fetching stats in RFC3339 format.  
`database` |  `string` Optional. Filters results to a specific database name.  
`username` |  `string` Optional. Filters results to a specific database user.  
`queryId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Fetches aggregated stats for a single, specific query ID.  
`pageSize` |  `integer` Optional. The maximum number of query stats to return.  
`pageToken` |  `string` Optional. Token for fetching the next set of results.  
  
## Output Schema

Response message containing query execution statistics, including query ID, database, sum and average of execution time, execution count, sum of wait time, and normalized query text.

### FetchQueryStatsResponse

JSON representation  
---  
      
    
    {
      "results": [
        array
      ],
      "metadata": {
        object ([ResultSetMetadata](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.ResultSetMetadata))
      },
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Rows of data returned based on the user query.  
`metadata` |  `object (`[ResultSetMetadata](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.ResultSetMetadata)`)` List of all the fields the client has interactions for.  
`nextPageToken` |  `string` Support for pagination.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### ResultSetMetadata

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.Field))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.Field)`)` Information on all columns of the result row.  
  
### Field

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([FieldType](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.FieldType)),
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Field name according to the public schema.  
`type` |  `enum (`[FieldType](https://docs.cloud.google.com/alloydb/docs/reference/mcp/databaseinsights/mcp/tools_list/get_advanced_aggregated_query_stats#Output.Schema.FieldType)`)` Field type defined according to the public schema or depends on the aggregation method in case of an aggregation field.  
`description` |  `string` Description of the value the field holds.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a Value with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### FieldType

Type of field, which will define how to read a particular key.

Enums  
---  
`FIELD_TYPE_UNSPECIFIED` | Field type is unknown.  
`INT64` | Int64 field type.  
`UINT64` | Unsigned int64 field type.  
`INT32` | Int32 field type.  
`UINT32` | Unsigned int64 field type.  
`STRING` | String field type.  
`DOUBLE` | Double based data type.  
`ARRAY` | Trace info type.  
`BOOL` | Boolean field type.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
