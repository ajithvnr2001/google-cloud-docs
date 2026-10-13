---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-LicenseManager-Rest-ServiceStub/
title: License Manager V1 API - Class Google::Cloud::LicenseManager::V1::LicenseManager::Rest::ServiceStub (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:21.091151+00:00
---

# License Manager V1 API - Class Google::Cloud::LicenseManager::V1::LicenseManager::Rest::ServiceStub (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-LicenseManager-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  License Manager V1 API - Class Google::Cloud::LicenseManager::V1::LicenseManager::Rest::ServiceStub (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the License Manager V1 API class Google::Cloud::LicenseManager::V1::LicenseManager::Rest::ServiceStub.

REST service stub for the LicenseManager service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #aggregate_usage
    
    
    def aggregate_usage(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::AggregateUsageResponse

Baseline implementation for the aggregate_usage REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::AggregateUsageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-AggregateUsageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::AggregateUsageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-AggregateUsageResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::AggregateUsageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-AggregateUsageResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_configuration
    
    
    def create_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::CreateConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-CreateConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #deactivate_configuration
    
    
    def deactivate_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the deactivate_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::DeactivateConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-DeactivateConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_configuration
    
    
    def delete_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::DeleteConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-DeleteConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_configuration
    
    
    def get_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::Configuration

Baseline implementation for the get_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::GetConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-GetConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Configuration)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Configuration)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_instance
    
    
    def get_instance(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::Instance

Baseline implementation for the get_instance REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-GetInstanceRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Instance)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_product
    
    
    def get_product(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::Product

Baseline implementation for the get_product REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::GetProductRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-GetProductRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::Product](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Product)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::Product](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Product)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_configurations
    
    
    def list_configurations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::ListConfigurationsResponse

Baseline implementation for the list_configurations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::ListConfigurationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListConfigurationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::ListConfigurationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListConfigurationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::ListConfigurationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListConfigurationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_instances
    
    
    def list_instances(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::ListInstancesResponse

Baseline implementation for the list_instances REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListInstancesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListInstancesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::ListInstancesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListInstancesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_products
    
    
    def list_products(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::ListProductsResponse

Baseline implementation for the list_products REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::ListProductsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListProductsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::ListProductsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListProductsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::ListProductsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListProductsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #query_configuration_license_usage
    
    
    def query_configuration_license_usage(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::LicenseManager::V1::QueryConfigurationLicenseUsageResponse

Baseline implementation for the query_configuration_license_usage REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::QueryConfigurationLicenseUsageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-QueryConfigurationLicenseUsageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::LicenseManager::V1::QueryConfigurationLicenseUsageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-QueryConfigurationLicenseUsageResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::LicenseManager::V1::QueryConfigurationLicenseUsageResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-QueryConfigurationLicenseUsageResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #reactivate_configuration
    
    
    def reactivate_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the reactivate_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::ReactivateConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ReactivateConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_configuration
    
    
    def update_configuration(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_configuration REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::LicenseManager::V1::UpdateConfigurationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-UpdateConfigurationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
