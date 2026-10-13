---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-FileResource/
title: Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:47.775575+00:00
---

# Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-FileResource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.1  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Cloud OS Config V1alpha API class Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource.

A resource that manages the state of a file.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #content
    
    
    def content() -> ::String

**Returns**

  * (::String) — A a file with this content. The size of the content is limited to 1024 characters.

Note: The following fields are mutually exclusive: `content`, `file`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #content=
    
    
    def content=(value) -> ::String

**Parameter**

  * **value** (::String) — A a file with this content. The size of the content is limited to 1024 characters.

Note: The following fields are mutually exclusive: `content`, `file`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A a file with this content. The size of the content is limited to 1024 characters.

Note: The following fields are mutually exclusive: `content`, `file`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #file
    
    
    def file() -> ::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::File

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::File](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-File)) — A remote or local source.

Note: The following fields are mutually exclusive: `file`, `content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #file=
    
    
    def file=(value) -> ::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::File

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::File](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-File)) — A remote or local source.

Note: The following fields are mutually exclusive: `file`, `content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::File](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-File)) — A remote or local source.

Note: The following fields are mutually exclusive: `file`, `content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — Required. The absolute path of the file within the VM. 



### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The absolute path of the file within the VM. 



**Returns**

  * (::String) — Required. The absolute path of the file within the VM. 



### #permissions
    
    
    def permissions() -> ::String

**Returns**

  * (::String) — Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.

Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 




### #permissions=
    
    
    def permissions=(value) -> ::String

**Parameter**

  * **value** (::String) — Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.

Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 




**Returns**

  * (::String) — Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755.

Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 




### #state
    
    
    def state() -> ::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource::DesiredState

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-FileResource-DesiredState)) — Required. Desired state of the file. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource::DesiredState

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-FileResource-DesiredState)) — Required. Desired state of the file. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicy::Resource::FileResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicy-Resource-FileResource-DesiredState)) — Required. Desired state of the file. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
