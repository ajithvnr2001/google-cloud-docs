---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation/
title: gapic-common - Class Gapic::Operation (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:12.287935+00:00
---

# gapic-common - Class Gapic::Operation (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Operation (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Operation.

A class used to wrap Google::Longrunning::Operation objects. This class provides helper methods to check the status of an Operation

## Inherits

  * Object 



## Examples

Checking Operation status
    
    
    # this example assumes both api_client and operations_client
    # already exist.
    require "gapic/operation"
    
    op = Gapic::Operation.new(
      api_client.method_that_returns_longrunning_operation(),
      operations_client,
      Google::Example::ResultType,
      Google::Example::MetadataType
    )
    
    op.done? # => false
    op.reload! # => operation completed
    
    if op.done?
      results = op.results
      handle_error(results) if op.error?
      # Handle results.
    end

Working with callbacks
    
    
    # this example assumes both api_client and operations_client
    # already exist.
    require "gapic/operation"
    
    op = Gapic::Operation.new(
      api_client.method_that_returns_longrunning_operation(),
      operations_client,
      Google::Example::ResultType,
      Google::Example::MetadataType
    )
    
    # Register a callback to be run when an operation is done.
    op.on_done do |operation|
      raise operation.results.message if operation.error?
      # process(operation.results)
      # process(operation.metadata)
    end
    
    # Reload the operation running callbacks if operation completed.
    op.reload!
    
    # Or block until the operation completes, passing a block to be called
    # on completion.
    op.wait_until_done! do |operation|
      raise operation.results.message if operation.error?
      # process(operation.results)
      # process(operation.rmetadata)
    end

## Methods 

### #cancel
    
    
    def cancel(options: nil)

Cancels the operation.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. 



### #delete
    
    
    def delete(options: nil)

Deletes the operation.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. 



### #done?
    
    
    def done?() -> Boolean

Checks if the operation is done. This does not send a new api call, but checks the result of the previous api call to see if done.

**Returns**

  * (Boolean) — Whether the operation is done. 



### #error
    
    
    def error() -> Google::Rpc::Status, nil

If the operation response is an error, the error will be returned, otherwise returns nil.

**Returns**

  * (Google::Rpc::Status, nil) — The error object. 



### #error?
    
    
    def error?() -> Boolean

Checks if the operation is done and the result is an error. If the operation is not finished then this will return false.

**Returns**

  * (Boolean) — Whether an error has been returned. 



### #grpc_op
    
    
    def grpc_op() -> Google::Longrunning::Operation

**Returns**

  * (Google::Longrunning::Operation) — The wrapped grpc operation object. 



### #initialize
    
    
    def initialize(grpc_op, client, result_type: nil, metadata_type: nil, options: {}) -> Operation

**Parameters**

  * **grpc_op** (Google::Longrunning::Operation) — The inital longrunning operation. 
  * **client** (Google::Longrunning::OperationsClient) — The client that handles the grpc operations. 
  * **result_type** (Class) _(defaults to: nil)_ — The class type to be unpacked from the result. If not provided the class type will be looked up. Optional. 
  * **metadata_type** (Class) _(defaults to: nil)_ — The class type to be unpacked from the metadata. If not provided the class type will be looked up. Optional. 
  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions)) _(defaults to: {})_ — call options for this operation 



**Returns**

  * ([Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — a new instance of Operation 



### #metadata
    
    
    def metadata() -> Object, nil

Returns the metadata of an operation. If a type is provided, the metadata will be unpacked using the type provided; returning nil if the metadata is not of the type provided. If the type is not of provided, the metadata will be unpacked using the metadata's type_url if the type_url is found in the `Google::Protobuf::DescriptorPool.generated_pool`. If the type cannot be found the raw metadata is retuned.

**Returns**

  * (Object, nil) — The metadata of the operation. Can be nil. 



### #name
    
    
    def name() -> String

Returns the server-assigned name of the operation, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the name should have the format of operations/some/unique/name.

**Returns**

  * (String) — The name of the operation. 



### #on_done
    
    
    def on_done(&block) { |operation| ... }

Registers a callback to be run when a refreshed operation is marked as done. If the operation has completed prior to a call to this function the callback will be called instead of registered.

**Yield Parameter**

  * **operation** ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Yields the finished Operation. 



### #refresh!
    
    
    def refresh!(options: nil) -> Gapic::Operation

**Alias Of** : [#reload!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation#Gapic__Operation_reload!_instance_)

Reloads the operation object.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. 



**Returns**

  * ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Since this method changes internal state, it returns itself. 



### #reload!
    
    
    def reload!(options: nil) -> Gapic::Operation

**Aliases**

  * [#refresh!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation#Gapic__Operation_refresh!_instance_)



Reloads the operation object.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided to customize the options object, using keys that match the arguments for CallOptions.new. 



**Returns**

  * ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Since this method changes internal state, it returns itself. 



### #response
    
    
    def response() -> Object, nil

If the operation is done, returns the response, otherwise returns nil.

**Returns**

  * (Object, nil) — The response of the operation. 



### #response?
    
    
    def response?() -> Boolean

Checks if the operation is done and the result is a response. If the operation is not finished then this will return false.

**Returns**

  * (Boolean) — Whether a response has been returned. 



### #results
    
    
    def results() -> Object, Google::Rpc::Status, nil

If the operation is done, returns the response. If the operation response is an error, the error will be returned. Otherwise returns nil.

**Returns**

  * (Object, Google::Rpc::Status, nil) — The result of the operation. If it is an error a `Google::Rpc::Status` will be returned. 



### #wait_until_done!
    
    
    def wait_until_done!(retry_policy: nil) { |operation| ... }

Blocking method to wait until the operation has completed or the maximum timeout has been reached. Upon completion, registered callbacks will be called, then - if a block is given - the block will be called.

**Parameter**

  * **retry_policy** ([RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation-RetryPolicy), Hash, Proc) _(defaults to: nil)_ — The policy for retry. A custom proc that takes the error as an argument and blocks can also be provided. 



**Yield Parameter**

  * **operation** ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Yields the finished Operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
