---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-phishing_protection/latest/Google-Cloud-PhishingProtection/
title: Phishing Protection API - Module Google::Cloud::PhishingProtection (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:55.051537+00:00
---

# Phishing Protection API - Module Google::Cloud::PhishingProtection (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-phishing_protection/latest/Google-Cloud-PhishingProtection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Phishing Protection API - Module Google::Cloud::PhishingProtection (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.0  0.16.3  0.15.2  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Phishing Protection API module Google::Cloud::PhishingProtection.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-phishing_protection library.

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

  * (::Google::Cloud.configure.phishing_protection) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .phishing_protection_service
    
    
    def self.phishing_protection_service(version: :v1beta1, transport: :grpc, &block) -> ::Object

Create a new client object for PhishingProtectionService.

By default, this returns an instance of [Google::Cloud::PhishingProtection::V1beta1::PhishingProtectionService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-phishing_protection-v1beta1/latest/Google-Cloud-PhishingProtection-V1beta1-PhishingProtectionService-Client) for a gRPC client for version V1beta1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PhishingProtectionService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the PhishingProtectionService service. You can determine whether the method will succeed by calling [PhishingProtection.phishing_protection_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-phishing_protection/latest/Google-Cloud-PhishingProtection#Google__Cloud__PhishingProtection_phishing_protection_service_available__class_ "Google::Cloud::PhishingProtection.phishing_protection_service_available? \(method\)").

#### About PhishingProtectionService

Service to report phishing URIs.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1beta1)_ — The API version to connect to. Optional. Defaults to `:v1beta1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .phishing_protection_service_available?
    
    
    def self.phishing_protection_service_available?(version: :v1beta1, transport: :grpc) -> boolean

Determines whether the PhishingProtectionService service is supported by the current client. If true, you can retrieve a client object by calling [PhishingProtection.phishing_protection_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-phishing_protection/latest/Google-Cloud-PhishingProtection#Google__Cloud__PhishingProtection_phishing_protection_service_class_ "Google::Cloud::PhishingProtection.phishing_protection_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PhishingProtectionService service, or if the versioned client gem needs an update to support the PhishingProtectionService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1beta1)_ — The API version to connect to. Optional. Defaults to `:v1beta1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "0.18.1"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
