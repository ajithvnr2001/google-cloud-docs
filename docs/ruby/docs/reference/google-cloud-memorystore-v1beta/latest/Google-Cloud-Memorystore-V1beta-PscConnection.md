---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-PscConnection/
title: Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::PscConnection (v0.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:38.739364+00:00
---

# Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::PscConnection (v0.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-PscConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1BETA API - Class Google::Cloud::Memorystore::V1beta::PscConnection (v0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1BETA API class Google::Cloud::Memorystore::V1beta::PscConnection.

User created Psc connection configuration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connection_type
    
    
    def connection_type() -> ::Google::Cloud::Memorystore::V1beta::ConnectionType

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::ConnectionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-ConnectionType)) — Output only. Type of the PSC connection. 



### #forwarding_rule
    
    
    def forwarding_rule() -> ::String

**Returns**

  * (::String) — Required. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwarding_rule} 



### #forwarding_rule=
    
    
    def forwarding_rule=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwarding_rule} 



**Returns**

  * (::String) — Required. The URI of the consumer side forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwarding_rule} 



### #ip_address
    
    
    def ip_address() -> ::String

**Returns**

  * (::String) — Required. The IP allocated on the consumer network for the PSC forwarding rule. 



### #ip_address=
    
    
    def ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The IP allocated on the consumer network for the PSC forwarding rule. 



**Returns**

  * (::String) — Required. The IP allocated on the consumer network for the PSC forwarding rule. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_name}. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_name}. 



**Returns**

  * (::String) — Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_name}. 



### #port
    
    
    def port() -> ::Integer

**Returns**

  * (::Integer) — Optional. port will only be set for Primary/Reader or Discovery endpoint. 



### #port=
    
    
    def port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. port will only be set for Primary/Reader or Discovery endpoint. 



**Returns**

  * (::Integer) — Optional. port will only be set for Primary/Reader or Discovery endpoint. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — Output only. The consumer project_id where the forwarding rule is created from. 



### #psc_connection_id
    
    
    def psc_connection_id() -> ::String

**Returns**

  * (::String) — Required. The PSC connection id of the forwarding rule connected to the service attachment. 



### #psc_connection_id=
    
    
    def psc_connection_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The PSC connection id of the forwarding rule connected to the service attachment. 



**Returns**

  * (::String) — Required. The PSC connection id of the forwarding rule connected to the service attachment. 



### #psc_connection_status
    
    
    def psc_connection_status() -> ::Google::Cloud::Memorystore::V1beta::PscConnectionStatus

**Returns**

  * ([::Google::Cloud::Memorystore::V1beta::PscConnectionStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1beta/latest/Google-Cloud-Memorystore-V1beta-PscConnectionStatus)) — Output only. The status of the PSC connection: whether a connection exists and ACTIVE or it no longer exists. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status. 



### #service_attachment
    
    
    def service_attachment() -> ::String

**Returns**

  * (::String) — Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}. 



### #service_attachment=
    
    
    def service_attachment=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}. 



**Returns**

  * (::String) — Required. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
