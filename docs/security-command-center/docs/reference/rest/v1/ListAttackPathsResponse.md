---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse/
title: ListAttackPathsResponse \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:40.449628+00:00
---

# ListAttackPathsResponse  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  ListAttackPathsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AttackPath
    * JSON representation
  * AttackPathNode
    * JSON representation
  * PathNodeAssociatedFinding
    * JSON representation
  * AttackStepNode
    * JSON representation
  * NodeType
  * AttackPathEdge
    * JSON representation



Response message for listing the attack paths for a given simulation or valued resource.

JSON representation  
---  
      
    
    {
      "attackPaths": [
        {
          object ([AttackPath](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPath))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`attackPaths[]` |  `object (`[AttackPath](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPath)`)` The attack paths that the attack path simulation identified.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results.  
  
## AttackPath

A path that an attacker could take to reach an exposed resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "pathNodes": [
        {
          object ([AttackPathNode](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPathNode))
        }
      ],
      "edges": [
        {
          object ([AttackPathEdge](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPathEdge))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The attack path name, for example, `organizations/12/simulation/34/valuedResources/56/attackPaths/78`  
`pathNodes[]` |  `object (`[AttackPathNode](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPathNode)`)` A list of nodes that exist in this attack path.  
`edges[]` |  `object (`[AttackPathEdge](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackPathEdge)`)` A list of the edges between nodes in this attack path.  
  
## AttackPathNode

Represents one point that an attacker passes through in this attack path.

JSON representation  
---  
      
    
    {
      "resource": string,
      "resourceType": string,
      "displayName": string,
      "associatedFindings": [
        {
          object ([PathNodeAssociatedFinding](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#PathNodeAssociatedFinding))
        }
      ],
      "uuid": string,
      "attackSteps": [
        {
          object ([AttackStepNode](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackStepNode))
        }
      ]
    }  
  
Fields  
---  
`resource` |  `string` The name of the resource at this point in the attack path. The format of the name follows the Cloud Asset Inventory [resource name format](https://cloud.google.com/asset-inventory/docs/resource-name-format)  
`resourceType` |  `string` The [supported resource type](https://cloud.google.com/asset-inventory/docs/supported-asset-types)  
`displayName` |  `string` Human-readable name of this resource.  
`associatedFindings[]` |  `object (`[PathNodeAssociatedFinding](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#PathNodeAssociatedFinding)`)` The findings associated with this node in the attack path.  
`uuid` |  `string` Unique id of the attack path node.  
`attackSteps[]` |  `object (`[AttackStepNode](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#AttackStepNode)`)` A list of attack step nodes that exist in this attack path node.  
  
## PathNodeAssociatedFinding

A finding that is associated with this node in the attack path.

JSON representation  
---  
      
    
    {
      "canonicalFinding": string,
      "findingCategory": string,
      "name": string
    }  
  
Fields  
---  
`canonicalFinding` |  `string` Canonical name of the associated findings. Example: `organizations/123/sources/456/findings/789`  
`findingCategory` |  `string` The additional taxonomy group within findings from a given source.  
`name` |  `string` Full resource name of the finding.  
  
## AttackStepNode

Detailed steps the attack can take between path nodes.

JSON representation  
---  
      
    
    {
      "uuid": string,
      "type": enum ([NodeType](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#NodeType)),
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "description": string
    }  
  
Fields  
---  
`uuid` |  `string` Unique ID for one Node  
`type` |  `enum (`[NodeType](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/ListAttackPathsResponse#NodeType)`)` Attack step type. Can be either AND, OR or DEFENSE  
`displayName` |  `string` User friendly name of the attack step  
`labels` |  `map (key: string, value: string)` Attack step labels for metadataAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Attack step description  
  
## NodeType

The type of the incoming attack step node.

Enums  
---  
`NODE_TYPE_UNSPECIFIED` | Type not specified  
`NODE_TYPE_AND` | Incoming edge joined with AND  
`NODE_TYPE_OR` | Incoming edge joined with OR  
`NODE_TYPE_DEFENSE` | Incoming edge is defense  
`NODE_TYPE_ATTACKER` | Incoming edge is attacker  
  
## AttackPathEdge

Represents a connection between a source node and a destination node in this attack path.

JSON representation  
---  
      
    
    {
      "source": string,
      "destination": string
    }  
  
Fields  
---  
`source` |  `string` The attack node uuid of the source node.  
`destination` |  `string` The attack node uuid of the destination node.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
