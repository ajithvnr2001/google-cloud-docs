---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client/
title: Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Client (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:24.791357+00:00
---

# Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Client (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::Completion::Client (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.1  0.8.1  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Talent Solution V4 API class Google::Cloud::Talent::V4::Completion::Client.

Client for the Completion service.

A service handles auto completion.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Talent::V4::Completion::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Completion Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration "Google::Cloud::Talent::V4::Completion::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Completion clients
    ::Google::Cloud::Talent::V4::Completion::Client.configure do |config|
      config.timeout = 10.0
    end

### #complete_query
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::Talent::V4::CompleteQueryResponse
    def complete_query(tenant: nil, query: nil, language_codes: nil, page_size: nil, company: nil, scope: nil, type: nil) -> ::Google::Cloud::Talent::V4::CompleteQueryResponse

Completes the specified prefix with keyword suggestions. Intended for use by a job search auto-complete search box.

**Overloads**
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::Talent::V4::CompleteQueryResponse

Pass arguments to `complete_query` via a request object, either of type [Google::Cloud::Talent::V4::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest "Google::Cloud::Talent::V4::CompleteQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Talent::V4::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def complete_query(tenant: nil, query: nil, language_codes: nil, page_size: nil, company: nil, scope: nil, type: nil) -> ::Google::Cloud::Talent::V4::CompleteQueryResponse

Pass arguments to `complete_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **tenant** (::String) — Required. Resource name of tenant the completion is performed within.

The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar". 

  * **query** (::String) — Required. The query used to generate suggestions.

The maximum number of allowed characters is 255. 

  * **language_codes** (::Array<::String>) — The list of languages of the query. This is the BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).

The maximum number of allowed characters is 255. 

  * **page_size** (::Integer) — Required. Completion result count.

The maximum allowed page size is 10. 

  * **company** (::String) — If provided, restricts completion to specified company.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz". 

  * **scope** ([::Google::Cloud::Talent::V4::CompleteQueryRequest::CompletionScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest-CompletionScope)) — The scope of the completion. The defaults is [CompletionScope.PUBLIC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest-CompletionScope#Google__Cloud__Talent__V4__CompleteQueryRequest__CompletionScope__PUBLIC "Google::Cloud::Talent::V4::CompleteQueryRequest::CompletionScope::PUBLIC \(constant\)"). 
  * **type** ([::Google::Cloud::Talent::V4::CompleteQueryRequest::CompletionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest-CompletionType)) — The completion topic. The default is [CompletionType.COMBINED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryRequest-CompletionType#Google__Cloud__Talent__V4__CompleteQueryRequest__CompletionType__COMBINED "Google::Cloud::Talent::V4::CompleteQueryRequest::CompletionType::COMBINED \(constant\)"). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Talent::V4::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CompleteQueryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/talent/v4"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Talent::V4::Completion::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Talent::V4::CompleteQueryRequest.new
    
    # Call the complete_query method.
    result = client.complete_query request
    
    # The returned object is of type Google::Cloud::Talent::V4::CompleteQueryResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Completion Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client#Google__Cloud__Talent__V4__Completion__Client_configure_class_ "Google::Cloud::Talent::V4::Completion::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration "Google::Cloud::Talent::V4::Completion::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Completion client object.

**Yields**

  * (config) — Configure the Completion client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Completion-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Talent::V4::Completion::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Talent::V4::Completion::Client.new do |config|
      config.timeout = 10.0
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
