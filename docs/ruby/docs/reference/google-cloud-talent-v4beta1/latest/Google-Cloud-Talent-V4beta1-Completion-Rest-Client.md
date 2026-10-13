---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client/
title: Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::Completion::Rest::Client (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:46.647598+00:00
---

# Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::Completion::Rest::Client (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::Completion::Rest::Client (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.1 (latest)  0.19.0  0.18.1  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Talent Solution V4beta1 API class Google::Cloud::Talent::V4beta1::Completion::Rest::Client.

REST client for the Completion service.

A service handles auto completion.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Talent::V4beta1::Completion::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Completion Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration "Google::Cloud::Talent::V4beta1::Completion::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Completion clients
    ::Google::Cloud::Talent::V4beta1::Completion::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #complete_query
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::Talent::V4beta1::CompleteQueryResponse
    def complete_query(parent: nil, query: nil, language_codes: nil, page_size: nil, company: nil, scope: nil, type: nil) -> ::Google::Cloud::Talent::V4beta1::CompleteQueryResponse

Completes the specified prefix with keyword suggestions. Intended for use by a job search auto-complete search box.

**Overloads**
    
    
    def complete_query(request, options = nil) -> ::Google::Cloud::Talent::V4beta1::CompleteQueryResponse

Pass arguments to `complete_query` via a request object, either of type [Google::Cloud::Talent::V4beta1::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest "Google::Cloud::Talent::V4beta1::CompleteQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Talent::V4beta1::CompleteQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def complete_query(parent: nil, query: nil, language_codes: nil, page_size: nil, company: nil, scope: nil, type: nil) -> ::Google::Cloud::Talent::V4beta1::CompleteQueryResponse

Pass arguments to `complete_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Resource name of tenant the completion is performed within.

The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenant/bar".

If tenant id is unspecified, the default tenant is used, for example, "projects/foo". 

  * **query** (::String) — Required. The query used to generate suggestions.

The maximum number of allowed characters is 255. 

  * **language_codes** (::Array<::String>) — The list of languages of the query. This is the BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).

The maximum number of allowed characters is 255. 

  * **page_size** (::Integer) — Required. Completion result count.

The maximum allowed page size is 10. 

  * **company** (::String) — If provided, restricts completion to specified company.

The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".

If tenant id is unspecified, the default tenant is used, for example, "projects/foo". 

  * **scope** ([::Google::Cloud::Talent::V4beta1::CompleteQueryRequest::CompletionScope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest-CompletionScope)) — The scope of the completion. The defaults is [CompletionScope.PUBLIC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest-CompletionScope#Google__Cloud__Talent__V4beta1__CompleteQueryRequest__CompletionScope__PUBLIC "Google::Cloud::Talent::V4beta1::CompleteQueryRequest::CompletionScope::PUBLIC \(constant\)"). 
  * **type** ([::Google::Cloud::Talent::V4beta1::CompleteQueryRequest::CompletionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest-CompletionType)) — The completion topic. The default is [CompletionType.COMBINED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryRequest-CompletionType#Google__Cloud__Talent__V4beta1__CompleteQueryRequest__CompletionType__COMBINED "Google::Cloud::Talent::V4beta1::CompleteQueryRequest::CompletionType::COMBINED \(constant\)"). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4beta1::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4beta1::CompleteQueryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CompleteQueryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/talent/v4beta1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Talent::V4beta1::Completion::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Talent::V4beta1::CompleteQueryRequest.new
    
    # Call the complete_query method.
    result = client.complete_query request
    
    # The returned object is of type Google::Cloud::Talent::V4beta1::CompleteQueryResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Completion Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client#Google__Cloud__Talent__V4beta1__Completion__Rest__Client_configure_class_ "Google::Cloud::Talent::V4beta1::Completion::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration "Google::Cloud::Talent::V4beta1::Completion::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Completion REST client object.

**Yields**

  * (config) — Configure the Completion client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Completion-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Talent::V4beta1::Completion::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Talent::V4beta1::Completion::Rest::Client.new do |config|
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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
