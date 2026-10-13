---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-ConnectionDetail/
title: Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::ConnectionDetail (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:24.797335+00:00
---

# Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::ConnectionDetail (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-ConnectionDetail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1 API - Class Google::Cloud::Redis::Cluster::V1::ConnectionDetail (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.6.0  0.5.0  0.4.2  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1 API class Google::Cloud::Redis::Cluster::V1::ConnectionDetail.

Detailed information of each PSC connection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #psc_auto_connection
    
    
    def psc_auto_connection() -> ::Google::Cloud::Redis::Cluster::V1::PscAutoConnection

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::PscAutoConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscAutoConnection)) — Detailed information of a PSC connection that is created through service connectivity automation.

Note: The following fields are mutually exclusive: `psc_auto_connection`, `psc_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #psc_auto_connection=
    
    
    def psc_auto_connection=(value) -> ::Google::Cloud::Redis::Cluster::V1::PscAutoConnection

**Parameter**

  * **value** ([::Google::Cloud::Redis::Cluster::V1::PscAutoConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscAutoConnection)) — Detailed information of a PSC connection that is created through service connectivity automation.

Note: The following fields are mutually exclusive: `psc_auto_connection`, `psc_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::PscAutoConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscAutoConnection)) — Detailed information of a PSC connection that is created through service connectivity automation.

Note: The following fields are mutually exclusive: `psc_auto_connection`, `psc_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #psc_connection
    
    
    def psc_connection() -> ::Google::Cloud::Redis::Cluster::V1::PscConnection

**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::PscConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscConnection)) — Detailed information of a PSC connection that is created by the customer who owns the cluster.

Note: The following fields are mutually exclusive: `psc_connection`, `psc_auto_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #psc_connection=
    
    
    def psc_connection=(value) -> ::Google::Cloud::Redis::Cluster::V1::PscConnection

**Parameter**

  * **value** ([::Google::Cloud::Redis::Cluster::V1::PscConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscConnection)) — Detailed information of a PSC connection that is created by the customer who owns the cluster.

Note: The following fields are mutually exclusive: `psc_connection`, `psc_auto_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Redis::Cluster::V1::PscConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-cluster-v1/latest/Google-Cloud-Redis-Cluster-V1-PscConnection)) — Detailed information of a PSC connection that is created by the customer who owns the cluster.

Note: The following fields are mutually exclusive: `psc_connection`, `psc_auto_connection`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
