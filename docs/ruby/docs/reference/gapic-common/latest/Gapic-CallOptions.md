---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions/
title: gapic-common - Class Gapic::CallOptions (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:08.883885+00:00
---

# gapic-common - Class Gapic::CallOptions (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::CallOptions (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::CallOptions.

Encapsulates the overridable settings for a particular RPC call.

## Inherits

  * Object 



## Methods 

### #initialize
    
    
    def initialize(timeout: nil, metadata: nil, retry_policy: nil) -> CallOptions

Create a new Options object instance.

**Parameters**

  * **timeout** (Numeric) _(defaults to: nil)_ — The client-side timeout for RPC calls. 
  * **metadata** (Hash) _(defaults to: nil)_ — The request header params. 
  * **retry_policy** (Hash, [RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions-RetryPolicy), Proc) _(defaults to: nil)_ — The policy for error retry. A Hash can be provided to customize the policy object, using keys that match the arguments for [RetryPolicy#initialize](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions-RetryPolicy#Gapic__CallOptions__RetryPolicy_initialize_instance_ "Gapic::CallOptions::RetryPolicy#initialize \(method\)").

A Proc object can also be provided. The Proc should accept an error as an argument, and return `true` if the error should be retried or `false` if not. If the error is to be retried, the Proc object must also block with an incremental delay before returning `true`. 




**Returns**

  * ([CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions)) — a new instance of CallOptions 



### #merge
    
    
    def merge(**kwargs) -> CallOptions

Return a new CallOptions with the given modifications. The current object is not modified.

**Parameter**

  * **kwargs** (keywords) — Updated fields. See [#initialize](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions#Gapic__CallOptions_initialize_instance_ "Gapic::CallOptions#initialize \(method\)") for details. 



**Returns**

  * ([CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions)) — A new CallOptions object. 



### #metadata
    
    
    def metadata() -> Hash

**Returns**

  * (Hash) 



### #retry_policy
    
    
    def retry_policy() -> RetryPolicy, Object

**Returns**

  * ([RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions-RetryPolicy), Object) 



### #timeout
    
    
    def timeout() -> Numeric, nil

**Returns**

  * (Numeric, nil) 



### #to_h
    
    
    def to_h() -> Hash

Convert to hash form.

**Returns**

  * (Hash) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
