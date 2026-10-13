---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroup/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InterconnectAttachmentGroup (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:01.842341+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InterconnectAttachmentGroup (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InterconnectAttachmentGroup (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::InterconnectAttachmentGroup.

An interconnect attachment group resource allows customers to create, analyze, and expand highly available deployments.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attachments
    
    
    def attachments() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupAttachment}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupAttachment}) — Attachments in the AttachmentGroup. Keys are arbitrary user-specified strings. Users are encouraged, but not required, to use their preferred format for resource links as keys. Note that there are add-members and remove-members methods in gcloud. The size of this map is limited by an "Attachments per group" quota. 



### #attachments=
    
    
    def attachments=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupAttachment}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupAttachment}) — Attachments in the AttachmentGroup. Keys are arbitrary user-specified strings. Users are encouraged, but not required, to use their preferred format for resource links as keys. Note that there are add-members and remove-members methods in gcloud. The size of this map is limited by an "Attachments per group" quota. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupAttachment}) — Attachments in the AttachmentGroup. Keys are arbitrary user-specified strings. Users are encouraged, but not required, to use their preferred format for resource links as keys. Note that there are add-members and remove-members methods in gcloud. The size of this map is limited by an "Attachments per group" quota. 



### #configured
    
    
    def configured() -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupConfigured

**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupConfigured](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupConfigured)) 



### #configured=
    
    
    def configured=(value) -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupConfigured

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupConfigured](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupConfigured)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupConfigured](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupConfigured)) 



### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



**Returns**

  * (::String) — Output only. [Output Only] Creation timestamp inRFC3339 text format. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional description of this resource. Provide this property when you create the resource. 



**Returns**

  * (::String) — An optional description of this resource. Provide this property when you create the resource. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Opaque system-generated token that uniquely identifies the configuration. If provided when patching a configuration in update mode, the provided token must match the current token or the update is rejected. This provides a reliable means of doing read-modify-write (optimistic locking) as described byAIP 154. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Opaque system-generated token that uniquely identifies the configuration. If provided when patching a configuration in update mode, the provided token must match the current token or the update is rejected. This provides a reliable means of doing read-modify-write (optimistic locking) as described byAIP 154. 



**Returns**

  * (::String) — Opaque system-generated token that uniquely identifies the configuration. If provided when patching a configuration in update mode, the provided token must match the current token or the update is rejected. This provides a reliable means of doing read-modify-write (optimistic locking) as described byAIP 154. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier. 



**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier. 



### #intent
    
    
    def intent() -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupIntent

**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupIntent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupIntent)) 



### #intent=
    
    
    def intent=(value) -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupIntent

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupIntent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupIntent)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupIntent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupIntent)) 



### #interconnect_group
    
    
    def interconnect_group() -> ::String

**Returns**

  * (::String) — The URL of an InterconnectGroup that groups these Attachments' Interconnects. Customers do not need to set this unless directed by Google Support. 



### #interconnect_group=
    
    
    def interconnect_group=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL of an InterconnectGroup that groups these Attachments' Interconnects. Customers do not need to set this unless directed by Google Support. 



**Returns**

  * (::String) — The URL of an InterconnectGroup that groups these Attachments' Interconnects. Customers do not need to set this unless directed by Google Support. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#interconnectAttachmentGroup. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Always compute#interconnectAttachmentGroup. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always compute#interconnectAttachmentGroup. 



### #logical_structure
    
    
    def logical_structure() -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupLogicalStructure

**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupLogicalStructure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupLogicalStructure)) 



### #logical_structure=
    
    
    def logical_structure=(value) -> ::Google::Cloud::Compute::V1::InterconnectAttachmentGroupLogicalStructure

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupLogicalStructure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupLogicalStructure)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::InterconnectAttachmentGroupLogicalStructure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroupLogicalStructure)) 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



**Returns**

  * (::String) — Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for the resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined URL for the resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for the resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
