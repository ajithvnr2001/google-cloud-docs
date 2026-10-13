---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub-RpcCall/
title: gapic-common - Class Gapic::ServiceStub::RpcCall (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:15.921767+00:00
---

# gapic-common - Class Gapic::ServiceStub::RpcCall (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub-RpcCall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::ServiceStub::RpcCall (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::ServiceStub::RpcCall.

## Inherits

  * Object 



## Methods 

### #call
    
    
    def call(request, options: nil) { |response, operation| ... } -> Object

Invoke the RPC call.

**Parameters**

  * **request** (Object) — The request object. 
  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. This object should only be used once. 



**Yields**

  * (response, operation) — Access the response along with the RPC operation. Additionally, throwing `:response, obj` within the block will change the return value to `obj`. 



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
    echo_call = Gapic::ServiceStub::RpcCall.new echo_stub.method :echo
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    response = echo_call.call request

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
    echo_call = Gapic::ServiceStub::RpcCall.new echo_stub.method :echo
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    options = Gapic::CallOptions.new(
      retry_policy = {
        retry_codes: [::GRPC::Core::StatusCodes::UNAVAILABLE]
      }
    )
    response = echo_call.call request, options: options

Accessing the RPC operation using a block:
    
    
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
    echo_call = Gapic::ServiceStub::RpcCall.new echo_stub.method :echo
    
    request = Google::Showcase::V1beta1::EchoRequest.new
    metadata = echo_call.call request do |_response, operation|
      throw :response, operation.trailing_metadata
    end

### #initialize
    
    
    def initialize(stub_method, stub_logger: nil, method_name: nil) -> RpcCall

Creates an API object for making a single RPC call.

In typical usage, `stub_method` will be a proc used to make an RPC request. This will mostly likely be a bound method from a request Stub used to make an RPC call.

The result is created by applying a series of function decorators defined in this module to `stub_method`.

The result is another proc which has the same signature as the original.

**Parameter**

  * **stub_method** (Proc) — Used to make a bare rpc call. 



**Returns**

  * ([RpcCall](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-ServiceStub-RpcCall)) — a new instance of RpcCall 



### #stub_method
    
    
    def stub_method()

Returns the value of attribute stub_method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
