---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub/
title: gapic-common - Class Gapic::ServiceStub (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:16.028612+00:00
---

# gapic-common - Class Gapic::ServiceStub (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::ServiceStub (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::ServiceStub.

Gapic gRPC Stub

This class wraps the actual gRPC Stub and ChannelPool objects.

## Inherits

  * Object 



## Includes

  * [Gapic::LoggingConcerns](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-LoggingConcerns)
  * [Gapic::UniverseDomainConcerns](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-UniverseDomainConcerns)



## Methods 

### #call_rpc
    
    
    def call_rpc(method_name, request, options: nil, &block) { |response, operation| ... } -> Object

Invoke the specified RPC call.

**Parameters**

  * **method_name** (Symbol) — The RPC method name. 
  * **request** (Object) — The request object. 
  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. This object should only be used once. 



**Yields**

  * (response, operation) — Access the response along with the RPC operation. 



**Yield Parameters**

  * **response** (Object) — The response object. 
  * **operation** (::GRPC::ActiveCall::Operation) — The RPC operation for the response. 



**Returns**

  * (Object) — The response object. 



**Examples**
    
    
    require "google/showcase/v1beta1/echo_pb"
    require "google/showcase/v1beta1/echo_services_pb"
    require "gapic"
    require "gapic/grpc"
    
    echo_channel = ::GRPC::Core::Channel.new(
      "localhost:7469", nil, :this_channel_is_insecure
    )
    echo_stub = Gapic::ServiceStub.new(
      Google::Showcase::V1beta1::Echo::Stub,
      endpoint: "localhost:7469", credentials: echo_channel
    )
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    response = echo_stub.call_rpc :echo, request

Using custom call options:
    
    
    require "google/showcase/v1beta1/echo_pb"
    require "google/showcase/v1beta1/echo_services_pb"
    require "gapic"
    require "gapic/grpc"
    
    echo_channel = ::GRPC::Core::Channel.new(
      "localhost:7469", nil, :this_channel_is_insecure
    )
    echo_stub = Gapic::ServiceStub.new(
      Google::Showcase::V1beta1::Echo::Stub,
      endpoint: "localhost:7469", credentials: echo_channel
    )
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    options = Gapic::CallOptions.new(
      retry_policy = {
        retry_codes: [::GRPC::Core::StatusCodes::UNAVAILABLE]
      }
    )
    response = echo_stub.call_rpc :echo, request
                                  options: options

Accessing the response and RPC operation using a block:
    
    
    require "google/showcase/v1beta1/echo_pb"
    require "google/showcase/v1beta1/echo_services_pb"
    require "gapic"
    require "gapic/grpc"
    
    echo_channel = ::GRPC::Core::Channel.new(
      "localhost:7469", nil, :this_channel_is_insecure
    )
    echo_stub = Gapic::ServiceStub.new(
      Google::Showcase::V1beta1::Echo::Stub,
      endpoint: "localhost:7469", credentials: echo_channel
    )
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    echo_stub.call_rpc :echo, request do |response, operation|
      operation.trailing_metadata
    end

### #channel_pool
    
    
    def channel_pool() -> Gapic::ServiceStub::ChannelPool

**Returns**

  * (Gapic::ServiceStub::ChannelPool) — The instance of the ChannelPool class. 



### #create_channel_pool
    
    
    def create_channel_pool(grpc_stub_class, endpoint:, credentials:, channel_args: nil, interceptors: nil, channel_pool_config: nil)

### #create_grpc_stub
    
    
    def create_grpc_stub(grpc_stub_class, endpoint:, credentials:, channel_args: nil, interceptors: nil)

### #grpc_stub
    
    
    def grpc_stub() -> Object

**Returns**

  * (Object) — The instance of the gRPC stub class (`grpc_stub_class`) constructor argument. 



### #initialize
    
    
    def initialize(grpc_stub_class, credentials:, endpoint: nil, endpoint_template: nil, universe_domain: nil, channel_args: nil, interceptors: nil, channel_pool_config: nil, logger: :default) -> ServiceStub

Creates a Gapic gRPC stub object.

**Parameters**

  * **grpc_stub_class** (Class) — gRPC stub class to create a new instance of. 
  * **endpoint** (String) _(defaults to: nil)_ — The endpoint of the API. Overrides any endpoint_template. 
  * **endpoint_template** (String) _(defaults to: nil)_ — The endpoint of the API, where the universe domain component of the hostname is marked by the string in the constant [UniverseDomainConcerns::ENDPOINT_SUBSTITUTION](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-UniverseDomainConcerns#Gapic__UniverseDomainConcerns__ENDPOINT_SUBSTITUTION "Gapic::UniverseDomainConcerns::ENDPOINT_SUBSTITUTION \(constant\)"). 
  * **universe_domain** (String) _(defaults to: nil)_ — The universe domain in which calls should be made. Defaults to `googleapis.com`. 
  * **credentials** (Google::Auth::Credentials, Signet::OAuth2::Client, String, Hash, Proc, ::GRPC::Core::Channel, ::GRPC::Core::ChannelCredentials) — 

Provides the means for authenticating requests made by the client. This parameter can be many types:

    * A `Google::Auth::Credentials` uses a the properties of its represented keyfile for authenticating requests made by this client.
    * A `Signet::OAuth2::Client` object used to apply the OAuth credentials.
    * A `::GRPC::Core::Channel` will be used to make calls through.
    * A `::GRPC::Core::ChannelCredentials` for the setting up the RPC client. The channel credentials should already be composed with a `::GRPC::Core::CallCredentials` object.
    * A `Proc` will be used as an updater_proc for the Grpc channel. The proc transforms the metadata for requests, generally, to give OAuth credentials.
  * **channel_args** (Hash) _(defaults to: nil)_ — The channel arguments. (This argument is ignored when `credentials` is provided as a `::GRPC::Core::Channel`.) 
  * **interceptors** (Array<::GRPC::ClientInterceptor>) _(defaults to: nil)_ — An array of GRPC::ClientInterceptor objects that will be used for intercepting calls before they are executed Interceptors are an EXPERIMENTAL API. 
  * **channel_pool_config** (::Gapic::ServiceStub:ChannelPool::Configuration) _(defaults to: nil)_ — The configuration for channel pool. This argument will raise error when `credentials` is provided as a `::GRPC::Core::Channel`. 
  * **logger** (Logger, :default, nil) _(defaults to: :default)_ — An explicit logger to use, or one of the values `:default` (the default) to construct a default logger, or `nil` to disable logging explicitly. 



**Returns**

  * ([ServiceStub](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub)) — a new instance of ServiceStub 



**Raises**

  * (ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
