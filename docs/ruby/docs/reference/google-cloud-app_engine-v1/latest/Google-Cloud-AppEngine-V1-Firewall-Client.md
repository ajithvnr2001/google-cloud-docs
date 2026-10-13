---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Firewall::Client (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:24.176242+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Firewall::Client (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Firewall::Client (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Firewall::Client.

Client for the Firewall service.

Firewall resources are used to define a collection of access control rules for an Application. Each rule is defined with a position which specifies the rule's order in the sequence of rules, an IP range to be matched against requests, and an action to take upon matching requests.

Every request is evaluated against the Firewall rules in priority order. Processesing stops at the first rule which matches the request's IP address. A final rule always specifies an action that applies to all remaining IP addresses. The default final rule for a newly-created application will be set to "allow" if not otherwise specified by the user.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Firewall Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration "Google::Cloud::AppEngine::V1::Firewall::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Firewall clients
    ::Google::Cloud::AppEngine::V1::Firewall::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_update_ingress_rules
    
    
    def batch_update_ingress_rules(request, options = nil) -> ::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse
    def batch_update_ingress_rules(name: nil, ingress_rules: nil) -> ::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse

Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.

If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list.

**Overloads**
    
    
    def batch_update_ingress_rules(request, options = nil) -> ::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse

Pass arguments to `batch_update_ingress_rules` via a request object, either of type [BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BatchUpdateIngressRulesRequest "Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BatchUpdateIngressRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_update_ingress_rules(name: nil, ingress_rules: nil) -> ::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse

Pass arguments to `batch_update_ingress_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the Firewall collection to set. Example: `apps/myapp/firewall/ingressRules`. 
  * **ingress_rules** (::Array<[::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule), ::Hash>) — A list of FirewallRules to replace the existing set. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BatchUpdateIngressRulesResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-BatchUpdateIngressRulesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesRequest.new
    
    # Call the batch_update_ingress_rules method.
    result = client.batch_update_ingress_rules request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::BatchUpdateIngressRulesResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Firewall Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client#Google__Cloud__AppEngine__V1__Firewall__Client_configure_class_ "Google::Cloud::AppEngine::V1::Firewall::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration "Google::Cloud::AppEngine::V1::Firewall::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration)) 



### #create_ingress_rule
    
    
    def create_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule
    def create_ingress_rule(parent: nil, rule: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Creates a firewall rule for the application.

**Overloads**
    
    
    def create_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `create_ingress_rule` via a request object, either of type [CreateIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateIngressRuleRequest "Google::Cloud::AppEngine::V1::CreateIngressRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::CreateIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateIngressRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_ingress_rule(parent: nil, rule: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `create_ingress_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Name of the parent Firewall collection in which to create a new rule. Example: `apps/myapp/firewall/ingressRules`. 
  * **rule** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule), ::Hash) — A FirewallRule containing the new resource.

The user may optionally provide a position at which the new rule will be placed. The positions define a sequential list starting at 1. If a rule already exists at the given position, rules greater than the provided position will be moved forward by one.

If no position is provided, the server will place the rule as the second to last rule in the sequence before the required default allow-all or deny-all rule. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::CreateIngressRuleRequest.new
    
    # Call the create_ingress_rule method.
    result = client.create_ingress_rule request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::FirewallRule.
    p result

### #delete_ingress_rule
    
    
    def delete_ingress_rule(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_ingress_rule(name: nil) -> ::Google::Protobuf::Empty

Deletes the specified firewall rule.

**Overloads**
    
    
    def delete_ingress_rule(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_ingress_rule` via a request object, either of type [DeleteIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteIngressRuleRequest "Google::Cloud::AppEngine::V1::DeleteIngressRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::DeleteIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteIngressRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_ingress_rule(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_ingress_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the Firewall resource to delete. Example: `apps/myapp/firewall/ingressRules/100`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::DeleteIngressRuleRequest.new
    
    # Call the delete_ingress_rule method.
    result = client.delete_ingress_rule request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_ingress_rule
    
    
    def get_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule
    def get_ingress_rule(name: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Gets the specified firewall rule.

**Overloads**
    
    
    def get_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `get_ingress_rule` via a request object, either of type [GetIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetIngressRuleRequest "Google::Cloud::AppEngine::V1::GetIngressRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::GetIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetIngressRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_ingress_rule(name: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `get_ingress_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the Firewall resource to retrieve. Example: `apps/myapp/firewall/ingressRules/100`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::GetIngressRuleRequest.new
    
    # Call the get_ingress_rule method.
    result = client.get_ingress_rule request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::FirewallRule.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Firewall client object.

**Yields**

  * (config) — Configure the Firewall client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Firewall-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AppEngine::V1::Firewall::Client.new do |config|
      config.timeout = 10.0
    end

### #list_ingress_rules
    
    
    def list_ingress_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::FirewallRule>
    def list_ingress_rules(parent: nil, page_size: nil, page_token: nil, matching_address: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::FirewallRule>

Lists the firewall rules of an application.

**Overloads**
    
    
    def list_ingress_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::FirewallRule>

Pass arguments to `list_ingress_rules` via a request object, either of type [ListIngressRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListIngressRulesRequest "Google::Cloud::AppEngine::V1::ListIngressRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::ListIngressRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListIngressRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_ingress_rules(parent: nil, page_size: nil, page_token: nil, matching_address: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::FirewallRule>

Pass arguments to `list_ingress_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Name of the Firewall collection to retrieve. Example: `apps/myapp/firewall/ingressRules`. 
  * **page_size** (::Integer) — Maximum results to return per page. 
  * **page_token** (::String) — Continuation token for fetching the next page of results. 
  * **matching_address** (::String) — A valid IP Address. If set, only rules matching this address will be returned. The first returned rule will be the rule that fires on requests from this IP. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::ListIngressRulesRequest.new
    
    # Call the list_ingress_rules method.
    result = client.list_ingress_rules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AppEngine::V1::FirewallRule.
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



### #update_ingress_rule
    
    
    def update_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule
    def update_ingress_rule(name: nil, rule: nil, update_mask: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Updates the specified firewall rule.

**Overloads**
    
    
    def update_ingress_rule(request, options = nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `update_ingress_rule` via a request object, either of type [UpdateIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateIngressRuleRequest "Google::Cloud::AppEngine::V1::UpdateIngressRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::UpdateIngressRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateIngressRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_ingress_rule(name: nil, rule: nil, update_mask: nil) -> ::Google::Cloud::AppEngine::V1::FirewallRule

Pass arguments to `update_ingress_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the Firewall resource to update. Example: `apps/myapp/firewall/ingressRules/100`. 
  * **rule** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule), ::Hash) — A FirewallRule containing the updated resource 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Firewall::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::UpdateIngressRuleRequest.new
    
    # Call the update_ingress_rule method.
    result = client.update_ingress_rule request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::FirewallRule.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
