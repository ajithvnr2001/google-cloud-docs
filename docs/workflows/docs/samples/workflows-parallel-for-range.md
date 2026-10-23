---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-for-range/
title: Perform a parallel for:range loop \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:56.383808+00:00
---

# Perform a parallel for:range loop  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-for-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Perform a parallel for:range loop Stay organized with collections  Save and categorize content based on your preferences. 

Uses a parallel for:range loop to translate text, specifying the beginning and end of an iteration range.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Replace experimental function with parallel step](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel)



## Code sample

### YAML
    
    
    main:
      params: []
      steps:
        - init:
            assign:
              - workflow_id: "translate"
              - texts_to_translate:
                  - text: "hello world!"
                    source: "en"
                    target: "fr"
                  - text: "你好 世界！"
                    source: "zh-CN"
                    target: "en"
                  - text: "No hablo español!"
                    source: "es"
                    target: "en"
              - translated: ["", "", ""]  # to write to this variable, you must share it
        - parallel_translate:
            parallel:
              shared: [translated]
              for:
                range: ${[0, len(texts_to_translate) - 1]}
                value: i
                steps:
                  - translate:
                      call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run
                      args:
                        workflow_id: ${workflow_id}
                        argument: ${texts_to_translate[i]}
                      result: r
                  - set_result:
                      assign:
                        - translated[i]: ${r}
        - return:
            return: ${translated}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
