---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BigtableOptions/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::BigtableOptions (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:43.959491+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::BigtableOptions (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BigtableOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::BigtableOptions (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::BigtableOptions.

The Bigtable Options object that contains information to support the import.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #families
    
    
    def families() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::DiscoveryEngine::V1::BigtableOptions::BigtableColumnFamily}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::DiscoveryEngine::V1::BigtableOptions::BigtableColumnFamily}) — The mapping from family names to an object that contains column families level information for the given column family. If a family is not present in this map it will be ignored. 



### #families=
    
    
    def families=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::DiscoveryEngine::V1::BigtableOptions::BigtableColumnFamily}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::DiscoveryEngine::V1::BigtableOptions::BigtableColumnFamily}) — The mapping from family names to an object that contains column families level information for the given column family. If a family is not present in this map it will be ignored. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::DiscoveryEngine::V1::BigtableOptions::BigtableColumnFamily}) — The mapping from family names to an object that contains column families level information for the given column family. If a family is not present in this map it will be ignored. 



### #key_field_name
    
    
    def key_field_name() -> ::String

**Returns**

  * (::String) — The field name used for saving row key value in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. 



### #key_field_name=
    
    
    def key_field_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The field name used for saving row key value in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. 



**Returns**

  * (::String) — The field name used for saving row key value in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
