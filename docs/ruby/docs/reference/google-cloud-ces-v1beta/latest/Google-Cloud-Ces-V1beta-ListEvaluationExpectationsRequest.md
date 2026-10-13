---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationExpectationsRequest/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationExpectationsRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:43.979993+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationExpectationsRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationExpectationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationExpectationsRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::ListEvaluationExpectationsRequest.

Request message for [EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluation_expectations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluation_expectations \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Filter to be applied when listing the evaluation expectations. See https://google.aip.dev/160 for more details. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filter to be applied when listing the evaluation expectations. See https://google.aip.dev/160 for more details. 



**Returns**

  * (::String) — Optional. Filter to be applied when listing the evaluation expectations. See https://google.aip.dev/160 for more details. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See https://google.aip.dev/132#ordering for more details. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See https://google.aip.dev/132#ordering for more details. 



**Returns**

  * (::String) — Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See https://google.aip.dev/132#ordering for more details. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationExpectationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationExpectationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationExpectationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluation_expectations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluation_expectations \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationExpectationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationExpectationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationExpectationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluation_expectations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluation_expectations \(method\)") call. 



**Returns**

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationExpectationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationExpectationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationExpectationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluation_expectations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluation_expectations \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the app to list evaluation expectations from. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the app to list evaluation expectations from. 



**Returns**

  * (::String) — Required. The resource name of the app to list evaluation expectations from. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
