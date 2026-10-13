---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-CreateExecutionRequest/
title: Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::CreateExecutionRequest (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:18.735267+00:00
---

# Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::CreateExecutionRequest (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-CreateExecutionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workflows Executions V1beta API - Class Google::Cloud::Workflows::Executions::V1beta::CreateExecutionRequest (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.1  0.12.1  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.6 

Reference documentation and code samples for the Workflows Executions V1beta API class Google::Cloud::Workflows::Executions::V1beta::CreateExecutionRequest.

Request for the [CreateExecution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-Executions-Client#Google__Cloud__Workflows__Executions__V1beta__Executions__Client_create_execution_instance_ "Google::Cloud::Workflows::Executions::V1beta::Executions::Client#create_execution \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #execution
    
    
    def execution() -> ::Google::Cloud::Workflows::Executions::V1beta::Execution

**Returns**

  * ([::Google::Cloud::Workflows::Executions::V1beta::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-Execution)) — Required. Execution to be created. 



### #execution=
    
    
    def execution=(value) -> ::Google::Cloud::Workflows::Executions::V1beta::Execution

**Parameter**

  * **value** ([::Google::Cloud::Workflows::Executions::V1beta::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-Execution)) — Required. Execution to be created. 



**Returns**

  * ([::Google::Cloud::Workflows::Executions::V1beta::Execution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-executions-v1beta/latest/Google-Cloud-Workflows-Executions-V1beta-Execution)) — Required. Execution to be created. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Name of the workflow for which an execution should be created. Format: projects/{project}/locations/{location}/workflows/{workflow} The latest revision of the workflow will be used. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the workflow for which an execution should be created. Format: projects/{project}/locations/{location}/workflows/{workflow} The latest revision of the workflow will be used. 



**Returns**

  * (::String) — Required. Name of the workflow for which an execution should be created. Format: projects/{project}/locations/{location}/workflows/{workflow} The latest revision of the workflow will be used. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
