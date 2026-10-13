---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/tagKeys/list/
title: Method: googleapis.cloudresourcemanager.v3.tagKeys.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:08.781073+00:00
---

# Method: googleapis.cloudresourcemanager.v3.tagKeys.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/tagKeys/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudresourcemanager.v3.tagKeys.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists all TagKeys for a parent resource.

## Arguments

Parameters  
---  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Optional. The maximum number of TagKeys to return in the response. The server allows a maximum of 300 TagKeys to return. If unspecified, the server will use 100 as the default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `ListTagKey` that indicates where this listing should continue from.  
`parent` |  `string` Required. The resource name of the new TagKey's parent. Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListTagKeysResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/Overview#ListTagKeysResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys/list).

### YAML
    
    
    - list:
        call: googleapis.cloudresourcemanager.v3.tagKeys.list
        args:
            pageSize: ...
            pageToken: ...
            parent: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.cloudresourcemanager.v3.tagKeys.list",
          "args": {
            "pageSize": "...",
            "pageToken": "...",
            "parent": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
