---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-retry-predicate/
title: Handle errors with custom predicate \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:43.947475+00:00
---

# Handle errors with custom predicate  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-retry-predicate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Handle errors with custom predicate Stay organized with collections  Save and categorize content based on your preferences. 

Defines a custom error handler, including a custom predicate and custom backoff parameters. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)



## Code sample

### YAML
    
    
    # Define a custom error handler, custom predicate, and custom backoff parameters
    # The `my_own_predicate` subworkflow accepts a map as an argument and defines the
    # exception; it returns true if a retry; false, otherwise
    # Expected outcome: the execution fails and returns an HTTP 404 Not Found error
    main:
      steps:
        - read_item:
            try:
              call: http.get
              args:
                url: https://example.com/someapi
              result: api_response
            retry:
              predicate: ${my_own_predicate}
              max_retries: 5
              backoff:
                initial_delay: 2
                max_delay: 60
                multiplier: 2
        - last_step:
            return: "OK"
    
    my_own_predicate:
      params: [e]
      steps:
        - log_error_tags:
            call: sys.log
            args:
              data: ${e.tags}
              severity: "INFO"
        - log_error_message:
            call: sys.log
            args:
              data: ${e.message}
              severity: "INFO"
        - log_error_code:
            call: sys.log
            args:
              data: ${e.code}
              severity: "INFO"
        - what_to_repeat:
            switch:
              - condition: ${e.code == 202}
                return: true
        - otherwise:
            return: false

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
