---
url: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology/
title: MCP Tools Reference: apptopology.googleapis.com \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:14.239654+00:00
---

# MCP Tools Reference: apptopology.googleapis.com  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  MCP Tools Reference: apptopology.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `generate_discovered_resources_topology`

Generate the topology for all discovered (including non-registrable) resources for given project based on the view option and filters. Constructing filters requires valid node labels, edge labels, and properties, which can be retrieved in bulk via `get_schema` or incrementally explored via `explore_schema`.

The following code sample shows how to use `curl` to call the `generate_discovered_resources_topology` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://apptopology.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "generate_discovered_resources_topology",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request for GenerateDiscoveredResourcesTopology.

### GenerateDiscoveredResourcesTopologyRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "topologyDomains": [
        string
      ],
    
      // Union field query can be only one of the following:
      "filter": {
        object ([GraphPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.GraphPattern))
      }
      // End of list of possible types for union field query.
    }  
  
Fields  
---  
`name` |  `string` Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported.  
`topologyDomains[]` |  `string` Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains.  
Union field `query`. Query the topology by building a graph pattern filter or pre-defined topology view. `query` can be only one of the following:  
`filter` |  `object (`[GraphPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.GraphPattern)`)` Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters.  
  
### GraphPattern

JSON representation  
---  
      
    
    {
      "startingNode": {
        object ([NodePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.NodePattern))
      },
      "neighbors": [
        {
          object ([ConnectedNodePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.ConnectedNodePattern))
        }
      ]
    }  
  
Fields  
---  
`startingNode` |  `object (`[NodePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.NodePattern)`)` Required. Pattern matcher to select the starting nodes in the graph.  
`neighbors[]` |  `object (`[ConnectedNodePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.ConnectedNodePattern)`)` Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.  
  
### NodePattern

JSON representation  
---  
      
    
    {
      "alias": string,
      "labelPropertiesPattern": {
        object ([LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.LabelPropertiesPattern))
      }
    }  
  
Fields  
---  
`alias` |  `string` Optional. Represents an identifier to be referenced in `property_matcher_expr`. For example, an alias for `app` can be referenced as `app.Base/location="us-central1"`. `alias` must be unique within the query, otherwise an error will be returned.  
`labelPropertiesPattern` |  `object (`[LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.LabelPropertiesPattern)`)` Optional. Matcher for labels/properties.  
  
### LabelPropertiesPattern

JSON representation  
---  
      
    
    {
      "labelMatcherExpr": string,
      "propertyMatcherExpr": string
    }  
  
Fields  
---  
`labelMatcherExpr` |  `string` Required. Matcher expression for labels. Allow OR / AND operators; The syntax is defined by the following grammar: - The label expression can use either `OR` or `AND` operator, but not a combination of both. Example: `AppHub/Application`, `AppHub/Workload OR AppHub/Service`  
`propertyMatcherExpr` |  `string` Optional. The syntax of the filter is defined by the following grammar: <https://google.aip.dev/160>.Referencing properties of graph elements using traversal operator `.`. Repeated properties cannot be traversed. e.g. `e.NodeName`, where `e` is a node or edge alias.The following properties are supported for all node and edge types:

  * `Labels`: repeated string property. Can be used to combine conditions between labels and properties. e.g. `e.Labels : "label_1"` to match a node/edge with label `label_1`.
  * `NodeName/EdgeName`: string property. Support for filtering by node or edge names. e.g. `app.NodeName = "apphub.io/Application"`

