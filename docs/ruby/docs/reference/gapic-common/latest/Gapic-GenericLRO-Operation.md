---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation/
title: gapic-common - Class Gapic::GenericLRO::Operation (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:10.861703+00:00
---

# gapic-common - Class Gapic::GenericLRO::Operation (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::GenericLRO::Operation (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::GenericLRO::Operation.

A class used to wrap the longrunning operation objects, including the nonstandard ones (`nonstandard` meaning not conforming to the AIP-151). It provides helper methods to poll and check for status of these operations.

## Inherits

  * [Gapic::GenericLRO::BaseOperation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-BaseOperation)



## Methods 

### #done?
    
    
    def done?() -> Boolean

Checks if the operation is done. This does not send a new api call, but checks the result of the previous api call to see if done.

**Returns**

  * (Boolean) — Whether the operation is done. 



### #error
    
    
    def error() -> Object, nil

If the operation response is an error, the error will be returned, otherwise returns nil.

**Returns**

  * (Object, nil) — The error object. 



### #error?
    
    
    def error?() -> Boolean

Checks if the operation is done and the result is an error. If the operation is not finished then this will return false.

**Returns**

  * (Boolean) — Whether an error has been returned. 



### #initialize
    
    
    def initialize(operation, client:, polling_method_name:, operation_status_field:, request_values: {}, operation_name_field: nil, operation_err_field: nil, operation_err_code_field: nil, operation_err_msg_field: nil, operation_copy_fields: {}, options: {}) -> Operation

**Parameters**

  * **operation** (Object) — The long-running operation object that is returned by the initial method call. 
  * **client** (Object) — The client that handles the polling for the longrunning operation. 
  * **polling_method_name** (String) — The name of the methods on the client that polls the longrunning operation. 
  * **operation_status_field** (String) — The name of the `status` field in the underlying long-running operation object. The `status` field signals that the operation has finished. It should either contain symbols, and be set to `:DONE` when finished or contain a boolean and be set to `true` when finished. 
  * **request_values** (Map<String, String>) _(defaults to: {})_ — The values that are to be copied from the request that triggered the longrunning operation, into the request that polls for the longrunning operation. The format is `name of the request field` -> `value`
  * **operation_name_field** (String, nil) _(defaults to: nil)_ — The name of the `name` field in the underlying long-running operation object. Optional. 
  * **operation_err_field** (String, nil) _(defaults to: nil)_ — The name of the `error` field in the underlying long-running operation object. The `error` field should be a message-type, and have same semantics as `google.rpc.Status`, including an integer `code` subfield, that carries an error code. If the `operation_err_field` field is given, the `operation_err_code_field` and `operation_err_msg_field` parameters are ignored. Optional. 
  * **operation_err_code_field** (String, nil) _(defaults to: nil)_ — The name of the `error_code` field in the underlying long-running operation object. It is ignored if `operation_err_field` is given. Optional. 
  * **operation_err_msg_field** (String, nil) _(defaults to: nil)_ — The name of the `error_message` field in the underlying long-running operation object. It is ignored if `operation_err_field` is given. Optional. 
  * **operation_copy_fields** (Map<String, String>) _(defaults to: {})_ — The map of the fields that need to be copied from the long-running operation object that the polling method returns to the polling request. The format is `name of the operation object field` -> `name of the request field` (`from` -> `to`) 
  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions)) _(defaults to: {})_ — call options for this operation 



**Returns**

  * ([Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation)) — a new instance of Operation 



### #name
    
    
    def name() -> String, nil

Returns the name of the operation, if specified.

**Returns**

  * (String, nil) — The name of the operation. 



### #on_done
    
    
    def on_done(&block) { |operation| ... }

Registers a callback to be run when a refreshed operation is marked as done. If the operation has completed prior to a call to this function the callback will be called instead of registered.

**Yield Parameter**

  * **operation** ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Yields the finished Operation. 



### #on_reload
    
    
    def on_reload(&block) { |operation| ... }

Registers a callback to be run when an operation is being reloaded. If the operation has completed prior to a call to this function the callback will NOT be called or registered.

**Yield Parameter**

  * **operation** ([Gapic::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation)) — Yields the finished Operation. 



### #refresh!
    
    
    def refresh!(options: nil) -> Gapic::GenericLRO::Operation

**Alias Of** : [#reload!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation#Gapic__GenericLRO__Operation_reload!_instance_)

Reloads the operation object.

to customize the options object, using keys that match the arguments for CallOptions.new.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided 



**Returns**

  * ([Gapic::GenericLRO::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation)) — Since this method changes internal state, it returns itself. 



### #reload!
    
    
    def reload!(options: nil) -> Gapic::GenericLRO::Operation

**Aliases**

  * [#refresh!](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation#Gapic__GenericLRO__Operation_refresh!_instance_)



Reloads the operation object.

to customize the options object, using keys that match the arguments for CallOptions.new.

**Parameter**

  * **options** ([Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: nil)_ — The options for making the RPC call. A Hash can be provided 



**Returns**

  * ([Gapic::GenericLRO::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation)) — Since this method changes internal state, it returns itself. 



### #response
    
    
    def response() -> Object, nil

If the operation is completed successfully, returns the underlying operation object, otherwise returns nil.

**Returns**

  * (Object, nil) — The response of the operation. 



### #response?
    
    
    def response?() -> Boolean

Checks if the operation is done and the result is not an error. If the operation is not finished then this will return false.

**Returns**

  * (Boolean) — Whether a response has been returned. 



### #results
    
    
    def results() -> Object, nil

If the operation is done, returns the response. If the operation response is an error, the error will be returned. Otherwise returns nil.

**Returns**

  * (Object, nil) — The result of the operation or an error. 



### #wait_until_done!
    
    
    def wait_until_done!(retry_policy: nil) { |operation| ... }

Blocking method to wait until the operation has completed or the maximum timeout has been reached. Upon completion, registered callbacks will be called, then - if a block is given - the block will be called.

**Parameter**

  * **retry_policy** (RetryPolicy, Hash, Proc) _(defaults to: nil)_ — The policy for retry. A custom proc that takes the error as an argument and blocks can also be provided. 



**Yield Parameter**

  * **operation** ([Gapic::GenericLRO::Operation](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-GenericLRO-Operation)) — Yields the finished Operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
