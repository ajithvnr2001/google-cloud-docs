---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Disk/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Disk (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:00.239904+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Disk (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Disk (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::Disk.

Describes the data disk used by a workflow job.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #disk_type
    
    
    def disk_type() -> ::String

**Returns**

  * (::String) — Disk storage type, as defined by Google Compute Engine. This must be a disk type appropriate to the project and zone in which the workers will run. If unknown or unspecified, the service will attempt to choose a reasonable default.

For example, the standard persistent disk type is a resource name typically ending in "pd-standard". If SSD persistent disks are available, the resource name typically ends with "pd-ssd". The actual valid values are defined the Google Compute Engine API, not by the Cloud Dataflow API; consult the Google Compute Engine documentation for more information about determining the set of available disk types for a particular project and zone.

Google Compute Engine Disk types are local to a particular project in a particular zone, and so the resource name will typically look something like this:

compute.googleapis.com/projects/project-id/zones/zone/diskTypes/pd-standard 




### #disk_type=
    
    
    def disk_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Disk storage type, as defined by Google Compute Engine. This must be a disk type appropriate to the project and zone in which the workers will run. If unknown or unspecified, the service will attempt to choose a reasonable default.

For example, the standard persistent disk type is a resource name typically ending in "pd-standard". If SSD persistent disks are available, the resource name typically ends with "pd-ssd". The actual valid values are defined the Google Compute Engine API, not by the Cloud Dataflow API; consult the Google Compute Engine documentation for more information about determining the set of available disk types for a particular project and zone.

Google Compute Engine Disk types are local to a particular project in a particular zone, and so the resource name will typically look something like this:

compute.googleapis.com/projects/project-id/zones/zone/diskTypes/pd-standard 




**Returns**

  * (::String) — Disk storage type, as defined by Google Compute Engine. This must be a disk type appropriate to the project and zone in which the workers will run. If unknown or unspecified, the service will attempt to choose a reasonable default.

For example, the standard persistent disk type is a resource name typically ending in "pd-standard". If SSD persistent disks are available, the resource name typically ends with "pd-ssd". The actual valid values are defined the Google Compute Engine API, not by the Cloud Dataflow API; consult the Google Compute Engine documentation for more information about determining the set of available disk types for a particular project and zone.

Google Compute Engine Disk types are local to a particular project in a particular zone, and so the resource name will typically look something like this:

compute.googleapis.com/projects/project-id/zones/zone/diskTypes/pd-standard 




### #mount_point
    
    
    def mount_point() -> ::String

**Returns**

  * (::String) — Directory in a VM where disk is mounted. 



### #mount_point=
    
    
    def mount_point=(value) -> ::String

**Parameter**

  * **value** (::String) — Directory in a VM where disk is mounted. 



**Returns**

  * (::String) — Directory in a VM where disk is mounted. 



### #size_gb
    
    
    def size_gb() -> ::Integer

**Returns**

  * (::Integer) — Size of disk in GB. If zero or unspecified, the service will attempt to choose a reasonable default. 



### #size_gb=
    
    
    def size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Size of disk in GB. If zero or unspecified, the service will attempt to choose a reasonable default. 



**Returns**

  * (::Integer) — Size of disk in GB. If zero or unspecified, the service will attempt to choose a reasonable default. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
