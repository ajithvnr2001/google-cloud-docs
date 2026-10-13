---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateSshScriptRequest/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:30.012361+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateSshScriptRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest.

Request message for 'GenerateSshScript' request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #migration_job
    
    
    def migration_job() -> ::String

**Returns**

  * (::String) — Name of the migration job resource to generate the SSH script. 



### #migration_job=
    
    
    def migration_job=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the migration job resource to generate the SSH script. 



**Returns**

  * (::String) — Name of the migration job resource to generate the SSH script. 



### #vm
    
    
    def vm() -> ::String

**Returns**

  * (::String) — Required. Bastion VM Instance name to use or to create. 



### #vm=
    
    
    def vm=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Bastion VM Instance name to use or to create. 



**Returns**

  * (::String) — Required. Bastion VM Instance name to use or to create. 



### #vm_creation_config
    
    
    def vm_creation_config() -> ::Google::Cloud::CloudDMS::V1::VmCreationConfig

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::VmCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmCreationConfig)) — The VM creation configuration

Note: The following fields are mutually exclusive: `vm_creation_config`, `vm_selection_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vm_creation_config=
    
    
    def vm_creation_config=(value) -> ::Google::Cloud::CloudDMS::V1::VmCreationConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::VmCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmCreationConfig)) — The VM creation configuration

Note: The following fields are mutually exclusive: `vm_creation_config`, `vm_selection_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::VmCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmCreationConfig)) — The VM creation configuration

Note: The following fields are mutually exclusive: `vm_creation_config`, `vm_selection_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vm_port
    
    
    def vm_port() -> ::Integer

**Returns**

  * (::Integer) — The port that will be open on the bastion host. 



### #vm_port=
    
    
    def vm_port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The port that will be open on the bastion host. 



**Returns**

  * (::Integer) — The port that will be open on the bastion host. 



### #vm_selection_config
    
    
    def vm_selection_config() -> ::Google::Cloud::CloudDMS::V1::VmSelectionConfig

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::VmSelectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmSelectionConfig)) — The VM selection configuration

Note: The following fields are mutually exclusive: `vm_selection_config`, `vm_creation_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vm_selection_config=
    
    
    def vm_selection_config=(value) -> ::Google::Cloud::CloudDMS::V1::VmSelectionConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::VmSelectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmSelectionConfig)) — The VM selection configuration

Note: The following fields are mutually exclusive: `vm_selection_config`, `vm_creation_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::VmSelectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmSelectionConfig)) — The VM selection configuration

Note: The following fields are mutually exclusive: `vm_selection_config`, `vm_creation_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
