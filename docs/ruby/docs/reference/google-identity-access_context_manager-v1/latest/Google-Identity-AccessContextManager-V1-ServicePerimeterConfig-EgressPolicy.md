---
url: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressPolicy/
title: Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressPolicy (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:58.726379+00:00
---

# Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressPolicy (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressPolicy (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Access Context Manager V1 API class Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressPolicy.

Policy for egress from perimeter.

[EgressPolicies] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] match requests based on `egress_from` and `egress_to` stanzas. For an [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to match, both `egress_from` and `egress_to` stanzas must be matched. If an [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] matches a request, the request is allowed to span the [ServicePerimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] boundary. For example, an [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] can be used to allow VMs on networks within the [ServicePerimeter] [google.identity.accesscontextmanager.v1.ServicePerimeter] to access a defined set of projects outside the perimeter in certain contexts (e.g. to read data from a Cloud Storage bucket or query against a BigQuery dataset).

[EgressPolicies] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] are concerned with the _resources_ that a request relates as well as the API services and API actions being used. They do not related to the direction of data movement. More detailed documentation for this concept can be found in the descriptions of [EgressFrom] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressFrom] and [EgressTo] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressTo].

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #egress_from
    
    
    def egress_from() -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressFrom

**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressFrom](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressFrom)) — Defines conditions on the source of a request causing this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



### #egress_from=
    
    
    def egress_from=(value) -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressFrom

**Parameter**

  * **value** ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressFrom](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressFrom)) — Defines conditions on the source of a request causing this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressFrom](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressFrom)) — Defines conditions on the source of a request causing this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



### #egress_to
    
    
    def egress_to() -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressTo

**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressTo](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressTo)) — Defines the conditions on the [ApiOperation] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation] and destination resources that cause this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



### #egress_to=
    
    
    def egress_to=(value) -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressTo

**Parameter**

  * **value** ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressTo](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressTo)) — Defines the conditions on the [ApiOperation] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation] and destination resources that cause this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig::EgressTo](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig-EgressTo)) — Defines the conditions on the [ApiOperation] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.ApiOperation] and destination resources that cause this [EgressPolicy] [google.identity.accesscontextmanager.v1.ServicePerimeterConfig.EgressPolicy] to apply. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
