---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequestOrBuilder
title: Interface SearchLineageStreamingRequestOrBuilder (0.91.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:38.578859+00:00
---

# Interface SearchLineageStreamingRequestOrBuilder (0.91.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchLineageStreamingRequestOrBuilder (0.91.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.91.0 (latest)  0.87.0  0.86.0  0.85.0  0.83.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface SearchLineageStreamingRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDirection()
    
    
    public abstract SearchLineageStreamingRequest.SearchDirection getDirection()

Required. Direction of the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchDirection direction = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.SearchDirection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchDirection)` | The direction.  
  
### getDirectionValue()
    
    
    public abstract int getDirectionValue()

Required. Direction of the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchDirection direction = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for direction.  
  
### getFilters()
    
    
    public abstract SearchLineageStreamingRequest.SearchFilters getFilters()

Optional. Filters for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchFilters filters = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.SearchFilters](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchFilters)` | The filters.  
  
### getFiltersOrBuilder()
    
    
    public abstract SearchLineageStreamingRequest.SearchFiltersOrBuilder getFiltersOrBuilder()

Optional. Filters for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchFilters filters = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.SearchFiltersOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchFiltersOrBuilder)` |   
  
### getLimits()
    
    
    public abstract SearchLineageStreamingRequest.SearchLimits getLimits()

Optional. Limits for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchLimits limits = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.SearchLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchLimits)` | The limits.  
  
### getLimitsOrBuilder()
    
    
    public abstract SearchLineageStreamingRequest.SearchLimitsOrBuilder getLimitsOrBuilder()

Optional. Limits for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchLimits limits = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.SearchLimitsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchLimitsOrBuilder)` |   
  
### getLocations(int index)
    
    
    public abstract String getLocations(int index)

Required. The locations to search in.

`repeated string locations = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The locations at the given index.  
  
### getLocationsBytes(int index)
    
    
    public abstract ByteString getLocationsBytes(int index)

Required. The locations to search in.

`repeated string locations = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the locations at the given index.  
  
### getLocationsCount()
    
    
    public abstract int getLocationsCount()

Required. The locations to search in.

`repeated string locations = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of locations.  
  
### getLocationsList()
    
    
    public abstract List<String> getLocationsList()

Required. The locations to search in.

`repeated string locations = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the locations.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The project and location to initiate the search from.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The project and location to initiate the search from.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRootCriteria()
    
    
    public abstract SearchLineageStreamingRequest.RootCriteria getRootCriteria()

Required. Criteria for the root of the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.RootCriteria root_criteria = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.RootCriteria](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.RootCriteria)` | The rootCriteria.  
  
### getRootCriteriaOrBuilder()
    
    
    public abstract SearchLineageStreamingRequest.RootCriteriaOrBuilder getRootCriteriaOrBuilder()

Required. Criteria for the root of the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.RootCriteria root_criteria = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest.RootCriteriaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.RootCriteriaOrBuilder)` |   
  
### hasFilters()
    
    
    public abstract boolean hasFilters()

Optional. Filters for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchFilters filters = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filters field is set.  
  
### hasLimits()
    
    
    public abstract boolean hasLimits()

Optional. Limits for the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.SearchLimits limits = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the limits field is set.  
  
### hasRootCriteria()
    
    
    public abstract boolean hasRootCriteria()

Required. Criteria for the root of the search.

` .google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.RootCriteria root_criteria = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rootCriteria field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
