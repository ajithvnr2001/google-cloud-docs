---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-PollingHarness/
title: gapic-common - Class Gapic::Common::PollingHarness (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:22.746250+00:00
---

# gapic-common - Class Gapic::Common::PollingHarness (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-PollingHarness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Common::PollingHarness (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Common::PollingHarness.

Provides a generic mechanism for periodic polling an operation.

Polling intervals are calculated from the provided retry policy.

Supports exponential backoff via `multiplier`, and automatically retries gRPC errors listed in `retry_codes`.

## Inherits

  * Object 



## Methods 

### #initialize
    
    
    def initialize(retry_policy: nil, **kwargs) -> PollingHarness

Create new Gapic::Common::PollingHarness instance.

**Parameters**

  * **retry_policy** ([Gapic::Common::RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy)) _(defaults to: nil)_ — The retry policy to use. If not provided, a new retry policy is constructed from the given kwargs. 
  * **kwargs** (keywords) — Keyword arguments used to create a new retry policy. See [RetryPolicy#initialize](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_initialize_instance_ "Gapic::Common::RetryPolicy#initialize \(method\)"). 



**Returns**

  * ([PollingHarness](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-PollingHarness)) — a new instance of PollingHarness 



### #retry_policy
    
    
    def retry_policy() -> Gapic::Common::RetryPolicy

**Returns**

  * ([Gapic::Common::RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy)) — The retry policy associated with this instance. 



### #wait
    
    
    def wait(wait_sentinel: nil, timeout_result: nil, mock_delay: false)

Perform polling with exponential backoff. Repeatedly calls the given block until it returns a result other than the given sentinel value (normally `nil`), then returns that final result.

Uses the retry policy regulate retries, including delays between tries, retriable errors, and final timeout. If an error code other than those listed in [RetryPolicy#retry_codes](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy#Gapic__Common__RetryPolicy_retry_codes_instance_ "Gapic::Common::RetryPolicy#retry_codes \(method\)") is raised, it is propagated out. If the timeout expires, the given timeout result (normally `nil`) is returned.

**Parameters**

  * **wait_sentinel** (Object) _(defaults to: nil)_ — The return value that should signal the polling harness to continue waiting. Any other value is treated as a real result and returned. Defaults to `nil`. 
  * **timeout_result** (Object) _(defaults to: nil)_ — The result to return if timeout occurs. Defaults to `nil`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
