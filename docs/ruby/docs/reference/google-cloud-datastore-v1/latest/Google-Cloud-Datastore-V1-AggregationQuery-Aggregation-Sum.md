---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Sum/
title: Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:19.244129+00:00
---

# Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AggregationQuery-Aggregation-Sum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Firestore in Datastore mode V1 API class Google::Cloud::Datastore::V1::AggregationQuery::Aggregation::Sum.

Sum of the values of the requested property.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns 0.

  * Returns a 64-bit integer if all aggregated numbers are integers and the sum result does not overflow. Otherwise, the result is returned as a double. Note that even if all the aggregated values are integers, the result is returned as a double if it cannot fit within a 64-bit signed integer. When this occurs, the returned value will lose precision.

  * When underflow occurs, floating-point aggregation is non-deterministic. This means that running the same query repeatedly without any changes to the underlying values could produce slightly different results each time. In those cases, values should be stored as integers over floating-point numbers.




## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #property
    
    
    def property() -> ::Google::Cloud::Datastore::V1::PropertyReference

**Returns**

  * ([::Google::Cloud::Datastore::V1::PropertyReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-PropertyReference)) — The property to aggregate on. 



### #property=
    
    
    def property=(value) -> ::Google::Cloud::Datastore::V1::PropertyReference

**Parameter**

  * **value** ([::Google::Cloud::Datastore::V1::PropertyReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-PropertyReference)) — The property to aggregate on. 



**Returns**

  * ([::Google::Cloud::Datastore::V1::PropertyReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-PropertyReference)) — The property to aggregate on. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
