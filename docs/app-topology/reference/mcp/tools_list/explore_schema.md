---
url: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema/
title: MCP Tools Reference: apptopology.googleapis.com \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:40:15.636952+00:00
---

# MCP Tools Reference: apptopology.googleapis.com  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  MCP Tools Reference: apptopology.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `explore_schema`

Explores the topology schema via multi-hop BFS traversal from starting label names within a domain schema.

The following code sample shows how to use `curl` to call the `explore_schema` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://apptopology.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "explore_schema",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request for ExploreSchema.

### ExploreSchemaRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "startLabels": [
        string
      ],
      "depth": integer,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the singleton domain schema resource. Format: `projects/{project}/locations/{location}/domains/{domain}/schema`  
`startLabels[]` |  `string` Optional. Starting label names to begin traversal. Substring, case-insensitive matches are performed against allowed label names in the schema. A maximum of 10 `start_labels` can be specified; providing more will result in an `INVALID_ARGUMENT` error. If `start_labels` is unset or empty, all authorized node types will be used as the starting set.  
`depth` |  `integer` Optional. The maximum depth of BFS traversal hops to perform from the starting node types or label names. Defaults to 0 if unspecified.  
`pageSize` |  `integer` Optional. The maximum number of schema elements to return in a single page.

  * The service might return fewer elements than this value if adding another edge and its required endpoint nodes exceeds `page_size`.
  * If omitted or set to 0, default (100) will be used.
  * Minimum page_size is 3 to ensure at least one edge and its endpoint nodes fit on a page; values below 3 (e.g. 1 or 2) are changed to 3.
  * Maximum value is 500.

  
`pageToken` |  `string` Optional. A page token received from a previous `ExploreSchema` call. Provide this to retrieve the subsequent page.When paginating, all other parameters (except page_size) provided to `ExploreSchema` must match the call that provided the page token.  
  
## Output Schema

Response for ExploreSchema.

### ExploreSchemaResponse

