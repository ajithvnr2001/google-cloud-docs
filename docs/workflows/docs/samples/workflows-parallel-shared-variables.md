---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-shared-variables/
title: Demonstrate variable scope in a parallel step \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:41.958626+00:00
---

# Demonstrate variable scope in a parallel step  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-shared-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Demonstrate variable scope in a parallel step Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates the scope of a shared variable, as well as variables that are local to their respective branch scopes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)



## Code sample

### YAML
    
    
    - assignStep:  # these variables can be read by any branch
        assign:
          - input: ["apples", "oranges"]
          - my_result: {}
    - parallelStep:
        parallel:
          shared: [my_result]  # my_result is now writable by any branch
          branches:
            - getStock:
                steps:
                  - callGetStock:
                      call: http.get
                      args:
                        url: ${"http://mystore.com/getStock/" + input[0]}
                      result: local_result  # local_result is local to this branch scope
                  - assignResult1:
                      assign:
                        - my_result["getStock"]: ${local_result.body.some.entry}  # ok, my_result has shared scope and is writable
                        - temp: 1  # ok, variable is local to branch scope
                        - temp2: "foo"  # ok, variable is local to branch scope
                      # - input: 5  # deployment error, defined in the parent scope but not marked "shared"
            - orderStock:
                steps:
                  - callOrderStock:
                      call: http.get
                      args:
                        url: ${"http://mystore.com/orderStock/" + input[1]}
                      result: local_result  # local_result is local to this branch
                  - assignResult2:
                      assign:
                        - my_result["orderStock"]: ${local_result.body.some.entry}  # ok, my_result has shared scope and is writable
                        - temp: 2  # ok, variable is local to branch scope
                      # - temp: ${temp2}  # deployment error, temp2 is not defined in this branch

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
