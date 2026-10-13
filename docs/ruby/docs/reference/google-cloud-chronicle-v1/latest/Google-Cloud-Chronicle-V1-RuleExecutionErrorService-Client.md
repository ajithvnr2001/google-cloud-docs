---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:17.964665+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.

Client for the RuleExecutionErrorService service.

RuleExecutionErrorService contains endpoints related to rule execution errors.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the RuleExecutionErrorService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration "Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all RuleExecutionErrorService clients
    ::Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the RuleExecutionErrorService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client#Google__Cloud__Chronicle__V1__RuleExecutionErrorService__Client_configure_class_ "Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration "Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new RuleExecutionErrorService client object.

**Yields**

  * (config) — Configure the RuleExecutionErrorService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionErrorService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_rule_execution_errors
    
    
    def list_rule_execution_errors(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Chronicle::V1::RuleExecutionError>
    def list_rule_execution_errors(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Chronicle::V1::RuleExecutionError>

Lists rule execution errors.

**Overloads**
    
    
    def list_rule_execution_errors(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Chronicle::V1::RuleExecutionError>

Pass arguments to `list_rule_execution_errors` via a request object, either of type [ListRuleExecutionErrorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListRuleExecutionErrorsRequest "Google::Cloud::Chronicle::V1::ListRuleExecutionErrorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListRuleExecutionErrorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListRuleExecutionErrorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_rule_execution_errors(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Chronicle::V1::RuleExecutionError>

Pass arguments to `list_rule_execution_errors` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance to list rule execution errors from. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **page_size** (::Integer) — The maximum number of rule execution errors to return. The service may return fewer than this value. If unspecified, at most 1000 rule execution errors will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000. 
  * **page_token** (::String) — A page token, received from a previous `ListRuleExecutionErrors` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListRuleExecutionErrors` must match the call that provided the page token. 

  * **filter** (::String) — A filter that can be used to retrieve specific rule execution errors. Only the following filters are allowed: ` rule = "{Rule.name}" curated_rule = "{CuratedRule.name}" ` The value for rule or curated_rule must be a valid rule resource name or a valid curated rule resource name specified in quotes.

For 'rule', an optional 'revision_id' can be specified which can be used to fetch errors for a given revision of the rule. A '-' is also allowed to fetch errors across all revisions of the rule. If unspecified, only errors corresponding to the most recent revision of the rule will be returned. So these variations are all allowed: ` rule = "{Rule.name}" rule = "{Rule.name}@{Rule.revision_id}" rule = "{Rule.name}@-" ` Revision IDs are not supported for curated rules. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Chronicle::V1::RuleExecutionError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionError)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Chronicle::V1::RuleExecutionError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RuleExecutionError)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::RuleExecutionErrorService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListRuleExecutionErrorsRequest.new
    
    # Call the list_rule_execution_errors method.
    result = client.list_rule_execution_errors request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::RuleExecutionError.
      p item
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
