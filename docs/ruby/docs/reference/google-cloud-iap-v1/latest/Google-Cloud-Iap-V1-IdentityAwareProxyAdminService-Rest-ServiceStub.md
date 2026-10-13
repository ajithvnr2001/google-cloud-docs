---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IdentityAwareProxyAdminService-Rest-ServiceStub/
title: Identity-Aware Proxy V1 API - Class Google::Cloud::Iap::V1::IdentityAwareProxyAdminService::Rest::ServiceStub (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:35.668067+00:00
---

# Identity-Aware Proxy V1 API - Class Google::Cloud::Iap::V1::IdentityAwareProxyAdminService::Rest::ServiceStub (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IdentityAwareProxyAdminService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity-Aware Proxy V1 API - Class Google::Cloud::Iap::V1::IdentityAwareProxyAdminService::Rest::ServiceStub (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.1  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Identity-Aware Proxy V1 API class Google::Cloud::Iap::V1::IdentityAwareProxyAdminService::Rest::ServiceStub.

REST service stub for the IdentityAwareProxyAdminService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_tunnel_dest_group
    
    
    def create_tunnel_dest_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::TunnelDestGroup

Baseline implementation for the create_tunnel_dest_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::CreateTunnelDestGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-CreateTunnelDestGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_tunnel_dest_group
    
    
    def delete_tunnel_dest_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_tunnel_dest_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::DeleteTunnelDestGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-DeleteTunnelDestGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_iam_policy
    
    
    def get_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::Policy

Baseline implementation for the get_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-GetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_iap_settings
    
    
    def get_iap_settings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::IapSettings

Baseline implementation for the get_iap_settings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::GetIapSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-GetIapSettingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::IapSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IapSettings)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::IapSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IapSettings)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_tunnel_dest_group
    
    
    def get_tunnel_dest_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::TunnelDestGroup

Baseline implementation for the get_tunnel_dest_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::GetTunnelDestGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-GetTunnelDestGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_tunnel_dest_groups
    
    
    def list_tunnel_dest_groups(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::ListTunnelDestGroupsResponse

Baseline implementation for the list_tunnel_dest_groups REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::ListTunnelDestGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ListTunnelDestGroupsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::ListTunnelDestGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ListTunnelDestGroupsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::ListTunnelDestGroupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ListTunnelDestGroupsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #set_iam_policy
    
    
    def set_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::Policy

Baseline implementation for the set_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-SetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #test_iam_permissions
    
    
    def test_iam_permissions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::TestIamPermissionsResponse

Baseline implementation for the test_iam_permissions REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-TestIamPermissionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_iap_settings
    
    
    def update_iap_settings(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::IapSettings

Baseline implementation for the update_iap_settings REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::UpdateIapSettingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-UpdateIapSettingsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::IapSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IapSettings)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::IapSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-IapSettings)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_tunnel_dest_group
    
    
    def update_tunnel_dest_group(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::TunnelDestGroup

Baseline implementation for the update_tunnel_dest_group REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::UpdateTunnelDestGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-UpdateTunnelDestGroupRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::TunnelDestGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-TunnelDestGroup)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #validate_iap_attribute_expression
    
    
    def validate_iap_attribute_expression(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Iap::V1::ValidateIapAttributeExpressionResponse

Baseline implementation for the validate_iap_attribute_expression REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Iap::V1::ValidateIapAttributeExpressionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ValidateIapAttributeExpressionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Iap::V1::ValidateIapAttributeExpressionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ValidateIapAttributeExpressionResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Iap::V1::ValidateIapAttributeExpressionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-iap-v1/latest/Google-Cloud-Iap-V1-ValidateIapAttributeExpressionResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
