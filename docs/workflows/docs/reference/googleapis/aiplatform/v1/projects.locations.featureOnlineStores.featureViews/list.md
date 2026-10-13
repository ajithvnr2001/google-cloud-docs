---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featureOnlineStores.featureViews/list/
title: Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:20.782670+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featureOnlineStores.featureViews/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.list Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Lists FeatureViews in a given FeatureOnlineStore.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`filter` |  `string` Lists the FeatureViews that match the filter expression. The following filters are supported: * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format. * `labels`: Supports key-value equality as well as key presence. Examples: * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> FeatureViews created or updated after 2020-01-31T15:30:00.000000Z. * `labels.active = yes AND labels.env = prod` \--> FeatureViews having both (active: yes) and (env: prod) labels. * `labels.env: *` \--> Any FeatureView which has a label with 'env' as the key.  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * `feature_view_id` * `create_time` * `update_time`  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of FeatureViews to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViews will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous FeatureOnlineStoreAdminService.ListFeatureViews call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeatureOnlineStoreAdminService.ListFeatureViews must match the call that provided the page token.  
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

If successful, the response contains an instance of [`GoogleCloudAiplatformV1ListFeatureViewsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1ListFeatureViewsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/list).

### YAML
    
    
    - list:
        call: googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.list
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
          "call": "googleapis.aiplatform.v1.projects.locations.featureOnlineStores.featureViews.list",
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
