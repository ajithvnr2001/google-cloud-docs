---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-MulticloudDataTransferConfig/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::MulticloudDataTransferConfig (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:56.651596+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::MulticloudDataTransferConfig (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-MulticloudDataTransferConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::MulticloudDataTransferConfig (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::MulticloudDataTransferConfig.

The `MulticloudDataTransferConfig` resource. It lists the services that you configure for Data Transfer Essentials billing and metering.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the `MulticloudDataTransferConfig` resource was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. A description of this resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A description of this resource. 



**Returns**

  * (::String) — Optional. A description of this resource. 



### #destinations_active_count
    
    
    def destinations_active_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of `Destination` resources in use with the `MulticloudDataTransferConfig` resource. 



### #destinations_count
    
    
    def destinations_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of `Destination` resources configured for the `MulticloudDataTransferConfig` resource. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding. 



**Returns**

  * (::String) — The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The name of the `MulticloudDataTransferConfig` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The name of the `MulticloudDataTransferConfig` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}`. 



**Returns**

  * (::String) — Identifier. The name of the `MulticloudDataTransferConfig` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}`. 



### #services
    
    
    def services() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::NetworkConnectivity::V1::StateTimeline}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::NetworkConnectivity::V1::StateTimeline}) — Optional. Maps services to their current or planned states. Service names are keys, and the associated values describe the state of the service. If a state change is expected, the value is either `ADDING` or `DELETING`, depending on the actions taken.

Sample output: "services": { "big-query": { "states": [ { "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING", }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE", } ] } } 




### #services=
    
    
    def services=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::NetworkConnectivity::V1::StateTimeline}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::NetworkConnectivity::V1::StateTimeline}) — Optional. Maps services to their current or planned states. Service names are keys, and the associated values describe the state of the service. If a state change is expected, the value is either `ADDING` or `DELETING`, depending on the actions taken.

Sample output: "services": { "big-query": { "states": [ { "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING", }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE", } ] } } 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::NetworkConnectivity::V1::StateTimeline}) — Optional. Maps services to their current or planned states. Service names are keys, and the associated values describe the state of the service. If a state change is expected, the value is either `ADDING` or `DELETING`, depending on the actions taken.

Sample output: "services": { "big-query": { "states": [ { "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING", }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE", } ] } } 




### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. The Google-generated unique ID for the `MulticloudDataTransferConfig` resource. This value is unique across all `MulticloudDataTransferConfig` resources. If a resource is deleted and another with the same name is created, the new resource is assigned a different and unique ID. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the `MulticloudDataTransferConfig` resource was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
