---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ReasoningEngineSpec-DeploymentSpec/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ReasoningEngineSpec::DeploymentSpec (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:02.736217+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ReasoningEngineSpec::DeploymentSpec (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ReasoningEngineSpec-DeploymentSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ReasoningEngineSpec::DeploymentSpec (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::ReasoningEngineSpec::DeploymentSpec.

The specification of a Reasoning Engine deployment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #container_concurrency
    
    
    def container_concurrency() -> ::Integer

**Returns**

  * (::Integer) — Optional. Concurrency for each container and agent server. Recommended value: 2 * cpu + 1. Defaults to 9. 



### #container_concurrency=
    
    
    def container_concurrency=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Concurrency for each container and agent server. Recommended value: 2 * cpu + 1. Defaults to 9. 



**Returns**

  * (::Integer) — Optional. Concurrency for each container and agent server. Recommended value: 2 * cpu + 1. Defaults to 9. 



### #env
    
    
    def env() -> ::Array<::Google::Cloud::AIPlatform::V1::EnvVar>

**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::EnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EnvVar)>) — Optional. Environment variables to be set with the Reasoning Engine deployment. The environment variables can be updated through the UpdateReasoningEngine API. 



### #env=
    
    
    def env=(value) -> ::Array<::Google::Cloud::AIPlatform::V1::EnvVar>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AIPlatform::V1::EnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EnvVar)>) — Optional. Environment variables to be set with the Reasoning Engine deployment. The environment variables can be updated through the UpdateReasoningEngine API. 



**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::EnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EnvVar)>) — Optional. Environment variables to be set with the Reasoning Engine deployment. The environment variables can be updated through the UpdateReasoningEngine API. 



### #max_instances
    
    
    def max_instances() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of application instances that can be launched to handle increased traffic. Defaults to 100. Range: [1, 1000].

If VPC-SC or PSC-I is enabled, the acceptable range is [1, 100]. 




### #max_instances=
    
    
    def max_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of application instances that can be launched to handle increased traffic. Defaults to 100. Range: [1, 1000].

If VPC-SC or PSC-I is enabled, the acceptable range is [1, 100]. 




**Returns**

  * (::Integer) — Optional. The maximum number of application instances that can be launched to handle increased traffic. Defaults to 100. Range: [1, 1000].

If VPC-SC or PSC-I is enabled, the acceptable range is [1, 100]. 




### #min_instances
    
    
    def min_instances() -> ::Integer

**Returns**

  * (::Integer) — Optional. The minimum number of application instances that will be kept running at all times. Defaults to 1. Range: [0, 10]. 



### #min_instances=
    
    
    def min_instances=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The minimum number of application instances that will be kept running at all times. Defaults to 1. Range: [0, 10]. 



**Returns**

  * (::Integer) — Optional. The minimum number of application instances that will be kept running at all times. Defaults to 1. Range: [0, 10]. 



### #psc_interface_config
    
    
    def psc_interface_config() -> ::Google::Cloud::AIPlatform::V1::PscInterfaceConfig

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PscInterfaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PscInterfaceConfig)) — Optional. Configuration for PSC-I. 



### #psc_interface_config=
    
    
    def psc_interface_config=(value) -> ::Google::Cloud::AIPlatform::V1::PscInterfaceConfig

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::PscInterfaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PscInterfaceConfig)) — Optional. Configuration for PSC-I. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PscInterfaceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PscInterfaceConfig)) — Optional. Configuration for PSC-I. 



### #resource_limits
    
    
    def resource_limits() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Optional. Resource limits for each container. Only 'cpu' and 'memory' keys are supported. Defaults to {"cpu": "4", "memory": "4Gi"}.

    * The only supported values for CPU are '1', '2', '4', '6' and '8'. For more information, go to https://cloud.google.com/run/docs/configuring/cpu.
    * The only supported values for memory are '1Gi', '2Gi', ... '32 Gi'.
    * For required cpu on different memory values, go to https://cloud.google.com/run/docs/configuring/memory-limits



### #resource_limits=
    
    
    def resource_limits=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — 

Optional. Resource limits for each container. Only 'cpu' and 'memory' keys are supported. Defaults to {"cpu": "4", "memory": "4Gi"}.

    * The only supported values for CPU are '1', '2', '4', '6' and '8'. For more information, go to https://cloud.google.com/run/docs/configuring/cpu.
    * The only supported values for memory are '1Gi', '2Gi', ... '32 Gi'.
    * For required cpu on different memory values, go to https://cloud.google.com/run/docs/configuring/memory-limits



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — 

Optional. Resource limits for each container. Only 'cpu' and 'memory' keys are supported. Defaults to {"cpu": "4", "memory": "4Gi"}.

    * The only supported values for CPU are '1', '2', '4', '6' and '8'. For more information, go to https://cloud.google.com/run/docs/configuring/cpu.
    * The only supported values for memory are '1Gi', '2Gi', ... '32 Gi'.
    * For required cpu on different memory values, go to https://cloud.google.com/run/docs/configuring/memory-limits



### #secret_env
    
    
    def secret_env() -> ::Array<::Google::Cloud::AIPlatform::V1::SecretEnvVar>

**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::SecretEnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SecretEnvVar)>) — Optional. Environment variables where the value is a secret in Cloud Secret Manager. To use this feature, add 'Secret Manager Secret Accessor' role (roles/secretmanager.secretAccessor) to AI Platform Reasoning Engine Service Agent. 



### #secret_env=
    
    
    def secret_env=(value) -> ::Array<::Google::Cloud::AIPlatform::V1::SecretEnvVar>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AIPlatform::V1::SecretEnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SecretEnvVar)>) — Optional. Environment variables where the value is a secret in Cloud Secret Manager. To use this feature, add 'Secret Manager Secret Accessor' role (roles/secretmanager.secretAccessor) to AI Platform Reasoning Engine Service Agent. 



**Returns**

  * (::Array<[::Google::Cloud::AIPlatform::V1::SecretEnvVar](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SecretEnvVar)>) — Optional. Environment variables where the value is a secret in Cloud Secret Manager. To use this feature, add 'Secret Manager Secret Accessor' role (roles/secretmanager.secretAccessor) to AI Platform Reasoning Engine Service Agent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
