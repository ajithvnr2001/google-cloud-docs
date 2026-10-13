---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MigrationService-Rest-Client-Configuration/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client::Configuration (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:41.371470+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client::Configuration (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MigrationService-Rest-Client-Configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client::Configuration (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client::Configuration.

Configuration class for the MigrationService REST API.

This class represents the configuration for MigrationService REST, providing control over timeouts, retry behavior, logging, transport parameters, and other low-level controls. Certain parameters can also be applied individually to specific RPCs. See [Rpcs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MigrationService-Rest-Client-Configuration-Rpcs "Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client::Configuration::Rpcs \(class\)") for a list of RPCs that can be configured independently.

Configuration can be applied globally to all clients, or to a single client on construction.

## Inherits

  * Object 



## Extended By

  * Gapic::Config 



## Example
    
    
    # Modify the global config, setting the timeout for
    # search_migratable_resources to 20 seconds,
    # and all remaining timeouts to 10 seconds.
    ::Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client.configure do |config|
      config.timeout = 10.0
      config.rpcs.search_migratable_resources.timeout = 20.0
    end
    
    # Apply the above configuration only to a new client.
    client = ::Google::Cloud::AIPlatform::V1::MigrationService::Rest::Client.new do |config|
      config.timeout = 10.0
      config.rpcs.search_migratable_resources.timeout = 20.0
    end

## Methods 

### #credentials
    
    
    def credentials() -> ::Object

Credentials to send with calls. You may provide any of the following types:

  * (`String`) The path to a service account key file in JSON format
  * (`Hash`) A service account key as a Hash
  * (`Google::Auth::Credentials`) A googleauth credentials object (see the [googleauth docs](https://rubydoc.info/gems/googleauth/Google/Auth/Credentials))
  * (`Signet::OAuth2::Client`) A signet oauth2 client object (see the [signet docs](https://rubydoc.info/gems/signet/Signet/OAuth2/Client))
  * (`nil`) indicating no credentials



Warning: If you accept a credential configuration (JSON file or Hash) from an external source for authentication to Google Cloud, you must validate it before providing it to a Google API client library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to [Validate credential configurations from external sources](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials).

**Returns**

  * (::Object) 



### #credentials=
    
    
    def credentials=(value) -> ::Object

Credentials to send with calls. You may provide any of the following types:

  * (`String`) The path to a service account key file in JSON format
  * (`Hash`) A service account key as a Hash
  * (`Google::Auth::Credentials`) A googleauth credentials object (see the [googleauth docs](https://rubydoc.info/gems/googleauth/Google/Auth/Credentials))
  * (`Signet::OAuth2::Client`) A signet oauth2 client object (see the [signet docs](https://rubydoc.info/gems/signet/Signet/OAuth2/Client))
  * (`nil`) indicating no credentials



Warning: If you accept a credential configuration (JSON file or Hash) from an external source for authentication to Google Cloud, you must validate it before providing it to a Google API client library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to [Validate credential configurations from external sources](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials).

**Parameter**

  * **value** (::Object) 



**Returns**

  * (::Object) 



### #endpoint
    
    
    def endpoint() -> ::String, nil

A custom service endpoint, as a hostname or hostname:port. The default is nil, indicating to use the default endpoint in the current universe domain.

**Returns**

  * (::String, nil) 



### #endpoint=
    
    
    def endpoint=(value) -> ::String, nil

A custom service endpoint, as a hostname or hostname:port. The default is nil, indicating to use the default endpoint in the current universe domain.

**Parameter**

  * **value** (::String, nil) 



**Returns**

  * (::String, nil) 



### #lib_name
    
    
    def lib_name() -> ::String

The library name as recorded in instrumentation and logging

**Returns**

  * (::String) 



### #lib_name=
    
    
    def lib_name=(value) -> ::String

The library name as recorded in instrumentation and logging

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #lib_version
    
    
    def lib_version() -> ::String

The library version as recorded in instrumentation and logging

**Returns**

  * (::String) 



### #lib_version=
    
    
    def lib_version=(value) -> ::String

The library version as recorded in instrumentation and logging

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #logger
    
    
    def logger() -> ::Logger, :default, nil

A custom logger to use for request/response debug logging, or the value `:default` (the default) to construct a default logger, or `nil` to explicitly disable logging.

**Returns**

  * (::Logger, :default, nil) 



### #logger=
    
    
    def logger=(value) -> ::Logger, :default, nil

A custom logger to use for request/response debug logging, or the value `:default` (the default) to construct a default logger, or `nil` to explicitly disable logging.

**Parameter**

  * **value** (::Logger, :default, nil) 



**Returns**

  * (::Logger, :default, nil) 



### #metadata
    
    
    def metadata() -> ::Hash{::Symbol=>::String}

Additional headers to be sent with the call.

**Returns**

  * (::Hash{::Symbol=>::String}) 



### #metadata=
    
    
    def metadata=(value) -> ::Hash{::Symbol=>::String}

Additional headers to be sent with the call.

**Parameter**

  * **value** (::Hash{::Symbol=>::String}) 



**Returns**

  * (::Hash{::Symbol=>::String}) 



### #quota_project
    
    
    def quota_project() -> ::String

A separate project against which to charge quota.

**Returns**

  * (::String) 



### #quota_project=
    
    
    def quota_project=(value) -> ::String

A separate project against which to charge quota.

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #retry_policy
    
    
    def retry_policy() -> ::Hash

The retry policy. The value is a hash with the following keys:

  * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
  * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
  * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
  * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
  * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Returns**

  * (::Hash) 



### #retry_policy=
    
    
    def retry_policy=(value) -> ::Hash

The retry policy. The value is a hash with the following keys:

  * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
  * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
  * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
  * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
  * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Parameter**

  * **value** (::Hash) 



**Returns**

  * (::Hash) 



### #rpcs
    
    
    def rpcs() -> Rpcs

Configurations for individual RPCs

**Returns**

  * ([Rpcs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MigrationService-Rest-Client-Configuration-Rpcs)) 



### #scope
    
    
    def scope() -> ::Array<::String>

The OAuth scopes

**Returns**

  * (::Array<::String>) 



### #scope=
    
    
    def scope=(value) -> ::Array<::String>

The OAuth scopes

**Parameter**

  * **value** (::Array<::String>) 



**Returns**

  * (::Array<::String>) 



### #timeout
    
    
    def timeout() -> ::Numeric

The call timeout in seconds.

**Returns**

  * (::Numeric) 



### #timeout=
    
    
    def timeout=(value) -> ::Numeric

The call timeout in seconds.

**Parameter**

  * **value** (::Numeric) 



**Returns**

  * (::Numeric) 



### #universe_domain
    
    
    def universe_domain() -> ::String, nil

The universe domain within which to make requests. This determines the default endpoint URL. The default value of nil uses the environment universe (usually the default "googleapis.com" universe).

**Returns**

  * (::String, nil) 



### #universe_domain=
    
    
    def universe_domain=(value) -> ::String, nil

The universe domain within which to make requests. This determines the default endpoint URL. The default value of nil uses the environment universe (usually the default "googleapis.com" universe).

**Parameter**

  * **value** (::String, nil) 



**Returns**

  * (::String, nil) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
