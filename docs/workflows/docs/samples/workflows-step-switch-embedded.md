---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-switch-embedded/
title: Use an embedded switch statement to execute steps \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:23.710424+00:00
---

# Use an embedded switch statement to execute steps  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-switch-embedded/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use an embedded switch statement to execute steps Stay organized with collections  Save and categorize content based on your preferences. 

Uses a switch structure to directly execute steps when a condition is met, without jumping to other steps. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)



## Code sample

### YAML
    
    
    - step1:
        assign:
          - a: 1
    - step2:
        switch:
          - condition: ${a==1}
            steps:
              - stepA:
                  assign:
                    - a: ${a+7}
              - stepB:
                  return: ${"increase a to:"+string(a)}
    - step3:
        return: ${"default a="+string(a)}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
