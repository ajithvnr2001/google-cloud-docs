---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_predicate/
title: Function: http.default_retry_predicate \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:07.043037+00:00
---

# Function: http.default_retry_predicate  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_predicate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: http.default_retry_predicate Stay organized with collections  Save and categorize content based on your preferences. 

Simple default retry predicate for idempotent targets.

If your target is non-idempotent, use [default_retry_predicate_non_idempotent](https://cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_predicate_non_idempotent) instead.

Retries on `429` (Too Many Requests), `502` (Bad Gateway), `503` (Service unavailable), and `504` (Gateway Timeout), as well as on any `ConnectionError`, `ConnectionFailedError`, and `TimeoutError`.

For more information, see [Retry steps](https://cloud.google.com/workflows/docs/reference/syntax/retrying).

## Arguments

Arguments  
---  
`exception` | The error to apply the retry criterion upon.  
  
## Returns

`true` when the retry criterion is satisfied, `false` otherwise.

## Examples
    
    
    # Make an HTTP request using a standard retry predicate
    # and custom maximum retries and backoff parameters
    - read_item:
        try:
          call: http.get
          args:
            url: https://example.com/someapi
          result: api_response
        retry:
          predicate: ${http.default_retry_predicate}
          max_retries: 5
          backoff:
            initial_delay: 2
            max_delay: 60
            multiplier: 2

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
