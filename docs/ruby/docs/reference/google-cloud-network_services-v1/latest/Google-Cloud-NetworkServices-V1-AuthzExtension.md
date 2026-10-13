---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-AuthzExtension/
title: Network Services V1 API - Class Google::Cloud::NetworkServices::V1::AuthzExtension (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:17.535022+00:00
---

# Network Services V1 API - Class Google::Cloud::NetworkServices::V1::AuthzExtension (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-AuthzExtension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Services V1 API - Class Google::Cloud::NetworkServices::V1::AuthzExtension (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Network Services V1 API class Google::Cloud::NetworkServices::V1::AuthzExtension.

`AuthzExtension` is a resource that allows traffic forwarding to a callout backend service to make an authorization decision.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #authority
    
    
    def authority() -> ::String

**Returns**

  * (::String) — Optional. The `:authority` header in the gRPC request sent from Envoy to the extension service. It is required when the `service` field points to a backend service or a wasm plugin. 



### #authority=
    
    
    def authority=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The `:authority` header in the gRPC request sent from Envoy to the extension service. It is required when the `service` field points to a backend service or a wasm plugin. 



**Returns**

  * (::String) — Optional. The `:authority` header in the gRPC request sent from Envoy to the extension service. It is required when the `service` field points to a backend service or a wasm plugin. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the resource was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. A human-readable description of the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A human-readable description of the resource. 



**Returns**

  * (::String) — Optional. A human-readable description of the resource. 



### #fail_open
    
    
    def fail_open() -> ::Boolean

**Returns**

  * (::Boolean) — 

Optional. Determines how the proxy behaves if the call to the extension fails or times out.

When set to `TRUE`, request or response processing continues without error. Any subsequent extensions in the extension chain are also executed. When set to `FALSE` or the default setting of `FALSE` is used, one of the following happens:

    * If response headers have not been delivered to the downstream client, a generic 500 error is returned to the client. The error response can be tailored by configuring a custom error response in the load balancer.

    * If response headers have been delivered, then the HTTP stream to the downstream client is reset.




### #fail_open=
    
    
    def fail_open=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

Optional. Determines how the proxy behaves if the call to the extension fails or times out.

When set to `TRUE`, request or response processing continues without error. Any subsequent extensions in the extension chain are also executed. When set to `FALSE` or the default setting of `FALSE` is used, one of the following happens:

    * If response headers have not been delivered to the downstream client, a generic 500 error is returned to the client. The error response can be tailored by configuring a custom error response in the load balancer.

    * If response headers have been delivered, then the HTTP stream to the downstream client is reset.




**Returns**

  * (::Boolean) — 

Optional. Determines how the proxy behaves if the call to the extension fails or times out.

When set to `TRUE`, request or response processing continues without error. Any subsequent extensions in the extension chain are also executed. When set to `FALSE` or the default setting of `FALSE` is used, one of the following happens:

    * If response headers have not been delivered to the downstream client, a generic 500 error is returned to the client. The error response can be tailored by configuring a custom error response in the load balancer.

    * If response headers have been delivered, then the HTTP stream to the downstream client is reset.




### #forward_attributes
    
    
    def forward_attributes() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of the Envoy attributes to forward to the extension server. The attributes provided here are included as part of the `ProcessingRequest.attributes` field (of type `map<string, google.protobuf.Struct>`), where the keys are the attribute names. Refer to the [documentation](https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference#attributes) for the names of attributes that can be forwarded. If omitted, no attributes are sent. Each element is a string indicating the attribute name. 



### #forward_attributes=
    
    
    def forward_attributes=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of the Envoy attributes to forward to the extension server. The attributes provided here are included as part of the `ProcessingRequest.attributes` field (of type `map<string, google.protobuf.Struct>`), where the keys are the attribute names. Refer to the [documentation](https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference#attributes) for the names of attributes that can be forwarded. If omitted, no attributes are sent. Each element is a string indicating the attribute name. 



**Returns**

  * (::Array<::String>) — Optional. List of the Envoy attributes to forward to the extension server. The attributes provided here are included as part of the `ProcessingRequest.attributes` field (of type `map<string, google.protobuf.Struct>`), where the keys are the attribute names. Refer to the [documentation](https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference#attributes) for the names of attributes that can be forwarded. If omitted, no attributes are sent. Each element is a string indicating the attribute name. 



### #forward_headers
    
    
    def forward_headers() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of the HTTP headers to forward to the extension (from the client). If omitted, all headers are sent. Each element is a string indicating the header name. 



### #forward_headers=
    
    
    def forward_headers=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of the HTTP headers to forward to the extension (from the client). If omitted, all headers are sent. Each element is a string indicating the header name. 



**Returns**

  * (::Array<::String>) — Optional. List of the HTTP headers to forward to the extension (from the client). If omitted, all headers are sent. Each element is a string indicating the header name. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Set of labels associated with the `AuthzExtension` resource.

The format must comply with [the requirements for labels](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Set of labels associated with the `AuthzExtension` resource.

The format must comply with [the requirements for labels](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Set of labels associated with the `AuthzExtension` resource.

The format must comply with [the requirements for labels](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements) for Google Cloud resources. 




### #load_balancing_scheme
    
    
    def load_balancing_scheme() -> ::Google::Cloud::NetworkServices::V1::LoadBalancingScheme

**Returns**

  * ([::Google::Cloud::NetworkServices::V1::LoadBalancingScheme](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-LoadBalancingScheme)) — Optional. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. Can be omitted for AuthzExtensions that do not reference a backend service. For more information, refer to [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service). 



### #load_balancing_scheme=
    
    
    def load_balancing_scheme=(value) -> ::Google::Cloud::NetworkServices::V1::LoadBalancingScheme

**Parameter**

  * **value** ([::Google::Cloud::NetworkServices::V1::LoadBalancingScheme](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-LoadBalancingScheme)) — Optional. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. Can be omitted for AuthzExtensions that do not reference a backend service. For more information, refer to [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service). 



**Returns**

  * ([::Google::Cloud::NetworkServices::V1::LoadBalancingScheme](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-LoadBalancingScheme)) — Optional. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: `INTERNAL_MANAGED`, `EXTERNAL_MANAGED`. Can be omitted for AuthzExtensions that do not reference a backend service. For more information, refer to [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service). 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Struct)) — Optional. The metadata provided here is included as part of the `metadata_context` (of type `google.protobuf.Struct`) in the `ProcessingRequest` message sent to the extension server. The metadata is available under the namespace `com.google.authz_extension.<resource_name>`. The following variables are supported in the metadata Struct:

`{forwarding_rule_id}` \- substituted with the forwarding rule's fully qualified resource name. 




### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Struct)) — Optional. The metadata provided here is included as part of the `metadata_context` (of type `google.protobuf.Struct`) in the `ProcessingRequest` message sent to the extension server. The metadata is available under the namespace `com.google.authz_extension.<resource_name>`. The following variables are supported in the metadata Struct:

`{forwarding_rule_id}` \- substituted with the forwarding rule's fully qualified resource name. 




**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Struct)) — Optional. The metadata provided here is included as part of the `metadata_context` (of type `google.protobuf.Struct`) in the `ProcessingRequest` message sent to the extension server. The metadata is available under the namespace `com.google.authz_extension.<resource_name>`. The following variables are supported in the metadata Struct:

`{forwarding_rule_id}` \- substituted with the forwarding rule's fully qualified resource name. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Identifier. Name of the `AuthzExtension` resource in the following format: `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Identifier. Name of the `AuthzExtension` resource in the following format: `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`. 



**Returns**

  * (::String) — Required. Identifier. Name of the `AuthzExtension` resource in the following format: `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`. 



### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — Required. The reference to the service that runs the extension.

To configure a callout extension, `service` must be a fully-qualified reference to a [backend service](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices) in the format: `https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` or `https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}`. 




### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The reference to the service that runs the extension.

To configure a callout extension, `service` must be a fully-qualified reference to a [backend service](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices) in the format: `https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` or `https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}`. 




**Returns**

  * (::String) — Required. The reference to the service that runs the extension.

To configure a callout extension, `service` must be a fully-qualified reference to a [backend service](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices) in the format: `https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}` or `https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}`. 




### #timeout
    
    
    def timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Duration)) — Required. Specifies the timeout for each individual message on the stream. The timeout must be between 10-10000 milliseconds. 



