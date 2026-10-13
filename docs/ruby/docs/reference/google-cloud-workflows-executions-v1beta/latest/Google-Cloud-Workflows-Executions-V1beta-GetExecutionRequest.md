---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-GetExecutionRequest/
title: Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::GetExecutionRequest (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:23.354871+00:00
---

# Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::GetExecutionRequest (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-GetExecutionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::GetExecutionRequest (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.1  0.12.1  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.6 

Reference documentation and code samples for the Workflows Executions V1beta API class Google::Cloud::Workflows::Executions::V1beta::GetExecutionRequest.

Request for the [GetExecution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-Executions-Client#Google__Cloud__Workflows__Executions__V1beta__Executions__Client_get_execution_instance_ "Google::Cloud::Workflows::Executions::V1beta::Executions::Client#get_execution \(method\)") method.

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

  * (::String) — Required. Name of the execution to be retrieved. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the execution to be retrieved. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} 



**Returns**

  * (::String) — Required. Name of the execution to be retrieved. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} 



### #view
    
    
    def view() -> ::Google::Cloud::Workflows::Executions::V1beta::ExecutionView

**Returns**

  * ([::Google::Cloud::Workflows::Executions::V1beta::ExecutionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-ExecutionView)) — Optional. A view defining which fields should be filled in the returned execution. The API will default to the FULL view. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Workflows::Executions::V1beta::ExecutionView

**Parameter**

  * **value** ([::Google::Cloud::Workflows::Executions::V1beta::ExecutionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-ExecutionView)) — Optional. A view defining which fields should be filled in the returned execution. The API will default to the FULL view. 



**Returns**

  * ([::Google::Cloud::Workflows::Executions::V1beta::ExecutionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-ExecutionView)) — Optional. A view defining which fields should be filled in the returned execution. The API will default to the FULL view. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
