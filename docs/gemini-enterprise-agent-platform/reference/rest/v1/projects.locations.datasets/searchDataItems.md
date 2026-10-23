---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems/
title: Method: datasets.searchDataItems \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:01.843382+00:00
---

# Method: datasets.searchDataItems  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: datasets.searchDataItems Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.searchDataItems

Searches DataItems in a Dataset.

### Endpoint

get  `https://{service-endpoint}/v1/{dataset}:searchDataItems`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`dataset` `string` Required. The resource name of the Dataset from which to search DataItems. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

### Query parameters

| `savedQuery  
**(deprecated)**` `string` The resource name of a SavedQuery(annotation set in UI). Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{savedQuery}` All of the search will be done in the context of this SavedQuery. | `dataLabelingJob` `string` The resource name of a DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{dataLabelingJob}` If this field is set, all of the search will be done in the context of this DataLabelingJob. | `dataItemFilter` `string` An expression for filtering the DataItem that will be returned.

  * `data_item_id` \- for = or !=.
  * `labeled` \- for = or !=.
  * `has_annotation(ANNOTATION_SPEC_ID)` \- true only for DataItem that have at least one annotation with annotationSpecId = `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob.

For example:

  * `dataItem=1`
  * `has_annotation(5)`

| `annotationsFilter  
**(deprecated)**` `string` An expression for filtering the Annotations that will be returned per DataItem. * `annotationSpecId` \- for = or !=. | `annotationFilters[]` `string` An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned. * `annotationSpecId` \- for = or !=. Must specify `savedQueryId=` \- saved query id that annotations should belong to. | `fieldMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields of `[DataItemView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#DataItemView)` to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. | `annotationsLimit` `integer` If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used. | `pageSize` `integer` Requested page size. Server may return fewer results than requested. Default and maximum page size is 100. | `orderBy  
**(deprecated)**` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. | `pageToken` `string` A token identifying a page of results for the server to return Typically obtained via `[SearchDataItemsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#body.SearchDataItemsResponse.FIELDS.next_page_token)` of the previous `[DatasetService.SearchDataItems](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#google.cloud.aiplatform.v1.DatasetService.SearchDataItems)` call. | `order` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`orderByDataItem` `string` A comma-separated list of data item fields to order by, sorted in ascending order. Use "desc" after a field name for descending. | `orderByAnnotation` `object (`[OrderByAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#OrderByAnnotation)`)` Expression that allows ranking results based on annotation's property. End of mutually exclusive fields.

### Request body

The request body must be empty.

### Response body

Response message for `[DatasetService.SearchDataItems](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#google.cloud.aiplatform.v1.DatasetService.SearchDataItems)`. If successful, the response body contains data with the following structure: | Fields  
  
`dataItemViews[]` `object (`[DataItemView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#DataItemView)`)` The DataItemViews read. | `nextPageToken` `string` A token to retrieve next page of results. Pass to `[SearchDataItemsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "dataItemViews": [
        {
          object ([DataItemView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.datasets/searchDataItems#DataItemView))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `dataset` resource:

  * `aiplatform.dataItems.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## OrderByAnnotation

Expression that allows ranking results based on annotation's property.

Fields  
  
`savedQuery` `string` Required. Saved query of the Annotation. Only Annotations belong to this saved query will be considered for ordering. | `orderBy` `string` A comma-separated list of annotation fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Must also specify savedQuery. | JSON representation  
---  
      
    
    {
      "savedQuery": string,
      "orderBy": string
    }  
  
## DataItemView

A container for a single DataItem and Annotations on it.

Fields  
  
`dataItem` `object (`[DataItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DataItem)`)` The DataItem. | `annotations[]` `object (`[Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Annotation)`)` The Annotations on the DataItem. If too many Annotations should be returned for the DataItem, this field will be truncated per annotationsLimit in request. If it was, then the hasTruncatedAnnotations will be set to true. | `hasTruncatedAnnotations` `boolean` True if and only if the Annotations field has been truncated. It happens if more Annotations for this DataItem met the request's annotationFilter than are allowed to be returned by annotationsLimit. Note that if Annotations field is not being returned due to field mask, then this field will not be set to true no matter how many Annotations are there. | JSON representation  
---  
      
    
    {
      "dataItem": {
        object ([DataItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DataItem))
      },
      "annotations": [
        {
          object ([Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Annotation))
        }
      ],
      "hasTruncatedAnnotations": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
