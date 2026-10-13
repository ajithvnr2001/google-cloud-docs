---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client/
title: Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:26.960282+00:00
---

# Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.

REST client for the OrgPolicyViolationsPreviewService service.

Violations Preview API service for OrgPolicy.

An [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") is a preview of the violations that will exist as soon as a proposed OrgPolicy change is submitted. To create an [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)"), the API user specifies the changes they wish to make and requests the generation of a preview via [GenerateViolationsPreview][]. the OrgPolicy Simulator service then scans the API user's currently existing resources to determine these resources violate the newly set OrgPolicy.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the OrgPolicyViolationsPreviewService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all OrgPolicyViolationsPreviewService clients
    ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the OrgPolicyViolationsPreviewService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client#Google__Cloud__PolicySimulator__V1__OrgPolicyViolationsPreviewService__Rest__Client_configure_class_ "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration)) 



### #create_org_policy_violations_preview
    
    
    def create_org_policy_violations_preview(request, options = nil) -> ::Gapic::Operation
    def create_org_policy_violations_preview(parent: nil, org_policy_violations_preview: nil, org_policy_violations_preview_id: nil) -> ::Gapic::Operation

CreateOrgPolicyViolationsPreview creates an [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") for the proposed changes in the provided [OrgPolicyViolationsPreview.OrgPolicyOverlay][]. The changes to OrgPolicy are specified by this `OrgPolicyOverlay`. The resources to scan are inferred from these specified changes.

**Overloads**
    
    
    def create_org_policy_violations_preview(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_org_policy_violations_preview` via a request object, either of type [CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-CreateOrgPolicyViolationsPreviewRequest "Google::Cloud::PolicySimulator::V1::CreateOrgPolicyViolationsPreviewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::PolicySimulator::V1::CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-CreateOrgPolicyViolationsPreviewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_org_policy_violations_preview(parent: nil, org_policy_violations_preview: nil, org_policy_violations_preview_id: nil) -> ::Gapic::Operation

Pass arguments to `create_org_policy_violations_preview` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The organization under which this [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") will be created.

Example: `organizations/my-example-org/locations/global`

  * **org_policy_violations_preview** ([::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview), ::Hash) — Required. The [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") to generate. 
  * **org_policy_violations_preview_id** (::String) — Optional. An optional user-specified ID for the [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)"). If not provided, a random ID will be generated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/policy_simulator/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::PolicySimulator::V1::CreateOrgPolicyViolationsPreviewRequest.new
    
    # Call the create_org_policy_violations_preview method.
    result = client.create_org_policy_violations_preview request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_org_policy_violations_preview
    
    
    def get_org_policy_violations_preview(request, options = nil) -> ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview
    def get_org_policy_violations_preview(name: nil) -> ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview

GetOrgPolicyViolationsPreview gets the specified [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)"). Each [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") is available for at least 7 days.

**Overloads**
    
    
    def get_org_policy_violations_preview(request, options = nil) -> ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview

Pass arguments to `get_org_policy_violations_preview` via a request object, either of type [GetOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-GetOrgPolicyViolationsPreviewRequest "Google::Cloud::PolicySimulator::V1::GetOrgPolicyViolationsPreviewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::PolicySimulator::V1::GetOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-GetOrgPolicyViolationsPreviewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_org_policy_violations_preview(name: nil) -> ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview

Pass arguments to `get_org_policy_violations_preview` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the OrgPolicyViolationsPreview to get. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/policy_simulator/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::PolicySimulator::V1::GetOrgPolicyViolationsPreviewRequest.new
    
    # Call the get_org_policy_violations_preview method.
    result = client.get_org_policy_violations_preview request
    
    # The returned object is of type Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new OrgPolicyViolationsPreviewService REST client object.

**Yields**

  * (config) — Configure the OrgPolicyViolationsPreviewService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_org_policy_violations
    
    
    def list_org_policy_violations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation>
    def list_org_policy_violations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation>

ListOrgPolicyViolations lists the [OrgPolicyViolations][] that are present in an [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)").

**Overloads**
    
    
    def list_org_policy_violations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation>

Pass arguments to `list_org_policy_violations` via a request object, either of type [ListOrgPolicyViolationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ListOrgPolicyViolationsRequest "Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ListOrgPolicyViolationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_org_policy_violations(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation>

Pass arguments to `list_org_policy_violations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The OrgPolicyViolationsPreview to get OrgPolicyViolations from. Format: organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreview} 
  * **page_size** (::Integer) — Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 1000 items will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.

When paginating, all other parameters must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolation)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/policy_simulator/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsRequest.new
    
    # Call the list_org_policy_violations method.
    result = client.list_org_policy_violations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolation.
      p item
    end

### #list_org_policy_violations_previews
    
    
    def list_org_policy_violations_previews(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview>
    def list_org_policy_violations_previews(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview>

ListOrgPolicyViolationsPreviews lists each [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") in an organization. Each [OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview "Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview \(class\)") is available for at least 7 days.

**Overloads**
    
    
    def list_org_policy_violations_previews(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview>

Pass arguments to `list_org_policy_violations_previews` via a request object, either of type [ListOrgPolicyViolationsPreviewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ListOrgPolicyViolationsPreviewsRequest "Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsPreviewsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsPreviewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ListOrgPolicyViolationsPreviewsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_org_policy_violations_previews(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview>

Pass arguments to `list_org_policy_violations_previews` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent the violations are scoped to. Format: `organizations/{organization}/locations/{location}`

Example: `organizations/my-example-org/locations/global`

  * **page_size** (::Integer) — Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 5 items will be returned. The maximum value is 10; values above 10 will be coerced to 10. 
  * **page_token** (::String) — Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.

When paginating, all other parameters must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreview)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/policy_simulator/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::PolicySimulator::V1::ListOrgPolicyViolationsPreviewsRequest.new
    
    # Call the list_org_policy_violations_previews method.
    result = client.list_org_policy_violations_previews request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreview.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::OrgPolicyViolationsPreviewService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-OrgPolicyViolationsPreviewService-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
