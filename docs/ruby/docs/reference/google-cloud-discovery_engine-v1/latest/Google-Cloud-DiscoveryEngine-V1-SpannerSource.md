---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SpannerSource/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SpannerSource (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:37.313613+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SpannerSource (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SpannerSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SpannerSource (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::SpannerSource.

The Spanner source for importing data

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database_id
    
    
    def database_id() -> ::String

**Returns**

  * (::String) — Required. The database ID of the source Spanner table. 



### #database_id=
    
    
    def database_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The database ID of the source Spanner table. 



**Returns**

  * (::String) — Required. The database ID of the source Spanner table. 



### #enable_data_boost
    
    
    def enable_data_boost() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to apply data boost on Spanner export. Enabling this option will incur additional cost. More info can be found [here](https://cloud.google.com/spanner/docs/databoost/databoost-overview#billing_and_quotas). 



### #enable_data_boost=
    
    
    def enable_data_boost=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to apply data boost on Spanner export. Enabling this option will incur additional cost. More info can be found [here](https://cloud.google.com/spanner/docs/databoost/databoost-overview#billing_and_quotas). 



**Returns**

  * (::Boolean) — Whether to apply data boost on Spanner export. Enabling this option will incur additional cost. More info can be found [here](https://cloud.google.com/spanner/docs/databoost/databoost-overview#billing_and_quotas). 



### #instance_id
    
    
    def instance_id() -> ::String

**Returns**

  * (::String) — Required. The instance ID of the source Spanner table. 



### #instance_id=
    
    
    def instance_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The instance ID of the source Spanner table. 



**Returns**

  * (::String) — Required. The instance ID of the source Spanner table. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — The project ID that contains the Spanner source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request. 



### #project_id=
    
    
    def project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The project ID that contains the Spanner source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request. 



**Returns**

  * (::String) — The project ID that contains the Spanner source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request. 



### #table_id
    
    
    def table_id() -> ::String

**Returns**

  * (::String) — Required. The table name of the Spanner database that needs to be imported. 



### #table_id=
    
    
    def table_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The table name of the Spanner database that needs to be imported. 



**Returns**

  * (::String) — Required. The table name of the Spanner database that needs to be imported. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
