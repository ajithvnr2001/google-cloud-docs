---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation/
title: Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:11.228985+00:00
---

# Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Firestore in Datastore mode V1 API class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation.

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

Optional. Optional name of the property to store the result of the aggregation.

If not provided, Datastore will pick a default name following the format `property_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS property_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS property_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [entity property name][google.datastore.v1.Entity.properties] limitations.



### #alias=
    
    
    def alias=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Optional name of the property to store the result of the aggregation.

If not provided, Datastore will pick a default name following the format `property_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS property_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS property_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [entity property name][google.datastore.v1.Entity.properties] limitations.



**Returns**

  * (::String) — 

Optional. Optional name of the property to store the result of the aggregation.

If not provided, Datastore will pick a default name following the format `property_<incremental_id++>`. For example:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); `

becomes:

` AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS property_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS property_2 OVER ( ... ); `

Requires:

    * Must be unique across all aggregation aliases.
    * Conform to [entity property name][google.datastore.v1.Entity.properties] limitations.



### #avg
    
    
    def avg() -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Avg

**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #avg=
    
    
    def avg=(value) -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Avg

**Parameter**

  * **value** ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Avg](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Avg)) — Average aggregator.

Note: The following fields are mutually exclusive: `avg`, `count`, `sum`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #count
    
    
    def count() -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Count

**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #count=
    
    
    def count=(value) -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Count

**Parameter**

  * **value** ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Count](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Count)) — Count aggregator.

Note: The following fields are mutually exclusive: `count`, `sum`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sum
    
    
    def sum() -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum

**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sum=
    
    
    def sum=(value) -> ::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum

**Parameter**

  * **value** ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Sum)) — Sum aggregator.

Note: The following fields are mutually exclusive: `sum`, `count`, `avg`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
