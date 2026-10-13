---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource/
title: Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:37.519639+00:00
---

# Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Cloud OS Config V1 API class Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource.

A resource that manages a system package.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #apt
    
    
    def apt() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::APT

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::APT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-APT)) — A package managed by Apt.

Note: The following fields are mutually exclusive: `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #apt=
    
    
    def apt=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::APT

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::APT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-APT)) — A package managed by Apt.

Note: The following fields are mutually exclusive: `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::APT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-APT)) — A package managed by Apt.

Note: The following fields are mutually exclusive: `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deb
    
    
    def deb() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Deb

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Deb](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Deb)) — A deb package file.

Note: The following fields are mutually exclusive: `deb`, `apt`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deb=
    
    
    def deb=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Deb

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Deb](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Deb)) — A deb package file.

Note: The following fields are mutually exclusive: `deb`, `apt`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Deb](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Deb)) — A deb package file.

Note: The following fields are mutually exclusive: `deb`, `apt`, `yum`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #desired_state
    
    
    def desired_state() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::DesiredState

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-DesiredState)) — Required. The desired state the agent should maintain for this package. 



### #desired_state=
    
    
    def desired_state=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::DesiredState

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-DesiredState)) — Required. The desired state the agent should maintain for this package. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::DesiredState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-DesiredState)) — Required. The desired state the agent should maintain for this package. 



### #googet
    
    
    def googet() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::GooGet

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::GooGet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-GooGet)) — A package managed by GooGet.

Note: The following fields are mutually exclusive: `googet`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #googet=
    
    
    def googet=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::GooGet

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::GooGet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-GooGet)) — A package managed by GooGet.

Note: The following fields are mutually exclusive: `googet`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::GooGet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-GooGet)) — A package managed by GooGet.

Note: The following fields are mutually exclusive: `googet`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #msi
    
    
    def msi() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::MSI

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::MSI](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-MSI)) — An MSI package.

Note: The following fields are mutually exclusive: `msi`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #msi=
    
    
    def msi=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::MSI

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::MSI](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-MSI)) — An MSI package.

Note: The following fields are mutually exclusive: `msi`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::MSI](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-MSI)) — An MSI package.

Note: The following fields are mutually exclusive: `msi`, `apt`, `deb`, `yum`, `zypper`, `rpm`, `googet`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rpm
    
    
    def rpm() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::RPM

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::RPM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-RPM)) — An rpm package file.

Note: The following fields are mutually exclusive: `rpm`, `apt`, `deb`, `yum`, `zypper`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rpm=
    
    
    def rpm=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::RPM

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::RPM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-RPM)) — An rpm package file.

Note: The following fields are mutually exclusive: `rpm`, `apt`, `deb`, `yum`, `zypper`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::RPM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-RPM)) — An rpm package file.

Note: The following fields are mutually exclusive: `rpm`, `apt`, `deb`, `yum`, `zypper`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #yum
    
    
    def yum() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::YUM

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::YUM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-YUM)) — A package managed by YUM.

Note: The following fields are mutually exclusive: `yum`, `apt`, `deb`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #yum=
    
    
    def yum=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::YUM

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::YUM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-YUM)) — A package managed by YUM.

Note: The following fields are mutually exclusive: `yum`, `apt`, `deb`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::YUM](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-YUM)) — A package managed by YUM.

Note: The following fields are mutually exclusive: `yum`, `apt`, `deb`, `zypper`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #zypper
    
    
    def zypper() -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Zypper

**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Zypper](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Zypper)) — A package managed by Zypper.

Note: The following fields are mutually exclusive: `zypper`, `apt`, `deb`, `yum`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #zypper=
    
    
    def zypper=(value) -> ::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Zypper

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Zypper](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Zypper)) — A package managed by Zypper.

Note: The following fields are mutually exclusive: `zypper`, `apt`, `deb`, `yum`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::OSPolicy::Resource::PackageResource::Zypper](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-OSPolicy-Resource-PackageResource-Zypper)) — A package managed by Zypper.

Note: The following fields are mutually exclusive: `zypper`, `apt`, `deb`, `yum`, `rpm`, `googet`, `msi`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