### #timeout=
    
    
    def timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Duration)) — Required. Specifies the timeout for each individual message on the stream. The timeout must be between 10-10000 milliseconds. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Duration)) — Required. Specifies the timeout for each individual message on the stream. The timeout must be between 10-10000 milliseconds. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the resource was updated. 



### #wire_format
    
    
    def wire_format() -> ::Google::Cloud::NetworkServices::V1::WireFormat

**Returns**

  * ([::Google::Cloud::NetworkServices::V1::WireFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-WireFormat)) — Optional. The format of communication supported by the callout extension. This field is supported only for regional `AuthzExtension` resources. If not specified, the default value `EXT_PROC_GRPC` is used. Global `AuthzExtension` resources use the `EXT_PROC_GRPC` wire format. 



### #wire_format=
    
    
    def wire_format=(value) -> ::Google::Cloud::NetworkServices::V1::WireFormat

**Parameter**

  * **value** ([::Google::Cloud::NetworkServices::V1::WireFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-WireFormat)) — Optional. The format of communication supported by the callout extension. This field is supported only for regional `AuthzExtension` resources. If not specified, the default value `EXT_PROC_GRPC` is used. Global `AuthzExtension` resources use the `EXT_PROC_GRPC` wire format. 



**Returns**

  * ([::Google::Cloud::NetworkServices::V1::WireFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-WireFormat)) — Optional. The format of communication supported by the callout extension. This field is supported only for regional `AuthzExtension` resources. If not specified, the default value `EXT_PROC_GRPC` is used. Global `AuthzExtension` resources use the `EXT_PROC_GRPC` wire format. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
