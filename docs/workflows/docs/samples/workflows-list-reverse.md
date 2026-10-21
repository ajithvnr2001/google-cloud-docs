---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-list-reverse/
title: Reverse a list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:12.406120+00:00
---

# Reverse a list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-list-reverse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Reverse a list Stay organized with collections  Save and categorize content based on your preferences. 

Reverses the elements in a list.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Lists](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists)



## Code sample

### YAML
    
    
    # Reverse the order of elements in a list
    # Expected output: `[3,2,1]`
    main:
      steps:
        - call_reverse_list:
            call: reverse_list
            args:
              source: [1, 2, 3]
            result: output
        - return_message:
            return: ${output}
    
    reverse_list:
      params: [source]
      steps:
        - init:
            assign:
              - dst: []
        - reverse:
            for:
              value: entry
              in: ${source}
              steps:
                - prepend_value:
                    assign:
                      - dst: ${list.prepend(dst, entry)}
        - return_destination:
            return: ${dst}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
