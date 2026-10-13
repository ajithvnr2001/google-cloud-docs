---
url: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema
title: REST Resource: projects.locations.domains.schema \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:16.901714+00:00
---

# REST Resource: projects.locations.domains.schema  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  REST Resource: projects.locations.domains.schema Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Schema
    * JSON representation
  * NodeType
    * JSON representation
  * EdgeType
    * JSON representation
  * LabelProperties
    * JSON representation
  * Property
    * JSON representation
  * StringValue
    * JSON representation
  * IntValue
    * JSON representation
  * BoolValue
    * JSON representation
  * DoubleValue
    * JSON representation
  * EdgeRule
    * JSON representation
  * NodeGroup
    * JSON representation
  * Methods



## Resource: Schema

Schema is a collection of supported node & edge labels and properties for an overlay.

JSON representation  
---  
      
    
    {
      "name": string,
      "nodeTypes": [
        {
          object ([NodeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeType))
        }
      ],
      "edgeTypes": [
        {
          object ([EdgeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeType))
        }
      ],
      "labelProperties": [
        {
          object ([LabelProperties](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#LabelProperties))
        }
      ],
      "edgeRules": [
        {
          object ([EdgeRule](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeRule))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the schema. Format: `projects/{project}/locations/{location}/domains/{domain}/schema`  
`nodeTypes[]` |  `object (`[NodeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeType)`)` A list of `NodeType`s defined within this schema. Refer to the documentation of `NodeType` for more details.  
`edgeTypes[]` |  `object (`[EdgeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeType)`)` A list of `EdgeType`s defined within this schema. Refer to the documentation of `EdgeType` for more details.  
`labelProperties[]` |  `object (`[LabelProperties](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#LabelProperties)`)` A list of supported labels and corresponding properties.  
`edgeRules[]` |  `object (`[EdgeRule](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeRule)`)` Edge rules. These will indicate which node types can be connected and through what edge type. This is a list of (sourceNodeType, edgeType, destinationNodeType) tuples.  
  
## NodeType

NodeType defines the schema of a node type in the graph.

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
  
## EdgeType

EdgeType defines the schema of an edge type in the graph.

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
  
## LabelProperties

Identifier for the label and corresponding properties.

JSON representation  
---  
      
    
    {
      "label": string,
      "properties": [
        {
          object ([Property](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#Property))
        }
      ],
      "description": string
    }  
  
Fields  
---  
`label` |  `string` Full qualified name of the label.  
`properties[]` |  `object (`[Property](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#Property)`)` List of properties associated with the label.  
`description` |  `string` A human-readable description of the label.  
  
## Property

Property defines the schema of a property in the graph.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": {
        object ([StringValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#StringValue))
      },
      "intValue": {
        object ([IntValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#IntValue))
      },
      "boolValue": {
        object ([BoolValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#BoolValue))
      },
      "doubleValue": {
        object ([DoubleValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#DoubleValue))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` `name` is the key string to identify the property in `Node`s & `Edge`s. Examples: `ProjectId`, `Base/displayName` etc.  
`description` |  `string` A human-readable description of the `PropertyType`, explaining its meaning, purpose, and any constraints or expectations on its value.  
REQUIRED Value type of the property. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `object (`[StringValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#StringValue)`)` StringValue represents a property that has a string value type.  
`intValue` |  `object (`[IntValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#IntValue)`)` IntValue represents a property that has an integer value type.  
`boolValue` |  `object (`[BoolValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#BoolValue)`)` BoolValue represents a property that has a boolean value type.  
`doubleValue` |  `object (`[DoubleValue](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#DoubleValue)`)` DoubleValue represents a property that has a double value type.  
End of mutually exclusive fields.  
  
## StringValue

StringValue represents a property that has a string value type.

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
  
## IntValue

IntValue represents a property that has an integer value type.

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
  
## BoolValue

BoolValue represents a property that has a boolean value type.

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
  
## DoubleValue

DoubleValue represents a property that has a double value type.

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
  
## EdgeRule

EdgeRule defines the connection rules for nodes in the graph.

JSON representation  
---  
      
    
    {
      "edgeType": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "srcNodeType": string,
      "srcNodeGroup": {
        object ([NodeGroup](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeGroup))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "destNodeType": string,
      "destNodeGroup": {
        object ([NodeGroup](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeGroup))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`edgeType` |  `string` Optional. Name of the connected edge type.  
Specifies the source criteria for this edge rule. An edge rule must define its source either statically via a specific node type, or dynamically via a group of nodes that match given constraints.This takes precedence over the `source_node_type` field. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`srcNodeType` |  `string` Optional. The specific node type name that acts as the source for this edge.  
`srcNodeGroup` |  `object (`[NodeGroup](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeGroup)`)` Optional. A dynamic group of nodes, defined by label constraints, that can act as the source for this edge.  
End of mutually exclusive fields.  
Specifies the destination criteria for this edge rule. An edge rule must define its destination either statically via a specific node type, or dynamically via a group of nodes that match given constraints.This takes precedence over the `destination_node_type` field. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`destNodeType` |  `string` Optional. The specific node type name that acts as the destination for this edge.  
`destNodeGroup` |  `object (`[NodeGroup](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeGroup)`)` Optional. A dynamic group of nodes, defined by label constraints, that can act as the destination for this edge.  
End of mutually exclusive fields.  
  
## NodeGroup

NodeGroup represents a dynamic collection of nodes that satisfy specific criteria. A node is considered part of this group if it matches the defined constraints.

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
  
## Methods  
  
---  
  
### `[explore](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema/explore)`

|  Explores the topology schema starting from given node types or label names up to a specified hop depth.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
