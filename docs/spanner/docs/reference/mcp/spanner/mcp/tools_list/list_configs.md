---
url: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs/
title: MCP Tools Reference: spanner.googleapis.com \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:27.906763+00:00
---

# MCP Tools Reference: spanner.googleapis.com  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MCP Tools Reference: spanner.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_configs`

List instance configs in a given project.

  * Response may include next_page_token to fetch additional configs using list_configs tool with page_token set.



The following sample demonstrate how to use `curl` to invoke the `list_configs` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://spanner.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_configs",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `ListInstanceConfigs`.

### ListInstanceConfigsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The name of the project for which a list of supported instance configurations is requested. Values are of the form `projects/<project>`.  
`pageSize` |  `integer` Number of instance configurations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `page_token` should contain a `next_page_token` from a previous `[ListInstanceConfigsResponse](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.ListInstanceConfigsResponse)`.  
  
## Output Schema

The response for `ListInstanceConfigs`.

### ListInstanceConfigsResponse

JSON representation  
---  
      
    
    {
      "instanceConfigs": [
        {
          object ([InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.InstanceConfig))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`instanceConfigs[]` |  `object (`[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.InstanceConfig)`)` The list of requested instance configurations.  
`nextPageToken` |  `string` `next_page_token` can be sent in a subsequent `ListInstanceConfigs` call to fetch more of the matching instance configurations.  
  
### InstanceConfig

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "configType": enum (Type),
      "replicas": [
        {
          object ([ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.ReplicaInfo))
        }
      ],
      "optionalReplicas": [
        {
          object ([ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.ReplicaInfo))
        }
      ],
      "baseConfig": string,
      "labels": {
        string: string,
        ...
      },
      "etag": string,
      "leaderOptions": [
        string
      ],
      "reconciling": boolean,
      "state": enum (State),
      "freeInstanceAvailability": enum (FreeInstanceAvailability),
      "quorumType": enum (QuorumType),
      "storageLimitPerProcessingUnit": string
    }  
  
Fields  
---  
`name` |  `string` A unique identifier for the instance configuration. Values are of the form `projects/<project>/instanceConfigs/[a-z][-a-z0-9]*`.User instance configuration must start with `custom-`.  
`displayName` |  `string` The name of this instance configuration as it appears in UIs.  
`configType` |  `enum (`Type`)` Output only. Whether this instance configuration is a Google-managed or user-managed configuration.  
`replicas[]` |  `object (`[ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.ReplicaInfo)`)` The geographic placement of nodes in this instance configuration and their replication properties.To create user-managed configurations, input `replicas` must include all replicas in `replicas` of the `base_config` and include one or more replicas in the `optional_replicas` of the `base_config`.  
`optionalReplicas[]` |  `object (`[ReplicaInfo](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs#Output.Schema.ReplicaInfo)`)` Output only. The available optional replicas to choose from for user-managed configurations. Populated for Google-managed configurations.  
`baseConfig` |  `string` Base configuration name, e.g. projects//instanceConfigs/nam3, based on which this configuration is created. Only set for user-managed configurations. `base_config` must refer to a configuration of type `GOOGLE_MANAGED` in the same project as this configuration.  
`labels` |  `map (key: string, value: string)` Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.).

  * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z][a-z0-9_-]{0,62}`.
  * Label values must be between 0 and 63 characters long and must conform to the regular expression `[a-z0-9_-]{0,63}`.
  * No more than 64 labels can be associated with a given resource.

See <https://goo.gl/xmQnxf> for more information on and examples of labels.If you plan to use labels in your own code, please note that additional characters may be allowed in the future. Therefore, you are advised to use an internal label representation, such as JSON, which doesn't rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance configuration from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance configuration updates in order to avoid race conditions: An etag is returned in the response which contains instance configurations, and systems are expected to put that etag in the request to update instance configuration to ensure that their change is applied to the same version of the instance configuration. If no etag is provided in the call to update the instance configuration, then the existing instance configuration is overwritten blindly.  
`leaderOptions[]` |  `string` Allowed values of the "default_leader" schema option for databases in instances that use this instance configuration.  
`reconciling` |  `boolean` Output only. If true, the instance configuration is being created or updated. If false, there are no ongoing operations for the instance configuration.  
`state` |  `enum (`State`)` Output only. The current instance configuration state. Applicable only for `USER_MANAGED` configurations.  
`freeInstanceAvailability` |  `enum (`FreeInstanceAvailability`)` Output only. Describes whether free instances are available to be created in this instance configuration.  
`quorumType` |  `enum (`QuorumType`)` Output only. The `QuorumType` of the instance configuration.  
`storageLimitPerProcessingUnit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The storage limit in bytes per processing unit.  
  
### ReplicaInfo

JSON representation  
---  
      
    
    {
      "location": string,
      "type": enum (ReplicaType),
      "defaultLeaderLocation": boolean
    }  
  
Fields  
---  
`location` |  `string` The location of the serving resources, e.g., "us-central1".  
`type` |  `enum (`ReplicaType`)` The type of replica.  
`defaultLeaderLocation` |  `boolean` If true, this location is designated as the default leader location where leader replicas are placed. See the [region types documentation](https://cloud.google.com/spanner/docs/instances#region_types) for more details.  
  
### LabelsEntry

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
