---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationsRequest/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationsRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:07.542823+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationsRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ListEvaluationsRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::ListEvaluationsRequest.

Request message for [EvaluationService.ListEvaluations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluations \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #evaluation_filter
    
    
    def evaluation_filter() -> ::String

**Returns**

  * (::String) — Optional. Filter to be applied on the evaluation when listing the evaluations. See https://google.aip.dev/160 for more details. Supported fields: evaluation_datasets 



### #evaluation_filter=
    
    
    def evaluation_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filter to be applied on the evaluation when listing the evaluations. See https://google.aip.dev/160 for more details. Supported fields: evaluation_datasets 



**Returns**

  * (::String) — Optional. Filter to be applied on the evaluation when listing the evaluations. See https://google.aip.dev/160 for more details. Supported fields: evaluation_datasets 



### #evaluation_run_filter
    
    
    def evaluation_run_filter() -> ::String

**Returns**

  * (::String) — Optional. Filter string for fields on the associated EvaluationRun resources. See https://google.aip.dev/160 for more details. Supported fields: create_time, initiated_by, app_version_display_name 



### #evaluation_run_filter=
    
    
    def evaluation_run_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filter string for fields on the associated EvaluationRun resources. See https://google.aip.dev/160 for more details. Supported fields: create_time, initiated_by, app_version_display_name 



**Returns**

  * (::String) — Optional. Filter string for fields on the associated EvaluationRun resources. See https://google.aip.dev/160 for more details. Supported fields: create_time, initiated_by, app_version_display_name 



### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Deprecated: Use evaluation_filter and evaluation_run_filter instead. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Deprecated: Use evaluation_filter and evaluation_run_filter instead. 



**Returns**

  * (::String) — Optional. Deprecated: Use evaluation_filter and evaluation_run_filter instead. 



### #last_ten_results
    
    
    def last_ten_results() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to include the last 10 evaluation results for each evaluation in the response. 



### #last_ten_results=
    
    
    def last_ten_results=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to include the last 10 evaluation results for each evaluation in the response. 



**Returns**

  * (::Boolean) — Optional. Whether to include the last 10 evaluation results for each evaluation in the response. 



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

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluations \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluations \(method\)") call. 



**Returns**

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ListEvaluationsResponse#Google__Cloud__Ces__V1beta__ListEvaluationsResponse_next_page_token_instance_ "Google::Cloud::Ces::V1beta::ListEvaluationsResponse#next_page_token \(method\)") value returned from a previous list [EvaluationService.ListEvaluations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-EvaluationService-Client#Google__Cloud__Ces__V1beta__EvaluationService__Client_list_evaluations_instance_ "Google::Cloud::Ces::V1beta::EvaluationService::Client#list_evaluations \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the app to list evaluations from. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the app to list evaluations from. 



**Returns**

  * (::String) — Required. The resource name of the app to list evaluations from. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
