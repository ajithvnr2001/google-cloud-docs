---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicy/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicy (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:35.186737+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicy (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicy (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ResourcePolicy.

Represents a Resource Policy resource. You can use resource policies to schedule actions for some Compute Engine resources. For example, you can use them toschedule persistent disk snapshots.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

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

  * (::String) 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #disk_consistency_group_policy
    
    
    def disk_consistency_group_policy() -> ::Google::Cloud::Compute::V1::ResourcePolicyDiskConsistencyGroupPolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyDiskConsistencyGroupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyDiskConsistencyGroupPolicy)) — Resource policy for disk consistency groups. 



### #disk_consistency_group_policy=
    
    
    def disk_consistency_group_policy=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicyDiskConsistencyGroupPolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicyDiskConsistencyGroupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyDiskConsistencyGroupPolicy)) — Resource policy for disk consistency groups. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyDiskConsistencyGroupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyDiskConsistencyGroupPolicy)) — Resource policy for disk consistency groups. 



### #group_placement_policy
    
    
    def group_placement_policy() -> ::Google::Cloud::Compute::V1::ResourcePolicyGroupPlacementPolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyGroupPlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyGroupPlacementPolicy)) — Resource policy for instances for placement configuration. 



### #group_placement_policy=
    
    
    def group_placement_policy=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicyGroupPlacementPolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicyGroupPlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyGroupPlacementPolicy)) — Resource policy for instances for placement configuration. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyGroupPlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyGroupPlacementPolicy)) — Resource policy for instances for placement configuration. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



**Returns**

  * (::Integer) — Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. 



### #instance_schedule_policy
    
    
    def instance_schedule_policy() -> ::Google::Cloud::Compute::V1::ResourcePolicyInstanceSchedulePolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyInstanceSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyInstanceSchedulePolicy)) — Resource policy for scheduling instance operations. 



### #instance_schedule_policy=
    
    
    def instance_schedule_policy=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicyInstanceSchedulePolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicyInstanceSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyInstanceSchedulePolicy)) — Resource policy for scheduling instance operations. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyInstanceSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyInstanceSchedulePolicy)) — Resource policy for scheduling instance operations. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#resource_policies for resource policies. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#resource_policies for resource policies. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#resource_policies for resource policies. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



**Returns**

  * (::String) — The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #resource_status
    
    
    def resource_status() -> ::Google::Cloud::Compute::V1::ResourcePolicyResourceStatus

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyResourceStatus)) — Output only. [Output Only] The system status of the resource policy. 



### #resource_status=
    
    
    def resource_status=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicyResourceStatus

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicyResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyResourceStatus)) — Output only. [Output Only] The system status of the resource policy. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyResourceStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyResourceStatus)) — Output only. [Output Only] The system status of the resource policy. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined fully-qualified URL for this resource. 



### #snapshot_schedule_policy
    
    
    def snapshot_schedule_policy() -> ::Google::Cloud::Compute::V1::ResourcePolicySnapshotSchedulePolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicySnapshotSchedulePolicy)) — Resource policy for persistent disks for creating snapshots. 



### #snapshot_schedule_policy=
    
    
    def snapshot_schedule_policy=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicySnapshotSchedulePolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicySnapshotSchedulePolicy)) — Resource policy for persistent disks for creating snapshots. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicySnapshotSchedulePolicy)) — Resource policy for persistent disks for creating snapshots. 



### #status
    
    
    def status() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The status of resource policy creation. Check the Status enum for the list of possible values. 



### #status=
    
    
    def status=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The status of resource policy creation. Check the Status enum for the list of possible values. 



**Returns**

  * (::String) — Output only. [Output Only] The status of resource policy creation. Check the Status enum for the list of possible values. 



### #workload_policy
    
    
    def workload_policy() -> ::Google::Cloud::Compute::V1::ResourcePolicyWorkloadPolicy

**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyWorkloadPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyWorkloadPolicy)) — Resource policy for defining instance placement for MIGs. 



### #workload_policy=
    
    
    def workload_policy=(value) -> ::Google::Cloud::Compute::V1::ResourcePolicyWorkloadPolicy

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::ResourcePolicyWorkloadPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyWorkloadPolicy)) — Resource policy for defining instance placement for MIGs. 



**Returns**

  * ([::Google::Cloud::Compute::V1::ResourcePolicyWorkloadPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyWorkloadPolicy)) — Resource policy for defining instance placement for MIGs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
