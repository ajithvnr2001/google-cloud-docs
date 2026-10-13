---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:18.035255+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings.

Settings for the cluster's primary instance

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database_flags
    
    
    def database_flags() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Database flags to pass to AlloyDB when DMS is creating the AlloyDB cluster and instances. See the AlloyDB documentation for how these can be used. 



### #database_flags=
    
    
    def database_flags=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Database flags to pass to AlloyDB when DMS is creating the AlloyDB cluster and instances. See the AlloyDB documentation for how these can be used. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Database flags to pass to AlloyDB when DMS is creating the AlloyDB cluster and instances. See the AlloyDB documentation for how these can be used. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Required. The ID of the AlloyDB primary instance. The ID must satisfy the regex expression "[a-z0-9-]+". 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the AlloyDB primary instance. The ID must satisfy the regex expression "[a-z0-9-]+". 



**Returns**

  * (::String) — Required. The ID of the AlloyDB primary instance. The ID must satisfy the regex expression "[a-z0-9-]+". 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB primary instance created by DMS. An object containing a list of 'key', 'value' pairs. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB primary instance created by DMS. An object containing a list of 'key', 'value' pairs. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB primary instance created by DMS. An object containing a list of 'key', 'value' pairs. 



### #machine_config
    
    
    def machine_config() -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings::MachineConfig

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings::MachineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings-MachineConfig)) — Configuration for the machines that host the underlying database engine. 



### #machine_config=
    
    
    def machine_config=(value) -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings::MachineConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings::MachineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings-MachineConfig)) — Configuration for the machines that host the underlying database engine. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings::MachineConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings-MachineConfig)) — Configuration for the machines that host the underlying database engine. 



### #private_ip
    
    
    def private_ip() -> ::String

**Returns**

  * (::String) — Output only. The private IP address for the Instance. This is the connection endpoint for an end-user application. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
