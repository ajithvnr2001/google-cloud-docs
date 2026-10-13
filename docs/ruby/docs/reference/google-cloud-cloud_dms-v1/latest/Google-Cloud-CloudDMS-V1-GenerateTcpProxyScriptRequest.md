---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateTcpProxyScriptRequest/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:30.543233+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateTcpProxyScriptRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest.

Request message for 'GenerateTcpProxyScript' request.

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

  * (::String) — Name of the migration job resource to generate the TCP Proxy script. 



### #migration_job=
    
    
    def migration_job=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the migration job resource to generate the TCP Proxy script. 



**Returns**

  * (::String) — Name of the migration job resource to generate the TCP Proxy script. 



### #vm_machine_type
    
    
    def vm_machine_type() -> ::String

**Returns**

  * (::String) — Required. The type of the Compute instance that will host the proxy. 



### #vm_machine_type=
    
    
    def vm_machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The type of the Compute instance that will host the proxy. 



**Returns**

  * (::String) — Required. The type of the Compute instance that will host the proxy. 



### #vm_name
    
    
    def vm_name() -> ::String

**Returns**

  * (::String) — Required. The name of the Compute instance that will host the proxy. 



### #vm_name=
    
    
    def vm_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the Compute instance that will host the proxy. 



**Returns**

  * (::String) — Required. The name of the Compute instance that will host the proxy. 



### #vm_subnet
    
    
    def vm_subnet() -> ::String

**Returns**

  * (::String) — Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region. 



### #vm_subnet=
    
    
    def vm_subnet=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region. 



**Returns**

  * (::String) — Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region. 



### #vm_zone
    
    
    def vm_zone() -> ::String

**Returns**

  * (::String) — Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example "us-central1-b". If not specified, uses the "-b" zone of the destination Connection Profile's region. 



### #vm_zone=
    
    
    def vm_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example "us-central1-b". If not specified, uses the "-b" zone of the destination Connection Profile's region. 



**Returns**

  * (::String) — Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example "us-central1-b". If not specified, uses the "-b" zone of the destination Connection Profile's region. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
