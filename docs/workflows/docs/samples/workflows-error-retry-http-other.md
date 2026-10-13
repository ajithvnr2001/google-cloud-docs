---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-retry-http-other/
title: Retry steps using a custom retry policy for an HTTP status code \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:21.455434+00:00
---

# Retry steps using a custom retry policy for an HTTP status code  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-error-retry-http-other/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Retry steps using a custom retry policy for an HTTP status code Stay organized with collections  Save and categorize content based on your preferences. 

Implements a custom retry policy that retries HTTP requests that return an HTTP status code 202.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)



## Code sample

### YAML
    
    
    main:
      steps:
        - read_item:
            try:
              steps:
                - callStep:
                    call: http.get
                    args:
                      url: https://host.com/api
                    result: api_response
                - checkNotOK:
                    switch:
                      - condition: ${api_response.code == 202}
                        raise: ${api_response}
            retry:
              predicate: ${custom_predicate}
              max_retries: 5
              backoff:
                initial_delay: 2
                max_delay: 60
                multiplier: 2
    
    custom_predicate:
      params: [e]
      steps:
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
