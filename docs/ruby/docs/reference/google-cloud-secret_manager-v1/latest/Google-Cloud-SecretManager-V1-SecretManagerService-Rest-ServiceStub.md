---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Rest-ServiceStub/
title: Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::SecretManagerService::Rest::ServiceStub (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:12.583918+00:00
---

# Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::SecretManagerService::Rest::ServiceStub (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretManagerService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1 API - Class Google::Cloud::SecretManager::V1::SecretManagerService::Rest::ServiceStub (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.21.0  0.20.0  0.19.2  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Secret Manager V1 API class Google::Cloud::SecretManager::V1::SecretManagerService::Rest::ServiceStub.

REST service stub for the SecretManagerService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #access_secret_version
    
    
    def access_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::AccessSecretVersionResponse

Baseline implementation for the access_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::AccessSecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-AccessSecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::AccessSecretVersionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-AccessSecretVersionResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::AccessSecretVersionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-AccessSecretVersionResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #add_secret_version
    
    
    def add_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the add_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::AddSecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-AddSecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_secret
    
    
    def create_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::Secret

Baseline implementation for the create_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::CreateSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-CreateSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_secret
    
    
    def delete_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::DeleteSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-DeleteSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #destroy_secret_version
    
    
    def destroy_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the destroy_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::DestroySecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-DestroySecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #disable_secret_version
    
    
    def disable_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the disable_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::DisableSecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-DisableSecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #enable_managed_rotation
    
    
    def enable_managed_rotation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the enable_managed_rotation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::EnableManagedRotationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-EnableManagedRotationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #enable_secret_version
    
    
    def enable_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the enable_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::EnableSecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-EnableSecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



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

  * **request_pb** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-GetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_secret
    
    
    def get_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::Secret

Baseline implementation for the get_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::GetSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-GetSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_secret_version
    
    
    def get_secret_version(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the get_secret_version REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::GetSecretVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-GetSecretVersionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_secret_versions
    
    
    def list_secret_versions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::ListSecretVersionsResponse

Baseline implementation for the list_secret_versions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::ListSecretVersionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretVersionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::ListSecretVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretVersionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::ListSecretVersionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretVersionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_secrets
    
    
    def list_secrets(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::ListSecretsResponse

Baseline implementation for the list_secrets REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::ListSecretsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::ListSecretsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::ListSecretsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-ListSecretsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #rotate_secret
    
    
    def rotate_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::SecretVersion

Baseline implementation for the rotate_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::RotateSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-RotateSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::SecretVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-SecretVersion)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #set_iam_policy
    
    
    def set_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::Policy

Baseline implementation for the set_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-SetIamPolicyRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #test_iam_permissions
    
    
    def test_iam_permissions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Iam::V1::TestIamPermissionsResponse

Baseline implementation for the test_iam_permissions REST call

**Parameters**

  * **request_pb** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-TestIamPermissionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_secret
    
    
    def update_secret(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::SecretManager::V1::Secret

Baseline implementation for the update_secret REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::SecretManager::V1::UpdateSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-UpdateSecretRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::SecretManager::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1/latest/Google-Cloud-SecretManager-V1-Secret)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
