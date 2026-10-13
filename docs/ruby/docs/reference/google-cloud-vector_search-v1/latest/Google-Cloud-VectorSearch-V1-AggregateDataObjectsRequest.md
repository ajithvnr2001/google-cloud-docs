---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-AggregateDataObjectsRequest/
title: Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::AggregateDataObjectsRequest (v0.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:54.768291+00:00
---

# Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::AggregateDataObjectsRequest (v0.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-AggregateDataObjectsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::AggregateDataObjectsRequest (v0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.1 

Reference documentation and code samples for the Vector Search V1 API class Google::Cloud::VectorSearch::V1::AggregateDataObjectsRequest.

Request message for [DataObjectSearchService.AggregateDataObjects](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-DataObjectSearchService-Client#Google__Cloud__VectorSearch__V1__DataObjectSearchService__Client_aggregate_data_objects_instance_ "Google::Cloud::VectorSearch::V1::DataObjectSearchService::Client#aggregate_data_objects \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #aggregate
    
    
    def aggregate() -> ::Google::Cloud::VectorSearch::V1::AggregationMethod

**Returns**

  * ([::Google::Cloud::VectorSearch::V1::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-AggregationMethod)) — Required. The aggregation method to apply to the query. 



### #aggregate=
    
    
    def aggregate=(value) -> ::Google::Cloud::VectorSearch::V1::AggregationMethod

**Parameter**

  * **value** ([::Google::Cloud::VectorSearch::V1::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-AggregationMethod)) — Required. The aggregation method to apply to the query. 



**Returns**

  * ([::Google::Cloud::VectorSearch::V1::AggregationMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-AggregationMethod)) — Required. The aggregation method to apply to the query. 



### #filter
    
    
    def filter() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Protobuf-Struct)) — Optional. A JSON filter expression, e.g. {"genre": \\{"$eq": "sci-fi"}}, represented as a google.protobuf.Struct. 



### #filter=
    
    
    def filter=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Protobuf-Struct)) — Optional. A JSON filter expression, e.g. {"genre": \\{"$eq": "sci-fi"}}, represented as a google.protobuf.Struct. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Protobuf-Struct)) — Optional. A JSON filter expression, e.g. {"genre": \\{"$eq": "sci-fi"}}, represented as a google.protobuf.Struct. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Collection for which to query. Format: `projects/{project}/locations/{location}/collections/{collection}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Collection for which to query. Format: `projects/{project}/locations/{location}/collections/{collection}`



**Returns**

  * (::String) — Required. The resource name of the Collection for which to query. Format: `projects/{project}/locations/{location}/collections/{collection}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
