---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.contexts/list/
title: Method: googleapis.aiplatform.v1.projects.locations.metadataStores.contexts.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:05.220913+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.metadataStores.contexts.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.contexts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.metadataStores.contexts.list Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Lists Contexts on the MetadataStore.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The MetadataStore whose Contexts should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`  
`filter` |  `string` Filter specifying the boolean condition for the Contexts to satisfy in order to be part of the result set. The syntax to define filter query is based on https://google.aip.dev/160. Following are the supported set of filters: * **Attribute filtering** : For example: `display_name = "test"`. Supported fields include: `name`, `display_name`, `schema_title`, `create_time`, and `update_time`. Time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`. * **Metadata field** : To filter on metadata fields use traversal operation as follows: `metadata..`. For example: `metadata.field_1.number_value = 10.0`. In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0` * **Parent Child filtering** : To filter Contexts based on parent-child relationship use the HAS operator as follows: `parent_contexts: "projects//locations//metadataStores//contexts/" child_contexts: "projects//locations//metadataStores//contexts/"` Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5. For example: `display_name = "test" AND metadata.field1.bool_value = true`.  
`orderBy` |  `string` How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see https://google.aip.dev/132#ordering for more details.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of Contexts to return. The service may return fewer. Must be in range 1-1000, inclusive. Defaults to 100.  
`pageToken` |  `string` A page token, received from a previous MetadataService.ListContexts call. Provide this to retrieve the subsequent page. When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)  
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

If successful, the response contains an instance of [`GoogleCloudAiplatformV1ListContextsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1ListContextsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores.contexts/list).

### YAML
    
    
    - list:
        call: googleapis.aiplatform.v1.projects.locations.metadataStores.contexts.list
        args:
            parent: ...
            filter: ...
            orderBy: ...
            pageSize: ...
            pageToken: ...
            region: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.aiplatform.v1.projects.locations.metadataStores.contexts.list",
          "args": {
            "parent": "...",
            "filter": "...",
            "orderBy": "...",
            "pageSize": "...",
            "pageToken": "...",
            "region": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
