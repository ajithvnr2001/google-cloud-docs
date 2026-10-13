---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config/
title: Cloud Build V1 API - Class Google::Cloud::Build::V1::PrivatePoolV1Config (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:07.654360+00:00
---

# Cloud Build V1 API - Class Google::Cloud::Build::V1::PrivatePoolV1Config (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Build V1 API - Class Google::Cloud::Build::V1::PrivatePoolV1Config (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.27.1  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Cloud Build V1 API class Google::Cloud::Build::V1::PrivatePoolV1Config.

Configuration for a V1 `PrivatePool`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #network_config
    
    
    def network_config() -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::NetworkConfig

**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-NetworkConfig)) — Network configuration for the pool. 



### #network_config=
    
    
    def network_config=(value) -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::NetworkConfig

**Parameter**

  * **value** ([::Google::Cloud::Build::V1::PrivatePoolV1Config::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-NetworkConfig)) — Network configuration for the pool. 



**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-NetworkConfig)) — Network configuration for the pool. 



### #private_service_connect
    
    
    def private_service_connect() -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::PrivateServiceConnect

**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::PrivateServiceConnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-PrivateServiceConnect)) — Immutable. Private Service Connect(PSC) Network configuration for the pool. 



### #private_service_connect=
    
    
    def private_service_connect=(value) -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::PrivateServiceConnect

**Parameter**

  * **value** ([::Google::Cloud::Build::V1::PrivatePoolV1Config::PrivateServiceConnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-PrivateServiceConnect)) — Immutable. Private Service Connect(PSC) Network configuration for the pool. 



**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::PrivateServiceConnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-PrivateServiceConnect)) — Immutable. Private Service Connect(PSC) Network configuration for the pool. 



### #worker_config
    
    
    def worker_config() -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::WorkerConfig

**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::WorkerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-WorkerConfig)) — Machine configuration for the workers in the pool. 



### #worker_config=
    
    
    def worker_config=(value) -> ::Google::Cloud::Build::V1::PrivatePoolV1Config::WorkerConfig

**Parameter**

  * **value** ([::Google::Cloud::Build::V1::PrivatePoolV1Config::WorkerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-WorkerConfig)) — Machine configuration for the workers in the pool. 



**Returns**

  * ([::Google::Cloud::Build::V1::PrivatePoolV1Config::WorkerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-PrivatePoolV1Config-WorkerConfig)) — Machine configuration for the workers in the pool. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
