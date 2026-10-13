---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1beta1/latest/Google-Cloud-Dataform-V1beta1-CreateWorkflowInvocationRequest/
title: Dataform V1beta1 API - Class Google::Cloud::Dataform::V1beta1::CreateWorkflowInvocationRequest (v1.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:49.783355+00:00
---

# Dataform V1beta1 API - Class Google::Cloud::Dataform::V1beta1::CreateWorkflowInvocationRequest (v1.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1beta1/latest/Google-Cloud-Dataform-V1beta1-CreateWorkflowInvocationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1beta1 API - Class Google::Cloud::Dataform::V1beta1::CreateWorkflowInvocationRequest (v1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Dataform V1beta1 API class Google::Cloud::Dataform::V1beta1::CreateWorkflowInvocationRequest.

`CreateWorkflowInvocation` request message.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The repository in which to create the workflow invocation. Must be in the format `projects/*/locations/*/repositories/*`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The repository in which to create the workflow invocation. Must be in the format `projects/*/locations/*/repositories/*`. 



**Returns**

  * (::String) — Required. The repository in which to create the workflow invocation. Must be in the format `projects/*/locations/*/repositories/*`. 



### #workflow_invocation
    
    
    def workflow_invocation() -> ::Google::Cloud::Dataform::V1beta1::WorkflowInvocation

**Returns**

  * ([::Google::Cloud::Dataform::V1beta1::WorkflowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1beta1/latest/Google-Cloud-Dataform-V1beta1-WorkflowInvocation)) — Required. The workflow invocation resource to create. 



### #workflow_invocation=
    
    
    def workflow_invocation=(value) -> ::Google::Cloud::Dataform::V1beta1::WorkflowInvocation

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1beta1::WorkflowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1beta1/latest/Google-Cloud-Dataform-V1beta1-WorkflowInvocation)) — Required. The workflow invocation resource to create. 



**Returns**

  * ([::Google::Cloud::Dataform::V1beta1::WorkflowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1beta1/latest/Google-Cloud-Dataform-V1beta1-WorkflowInvocation)) — Required. The workflow invocation resource to create. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
