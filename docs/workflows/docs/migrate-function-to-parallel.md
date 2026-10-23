---
url: https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel/
title: Replace experimental function with parallel\u00a0step \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:09.454770+00:00
---

# Replace experimental function with parallel step  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Replace experimental function with parallel step Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows [experimental function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/map), `experimental.executions.map`, starts a workflow execution for each corresponding argument, and waits for all of the executions to finish, returning a list where each element is the result of an execution.

If you are using `experimental.executions.map` to support parallel work, you can migrate your workflow to use parallel steps instead, executing ordinary [`for` loops](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration) in parallel.

A `parallel` step defines a part of your workflow where two or more steps can execute concurrently. A `parallel` step waits until all the steps defined within it have completed or are interrupted by an unhandled exception; execution then continues. Like `experimental.executions.map`, the execution order is not guaranteed. For details, see the syntax reference page for [parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps).

Note that the use of `experimental.executions.map` or `workflows.executions.run` requires additional [concurrent executions quota](https://docs.cloud.google.com/workflows/quotas#quotas). However, when using parallel steps with calls to connectors inlined (see the translation connector example), no additional execution quota is required.

The following examples are intended to assist you when replacing the use of `experimental.executions.map` with a `parallel` step.

## Translation workflow

Given a source and target language, the following workflow, named `translate`, uses the [Cloud Translation connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/translate/Overview) to translate some input text and return the result. Note that the Cloud Translation API must be enabled.

### YAML
    
    
      main:
        params: [args]
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
        - return_step:
            return: ${r}

### JSON
    
    
      {
        "main": {
          "params": [
            "args"
          ],
          "steps": [
            {
              "basic_translate": {
                "call": "googleapis.translate.v2.translations.translate",
                "args": {
                  "body": {
                    "q": "${args.text}",
                    "target": "${args.target}",
                    "format": "text",
                    "source": "${args.source}"
                  }
                },
                "result": "r"
              }
            },
            {
              "return_step": {
                "return": "${r}"
              }
            }
          ]
        }
      }

Input for the preceding example:
    
    
    {
      "text": "Bonjour",
      "target": "en",
      "source": "fr"
    }

The output should resemble the following:
    
    
    {
     "data": {
       "translations": [
         {
           "translatedText": "Hello"
         }
       ]
     }
    }

## Batch translation workflow using `experimental.executions.map`

The following workflow translates a batch of texts. For each input, `experimental.executions.map` executes the `translate` workflow created previously.

### YAML
    
    
      main:
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
         - translate_texts:
             call: experimental.executions.map
             args:
                 workflow_id: ${workflow_id}
                 arguments: ${texts_to_translate}
             result: translated
         - return:
                 return: ${translated}

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "init": {
                "assign": [
                  {
                    "workflow_id": "translate"
                  },
                  {
                    "texts_to_translate": [
                      {
                        "text": "hello world!",
                        "source": "en",
                        "target": "fr"
                      },
                      {
                        "text": "你好 世界！",
                        "source": "zh-CN",
                        "target": "en"
                      },
                      {
                        "text": "No hablo español!",
                        "source": "es",
                        "target": "en"
                      }
                    ]
                  }
                ]
              }
            },
            {
              "translate_texts": {
                "call": "experimental.executions.map",
                "args": {
                  "workflow_id": "${workflow_id}",
                  "arguments": "${texts_to_translate}"
                },
                "result": "translated"
              }
            },
            {
              "return": {
                "return": "${translated}"
              }
            }
          ]
        }
      }

The output should resemble the following:
    
    
    [
      {
        "data": {
          "translations": [
            {
              "translatedText": "Bonjour le monde!"
            }
          ]
        }
      },
      {
        "data": {
          "translations": [
            {
              "translatedText": "Hello world!"
            }
          ]
        }
      },
      {
        "data": {
          "translations": [
            {
              "translatedText": "I don't speak Spanish!"
            }
          ]
        }
      }
    ]

## Replace `experimental.executions.map` with a `for:in` loop

