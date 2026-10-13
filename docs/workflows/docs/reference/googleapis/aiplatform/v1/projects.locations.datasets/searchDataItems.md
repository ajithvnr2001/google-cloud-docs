---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.datasets/searchDataItems/
title: Method: googleapis.aiplatform.v1.projects.locations.datasets.searchDataItems \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:49.382252+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.datasets.searchDataItems  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.datasets/searchDataItems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.datasets.searchDataItems Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Searches DataItems in a Dataset.

## Arguments

Parameters  
---  
`dataset` |  `string` Required. The resource name of the Dataset from which to search DataItems. Format: `projects/{project}/locations/{location}/datasets/{dataset}`  
`annotationFilters` |  `string` An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned. * `annotation_spec_id` \- for = or !=. Must specify `saved_query_id=` \- saved query id that annotations should belong to.  
`annotationsFilter` |  `string` An expression for filtering the Annotations that will be returned per DataItem. * `annotation_spec_id` \- for = or !=.  
`annotationsLimit` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used.  
`dataItemFilter` |  `string` An expression for filtering the DataItem that will be returned. * `data_item_id` \- for = or !=. * `labeled` \- for = or !=. * `has_annotation(ANNOTATION_SPEC_ID)` \- true only for DataItem that have at least one annotation with annotation_spec_id = `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob. For example: * `data_item=1` * `has_annotation(5)`  
`dataLabelingJob` |  `string` The resource name of a DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}` If this field is set, all of the search will be done in the context of this DataLabelingJob.  
`fieldMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Mask specifying which fields of DataItemView to read.  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.  
`orderByAnnotation.orderBy` |  `string` A comma-separated list of annotation fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Must also specify saved_query.  
`orderByAnnotation.savedQuery` |  `string` Required. Saved query of the Annotation. Only Annotations belong to this saved query will be considered for ordering.  
`orderByDataItem` |  `string` A comma-separated list of data item fields to order by, sorted in ascending order. Use "desc" after a field name for descending.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Requested page size. Server may return fewer results than requested. Default and maximum page size is 100.  
`pageToken` |  `string` A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call.  
`savedQuery` |  `string` The resource name of a SavedQuery(annotation set in UI). Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}` All of the search will be done in the context of this SavedQuery.  
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

If successful, the response contains an instance of [`GoogleCloudAiplatformV1SearchDataItemsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1SearchDataItemsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets/searchDataItems).

### YAML
    
    
    - searchDataItems:
        call: googleapis.aiplatform.v1.projects.locations.datasets.searchDataItems
        args:
            dataset: ...
            annotationFilters: ...
            annotationsFilter: ...
            annotationsLimit: ...
            dataItemFilter: ...
            dataLabelingJob: ...
            fieldMask: ...
            orderBy: ...
            orderByAnnotation:
                orderBy: ...
                savedQuery: ...
            orderByDataItem: ...
            pageSize: ...
            pageToken: ...
            savedQuery: ...
            region: ...
        result: searchDataItemsResult

### JSON
    
    
    [
      {
        "searchDataItems": {
          "call": "googleapis.aiplatform.v1.projects.locations.datasets.searchDataItems",
          "args": {
            "dataset": "...",
            "annotationFilters": "...",
            "annotationsFilter": "...",
            "annotationsLimit": "...",
            "dataItemFilter": "...",
            "dataLabelingJob": "...",
            "fieldMask": "...",
            "orderBy": "...",
            "orderByAnnotation": {
              "orderBy": "...",
              "savedQuery": "..."
            },
            "orderByDataItem": "...",
            "pageSize": "...",
            "pageToken": "...",
            "savedQuery": "...",
            "region": "..."
          },
          "result": "searchDataItemsResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
