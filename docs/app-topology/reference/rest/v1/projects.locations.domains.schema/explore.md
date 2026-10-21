---
url: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema/explore/
title: Method: projects.locations.domains.schema.explore \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:13.399301+00:00
---

# Method: projects.locations.domains.schema.explore  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema/explore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  Method: projects.locations.domains.schema.explore Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Explores the topology schema starting from given node types or label names up to a specified hop depth.

### HTTP request

`POST https://apptopology.googleapis.com/v1/{name=projects/*/locations/*/domains/*/schema}:explore`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the singleton domain schema resource. Format: `projects/{project}/locations/{location}/domains/{domain}/schema`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "startLabels": [
        string
      ],
      "depth": integer,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`startLabels[]` |  `string` Optional. Starting label names to begin traversal. Substring, case-insensitive matches are performed against allowed label names in the schema. A maximum of 10 `startLabels` can be specified; providing more will result in an `INVALID_ARGUMENT` error. If `startLabels` is unset or empty, all authorized node types will be used as the starting set.  
`depth` |  `integer` Optional. The maximum depth of BFS traversal hops to perform from the starting node types or label names. Defaults to 0 if unspecified.  
`pageSize` |  `integer` Optional. The maximum number of schema elements to return in a single page.

  * The service might return fewer elements than this value if adding another edge and its required endpoint nodes exceeds `pageSize`.
  * If omitted or set to 0, default (100) will be used.
  * Minimum pageSize is 3 to ensure at least one edge and its endpoint nodes fit on a page; values below 3 (e.g. 1 or 2) are changed to 3.
  * Maximum value is 500.

  
`pageToken` |  `string` Optional. A page token received from a previous `schema.explore` call. Provide this to retrieve the subsequent page.When paginating, all other parameters (except pageSize) provided to `schema.explore` must match the call that provided the page token.  
  
### Response body

Response for schema.explore.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
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
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`nodeTypes[]` |  `object (`[NodeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#NodeType)`)` A list of `NodeType`s defined within this schema. Refer to the documentation of `NodeType` for more details.  
`edgeTypes[]` |  `object (`[EdgeType](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeType)`)` A list of `EdgeType`s defined within this schema. Refer to the documentation of `EdgeType` for more details.  
`labelProperties[]` |  `object (`[LabelProperties](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#LabelProperties)`)` A list of supported labels and corresponding properties.  
`edgeRules[]` |  `object (`[EdgeRule](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains.schema#EdgeRule)`)` Edge rules. These will indicate which node types can be connected and through what edge type. This is a list of (sourceNodeType, edgeType, destinationNodeType) tuples.  
`nextPageToken` |  `string` A token to retrieve the next page of results, or empty if there are no more results in the traversal set.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/apptopology.read-write`
  * `https://www.googleapis.com/auth/apptopology.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `apptopology.schemas.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
