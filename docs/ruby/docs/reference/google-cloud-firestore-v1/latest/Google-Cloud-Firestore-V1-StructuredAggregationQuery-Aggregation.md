---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation/
title: Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation (v2.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:44.603082+00:00
---

# Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation (v2.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation (v2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.1  2.1.1  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.8 

Reference documentation and code samples for the Cloud Firestore V1 API class Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation.

Defines an aggregation that produces a single result.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alias
    
    
    def alias() -> ::String

**Returns**

  * (::String) — 

Optional. Optional name of the field to store the result of the aggregation into.

If not provided, Firestore will pick a default name following the format `field_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [document field name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") limitations.



### #alias=
    
    
    def alias=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Optional name of the field to store the result of the aggregation into.

If not provided, Firestore will pick a default name following the format `field_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [document field name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") limitations.



**Returns**

  * (::String) — 

Optional. Optional name of the field to store the result of the aggregation into.

If not provided, Firestore will pick a default name following the format `field_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [document field name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") limitations.



### #avg
    
    
    def avg() -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Avg

**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #avg=
    
    
    def avg=(value) -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Avg

**Parameter**

  * **value** ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #count
    
    
    def count() -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Count

**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #count=
    
    
    def count=(value) -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Count

**Parameter**

  * **value** ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sum
    
    
    def sum() -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Sum

**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sum=
    
    
    def sum=(value) -> ::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Sum

**Parameter**

  * **value** ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Firestore::V1::StructuredAggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-StructuredAggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
