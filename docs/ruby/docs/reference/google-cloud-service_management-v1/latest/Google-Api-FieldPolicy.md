---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_management-v1/latest/Google-Api-FieldPolicy/
title: Service Management V1 API - Class Google::Api::FieldPolicy (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:00.584357+00:00
---

# Service Management V1 API - Class Google::Api::FieldPolicy (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_management-v1/latest/Google-Api-FieldPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Management V1 API - Class Google::Api::FieldPolicy (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.10 

Reference documentation and code samples for the Service Management V1 API class Google::Api::FieldPolicy.

Google API Policy Annotation

This message defines a simple API policy annotation that can be used to annotate API request and response message fields with applicable policies. One field may have multiple applicable policies that must all be satisfied before a request can be processed. This policy annotation is used to generate the overall policy that will be used for automatic runtime policy enforcement and documentation generation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #resource_permission
    
    
    def resource_permission() -> ::String

**Returns**

  * (::String) — Specifies the required permission(s) for the resource referred to by the field. It requires the field contains a valid resource reference, and the request must pass the permission checks to proceed. For example, "resourcemanager.projects.get". 



### #resource_permission=
    
    
    def resource_permission=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the required permission(s) for the resource referred to by the field. It requires the field contains a valid resource reference, and the request must pass the permission checks to proceed. For example, "resourcemanager.projects.get". 



**Returns**

  * (::String) — Specifies the required permission(s) for the resource referred to by the field. It requires the field contains a valid resource reference, and the request must pass the permission checks to proceed. For example, "resourcemanager.projects.get". 



### #resource_type
    
    
    def resource_type() -> ::String

**Returns**

  * (::String) — Specifies the resource type for the resource referred to by the field. 



### #resource_type=
    
    
    def resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the resource type for the resource referred to by the field. 



**Returns**

  * (::String) — Specifies the resource type for the resource referred to by the field. 



### #selector
    
    
    def selector() -> ::String

**Returns**

  * (::String) — Selects one or more request or response message fields to apply this `FieldPolicy`.

When a `FieldPolicy` is used in proto annotation, the selector must be left as empty. The service config generator will automatically fill the correct value.

When a `FieldPolicy` is used in service config, the selector must be a comma-separated string with valid request or response field paths, such as "foo.bar" or "foo.bar,foo.baz". 




### #selector=
    
    
    def selector=(value) -> ::String

**Parameter**

  * **value** (::String) — Selects one or more request or response message fields to apply this `FieldPolicy`.

When a `FieldPolicy` is used in proto annotation, the selector must be left as empty. The service config generator will automatically fill the correct value.

When a `FieldPolicy` is used in service config, the selector must be a comma-separated string with valid request or response field paths, such as "foo.bar" or "foo.bar,foo.baz". 




**Returns**

  * (::String) — Selects one or more request or response message fields to apply this `FieldPolicy`.

When a `FieldPolicy` is used in proto annotation, the selector must be left as empty. The service config generator will automatically fill the correct value.

When a `FieldPolicy` is used in service config, the selector must be a comma-separated string with valid request or response field paths, such as "foo.bar" or "foo.bar,foo.baz". 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
