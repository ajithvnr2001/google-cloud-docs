---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-conditional-jump/
title: Conditional jump to a specific step \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:11.192206+00:00
---

# Conditional jump to a specific step  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-conditional-jump/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Conditional jump to a specific step Stay organized with collections  Save and categorize content based on your preferences. 

Jumps to a specific step depending on the value returned by the first step of the workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)



## Code sample

### YAML
    
    
    - first_step:
        call: http.get
        args:
          url: https://www.example.com/callA
        result: first_result
    - where_to_jump:
        switch:
          - condition: ${first_result.body.SomeField < 10}
            next: small
          - condition: ${first_result.body.SomeField < 100}
            next: medium
        next: large
    - small:
        call: http.get
        args:
          url: https://www.example.com/SmallFunc
        next: end
    - medium:
        call: http.get
        args:
          url: https://www.example.com/MediumFunc
        next: end
    - large:
        call: http.get
        args:
          url: https://www.example.com/LargeFunc
        next: end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
