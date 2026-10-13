---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingConfigProto/
title: Kubernetes Engine V1beta1 API - Class Google::Api::BatchingConfigProto (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:44.580770+00:00
---

# Kubernetes Engine V1beta1 API - Class Google::Api::BatchingConfigProto (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingConfigProto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Class Google::Api::BatchingConfigProto (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API class Google::Api::BatchingConfigProto.

`BatchingConfigProto` defines the batching configuration for an API method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #batch_descriptor
    
    
    def batch_descriptor() -> ::Google::Api::BatchingDescriptorProto

**Returns**

  * ([::Google::Api::BatchingDescriptorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingDescriptorProto)) — The request and response fields used in batching. 



### #batch_descriptor=
    
    
    def batch_descriptor=(value) -> ::Google::Api::BatchingDescriptorProto

**Parameter**

  * **value** ([::Google::Api::BatchingDescriptorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingDescriptorProto)) — The request and response fields used in batching. 



**Returns**

  * ([::Google::Api::BatchingDescriptorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingDescriptorProto)) — The request and response fields used in batching. 



### #thresholds
    
    
    def thresholds() -> ::Google::Api::BatchingSettingsProto

**Returns**

  * ([::Google::Api::BatchingSettingsProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingSettingsProto)) — The thresholds which trigger a batched request to be sent. 



### #thresholds=
    
    
    def thresholds=(value) -> ::Google::Api::BatchingSettingsProto

**Parameter**

  * **value** ([::Google::Api::BatchingSettingsProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingSettingsProto)) — The thresholds which trigger a batched request to be sent. 



**Returns**

  * ([::Google::Api::BatchingSettingsProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Api-BatchingSettingsProto)) — The thresholds which trigger a batched request to be sent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
