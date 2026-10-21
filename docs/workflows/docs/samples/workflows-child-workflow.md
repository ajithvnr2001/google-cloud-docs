---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-child-workflow/
title: Execute other workflows in parallel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:45.546244+00:00
---

# Execute other workflows in parallel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-child-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Execute other workflows in parallel Stay organized with collections  Save and categorize content based on your preferences. 

Run a workflow that executes other workflows in parallel.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Run a workflow that executes other workflows in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/execute-workflows-from-workflow)
  * [Use a Cloud Tasks queue to buffer your workflow executions](https://docs.cloud.google.com/workflows/docs/tutorials/buffer-workflows-executions)



## Code sample

### YAML
    
    
    main:
      params: [args]
      steps:
        - init:
            assign:
              - iteration : ${args.iteration}
        - wait:
            call: sys.sleep
            args:
                seconds: 10
        - check_iteration_even_or_odd:
            switch:
              - condition: ${iteration % 2 == 0}
                next: raise_error
        - return_message:
            return: ${"Hello world"+iteration}
        - raise_error:
            raise: ${"Error with iteration "+iteration}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