Other properties types can be found at <https://apptopology.googleapis.com/v1/GetSchema>The following operators are supported on properties: 1. Checking if a non-repeated property of a graph element is equal to a scalar value using the equality operator `=`. - LHS must be a node/edge property. - RHS must be a scalar literal. - Supported value types: string (enclosed in double quotes), int, double, and boolean. e.g. `e.project = "project_1"`

  1. Checking if a non-repeated property of a graph element satisfies a condition using the comparison operators `>`, `<`, `>=`, `<=`.


  * LHS must be a node/edge property.
  * RHS must be a scalar literal.
  * Supported value types: string (enclosed in double quotes), int, double. e.g. `e.NumericProperty < 0.1`


  1. Checking if a scalar value is present in a repeated property HAS operator `:`.


  * LHS must be a repeated property.
  * RHS must be a scalar literal.
  * Supported value types: string (enclosed in double quotes), int, double. e.g. `e.Labels : "label_1"`, where `e.Labels` is a repeated string property.


  1. Checking if a property is present using HAS_PROPERTY operator `:`.


  * LHS must be a node or edge alias.
  * RHS must be a property name. e.g. `e : Base/Location`, where `e` is a node or edge alias.


  1. Combining multiple filters using logical operators : `AND`, and `OR`.


  * Parentheses must be used to resolve ambiguity. e.g. `e.Base/Location = "us-central1" AND e.project = "project_1"`


  1. The following custom functions are supported:


  * **EQUALS_ANY(arg1, arg2, arg3, ...)**
    * Checks if `arg1` (a non-repeated property) equals any of the subsequent scalar literal arguments.
    * arg1: non-repeated property. Supported value types: string (enclosed in double quotes), int, double.
    * arg2, arg3, ...: The remaining arguments are literal values to compare against. All the arguments must be of the same type.
    * e.g. `EQUALS_ANY(e.project, "project_1", "project_2")`
  * **CONTAINS_ANY(arg1, arg2, arg3, ...)**
    * Checks if a repeated property has any of the given scalar literals. arg1: repeated_property. Supported element types: string (enclosed in double quotes), int, double.
    * arg2, arg3, ...: The remaining arguments are literal values to compare against. All the arguments must be of the same type.
    * e.g. `CONTAINS_ANY(e.folders, "folder_1", "folder_2")`
  * **CONTAINS_ANY_LESS_THAN(arg1, arg2)**
    * Checks if a repeated property has any element less than the given scalar literal.
    * arg1: repeated_property. Supported element types are: int, double.
    * arg2: scalar literal
    * e.g. `CONTAINS_ANY_LESS_THAN(e.NumericProperty, 0.1)`
  * **CONTAINS_ANY_GREATER_THAN(arg1, arg2)**
    * Checks if a repeated property has any element greater than the given scalar literal.
    * arg1: repeated_property. Supported element types are: int, double.
    * arg2: scalar literal
    * e.g. `CONTAINS_ANY_GREATER_THAN(e.NumericProperty, 0.1)`
  * **CONTAINS_ANY_LESS_OR_EQUAL(arg1, arg2)**
    * Checks if a repeated property has any element less than or equal to the given scalar literal.
    * arg1: repeated_property. Supported element types are: int, double.
    * arg2: scalar literal
    * e.g. `CONTAINS_ANY_LESS_OR_EQUAL(e.NumericProperty, 0.1)`
  * **CONTAINS_ANY_GREATER_OR_EQUAL(arg1, arg2)**
    * Checks if a repeated property has any element greater than or equal to the given scalar literal.
    * arg1: repeated_property. Supported element types are: int, double.
    * arg2: scalar literal
    * e.g. `CONTAINS_ANY_GREATER_OR_EQUAL(e.NumericProperty, 0.1)`

NOTE: - For Alert nodes, only the equality operator `=` is supported. The expression cannot be a composite boolean expression (i.e., combining multiple conditions with AND/OR is not supported; it must be simple). e.g. `a.NodeName = "alert-1"` is supported, but `a.NodeName = "alert-1" OR a.NodeName = "alert-2"` is not supported. - For traffic edges, filters cannot be added.  
  
### ConnectedNodePattern

JSON representation  
---  
      
    
    {
      "edge": {
        object ([EdgePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.EdgePattern))
      },
      "graph": {
        object ([GraphPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.GraphPattern))
      }
    }  
  
Fields  
---  
`edge` |  `object (`[EdgePattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.EdgePattern)`)` Required. To match the edge connected the neighbor subgraph.  
`graph` |  `object (`[GraphPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.GraphPattern)`)` Required. Recursive matcher to match the neighbor subgraph.  
  
