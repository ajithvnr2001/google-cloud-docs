---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-map/
title: Use a for-in loop to iterate through a map \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:24.683695+00:00
---

# Use a for-in loop to iterate through a map  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use a for-in loop to iterate through a map Stay organized with collections  Save and categorize content based on your preferences. 

Uses a for-in loop to iterate through a map.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)



## Code sample

### YAML
    
    
    - assignStep:
        assign:
          - map:
              1: 10
              2: 20
              3: 30
          - sum: 0
    - loopStep:
        for:
          value: key                        # key = 1, 2, 3
          in: ${keys(map)}                  # [1, 2, 3]
          steps:
            - sumStep:
                assign:
                  - sum: ${sum + map[key]}
    - returnStep:
        return: ${sum}                      # sum is 60

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
