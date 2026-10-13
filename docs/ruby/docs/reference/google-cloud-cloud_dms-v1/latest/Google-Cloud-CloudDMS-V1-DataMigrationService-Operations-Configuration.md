---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Operations-Configuration/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Operations::Configuration (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:25.611373+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Operations::Configuration (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Operations-Configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Operations::Configuration (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::DataMigrationService::Operations::Configuration.

Configuration class for the Operations API.

This class represents the configuration for Operations, providing control over timeouts, retry behavior, logging, transport parameters, and other low-level controls. Certain parameters can also be applied individually to specific RPCs. See Longrunning::Operations::Client::Configuration::Rpcs for a list of RPCs that can be configured independently.

Configuration can be applied globally to all clients, or to a single client on construction.

## Inherits

  * Object 



## Extended By

  * Gapic::Config 



## Example
    
    
    # Modify the global config, setting the timeout for
    # list_operations to 20 seconds,
    # and all remaining timeouts to 10 seconds.
    ::Google::Longrunning::Operations::Client.configure do |config|
      config.timeout = 10.0
      config.rpcs.list_operations.timeout = 20.0
    end
    
    # Apply the above configuration only to a new client.
    client = ::Google::Longrunning::Operations::Client.new do |config|
      config.timeout = 10.0
      config.rpcs.list_operations.timeout = 20.0
    end

## Methods 

### #channel_args
    
    
    def channel_args() -> ::Hash

Extra parameters passed to the gRPC channel. Note: this is ignored if a `GRPC::Core::Channel` object is provided as the credential.

**Returns**

  * (::Hash) 



### #channel_args=
    
    
    def channel_args=(value) -> ::Hash

Extra parameters passed to the gRPC channel. Note: this is ignored if a `GRPC::Core::Channel` object is provided as the credential.

**Parameter**

  * **value** (::Hash) 



**Returns**

  * (::Hash) 



### #channel_pool
    
    
    def channel_pool() -> ::Gapic::ServiceStub::ChannelPool::Configuration

Configuration for the channel pool

**Returns**

  * (::Gapic::ServiceStub::ChannelPool::Configuration) 



### #credentials
    
    
    def credentials() -> ::Object

Credentials to send with calls. You may provide any of the following types:

  * (`Google::Auth::Credentials`) A googleauth credentials object (see the [googleauth docs](https://rubydoc.info/gems/googleauth/Google/Auth/Credentials))
  * (`Signet::OAuth2::Client`) A signet oauth2 client object (see the [signet docs](https://rubydoc.info/gems/signet/Signet/OAuth2/Client))
  * (`GRPC::Core::Channel`) a gRPC channel with included credentials
  * (`GRPC::Core::ChannelCredentials`) a gRPC credentails object
  * (`nil`) indicating no credentials



external source for authentication to Google Cloud, you must validate it before providing it to a Google API client library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to [Validate credential configurations from external sources](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials).

**Returns**

  * (::Object) 



**Example**
    
    
    # The recommended way to provide credentials is to use the `make_creds` method
    # on the appropriate credentials class for your environment.
    
    require "googleauth"
    
    credentials = ::Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: ::File.open("/path/to/keyfile.json")
    )
    
    client = ::Google::Longrunning::Operations::Client.new do |config|
      config.credentials = credentials
    end

### #credentials=
    
    
    def credentials=(value) -> ::Object

Credentials to send with calls. You may provide any of the following types:

  * (`Google::Auth::Credentials`) A googleauth credentials object (see the [googleauth docs](https://rubydoc.info/gems/googleauth/Google/Auth/Credentials))
  * (`Signet::OAuth2::Client`) A signet oauth2 client object (see the [signet docs](https://rubydoc.info/gems/signet/Signet/OAuth2/Client))
  * (`GRPC::Core::Channel`) a gRPC channel with included credentials
  * (`GRPC::Core::ChannelCredentials`) a gRPC credentails object
  * (`nil`) indicating no credentials



external source for authentication to Google Cloud, you must validate it before providing it to a Google API client library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. For more information, refer to [Validate credential configurations from external sources](https://cloud.google.com/docs/authentication/external/externally-sourced-credentials).

**Parameter**

  * **value** (::Object) 



**Returns**

  * (::Object) 



**Example**
    
    
    # The recommended way to provide credentials is to use the `make_creds` method
    # on the appropriate credentials class for your environment.
    
    require "googleauth"
    
    credentials = ::Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: ::File.open("/path/to/keyfile.json")
    )
    
    client = ::Google::Longrunning::Operations::Client.new do |config|
      config.credentials = credentials
    end

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



### #interceptors
    
    
    def interceptors() -> ::Array<::GRPC::ClientInterceptor>

An array of interceptors that are run before calls are executed.

**Returns**

  * (::Array<::GRPC::ClientInterceptor>) 



### #interceptors=
    
    
    def interceptors=(value) -> ::Array<::GRPC::ClientInterceptor>

An array of interceptors that are run before calls are executed.

**Parameter**

  * **value** (::Array<::GRPC::ClientInterceptor>) 



**Returns**

  * (::Array<::GRPC::ClientInterceptor>) 



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

Additional gRPC headers to be sent with the call.

**Returns**

  * (::Hash{::Symbol=>::String}) 



### #metadata=
    
    
    def metadata=(value) -> ::Hash{::Symbol=>::String}

Additional gRPC headers to be sent with the call.

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

  * ([Rpcs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Operations-Configuration-Rpcs)) 



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