JSON representation  
---  
      
    
    {
      "nodeTypes": [
        {
          object ([NodeType](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeType))
        }
      ],
      "edgeTypes": [
        {
          object ([EdgeType](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.EdgeType))
        }
      ],
      "labelProperties": [
        {
          object ([LabelProperties](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.LabelProperties))
        }
      ],
      "edgeRules": [
        {
          object ([EdgeRule](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.EdgeRule))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`nodeTypes[]` |  `object (`[NodeType](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeType)`)` A list of `NodeType`s defined within this schema. Refer to the documentation of `NodeType` for more details.  
`edgeTypes[]` |  `object (`[EdgeType](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.EdgeType)`)` A list of `EdgeType`s defined within this schema. Refer to the documentation of `EdgeType` for more details.  
`labelProperties[]` |  `object (`[LabelProperties](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.LabelProperties)`)` A list of supported labels and corresponding properties.  
`edgeRules[]` |  `object (`[EdgeRule](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.EdgeRule)`)` Edge rules. These will indicate which node types can be connected and through what edge type. This is a list of (source_node_type, edge_type, destination_node_type) tuples.  
`nextPageToken` |  `string` A token to retrieve the next page of results, or empty if there are no more results in the traversal set.  
  
### NodeType

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": [
        string
      ],
      "description": string,
      "optionalLabels": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `string` REQUIRED Name of the node type. This name is used to access the node type while defining the schema.  
`labels[]` |  `string` Labels attached to the node. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the node type.  
`description` |  `string` A human-readable description of the `NodeType`.  
`optionalLabels[]` |  `string` A node of this node type can have 0 or more of these labels. These node objects of this node type will have these labels alongside the required labels.  
  
### EdgeType

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": [
        string
      ],
      "description": string,
      "optionalLabels": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `string` REQUIRED Name of the edge type. This name is used to access the edge type while defining the schema.  
`labels[]` |  `string` Labels attached to the edge. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the edge type.  
`description` |  `string` A human-readable description of the `EdgeType`.  
`optionalLabels[]` |  `string` An edge of this edge type can have 0 or more of these labels. These edge objects of this edge type will have these labels alongside the required labels.  
  
### LabelProperties

JSON representation  
---  
      
    
    {
      "label": string,
      "properties": [
        {
          object ([Property](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.Property))
        }
      ],
      "description": string
    }  
  
Fields  
---  
`label` |  `string` Full qualified name of the label.  
`properties[]` |  `object (`[Property](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.Property)`)` List of properties associated with the label.  
`description` |  `string` A human-readable description of the label.  
  
### Property

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
    
      // Union field value can be only one of the following:
      "stringValue": {
        object ([StringValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.StringValue))
      },
      "intValue": {
        object ([IntValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.IntValue))
      },
      "boolValue": {
        object ([BoolValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.BoolValue))
      },
      "doubleValue": {
        object ([DoubleValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.DoubleValue))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`name` |  `string` `name` is the key string to identify the property in `Node`s & `Edge`s. Examples: `ProjectId`, `Base/displayName` etc.  
`description` |  `string` A human-readable description of the `PropertyType`, explaining its meaning, purpose, and any constraints or expectations on its value.  
Union field `value`. REQUIRED Value type of the property. `value` can be only one of the following:  
`stringValue` |  `object (`[StringValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.StringValue)`)` StringValue represents a property that has a string value type.  
`intValue` |  `object (`[IntValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.IntValue)`)` IntValue represents a property that has an integer value type.  
`boolValue` |  `object (`[BoolValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.BoolValue)`)` BoolValue represents a property that has a boolean value type.  
`doubleValue` |  `object (`[DoubleValue](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.DoubleValue)`)` DoubleValue represents a property that has a double value type.  
  
### StringValue

JSON representation  
---  
      
    
    {
      "repeated": boolean,
      "allowedValues": [
        string
      ]
    }  
  
Fields  
---  
`repeated` |  `boolean` OPTIONAL Whether the property is repeated.  
`allowedValues[]` |  `string` OPTIONAL Allowed values for the property. If provided, the property value must be one of the allowed values.  
  
### IntValue

JSON representation  
---  
      
    
    {
      "repeated": boolean,
      "allowedValues": [
        string
      ]
    }  
  
Fields  
---  
`repeated` |  `boolean` OPTIONAL Whether the property is repeated.  
`allowedValues[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` OPTIONAL Allowed values for the property. If provided, the property value must be one of the allowed values.  
  
### BoolValue

JSON representation  
---  
      
    
    {
      "repeated": boolean,
      "allowedValues": [
        boolean
      ]
    }  
  
Fields  
---  
`repeated` |  `boolean` OPTIONAL Whether the property is repeated.  
`allowedValues[]` |  `boolean` OPTIONAL Allowed values for the property. If provided, the property value must be one of the allowed values.  
  
### DoubleValue

JSON representation  
---  
      
    
    {
      "repeated": boolean,
      "allowedValues": [
        number
      ]
    }  
  
Fields  
---  
`repeated` |  `boolean` OPTIONAL Whether the property is repeated.  
`allowedValues[]` |  `number` OPTIONAL Allowed values for the property. If provided, the property value must be one of the allowed values.  
  
### EdgeRule

JSON representation  
---  
      
    
    {
      "edgeType": string,
    
      // Union field source_node can be only one of the following:
      "srcNodeType": string,
      "srcNodeGroup": {
        object ([NodeGroup](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeGroup))
      }
      // End of list of possible types for union field source_node.
    
      // Union field destination_node can be only one of the following:
      "destNodeType": string,
      "destNodeGroup": {
        object ([NodeGroup](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeGroup))
      }
      // End of list of possible types for union field destination_node.
    }  
  
Fields  
---  
`edgeType` |  `string` Optional. Name of the connected edge type.  
Union field `source_node`. Specifies the source criteria for this edge rule. An edge rule must define its source either statically via a specific node type, or dynamically via a group of nodes that match given constraints.This takes precedence over the `source_node_type` field. `source_node` can be only one of the following:  
`srcNodeType` |  `string` Optional. The specific node type name that acts as the source for this edge.  
`srcNodeGroup` |  `object (`[NodeGroup](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeGroup)`)` Optional. A dynamic group of nodes, defined by label constraints, that can act as the source for this edge.  
Union field `destination_node`. Specifies the destination criteria for this edge rule. An edge rule must define its destination either statically via a specific node type, or dynamically via a group of nodes that match given constraints.This takes precedence over the `destination_node_type` field. `destination_node` can be only one of the following:  
`destNodeType` |  `string` Optional. The specific node type name that acts as the destination for this edge.  
`destNodeGroup` |  `object (`[NodeGroup](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema#Output.Schema.NodeGroup)`)` Optional. A dynamic group of nodes, defined by label constraints, that can act as the destination for this edge.  
  
### NodeGroup

JSON representation  
---  
      
    
    {
      "anyLabels": [
        string
      ]
    }  
  
Fields  
---  
`anyLabels[]` |  `string` Optional. A node must have at least one of these labels to be included in the group. If empty or unset, this constraint is not applied.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
