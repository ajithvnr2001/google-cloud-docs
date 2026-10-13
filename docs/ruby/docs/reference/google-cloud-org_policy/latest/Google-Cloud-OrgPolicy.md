---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy/latest/Google-Cloud-OrgPolicy/
title: Organization Policy API - Module Google::Cloud::OrgPolicy (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:43.591602+00:00
---

# Organization Policy API - Module Google::Cloud::OrgPolicy (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy/latest/Google-Cloud-OrgPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Organization Policy API - Module Google::Cloud::OrgPolicy (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.3 

Reference documentation and code samples for the Organization Policy API module Google::Cloud::OrgPolicy.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-org_policy library.

The following configuration parameters are supported:

  * `credentials` (_type:_ `String, Hash, Google::Auth::Credentials`) - The path to the keyfile as a String, the contents of the keyfile as a Hash, or a Google::Auth::Credentials object.
  * `lib_name` (_type:_ `String`) - The library name as recorded in instrumentation and logging.
  * `lib_version` (_type:_ `String`) - The library version as recorded in instrumentation and logging.
  * `interceptors` (_type:_ `Array<GRPC::ClientInterceptor>`) - An array of interceptors that are run before calls are executed.
  * `timeout` (_type:_ `Numeric`) - Default timeout in seconds.
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers to be sent with the call.
  * `retry_policy` (_type:_ `Hash`) - The retry policy. The value is a hash with the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Yields**

  * (::Google::Cloud.configure.org_policy) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .org_policy
    
    
    def self.org_policy(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for OrgPolicy.

By default, this returns an instance of [Google::Cloud::OrgPolicy::V2::OrgPolicy::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-OrgPolicy-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the OrgPolicy service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the OrgPolicy service. You can determine whether the method will succeed by calling [OrgPolicy.org_policy_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy/latest/Google-Cloud-OrgPolicy#Google__Cloud__OrgPolicy_org_policy_available__class_ "Google::Cloud::OrgPolicy.org_policy_available? \(method\)").

#### About OrgPolicy

An interface for managing organization policies.

The Organization Policy Service provides a simple mechanism for organizations to restrict the allowed configurations across their entire resource hierarchy.

You can use a policy to configure restrictions on resources. For example, you can enforce a policy that restricts which Google Cloud APIs can be activated in a certain part of your resource hierarchy, or prevents serial port access to VM instances in a particular folder.

Policies are inherited down through the resource hierarchy. A policy applied to a parent resource automatically applies to all its child resources unless overridden with a policy lower in the hierarchy.

A constraint defines an aspect of a resource's configuration that can be controlled by an organization's policy administrator. Policies are a collection of constraints that defines their allowable configuration on a particular resource and its child resources.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .org_policy_available?
    
    
    def self.org_policy_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the OrgPolicy service is supported by the current client. If true, you can retrieve a client object by calling [OrgPolicy.org_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy/latest/Google-Cloud-OrgPolicy#Google__Cloud__OrgPolicy_org_policy_class_ "Google::Cloud::OrgPolicy.org_policy \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the OrgPolicy service, or if the versioned client gem needs an update to support the OrgPolicy service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "1.7.0"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