### EdgePattern

JSON representation  
---  
      
    
    {
      "direction": enum ([Direction](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.Direction)),
      "labelPropertiesPattern": {
        object ([LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.LabelPropertiesPattern))
      },
      "alias": string
    }  
  
Fields  
---  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.Direction)`)` Required. The direction of the edge to match.  
`labelPropertiesPattern` |  `object (`[LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Input.Schema.LabelPropertiesPattern)`)` Required. Matcher for labels/properties.  
`alias` |  `string` Optional. Represents an identifier to be referenced in `property_matcher_expr`. For example, an alias for `edge` can be referenced as `edge.description = "value_1"`. `alias` must be unique within the query, otherwise an error will be returned.  
  
### Direction

The direction of the edge to match.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Defaults to DIRECTION_UNSPECIFIED.  
`ANY` | Match any edge direction.  
`TO` | Match the edge direction from source to destination.  
`FROM` | Match the edge direction from destination to source.  
  
## Output Schema

Response for GenerateDiscoveredResourcesTopology.

### GenerateDiscoveredResourcesTopologyResponse

JSON representation  
---  
      
    
    {
      "graph": {
        object ([Graph](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Graph))
      }
    }  
  
Fields  
---  
`graph` |  `object (`[Graph](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Graph)`)` The generated topology graph.  
  
### Graph

JSON representation  
---  
      
    
    {
      "nodes": [
        {
          object ([Node](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Node))
        }
      ],
      "edges": [
        {
          object ([Edge](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Edge))
        }
      ]
    }  
  
Fields  
---  
`nodes[]` |  `object (`[Node](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Node)`)` A collection of unique nodes that make up the graph.  
`edges[]` |  `object (`[Edge](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.Edge)`)` Collection of unique edges connecting the `nodes` in the graph. Both source and destination nodes for each edges will be present in the `nodes` list.  
  
### Node

JSON representation  
---  
      
    
    {
      "properties": {
        object
      },
      "name": string,
      "labels": [
        string
      ],
      "context": {
        object ([EntityContext](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.EntityContext))
      }
    }  
  
Fields  
---  
`properties` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Properties associated with the node. Refer to <https://apptopology.googleapis.com/v1/GetSchema> for a detailed list of node properties.  
`name` |  `string` The global unique name of the node. For standard Google Cloud Platform resources, this MUST be the canonical Full Resource Name.Examples:

  * type: compute.googleapis.com/Instance name: "//compute.googleapis.com/projects/my-project-id/zones/us-central1-a/instances/my-vm-1"
  * type: container.googleapis.com/Cluster name: "//container.googleapis.com/projects/my-project-id/locations/us-central1/clusters/my-cluster"

  
`labels[]` |  `string` Labels attached to the node. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the node type.  
`context` |  `object (`[EntityContext](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.EntityContext)`)` The context of the node.  
  
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
  
### EntityContext

JSON representation  
---  
      
    
    {
      "type": string
    }  
  
Fields  
---  
`type` |  `string` The primary, namespaced type dictating the node naming format and supported labels, and defined in the `Schema` (Schema.node_types/edge_types.name), e.g., `Base/compute.googleapis.com/Instance`.  
  
### Edge

JSON representation  
---  
      
    
    {
      "properties": {
        object
      },
      "sourceNodeName": string,
      "destinationNodeName": string,
      "labels": [
        string
      ],
      "context": {
        object ([EntityContext](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.EntityContext))
      }
    }  
  
Fields  
---  
`properties` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Properties associated with the edge. Refer to <https://apptopology.googleapis.com/v1/GetSchema> for a detailed list of edge properties.  
`sourceNodeName` |  `string` The name of the source node for this edge. This is the `name` field in the Node.  
`destinationNodeName` |  `string` The name of the destination node for this edge. This is the `name` field in the Node.  
`labels[]` |  `string` Labels attached to the edge. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the edge type.  
`context` |  `object (`[EntityContext](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#Output.Schema.EntityContext)`)` The context of the edge.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
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
