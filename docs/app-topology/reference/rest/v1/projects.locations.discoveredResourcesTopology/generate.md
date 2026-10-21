---
url: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate/
title: Method: projects.locations.discoveredResourcesTopology.generate \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:14.078740+00:00
---

# Method: projects.locations.discoveredResourcesTopology.generate  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  Method: projects.locations.discoveredResourcesTopology.generate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * GraphPattern
    * JSON representation
  * NodePattern
    * JSON representation
  * LabelPropertiesPattern
    * JSON representation
  * ConnectedNodePattern
    * JSON representation
  * EdgePattern
    * JSON representation
  * Direction
  * Graph
    * JSON representation
  * Node
    * JSON representation
  * EntityContext
    * JSON representation
  * Edge
    * JSON representation
  * Try it!



Generate the topology for all resources in the given project. If the project represents an [app boundary](https://cloud.google.com/app-hub/docs/reference/rest/v1/Boundary), the topology is generated for all resources in the boundary.

### HTTP request

`POST https://apptopology.googleapis.com/v1/{name=projects/*/locations/*/discoveredResourcesTopology}:generate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The project to query discoverable resources on. Expected format: `projects/{project}/locations/{location}/discoveredResourcesTopology`. Only `global` location is supported.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "topologyDomains": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "filter": {
        object ([GraphPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#GraphPattern))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`topologyDomains[]` |  `string` Required. The full resource name of the domain of the app topology. Format: `projects/{project}/locations/{location}/domains/{domain}` Caller must have apptopology.domains.get permission on each of the domains.  
Query the topology by building a graph pattern filter or pre-defined topology view. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`filter` |  `object (`[GraphPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#GraphPattern)`)` Filters for the topology nodes and edges; Detail format see GraphPattern proto. A separate 'LookupSchema' method will be added that will return the necessary information to be able to construct these filters.  
End of mutually exclusive fields.  
  
### Response body

Response for discoveredResourcesTopology.generate.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "graph": {
        object ([Graph](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Graph))
      }
    }  
  
Fields  
---  
`graph` |  `object (`[Graph](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Graph)`)` The generated topology graph.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/apptopology.read-write`
  * `https://www.googleapis.com/auth/apptopology.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `apptopology.discoveredResourcesTopologies.generate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GraphPattern

Recursive graph pattern matcher to select and constrain the returned topology. AppTopology API allows cycle in the graph traversal and will return unique node and edge results in the response. SLO is guaranteed for at most 5 hops in the graph traversal.

JSON representation  
---  
      
    
    {
      "startingNode": {
        object ([NodePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#NodePattern))
      },
      "neighbors": [
        {
          object ([ConnectedNodePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#ConnectedNodePattern))
        }
      ]
    }  
  
Fields  
---  
`startingNode` |  `object (`[NodePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#NodePattern)`)` Required. Pattern matcher to select the starting nodes in the graph.  
`neighbors[]` |  `object (`[ConnectedNodePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#ConnectedNodePattern)`)` Optional. Pattern matcher to match the connected subgraphs; all of these are ANDed.  
  
## NodePattern

Node pattern matcher to match the node id, labels and properties.

JSON representation  
---  
      
    
    {
      "alias": string,
      "labelPropertiesPattern": {
        object ([LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#LabelPropertiesPattern))
      }
    }  
  
Fields  
---  
`alias` |  `string` Optional. Represents an identifier to be referenced in `propertyMatcherExpr`. For example, an alias for `app` can be referenced as `app.Base/location="us-central1"`. `alias` must be unique within the query, otherwise an error will be returned.  
`labelPropertiesPattern` |  `object (`[LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#LabelPropertiesPattern)`)` Optional. Matcher for labels/properties.  
  
## LabelPropertiesPattern

Matcher for label and property. The matcher accepts both exact match and expression.

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
  
## ConnectedNodePattern

Edge pattern matcher to match the edge direction, labels and properties.

JSON representation  
---  
      
    
    {
      "edge": {
        object ([EdgePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EdgePattern))
      },
      "graph": {
        object ([GraphPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#GraphPattern))
      }
    }  
  
Fields  
---  
`edge` |  `object (`[EdgePattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EdgePattern)`)` Required. To match the edge connected the neighbor subgraph.  
`graph` |  `object (`[GraphPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#GraphPattern)`)` Required. Recursive matcher to match the neighbor subgraph.  
  
## EdgePattern

Edge pattern matcher to match the edge direction, labels and properties.

JSON representation  
---  
      
    
    {
      "direction": enum ([Direction](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Direction)),
      "labelPropertiesPattern": {
        object ([LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#LabelPropertiesPattern))
      },
      "alias": string
    }  
  
Fields  
---  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Direction)`)` Required. The direction of the edge to match.  
`labelPropertiesPattern` |  `object (`[LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#LabelPropertiesPattern)`)` Required. Matcher for labels/properties.  
`alias` |  `string` Optional. Represents an identifier to be referenced in `propertyMatcherExpr`. For example, an alias for `edge` can be referenced as `edge.description = "value_1"`. `alias` must be unique within the query, otherwise an error will be returned.  
  
## Direction

The direction of the edge to match.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Defaults to DIRECTION_UNSPECIFIED.  
`ANY` | Match any edge direction.  
`TO` | Match the edge direction from source to destination.  
`FROM` | Match the edge direction from destination to source.  
  
## Graph

Represents a graph structure composed of nodes and edges.

JSON representation  
---  
      
    
    {
      "nodes": [
        {
          object ([Node](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Node))
        }
      ],
      "edges": [
        {
          object ([Edge](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Edge))
        }
      ]
    }  
  
Fields  
---  
`nodes[]` |  `object (`[Node](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Node)`)` A collection of unique nodes that make up the graph.  
`edges[]` |  `object (`[Edge](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#Edge)`)` Collection of unique edges connecting the `nodes` in the graph. Both source and destination nodes for each edges will be present in the `nodes` list.  
  
## Node

Represents a single node in the graph.

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
        object ([EntityContext](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EntityContext))
      }
    }  
  
Fields  
---  
`properties` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Properties associated with the node. Refer to <https://apptopology.googleapis.com/v1/GetSchema> for a detailed list of node properties.  
`name` |  `string` The global unique name of the node. For standard Google Cloud Platform resources, this MUST be the canonical Full Resource Name.Examples:

  * type: compute.googleapis.com/Instance name: "//compute.googleapis.com/projects/my-project-id/zones/us-central1-a/instances/my-vm-1"
  * type: container.googleapis.com/Cluster name: "//container.googleapis.com/projects/my-project-id/locations/us-central1/clusters/my-cluster"

  
`labels[]` |  `string` Labels attached to the node. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the node type.  
`context` |  `object (`[EntityContext](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EntityContext)`)` The context of the node.  
  
## EntityContext

Represents the context of an entity (node or edge) in the graph.

JSON representation  
---  
      
    
    {
      "type": string
    }  
  
Fields  
---  
`type` |  `string` The primary, namespaced type dictating the node naming format and supported labels, and defined in the `Schema` (Schema.node_types/edgeTypes.name), e.g., `Base/compute.googleapis.com/Instance`.  
  
## Edge

Represents a single edge connecting two nodes in the graph.

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
        object ([EntityContext](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EntityContext))
      }
    }  
  
Fields  
---  
`properties` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Properties associated with the edge. Refer to <https://apptopology.googleapis.com/v1/GetSchema> for a detailed list of edge properties.  
`sourceNodeName` |  `string` The name of the source node for this edge. This is the `name` field in the Node.  
`destinationNodeName` |  `string` The name of the destination node for this edge. This is the `name` field in the Node.  
`labels[]` |  `string` Labels attached to the edge. Composable, namespaced building blocks that define core attributes through associated properties. Multiple labels aggregate to fully specify the functional traits and property schema of the edge type.  
`context` |  `object (`[EntityContext](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.discoveredResourcesTopology/generate#EntityContext)`)` The context of the edge.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
