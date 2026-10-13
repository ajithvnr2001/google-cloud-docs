---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:17.927790+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::AlloyDbSettings (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::AlloyDbSettings.

Settings for creating an AlloyDB cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::EncryptionConfig

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



### #initial_user
    
    
    def initial_user() -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::UserPassword

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-UserPassword)) — Required. Input only. Initial user to setup during cluster creation. Required. 



### #initial_user=
    
    
    def initial_user=(value) -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::UserPassword

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-UserPassword)) — Required. Input only. Initial user to setup during cluster creation. Required. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-UserPassword)) — Required. Input only. Initial user to setup during cluster creation. Required. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB cluster created by DMS. An object containing a list of 'key', 'value' pairs. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB cluster created by DMS. An object containing a list of 'key', 'value' pairs. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for the AlloyDB cluster created by DMS. An object containing a list of 'key', 'value' pairs. 



### #primary_instance_settings
    
    
    def primary_instance_settings() -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings)) 



### #primary_instance_settings=
    
    
    def primary_instance_settings=(value) -> ::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings)) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbSettings::PrimaryInstanceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbSettings-PrimaryInstanceSettings)) 



### #vpc_network
    
    
    def vpc_network() -> ::String

**Returns**

  * (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: "projects/{project_number}/global/networks/{network_id}". This is required to create a cluster. 



### #vpc_network=
    
    
    def vpc_network=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: "projects/{project_number}/global/networks/{network_id}". This is required to create a cluster. 



**Returns**

  * (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: "projects/{project_number}/global/networks/{network_id}". This is required to create a cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
