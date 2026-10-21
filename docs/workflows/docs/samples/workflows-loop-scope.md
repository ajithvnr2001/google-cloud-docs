---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-loop-scope/
title: Demonstrate local scope of variable created inside a for loop \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:12.324953+00:00
---

# Demonstrate local scope of variable created inside a for loop  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-loop-scope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Demonstrate local scope of variable created inside a for loop Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how any variable created in a loop does not exist outside of that loop.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)
  * [Variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables)



## Code sample

### YAML
    
    
    - init:
        assign:
          - workflowScope: foo
    - outerLoop:
        for:
          value: outerLoopValue  # outerLoopValue does not exist outside of outerLoop step
          in: [1, 2, 3, 4]
          steps:
            - outerLoopAssign:
                assign:
                  - outerLoopScope: ${workflowScope}  # outerLoopScope is a new variable and does not exist outside of outerLoop step
            - innerLoop:
                for:
                  value: innerLoopValue  # innerLoopValue does not exist outside of innerLoop step
                  in: [5, 6, 7, 8]
                  steps:
                    - innerLoopAssign:
                        assign:
                          - workflowScope: ${innerLoopValue}
                          - innerLoopScope: ${outerLoopScope}  # innerLoopScope is a new variable and does not exist outside of innerLoop step
    - final:
        return:
          - ${workflowScope}  # allowed
          # - ${outerLoopScope}  # not allowed
          # - ${innerLoopScope}  # not allowed
          # - ${outerLoopValue}  # not allowed

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