Instead of using the experimental function, you can use a parallel `for:in` loop to translate the text. In the following example, the secondary workflow, `translate`, can be used as is and the output should remain unchanged. You also have the option of starting other secondary workflow executions in [parallel branches](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#parallel-branch).

A [shared variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#variables), `translated`, is used to store the results and is populated with empty strings to enable static array indexing. If ordering is not required, you can use [`list.concat`](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/concat) to append the results. All assignments in parallel steps are atomic.

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
                in: ${texts_to_translate}
                index: i  # optional, use if index is required
                value: arg
                steps:
                  - translate:
                      call: googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run
                      args:
                        workflow_id: ${workflow_id}
                        argument: ${arg}
                      result: r
                  - set_result:
                      assign:
                        - translated[i]: ${r}
        - return:
            return: ${translated}

### JSON
    
    
    {
      "main": {
        "params": [],
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "workflow_id": "translate"
                },
                {
                  "texts_to_translate": [
                    {
                      "text": "hello world!",
                      "source": "en",
                      "target": "fr"
                    },
                    {
                      "text": "你好 世界！",
                      "source": "zh-CN",
                      "target": "en"
                    },
                    {
                      "text": "No hablo español!",
                      "source": "es",
                      "target": "en"
                    }
                  ]
                },
                {
                  "translated": [
                    "",
                    "",
                    ""
                  ]
                }
              ]
            }
          },
          {
            "parallel_translate": {
              "parallel": {
                "shared": [
                  "translated"
                ],
                "for": {
                  "in": "${texts_to_translate}",
                  "index": "i",
                  "value": "arg",
                  "steps": [
                    {
                      "translate": {
                        "call": "googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run",
                        "args": {
                          "workflow_id": "${workflow_id}",
                          "argument": "${arg}"
                        },
                        "result": "r"
                      }
                    },
                    {
                      "set_result": {
                        "assign": [
                          {
                            "translated[i]": "${r}"
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "return": {
              "return": "${translated}"
            }
          }
        ]
      }
    }

## Replace `experimental.executions.map` with a `for:range` loop

Instead of using the experimental function, you can use a parallel `for:range` loop to translate the text. By using a `for:range` loop, you can specify the beginning and end of an iteration range. The output should remain unchanged.

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

### JSON
    
    
    {
      "main": {
        "params": [],
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "workflow_id": "translate"
                },
                {
                  "texts_to_translate": [
                    {
                      "text": "hello world!",
                      "source": "en",
                      "target": "fr"
                    },
                    {
                      "text": "你好 世界！",
                      "source": "zh-CN",
                      "target": "en"
                    },
                    {
                      "text": "No hablo español!",
                      "source": "es",
                      "target": "en"
                    }
                  ]
                },
                {
                  "translated": [
                    "",
                    "",
                    ""
                  ]
                }
              ]
            }
          },
          {
            "parallel_translate": {
              "parallel": {
                "shared": [
                  "translated"
                ],
                "for": {
                  "range": "${[0, len(texts_to_translate) - 1]}",
                  "value": "i",
                  "steps": [
                    {
                      "translate": {
                        "call": "googleapis.workflowexecutions.v1.projects.locations.workflows.executions.run",
                        "args": {
                          "workflow_id": "${workflow_id}",
                          "argument": "${texts_to_translate[i]}"
                        },
                        "result": "r"
                      }
                    },
                    {
                      "set_result": {
                        "assign": [
                          {
                            "translated[i]": "${r}"
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "return": {
              "return": "${translated}"
            }
          }
        ]
      }
    }

## Inline the workflow source code

If the secondary workflow is relatively brief, you might want to include it directly within the main workflow for easier readability. For example, in the following workflow, the source code for the `translate` workflow has been inlined.

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

### JSON
    
    
    {
      "main": {
        "params": [
          "args"
        ],
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "workflow_id": "translate"
                },
                {
                  "texts_to_translate": [
                    {
                      "text": "hello world!",
                      "source": "en",
                      "target": "fr"
                    },
                    {
                      "text": "你好 世界！",
                      "source": "zh-CN",
                      "target": "en"
                    },
                    {
                      "text": "No hablo español!",
                      "source": "es",
                      "target": "en"
                    }
                  ]
                },
                {
                  "translated": [
                    "",
                    "",
                    ""
                  ]
                }
              ]
            }
          },
          {
            "parallel_translate": {
              "parallel": {
                "shared": [
                  "translated"
                ],
                "for": {
                  "range": "${[0, len(texts_to_translate) - 1]}",
                  "value": "i",
                  "steps": [
                    {
                      "basic_translate": {
                        "call": "googleapis.translate.v2.translations.translate",
                        "args": {
                          "body": {
                            "q": "${args.text}",
                            "target": "${args.target}",
                            "format": "text",
                            "source": "${args.source}"
                          }
                        },
                        "result": "r"
                      }
                    },
                    {
                      "set_result": {
                        "assign": [
                          {
                            "translated[i]": "${r}"
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "return": {
              "return": "${translated}"
            }
          }
        ]
      }
    }

## What's next

  * [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel/execute-parallel-steps)
  * [Quotas and limits for parallel steps](https://docs.cloud.google.com/workflows/quotas#parallel_steps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
