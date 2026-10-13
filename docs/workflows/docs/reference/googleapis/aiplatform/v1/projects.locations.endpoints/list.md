---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.endpoints/list/
title: Method: googleapis.aiplatform.v1.projects.locations.endpoints.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:03.340879+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.endpoints.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.endpoints/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.endpoints.list Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Lists Endpoints in a Location.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The resource name of the Location from which to list the Endpoints. Format: `projects/{project}/locations/{location}`  
`filter` |  `string` Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. * `endpoint` supports `=` and `!=`. `endpoint` represents the Endpoint ID, i.e. the last segment of the Endpoint's resource name. * `display_name` supports `=` and `!=`. * `labels` supports general map functions that is: * `labels.key=value` \- key:value equality * `labels.key:*` or `labels:key` \- key existence * A key including a space must be quoted. `labels."a key"`. * `base_model_name` only supports `=`. Some examples: * `endpoint=1` * `displayName="myDisplayName"` * `labels.myKey="myValue"` * `baseModelName="text-bison"`  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * `display_name` * `create_time` * `update_time` Example: `display_name, create_time desc`.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Optional. The standard list page size.  
`pageToken` |  `string` Optional. The standard list page token. Typically obtained via ListEndpointsResponse.next_page_token of the previous EndpointService.ListEndpoints call.  
`readMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Optional. Mask specifying which fields to read.  
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

If successful, the response contains an instance of [`GoogleCloudAiplatformV1ListEndpointsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1ListEndpointsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/list).

### YAML
    
    
    - list:
        call: googleapis.aiplatform.v1.projects.locations.endpoints.list
        args:
            parent: ...
            filter: ...
            orderBy: ...
            pageSize: ...
            pageToken: ...
            readMask: ...
            region: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.aiplatform.v1.projects.locations.endpoints.list",
          "args": {
            "parent": "...",
            "filter": "...",
            "orderBy": "...",
            "pageSize": "...",
            "pageToken": "...",
            "readMask": "...",
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
