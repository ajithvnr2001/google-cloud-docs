---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchDataItemsRequestOrBuilder
title: Interface SearchDataItemsRequestOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:22.568823+00:00
---

# Interface SearchDataItemsRequestOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchDataItemsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchDataItemsRequestOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface SearchDataItemsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnnotationFilters(int index)
    
    
    public abstract String getAnnotationFilters(int index)

An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned.

  * `annotation_spec_id` \- for = or !=. Must specify `saved_query_id=` \- saved query id that annotations should belong to.



`repeated string annotation_filters = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The annotationFilters at the given index.  
  
### getAnnotationFiltersBytes(int index)
    
    
    public abstract ByteString getAnnotationFiltersBytes(int index)

An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned.

  * `annotation_spec_id` \- for = or !=. Must specify `saved_query_id=` \- saved query id that annotations should belong to.



`repeated string annotation_filters = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the annotationFilters at the given index.  
  
### getAnnotationFiltersCount()
    
    
    public abstract int getAnnotationFiltersCount()

An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned.

  * `annotation_spec_id` \- for = or !=. Must specify `saved_query_id=` \- saved query id that annotations should belong to.



`repeated string annotation_filters = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of annotationFilters.  
  
### getAnnotationFiltersList()
    
    
    public abstract List<String> getAnnotationFiltersList()

An expression that specifies what Annotations will be returned per DataItem. Annotations satisfied either of the conditions will be returned.

  * `annotation_spec_id` \- for = or !=. Must specify `saved_query_id=` \- saved query id that annotations should belong to.



`repeated string annotation_filters = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the annotationFilters.  
  
### getAnnotationsFilter() (deprecated)
    
    
    public abstract String getAnnotationsFilter()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.annotations_filter is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=741_

An expression for filtering the Annotations that will be returned per DataItem.

  * `annotation_spec_id` \- for = or !=.



`string annotations_filter = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The annotationsFilter.  
  
### getAnnotationsFilterBytes() (deprecated)
    
    
    public abstract ByteString getAnnotationsFilterBytes()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.annotations_filter is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=741_

An expression for filtering the Annotations that will be returned per DataItem.

  * `annotation_spec_id` \- for = or !=.



`string annotations_filter = 5 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for annotationsFilter.  
  
### getAnnotationsLimit()
    
    
    public abstract int getAnnotationsLimit()

If set, only up to this many of Annotations will be returned per DataItemView. The maximum value is 1000. If not set, the maximum value will be used.

`int32 annotations_limit = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The annotationsLimit.  
  
### getDataItemFilter()
    
    
    public abstract String getDataItemFilter()

An expression for filtering the DataItem that will be returned.

  * `data_item_id` \- for = or !=.
  * `labeled` \- for = or !=.
  * `has_annotation(ANNOTATION_SPEC_ID)` \- true only for DataItem that have at least one annotation with annotation_spec_id = `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob.

For example:

  * `data_item=1`

  * `has_annotation(5)`



`string data_item_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataItemFilter.  
  
### getDataItemFilterBytes()
    
    
    public abstract ByteString getDataItemFilterBytes()

An expression for filtering the DataItem that will be returned.

  * `data_item_id` \- for = or !=.
  * `labeled` \- for = or !=.
  * `has_annotation(ANNOTATION_SPEC_ID)` \- true only for DataItem that have at least one annotation with annotation_spec_id = `ANNOTATION_SPEC_ID` in the context of SavedQuery or DataLabelingJob.

For example:

  * `data_item=1`

  * `has_annotation(5)`



`string data_item_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataItemFilter.  
  
### getDataLabelingJob()
    
    
    public abstract String getDataLabelingJob()

The resource name of a DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}` If this field is set, all of the search will be done in the context of this DataLabelingJob.

`string data_labeling_job = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataLabelingJob.  
  
### getDataLabelingJobBytes()
    
    
    public abstract ByteString getDataLabelingJobBytes()

The resource name of a DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}` If this field is set, all of the search will be done in the context of this DataLabelingJob.

`string data_labeling_job = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataLabelingJob.  
  
### getDataset()
    
    
    public abstract String getDataset()

