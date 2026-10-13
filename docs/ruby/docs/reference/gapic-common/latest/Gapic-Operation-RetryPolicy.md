---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation-RetryPolicy/
title: gapic-common - Class Gapic::Operation::RetryPolicy (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:11.535747+00:00
---

# gapic-common - Class Gapic::Operation::RetryPolicy (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation-RetryPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Operation::RetryPolicy (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Operation::RetryPolicy.

The policy for retrying operation reloads using an incremental backoff.

A new object instance should be used for every Operation invocation.

## Inherits

  * [Gapic::Common::RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Common-RetryPolicy)



## Methods 

### #initialize
    
    
    def initialize(initial_delay: nil, multiplier: nil, max_delay: nil, timeout: nil, jitter: nil) -> RetryPolicy

Create new Operation RetryPolicy.

**Parameters**

  * **initial_delay** (Numeric) _(defaults to: nil)_ — Initial delay in seconds. 
  * **multiplier** (Numeric) _(defaults to: nil)_ — The delay scaling factor for each subsequent retry attempt. 
  * **max_delay** (Numeric) _(defaults to: nil)_ — Maximum delay in seconds. 
  * **timeout** (Numeric) _(defaults to: nil)_ — Timeout threshold value in seconds. 
  * **jitter** (Numeric) _(defaults to: nil)_ — Random jitter added to the delay in seconds. 



**Returns**

  * ([RetryPolicy](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Operation-RetryPolicy)) — a new instance of RetryPolicy 



## Constants 

### DEFAULT_INITIAL_DELAY

**value:** 10

### DEFAULT_MAX_DELAY

**value:** 300

### DEFAULT_MULTIPLIER

**value:** 1.3

### DEFAULT_TIMEOUT

**value:** 3600

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
