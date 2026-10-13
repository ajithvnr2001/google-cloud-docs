---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File/
title: Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::File (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:25.342824+00:00
---

# Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::File (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::File (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Security Command Center V2 API class Google::Cloud::SecurityCenter::V2::File.

File information about the related binary/library used by an executable, or the script used by a script interpreter

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #contents
    
    
    def contents() -> ::String

**Returns**

  * (::String) — Prefix of the file contents as a JSON-encoded string. 



### #contents=
    
    
    def contents=(value) -> ::String

**Parameter**

  * **value** (::String) — Prefix of the file contents as a JSON-encoded string. 



**Returns**

  * (::String) — Prefix of the file contents as a JSON-encoded string. 



### #disk_path
    
    
    def disk_path() -> ::Google::Cloud::SecurityCenter::V2::File::DiskPath

**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::File::DiskPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-DiskPath)) — Path of the file in terms of underlying disk/partition identifiers. 



### #disk_path=
    
    
    def disk_path=(value) -> ::Google::Cloud::SecurityCenter::V2::File::DiskPath

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V2::File::DiskPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-DiskPath)) — Path of the file in terms of underlying disk/partition identifiers. 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V2::File::DiskPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-DiskPath)) — Path of the file in terms of underlying disk/partition identifiers. 



### #hashed_size
    
    
    def hashed_size() -> ::Integer

**Returns**

  * (::Integer) — The length in bytes of the file prefix that was hashed. If hashed_size == size, any hashes reported represent the entire file. 



### #hashed_size=
    
    
    def hashed_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The length in bytes of the file prefix that was hashed. If hashed_size == size, any hashes reported represent the entire file. 



**Returns**

  * (::Integer) — The length in bytes of the file prefix that was hashed. If hashed_size == size, any hashes reported represent the entire file. 



### #operations
    
    
    def operations() -> ::Array<::Google::Cloud::SecurityCenter::V2::File::FileOperation>

**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V2::File::FileOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-FileOperation)>) — Operation(s) performed on a file. 



### #operations=
    
    
    def operations=(value) -> ::Array<::Google::Cloud::SecurityCenter::V2::File::FileOperation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SecurityCenter::V2::File::FileOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-FileOperation)>) — Operation(s) performed on a file. 



**Returns**

  * (::Array<[::Google::Cloud::SecurityCenter::V2::File::FileOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-File-FileOperation)>) — Operation(s) performed on a file. 



### #partially_hashed
    
    
    def partially_hashed() -> ::Boolean

**Returns**

  * (::Boolean) — True when the hash covers only a prefix of the file. 



### #partially_hashed=
    
    
    def partially_hashed=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — True when the hash covers only a prefix of the file. 



**Returns**

  * (::Boolean) — True when the hash covers only a prefix of the file. 



### #path
    
    
    def path() -> ::String

**Returns**

  * (::String) — Absolute path of the file as a JSON encoded string. 



### #path=
    
    
    def path=(value) -> ::String

**Parameter**

  * **value** (::String) — Absolute path of the file as a JSON encoded string. 



**Returns**

  * (::String) — Absolute path of the file as a JSON encoded string. 



### #sha256
    
    
    def sha256() -> ::String

**Returns**

  * (::String) — SHA256 hash of the first hashed_size bytes of the file encoded as a hex string. If hashed_size == size, sha256 represents the SHA256 hash of the entire file. 



### #sha256=
    
    
    def sha256=(value) -> ::String

**Parameter**

  * **value** (::String) — SHA256 hash of the first hashed_size bytes of the file encoded as a hex string. If hashed_size == size, sha256 represents the SHA256 hash of the entire file. 



**Returns**

  * (::String) — SHA256 hash of the first hashed_size bytes of the file encoded as a hex string. If hashed_size == size, sha256 represents the SHA256 hash of the entire file. 



### #size
    
    
    def size() -> ::Integer

**Returns**

  * (::Integer) — Size of the file in bytes. 



### #size=
    
    
    def size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Size of the file in bytes. 



**Returns**

  * (::Integer) — Size of the file in bytes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
