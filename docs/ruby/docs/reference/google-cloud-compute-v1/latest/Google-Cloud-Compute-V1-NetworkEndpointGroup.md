---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::NetworkEndpointGroup (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:19.271132+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::NetworkEndpointGroup (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::NetworkEndpointGroup (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::NetworkEndpointGroup.

Represents a collection of network endpoints.

A network endpoint group (NEG) defines how a set of endpoints should be reached, whether they are reachable, and where they are located. For more information about using NEGs for different use cases, seeNetwork endpoint groups overview.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API \- To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API \- To manage NEGs with global scope (such as global internet NEGs):global API

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata defined as annotations on the network endpoint group. 



### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata defined as annotations on the network endpoint group. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Metadata defined as annotations on the network endpoint group. 



### #app_engine
    
    
    def app_engine() -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupAppEngine

**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupAppEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupAppEngine)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



### #app_engine=
    
    
    def app_engine=(value) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupAppEngine

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::NetworkEndpointGroupAppEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupAppEngine)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupAppEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupAppEngine)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



### #cloud_function
    
    
    def cloud_function() -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudFunction

**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudFunction)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



### #cloud_function=
    
    
    def cloud_function=(value) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudFunction

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudFunction)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudFunction)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



### #cloud_run
    
    
    def cloud_run() -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudRun

**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudRun)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



### #cloud_run=
    
    
    def cloud_run=(value) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudRun

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudRun)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupCloudRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupCloudRun)) — Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set. 



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



### #default_port
    
    
    def default_port() -> ::Integer

**Returns**

  * (::Integer) — The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified. 




### #default_port=
    
    
    def default_port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified. 




**Returns**

  * (::Integer) — The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified. 




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



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



**Returns**

  * (::String) — Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required. 



**Returns**

  * (::String) — The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required. 



### #network_endpoint_type
    
    
    def network_endpoint_type() -> ::String

**Returns**

  * (::String) — Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values. 



### #network_endpoint_type=
    
    
    def network_endpoint_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values. 



**Returns**

  * (::String) — Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values. 



### #psc_data
    
    
    def psc_data() -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupPscData

**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupPscData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupPscData)) — Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 



### #psc_data=
    
    
    def psc_data=(value) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroupPscData

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::NetworkEndpointGroupPscData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupPscData)) — Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroupPscData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroupPscData)) — Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 



### #psc_target_service
    
    
    def psc_target_service() -> ::String

**Returns**

  * (::String) — The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 




### #psc_target_service=
    
    
    def psc_target_service=(value) -> ::String

**Parameter**

  * **value** (::String) — The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 




**Returns**

  * (::String) — The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT. 




### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The URL of theregion where the network endpoint group is located. 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The URL of theregion where the network endpoint group is located. 



**Returns**

  * (::String) — Output only. [Output Only] The URL of theregion where the network endpoint group is located. 



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



### #size
    
    
    def size() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output only] Number of network endpoints in the network endpoint group. 



### #size=
    
    
    def size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output only] Number of network endpoints in the network endpoint group. 



**Returns**

  * (::Integer) — Output only. [Output only] Number of network endpoints in the network endpoint group. 



### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — Optional URL of the subnetwork to which all network endpoints in the NEG belong. 



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional URL of the subnetwork to which all network endpoints in the NEG belong. 



**Returns**

  * (::String) — Optional URL of the subnetwork to which all network endpoints in the NEG belong. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] The URL of thezone where the network endpoint group is located. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] The URL of thezone where the network endpoint group is located. 



**Returns**

  * (::String) — Output only. [Output Only] The URL of thezone where the network endpoint group is located. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
