---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list/
title: Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:23.959865+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Lists FeatureViewSyncs in a given FeatureView.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`filter` |  `string` Lists the FeatureViewSyncs that match the filter expression. The following filters are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. Examples: * `create_time > \"2020-01-31T15:30:00.000000Z\"` \--> FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z.  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * `create_time`  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViewSyncs call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViewSyncs must match the call that provided the page token.  
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

If successful, the response contains an instance of [`GoogleCloudAiplatformV1ListFeatureViewSyncsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1ListFeatureViewSyncsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list).

### YAML
    
    
    - list:
        call: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list
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
          "call": "googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list",
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
