---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_connector/
title: MCP Tools Reference: managedkafka \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:29.776228+00:00
---

# MCP Tools Reference: managedkafka  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/get_connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  MCP Tools Reference: managedkafka Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_connector`

Get the details of an existing Google Cloud Managed Service for Apache Kafka Connect connector.

The following sample demonstrate how to use `curl` to invoke the `get_connector` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://managedkafka.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_connector",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for GetConnector.

### GetConnectorRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the connector to retrieve. Format: projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}/connectors/{connector_id}  
  
## Output Schema

A Kafka Connect connector in a given ConnectCluster.

### Connector

JSON representation  
---  
      
    
    {
      "name": string,
      "configs": {
        string: string,
        ...
      },
      "state": enum (State),
    
      // Union field restart_policy can be only one of the following:
      "taskRestartPolicy": {
        object ([TaskRetryPolicy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_connector#Output.Schema.TaskRetryPolicy))
      }
      // End of list of possible types for union field restart_policy.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the connector. Structured like: projects/{project}/locations/{location}/connectClusters/{connect_cluster}/connectors/{connector}  
`configs` |  `map (key: string, value: string)` Optional. Connector config as keys/values. The keys of the map are connector property names, for example: `connector.class`, `tasks.max`, `key.converter`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`State`)` Output only. The current state of the connector.  
Union field `restart_policy`. A policy that specifies how to restart the failed connectors/tasks in a Cluster resource. If not set, the failed connectors/tasks won't be restarted. `restart_policy` can be only one of the following:  
`taskRestartPolicy` |  `object (`[TaskRetryPolicy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/mcp/tools_list/create_connector#Output.Schema.TaskRetryPolicy)`)` Optional. Restarts the individual tasks of a Connector.  
  
### TaskRetryPolicy

JSON representation  
---  
      
    
    {
      "minimumBackoff": string,
      "maximumBackoff": string,
      "taskRetryDisabled": boolean
    }  
  
Fields  
---  
`minimumBackoff` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The minimum amount of time to wait before retrying a failed task. This sets a lower bound for the backoff delay.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`maximumBackoff` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The maximum amount of time to wait before retrying a failed task. This sets an upper bound for the backoff delay.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`taskRetryDisabled` |  `boolean` Optional. If true, task retry is disabled.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### ConfigsEntry

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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
