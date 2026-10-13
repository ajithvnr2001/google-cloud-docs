---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroup/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::WireGroup (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:38.075373+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::WireGroup (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::WireGroup (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::WireGroup.

A resource that represents a group of redundant wires.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #admin_enabled
    
    
    def admin_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true. 



### #admin_enabled=
    
    
    def admin_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true. 



**Returns**

  * (::Boolean) — Indicates whether the wires in the wire group are enabled. When false, the wires in the wire group are disabled. When true and when there is simultaneously no wire-specific override of `adminEnabled` to false, a given wire is enabled. Defaults to true. 



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

  * (::String) — An optional description of the wire group. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional description of the wire group. 



**Returns**

  * (::String) — An optional description of the wire group. 



### #endpoints
    
    
    def endpoints() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::WireGroupEndpoint}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::WireGroupEndpoint}) — 

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

    * Key: an RFC1035 user-specified label.
    * Value: an Endpoint object.



### #endpoints=
    
    
    def endpoints=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::WireGroupEndpoint}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::WireGroupEndpoint}) — 

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

    * Key: an RFC1035 user-specified label.
    * Value: an Endpoint object.



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::WireGroupEndpoint}) — 

A map that contains the logical endpoints of the wire group. Specify key-value pairs for the map as follows:

    * Key: an RFC1035 user-specified label.
    * Value: an Endpoint object.



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



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#wireGroups for wire groups. 



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



### #reconciling
    
    
    def reconciling() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. [Output Only] Indicates whether there are wire changes yet to be processed. 



### #reconciling=
    
    
    def reconciling=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Output only. [Output Only] Indicates whether there are wire changes yet to be processed. 



**Returns**

  * (::Boolean) — Output only. [Output Only] Indicates whether there are wire changes yet to be processed. 



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



### #topology
    
    
    def topology() -> ::Google::Cloud::Compute::V1::WireGroupTopology

**Returns**

  * ([::Google::Cloud::Compute::V1::WireGroupTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroupTopology)) — Output only. Topology details for the wire group configuration. 



### #topology=
    
    
    def topology=(value) -> ::Google::Cloud::Compute::V1::WireGroupTopology

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::WireGroupTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroupTopology)) — Output only. Topology details for the wire group configuration. 



**Returns**

  * ([::Google::Cloud::Compute::V1::WireGroupTopology](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroupTopology)) — Output only. Topology details for the wire group configuration. 



### #wire_properties
    
    
    def wire_properties() -> ::Google::Cloud::Compute::V1::WireProperties

**Returns**

  * ([::Google::Cloud::Compute::V1::WireProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireProperties)) — Properties for all wires in the wire group. 



### #wire_properties=
    
    
    def wire_properties=(value) -> ::Google::Cloud::Compute::V1::WireProperties

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::WireProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireProperties)) — Properties for all wires in the wire group. 



**Returns**

  * ([::Google::Cloud::Compute::V1::WireProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireProperties)) — Properties for all wires in the wire group. 



### #wires
    
    
    def wires() -> ::Array<::Google::Cloud::Compute::V1::Wire>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::Wire](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Wire)>) — Output only. The single/redundant wire(s) managed by the wire group. 



### #wires=
    
    
    def wires=(value) -> ::Array<::Google::Cloud::Compute::V1::Wire>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::Wire](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Wire)>) — Output only. The single/redundant wire(s) managed by the wire group. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::Wire](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Wire)>) — Output only. The single/redundant wire(s) managed by the wire group. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
