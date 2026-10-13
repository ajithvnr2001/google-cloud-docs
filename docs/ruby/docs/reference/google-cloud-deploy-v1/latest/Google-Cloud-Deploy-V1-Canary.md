---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Canary/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Canary (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:20.993860+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Canary (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Canary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Canary (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::Canary.

Canary represents the canary deployment strategy.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #canary_deployment
    
    
    def canary_deployment() -> ::Google::Cloud::Deploy::V1::CanaryDeployment

**Returns**

  * ([::Google::Cloud::Deploy::V1::CanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CanaryDeployment)) — Optional. Configures the progressive based deployment for a Target.

Note: The following fields are mutually exclusive: `canary_deployment`, `custom_canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #canary_deployment=
    
    
    def canary_deployment=(value) -> ::Google::Cloud::Deploy::V1::CanaryDeployment

**Parameter**

  * **value** ([::Google::Cloud::Deploy::V1::CanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CanaryDeployment)) — Optional. Configures the progressive based deployment for a Target.

Note: The following fields are mutually exclusive: `canary_deployment`, `custom_canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Deploy::V1::CanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CanaryDeployment)) — Optional. Configures the progressive based deployment for a Target.

Note: The following fields are mutually exclusive: `canary_deployment`, `custom_canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_canary_deployment
    
    
    def custom_canary_deployment() -> ::Google::Cloud::Deploy::V1::CustomCanaryDeployment

**Returns**

  * ([::Google::Cloud::Deploy::V1::CustomCanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CustomCanaryDeployment)) — Optional. Configures the progressive based deployment for a Target, but allows customizing at the phase level where a phase represents each of the percentage deployments.

Note: The following fields are mutually exclusive: `custom_canary_deployment`, `canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_canary_deployment=
    
    
    def custom_canary_deployment=(value) -> ::Google::Cloud::Deploy::V1::CustomCanaryDeployment

**Parameter**

  * **value** ([::Google::Cloud::Deploy::V1::CustomCanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CustomCanaryDeployment)) — Optional. Configures the progressive based deployment for a Target, but allows customizing at the phase level where a phase represents each of the percentage deployments.

Note: The following fields are mutually exclusive: `custom_canary_deployment`, `canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Deploy::V1::CustomCanaryDeployment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-CustomCanaryDeployment)) — Optional. Configures the progressive based deployment for a Target, but allows customizing at the phase level where a phase represents each of the percentage deployments.

Note: The following fields are mutually exclusive: `custom_canary_deployment`, `canary_deployment`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #runtime_config
    
    
    def runtime_config() -> ::Google::Cloud::Deploy::V1::RuntimeConfig

**Returns**

  * ([::Google::Cloud::Deploy::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-RuntimeConfig)) — Optional. Runtime specific configurations for the deployment strategy. The runtime configuration is used to determine how Cloud Deploy will split traffic to enable a progressive deployment. 



### #runtime_config=
    
    
    def runtime_config=(value) -> ::Google::Cloud::Deploy::V1::RuntimeConfig

**Parameter**

  * **value** ([::Google::Cloud::Deploy::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-RuntimeConfig)) — Optional. Runtime specific configurations for the deployment strategy. The runtime configuration is used to determine how Cloud Deploy will split traffic to enable a progressive deployment. 



**Returns**

  * ([::Google::Cloud::Deploy::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-RuntimeConfig)) — Optional. Runtime specific configurations for the deployment strategy. The runtime configuration is used to determine how Cloud Deploy will split traffic to enable a progressive deployment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
