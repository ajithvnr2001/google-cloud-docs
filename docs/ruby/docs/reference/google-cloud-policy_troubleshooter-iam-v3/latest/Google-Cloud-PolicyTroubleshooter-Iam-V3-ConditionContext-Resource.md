---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Resource/
title: Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:31.546955+00:00
---

# Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Policy Troubleshooter V3 API class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource.

Core attributes for a resource. A resource is an addressable (named) entity provided by the destination service. For example, a Compute Engine instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The stable identifier (name) of a resource on the `service`. A resource can be logically identified as `//{resource.service}/{resource.name}`. Unlike the resource URI, the resource name doesn't contain any protocol and version information.

For a list of full resource name formats, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The stable identifier (name) of a resource on the `service`. A resource can be logically identified as `//{resource.service}/{resource.name}`. Unlike the resource URI, the resource name doesn't contain any protocol and version information.

For a list of full resource name formats, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names 




**Returns**

  * (::String) — The stable identifier (name) of a resource on the `service`. A resource can be logically identified as `//{resource.service}/{resource.name}`. Unlike the resource URI, the resource name doesn't contain any protocol and version information.

For a list of full resource name formats, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names 




### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — The name of the service that this resource belongs to, such as `compute.googleapis.com`. The service name might not match the DNS hostname that actually serves the request.

For a full list of resource service values, see https://cloud.google.com/iam/help/conditions/resource-services 




### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the service that this resource belongs to, such as `compute.googleapis.com`. The service name might not match the DNS hostname that actually serves the request.

For a full list of resource service values, see https://cloud.google.com/iam/help/conditions/resource-services 




**Returns**

  * (::String) — The name of the service that this resource belongs to, such as `compute.googleapis.com`. The service name might not match the DNS hostname that actually serves the request.

For a full list of resource service values, see https://cloud.google.com/iam/help/conditions/resource-services 




### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of the resource, in the format `{service}/{kind}`.

For a full list of resource type values, see https://cloud.google.com/iam/help/conditions/resource-types 




### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the resource, in the format `{service}/{kind}`.

For a full list of resource type values, see https://cloud.google.com/iam/help/conditions/resource-types 




**Returns**

  * (::String) — The type of the resource, in the format `{service}/{kind}`.

For a full list of resource type values, see https://cloud.google.com/iam/help/conditions/resource-types 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
