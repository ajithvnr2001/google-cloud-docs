---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AIInference/
title: Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::AIInference (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:02.781326+00:00
---

# Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::AIInference (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AIInference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::AIInference (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.2  0.20.2  0.19.0  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.1  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2 

Reference documentation and code samples for the Cloud Pub/Sub V1 API class Google::Cloud::PubSub::V1::AIInference.

Configuration for making inference requests against Vertex AI models.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #endpoint
    
    
    def endpoint() -> ::String

**Returns**

  * (::String) — Required. An endpoint to a Vertex AI model of the form `projects/{project}/locations/{location}/endpoints/{endpoint}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`. Vertex AI API requests will be sent to this endpoint. 



### #endpoint=
    
    
    def endpoint=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. An endpoint to a Vertex AI model of the form `projects/{project}/locations/{location}/endpoints/{endpoint}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`. Vertex AI API requests will be sent to this endpoint. 



**Returns**

  * (::String) — Required. An endpoint to a Vertex AI model of the form `projects/{project}/locations/{location}/endpoints/{endpoint}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`. Vertex AI API requests will be sent to this endpoint. 



### #service_account_email
    
    
    def service_account_email() -> ::String

**Returns**

  * (::String) — Optional. The service account to use to make prediction requests against endpoints. The resource creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used. 



### #service_account_email=
    
    
    def service_account_email=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The service account to use to make prediction requests against endpoints. The resource creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used. 



**Returns**

  * (::String) — Optional. The service account to use to make prediction requests against endpoints. The resource creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub [service agent](https://cloud.google.com/iam/docs/service-agents), service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com, is used. 



### #unstructured_inference
    
    
    def unstructured_inference() -> ::Google::Cloud::PubSub::V1::AIInference::UnstructuredInference

**Returns**

  * ([::Google::Cloud::PubSub::V1::AIInference::UnstructuredInference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AIInference-UnstructuredInference)) — Optional. Requests and responses can be any arbitrary JSON object. 



### #unstructured_inference=
    
    
    def unstructured_inference=(value) -> ::Google::Cloud::PubSub::V1::AIInference::UnstructuredInference

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::AIInference::UnstructuredInference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AIInference-UnstructuredInference)) — Optional. Requests and responses can be any arbitrary JSON object. 



**Returns**

  * ([::Google::Cloud::PubSub::V1::AIInference::UnstructuredInference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AIInference-UnstructuredInference)) — Optional. Requests and responses can be any arbitrary JSON object. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
