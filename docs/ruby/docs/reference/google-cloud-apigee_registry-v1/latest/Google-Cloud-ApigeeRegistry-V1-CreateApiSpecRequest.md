---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiSpecRequest/
title: Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:58.626843+00:00
---

# Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateApiSpecRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Apigee Registry V1 API class Google::Cloud::ApigeeRegistry::V1::CreateApiSpecRequest.

Request message for CreateApiSpec.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_spec
    
    
    def api_spec() -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) — Required. The spec to create. 



### #api_spec=
    
    
    def api_spec=(value) -> ::Google::Cloud::ApigeeRegistry::V1::ApiSpec

**Parameter**

  * **value** ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) — Required. The spec to create. 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::ApiSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ApiSpec)) — Required. The spec to create. 



### #api_spec_id
    
    
    def api_spec_id() -> ::String

**Returns**

  * (::String) — Required. The ID to use for the spec, which will become the final component of the spec's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




### #api_spec_id=
    
    
    def api_spec_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to use for the spec, which will become the final component of the spec's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




**Returns**

  * (::String) — Required. The ID to use for the spec, which will become the final component of the spec's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.

Following AIP-162, IDs must not have the form of a UUID. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`



**Returns**

  * (::String) — Required. The parent, which owns this collection of specs. Format: `projects/*/locations/*/apis/*/versions/*`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
