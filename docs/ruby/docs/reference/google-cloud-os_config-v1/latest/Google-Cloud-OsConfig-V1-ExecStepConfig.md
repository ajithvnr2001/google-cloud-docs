---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-ExecStepConfig/
title: Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::ExecStepConfig (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:07.826132+00:00
---

# Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::ExecStepConfig (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-ExecStepConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::ExecStepConfig (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Cloud OS Config V1 API class Google::Cloud::OsConfig::V1::ExecStepConfig.

Common configurations for an ExecStep.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allowed_success_codes
    
    
    def allowed_success_codes() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — Defaults to [0]. A list of possible return values that the execution can return to indicate a success. 



### #allowed_success_codes=
    
    
    def allowed_success_codes=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — Defaults to [0]. A list of possible return values that the execution can return to indicate a success. 



**Returns**

  * (::Array<::Integer>) — Defaults to [0]. A list of possible return values that the execution can return to indicate a success. 



### #gcs_object
    
    
    def gcs_object() -> ::Google::Cloud::OsConfig::V1::GcsObject

**Returns**

  * ([::Google::Cloud::OsConfig::V1::GcsObject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-GcsObject)) — A Cloud Storage object containing the executable.

Note: The following fields are mutually exclusive: `gcs_object`, `local_path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_object=
    
    
    def gcs_object=(value) -> ::Google::Cloud::OsConfig::V1::GcsObject

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::GcsObject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-GcsObject)) — A Cloud Storage object containing the executable.

Note: The following fields are mutually exclusive: `gcs_object`, `local_path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::GcsObject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-GcsObject)) — A Cloud Storage object containing the executable.

Note: The following fields are mutually exclusive: `gcs_object`, `local_path`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #interpreter
    
    
    def interpreter() -> ::Google::Cloud::OsConfig::V1::ExecStepConfig::Interpreter

**Returns**

  * ([::Google::Cloud::OsConfig::V1::ExecStepConfig::Interpreter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-ExecStepConfig-Interpreter)) — The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)). 



### #interpreter=
    
    
    def interpreter=(value) -> ::Google::Cloud::OsConfig::V1::ExecStepConfig::Interpreter

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::ExecStepConfig::Interpreter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-ExecStepConfig-Interpreter)) — The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)). 



**Returns**

  * ([::Google::Cloud::OsConfig::V1::ExecStepConfig::Interpreter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-ExecStepConfig-Interpreter)) — The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\(Unix\)). 



### #local_path
    
    
    def local_path() -> ::String

**Returns**

  * (::String) — An absolute path to the executable on the VM.

Note: The following fields are mutually exclusive: `local_path`, `gcs_object`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #local_path=
    
    
    def local_path=(value) -> ::String

**Parameter**

  * **value** (::String) — An absolute path to the executable on the VM.

Note: The following fields are mutually exclusive: `local_path`, `gcs_object`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — An absolute path to the executable on the VM.

Note: The following fields are mutually exclusive: `local_path`, `gcs_object`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