Required. The resource name of the Dataset from which to search DataItems. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

` string dataset = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataset.  
  
### getDatasetBytes()
    
    
    public abstract ByteString getDatasetBytes()

Required. The resource name of the Dataset from which to search DataItems. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

` string dataset = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataset.  
  
### getFieldMask()
    
    
    public abstract FieldMask getFieldMask()

Mask specifying which fields of DataItemView to read.

`.google.protobuf.FieldMask field_mask = 6;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The fieldMask.  
  
### getFieldMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getFieldMaskOrBuilder()

Mask specifying which fields of DataItemView to read.

`.google.protobuf.FieldMask field_mask = 6;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### getOrderBy() (deprecated)
    
    
    public abstract String getOrderBy()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.order_by is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=765_

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

`string order_by = 9 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderBy.  
  
### getOrderByAnnotation()
    
    
    public abstract SearchDataItemsRequest.OrderByAnnotation getOrderByAnnotation()

Expression that allows ranking results based on annotation's property.

` .google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotation order_by_annotation = 13; `

**Returns**  
---  
**Type** | **Description**  
`[SearchDataItemsRequest.OrderByAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotation)` | The orderByAnnotation.  
  
### getOrderByAnnotationOrBuilder()
    
    
    public abstract SearchDataItemsRequest.OrderByAnnotationOrBuilder getOrderByAnnotationOrBuilder()

Expression that allows ranking results based on annotation's property.

` .google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotation order_by_annotation = 13; `

**Returns**  
---  
**Type** | **Description**  
`[SearchDataItemsRequest.OrderByAnnotationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotationOrBuilder)` |   
  
### getOrderByBytes() (deprecated)
    
    
    public abstract ByteString getOrderByBytes()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.order_by is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=765_

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

`string order_by = 9 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderBy.  
  
### getOrderByDataItem()
    
    
    public abstract String getOrderByDataItem()

A comma-separated list of data item fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

`string order_by_data_item = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderByDataItem.  
  
### getOrderByDataItemBytes()
    
    
    public abstract ByteString getOrderByDataItemBytes()

A comma-separated list of data item fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

`string order_by_data_item = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderByDataItem.  
  
### getOrderCase()
    
    
    public abstract SearchDataItemsRequest.OrderCase getOrderCase()

**Returns**  
---  
**Type** | **Description**  
`[SearchDataItemsRequest.OrderCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderCase)` |   
  
### getPageSize()
    
    
    public abstract int getPageSize()

Requested page size. Server may return fewer results than requested. Default and maximum page size is 100.

`int32 page_size = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call.

`string page_token = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

A token identifying a page of results for the server to return Typically obtained via SearchDataItemsResponse.next_page_token of the previous DatasetService.SearchDataItems call.

`string page_token = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getSavedQuery() (deprecated)
    
    
    public abstract String getSavedQuery()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.saved_query is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=710_

The resource name of a SavedQuery(annotation set in UI). Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}` All of the search will be done in the context of this SavedQuery.

`string saved_query = 2 [deprecated = true, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The savedQuery.  
  
### getSavedQueryBytes() (deprecated)
    
    
    public abstract ByteString getSavedQueryBytes()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.saved_query is deprecated. See google/cloud/aiplatform/v1beta1/dataset_service.proto;l=710_

The resource name of a SavedQuery(annotation set in UI). Format: `projects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}` All of the search will be done in the context of this SavedQuery.

`string saved_query = 2 [deprecated = true, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for savedQuery.  
  
### hasFieldMask()
    
    
    public abstract boolean hasFieldMask()

Mask specifying which fields of DataItemView to read.

`.google.protobuf.FieldMask field_mask = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fieldMask field is set.  
  
### hasOrderByAnnotation()
    
    
    public abstract boolean hasOrderByAnnotation()

Expression that allows ranking results based on annotation's property.

` .google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotation order_by_annotation = 13; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the orderByAnnotation field is set.  
  
### hasOrderByDataItem()
    
    
    public abstract boolean hasOrderByDataItem()

A comma-separated list of data item fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

`string order_by_data_item = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the orderByDataItem field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
