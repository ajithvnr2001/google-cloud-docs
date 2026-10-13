---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMappingRuleRequest/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:23.291059+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMappingRuleRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest.

Request message for 'CreateMappingRule' command.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mapping_rule
    
    
    def mapping_rule() -> ::Google::Cloud::CloudDMS::V1::MappingRule

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) — Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object. 



### #mapping_rule=
    
    
    def mapping_rule=(value) -> ::Google::Cloud::CloudDMS::V1::MappingRule

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) — Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) — Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object. 



### #mapping_rule_id
    
    
    def mapping_rule_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the rule to create. 



### #mapping_rule_id=
    
    
    def mapping_rule_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the rule to create. 



**Returns**

  * (::String) — Required. The ID of the rule to create. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent which owns this collection of mapping rules. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent which owns this collection of mapping rules. 



**Returns**

  * (::String) — Required. The parent which owns this collection of mapping rules. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Returns**

  * (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
