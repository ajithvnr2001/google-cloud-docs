---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-inline/
title: Perform a parallel step with the secondary workflow inlined \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:11.759790+00:00
---

# Perform a parallel step with the secondary workflow inlined  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-parallel-inline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Perform a parallel step with the secondary workflow inlined Stay organized with collections  Save and categorize content based on your preferences. 

Includes the source code for a secondary workflow directly within the main workflow for easier readability.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Replace experimental function with parallel step](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel)



## Code sample

### YAML
    
    
    main:
      params: [args]
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
              - translated: ["", "", ""]
        - parallel_translate:
            parallel:
              shared: [translated]  # to write to this variable, you must share it
              for:
                range: ${[0, len(texts_to_translate) - 1]}
                value: i
                steps:
                  - basic_translate:
                      call: googleapis.translate.v2.translations.translate
                      args:
                        body:
                          q: ${args.text}
                          target: ${args.target}
                          format: "text"
                          source: ${args.source}
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
