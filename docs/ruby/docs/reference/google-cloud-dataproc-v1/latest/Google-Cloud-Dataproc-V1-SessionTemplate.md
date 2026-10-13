---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplate (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:53.298120+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplate (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplate (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::SessionTemplate.

A representation of a session template.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the template was created. 



### #creator
    
    
    def creator() -> ::String

**Returns**

  * (::String) — Output only. The email address of the user who created the template. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Brief description of the template. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Brief description of the template. 



**Returns**

  * (::String) — Optional. Brief description of the template. 



### #environment_config
    
    
    def environment_config() -> ::Google::Cloud::Dataproc::V1::EnvironmentConfig

**Returns**

  * ([::Google::Cloud::Dataproc::V1::EnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-EnvironmentConfig)) — Optional. Environment configuration for session execution. 



### #environment_config=
    
    
    def environment_config=(value) -> ::Google::Cloud::Dataproc::V1::EnvironmentConfig

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::EnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-EnvironmentConfig)) — Optional. Environment configuration for session execution. 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::EnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-EnvironmentConfig)) — Optional. Environment configuration for session execution. 



### #jupyter_session
    
    
    def jupyter_session() -> ::Google::Cloud::Dataproc::V1::JupyterConfig

**Returns**

  * ([::Google::Cloud::Dataproc::V1::JupyterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-JupyterConfig)) — Optional. Jupyter session config.

Note: The following fields are mutually exclusive: `jupyter_session`, `spark_connect_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #jupyter_session=
    
    
    def jupyter_session=(value) -> ::Google::Cloud::Dataproc::V1::JupyterConfig

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::JupyterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-JupyterConfig)) — Optional. Jupyter session config.

Note: The following fields are mutually exclusive: `jupyter_session`, `spark_connect_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataproc::V1::JupyterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-JupyterConfig)) — Optional. Jupyter session config.

Note: The following fields are mutually exclusive: `jupyter_session`, `spark_connect_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to associate with sessions created using this template. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** can be empty, but, if present, must contain 1 to 63 characters and conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to associate with sessions created using this template. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** can be empty, but, if present, must contain 1 to 63 characters and conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to associate with sessions created using this template. Label **keys** must contain 1 to 63 characters, and must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). Label **values** can be empty, but, if present, must contain 1 to 63 characters and conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Identifier. The resource name of the session template. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Identifier. The resource name of the session template. 



**Returns**

  * (::String) — Required. Identifier. The resource name of the session template. 



### #runtime_config
    
    
    def runtime_config() -> ::Google::Cloud::Dataproc::V1::RuntimeConfig

**Returns**

  * ([::Google::Cloud::Dataproc::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-RuntimeConfig)) — Optional. Runtime configuration for session execution. 



### #runtime_config=
    
    
    def runtime_config=(value) -> ::Google::Cloud::Dataproc::V1::RuntimeConfig

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-RuntimeConfig)) — Optional. Runtime configuration for session execution. 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::RuntimeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-RuntimeConfig)) — Optional. Runtime configuration for session execution. 



### #spark_connect_session
    
    
    def spark_connect_session() -> ::Google::Cloud::Dataproc::V1::SparkConnectConfig

**Returns**

  * ([::Google::Cloud::Dataproc::V1::SparkConnectConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SparkConnectConfig)) — Optional. Spark connect session config.

Note: The following fields are mutually exclusive: `spark_connect_session`, `jupyter_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #spark_connect_session=
    
    
    def spark_connect_session=(value) -> ::Google::Cloud::Dataproc::V1::SparkConnectConfig

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::SparkConnectConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SparkConnectConfig)) — Optional. Spark connect session config.

Note: The following fields are mutually exclusive: `spark_connect_session`, `jupyter_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataproc::V1::SparkConnectConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SparkConnectConfig)) — Optional. Spark connect session config.

Note: The following fields are mutually exclusive: `spark_connect_session`, `jupyter_session`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time the template was last updated. 



### #uuid
    
    
    def uuid() -> ::String

**Returns**

  * (::String) — Output only. A session template UUID (Unique Universal Identifier). The service generates this value when it creates the session template. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
