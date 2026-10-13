---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy/
title: gapic-common - Class Gapic::Common::RetryPolicy (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:09.602310+00:00
---

# gapic-common - Class Gapic::Common::RetryPolicy (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Common::RetryPolicy (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Common::RetryPolicy.

Gapic Common retry policy base class.

A policy distinguishes "set to this value" from "never set". Every setting is stored as `nil` until someone supplies it, and the reader for each substitutes the corresponding `DEFAULT_` constant on the way out, so a reader can never say which of the two happened. That distinction is what lets [#apply_defaults](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_apply_defaults_instance_ "Gapic::Common::RetryPolicy#apply_defaults \(method\)") fill in gaps without overwriting a caller's choices, and [#overrides](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_overrides_instance_ "Gapic::Common::RetryPolicy#overrides \(method\)") report what a caller actually asked for.

## Inherits

  * Object 



## Methods 

### #call
    
    
    def call(error = nil) -> Boolean

**Aliases**

  * [#perform_delay](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_perform_delay_instance_)



Perform delay if and only if retriable.

If positional argument `error` is provided, the retriable logic uses `retry_codes`. Otherwise, `timeout` is used.

**Returns**

  * (Boolean) — Whether the delay was executed. 



### #delay
    
    
    def delay() -> Numeric

Current delay value in seconds.

**Returns**

  * (Numeric) — Time delay in seconds. 



### #dup
    
    
    def dup() -> RetryPolicy

Returns a duplicate in a non-executing state, i.e. with the deadline and current delay reset.

**Returns**

  * ([RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy)) 



### #initial_delay
    
    
    def initial_delay() -> Numeric

**Returns**

  * (Numeric) — Initial delay in seconds. 



### #initialize
    
    
    def initialize(initial_delay: nil, max_delay: nil, multiplier: nil, retry_codes: nil, timeout: nil, jitter: nil, retry_predicate: nil) -> RetryPolicy

Create new Gapic::Common::RetryPolicy instance.

**Parameters**

  * **initial_delay** (Numeric) _(defaults to: nil)_ — Initial delay in seconds. 
  * **max_delay** (Numeric) _(defaults to: nil)_ — Maximum delay in seconds. 
  * **multiplier** (Numeric) _(defaults to: nil)_ — The delay scaling factor for each subsequent retry attempt. 
  * **retry_codes** (Array<String|Integer>) _(defaults to: nil)_ — List of retry codes. 
  * **timeout** (Numeric) _(defaults to: nil)_ — Timeout threshold value in seconds. 
  * **jitter** (Numeric) _(defaults to: nil)_ — Random jitter added to the delay in seconds. 
  * **retry_predicate** (Proc, nil) _(defaults to: nil)_ — The predicate to evaluate whether to retry on a given error. Optional. If the predicate is specified, it is run first. If it returns nil, the decision on whether to retry is made on the basis of retry_codes. Otherwise, the truthiness of the return value determines whether to retry. 



**Returns**

  * ([RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy)) — a new instance of RetryPolicy 



**Raises**

  * (ArgumentError) 



### #jitter
    
    
    def jitter() -> Numeric

**Returns**

  * (Numeric) — Random jitter added to the delay in seconds. 



### #max_delay
    
    
    def max_delay() -> Numeric

**Returns**

  * (Numeric) — Maximum delay in seconds. 



### #multiplier
    
    
    def multiplier() -> Numeric

**Returns**

  * (Numeric) — The delay scaling factor for each subsequent retry attempt. 



### #perform_delay
    
    
    def perform_delay(error = nil) -> Boolean

**Alias Of** : [#call](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_call_instance_)

Perform delay if and only if retriable.

If positional argument `error` is provided, the retriable logic uses `retry_codes`. Otherwise, `timeout` is used.

**Returns**

  * (Boolean) — Whether the delay was executed. 



### #perform_delay!
    
    
    def perform_delay!() -> Boolean

Perform delay.

**Returns**

  * (Boolean) — Whether the delay was executed. 



### #perform_delay_count
    
    
    def perform_delay_count() -> Integer

Current number of times the delay has been performed

**Returns**

  * (Integer) 



### #retry_codes
    
    
    def retry_codes() -> Array<Integer>

**Returns**

  * (Array<Integer>) — List of retry codes. 



### #retry_predicate
    
    
    def retry_predicate() -> Proc, nil

The predicate to evaluate whether to retry on a given error. Optional.

When a predicate is specified:

  1. The predicate is executed first on the error.
  2. If it returns nil, the decision on whether to retry is made on the basis of retry_codes.
  3. Otherwise, the truthiness of the return value determines whether to retry.



**Returns**

  * (Proc, nil) 



### #start!
    
    
    def start!(mock_delay: false)

Start tracking the deadline and delay by initializing those values.

This is normally done when the object is constructed, but it can be done explicitly in order to reinitialize the state in case this retry policy was created in the past or is being reused.

**Parameter**

  * **mock_delay** (boolean, Proc) _(defaults to: false)_ — if truthy, delays are "mocked", meaning they do not actually take time, but are measured as if they did, which is useful for tests. If set to a Proc, it will be called whenever a delay would happen, and passed the delay in seconds, also useful for testing. 



### #timeout
    
    
    def timeout() -> Numeric

**Returns**

  * (Numeric) — Timeout threshold value in seconds. 



## Constants 

### DEFAULT_INITIAL_DELAY

**value:** 1

### DEFAULT_MAX_DELAY

**value:** 15

### DEFAULT_MULTIPLIER

**value:** 1.3

### DEFAULT_RETRY_CODES

**value:**[].freeze

### DEFAULT_TIMEOUT

**value:** 3600

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
