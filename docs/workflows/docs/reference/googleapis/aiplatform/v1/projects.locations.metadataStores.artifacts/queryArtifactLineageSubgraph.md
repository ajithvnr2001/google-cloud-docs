---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.artifacts/queryArtifactLineageSubgraph/
title: Method: googleapis.aiplatform.v1.projects.locations.metadataStores.artifacts.queryArtifactLineageSubgraph \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:01.447027+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.metadataStores.artifacts.queryArtifactLineageSubgraph  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.artifacts/queryArtifactLineageSubgraph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.metadataStores.artifacts.queryArtifactLineageSubgraph Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.

## Arguments

Parameters  
---  
`artifact` |  `string` Required. The resource name of the Artifact whose Lineage needs to be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}` The request may error with FAILED_PRECONDITION if the number of Artifacts, the number of Executions, or the number of Events that would be returned for the Context exceeds 1000.  
`filter` |  `string` Filter specifying the boolean condition for the Artifacts to satisfy in order to be part of the Lineage Subgraph. The syntax to define filter query is based on https://google.aip.dev/160. The supported set of filters include the following: * **Attribute filtering** : For example: `display_name = "test"` Supported fields include: `name`, `display_name`, `uri`, `state`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"` * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata..`. For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0` Each of the above supported filter types can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = "test" AND metadata.field1.bool_value = true`.  
`maxHops` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Specifies the size of the lineage graph in terms of number of hops from the specified artifact. Negative Value: INVALID_ARGUMENT error is returned 0: Only input artifact is returned. No value: Transitive closure is performed to return the complete graph.  
`region` |  `string` Required. Region of the HTTP endpoint. For example, if region is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. See [service endpoints](https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints).  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudAiplatformV1LineageSubgraph`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1LineageSubgraph).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores.artifacts/queryArtifactLineageSubgraph).

### YAML
    
    
    - queryArtifactLineageSubgraph:
        call: googleapis.aiplatform.v1.projects.locations.metadataStores.artifacts.queryArtifactLineageSubgraph
        args:
            artifact: ...
            filter: ...
            maxHops: ...
            region: ...
        result: queryArtifactLineageSubgraphResult

### JSON
    
    
    [
      {
        "queryArtifactLineageSubgraph": {
          "call": "googleapis.aiplatform.v1.projects.locations.metadataStores.artifacts.queryArtifactLineageSubgraph",
          "args": {
            "artifact": "...",
            "filter": "...",
            "maxHops": "...",
            "region": "..."
          },
          "result": "queryArtifactLineageSubgraphResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
