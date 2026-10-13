---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/steps/
title: Steps \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:56.405646+00:00
---

# Steps  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Steps Stay organized with collections  Save and categorize content based on your preferences. 

To create a workflow, you define the steps you want and their order of execution using the Workflows syntax. Every workflow must have at least one step.

By default, Workflows treats steps as if they are in an ordered list and executes them one at a time until all the steps have run. For example, this workflow has two steps:

### YAML
    
    
      - STEP_NAME_A:
          ...
      - STEP_NAME_B:
          ...
      

### JSON
    
    
      [
        {
          "STEP_NAME_A": {
            ...
          }
        },
        {
          "STEP_NAME_B": {
            ...
          }
        },
      ]
        

## Step names

Step names must be unique at the [subworkflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows) level. For example, in the following workflow, a step named `init` is allowed in both the `main` block and the subworkflow.

### YAML
    
    
    main:
        params: [input]
        steps:
        - init:
            call: sub
    sub:
        steps:
        - init:
            assign:
              - a: 0

### JSON
    
    
    {
      "main": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "init": {
              "call": "sub"
            }
          }
        ]
      },
      "sub": {
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "a": 0
                }
              ]
            }
          }
        ]
      }
    }

Workflows doesn't enforce a naming convention for step names. However, we recommend consistent usage such as creating step names that only include alphanumeric characters and underscores.

## Step types

Workflows supports various types of steps, including the following:

  * [Assign a variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables)
  * [Apply conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
  * [Invoke an HTTP endpoint](https://docs.cloud.google.com/workflows/docs/http-requests)
  * [Execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps)
  * [Return a value](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
  * [Pause a workflow](https://docs.cloud.google.com/workflows/docs/sleeping)



## Implicit step ordering

This sample shows implicit step ordering within a workflow. By default, the steps of a workflow are executed in the order they appear in the workflow definition.

### YAML
    
    
    - first_step:
        call: http.get
        args:
          url: https://www.example.com/callA
    - second_step:
        call: http.get
        args:
          url: https://www.example.com/callB
    - third_step:
        call: http.get
        args:
          url: https://www.example.com/callC

### JSON
    
    
    [
      {
        "first_step": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/callA"
          }
        }
      },
      {
        "second_step": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/callB"
          }
        }
      },
      {
        "third_step": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/callC"
          }
        }
      }
    ]

## Nested steps

You can use a `steps` block to nest a series of steps and further define a workflow:

### YAML
    
    
      - STEP_NAME:
        steps:
          - STEP_NAME_1:
              steps:
                  - STEP_NAME_A:
                      ...
                  - STEP_NAME_B:
                      ...
          - STEP_NAME_2:
              steps:
                  - STEP_NAME_C:
                      ...
      

### JSON
    
    
        {
          STEP_NAME: {
          "steps": [
            {
              STEP_NAME_1: {
                "steps": [
                  {
                    STEP_NAME_A:
                      ...
                  },
                  {
                    STEP_NAME_B:
                      ...
                  }
                ]
              }
            },
            {
              STEP_NAME_2: {
                "steps": [
                  {
                    STEP_NAME_C:
                      ...
                  }
                ]
              }
            }
          ]
        }
      }
        

Variables declared in a `steps` block have workflow-level scope and can be accessed outside of the block. Any step type can be nested inside of a `steps` block including `assign`, `call`, and `switch`. For example:

### YAML
    
    
      main:
          steps:
          - series_one:
              steps:
                  - step_a:
                      call: http.get
                      args:
                          url: https://host.com/api1
                      result: api_response1
                  - step_b:
                      assign:
                          - varA: "Monday"
                          - varB: "Tuesday"
          - series_two:
              steps:
                  - step_c:
                      call: http.get
                      args:
                          url: https://host.com/api2
                      result: api_response2
                  - step_d:
                      assign:
                          - varC: "Wednesday"
                          - varD: "Thursday"
      

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "series_one": {
                "steps": [
                  {
                    "step_a": {
                      "call": "http.get",
                      "args": {
                        "url": "https://host.com/api1"
                      },
                      "result": "api_response1"
                    }
                  },
                  {
                    "step_b": {
                      "assign": [
                        {
                          "varA": "Monday"
                        },
                        {
                          "varB": "Tuesday"
                        }
                      ]
                    }
                  }
                ]
              }
            },
            {
              "series_two": {
                "steps": [
                  {
                    "step_c": {
                      "call": "http.get",
                      "args": {
                        "url": "https://host.com/api2"
                      },
                      "result": "api_response2"
                    }
                  },
                  {
                    "step_d": {
                      "assign": [
                        {
                          "varC": "Wednesday"
                        },
                        {
                          "varD": "Thursday"
                        }
                      ]
                    }
                  }
                ]
              }
            }
          ]
        }
      }
        

Note that in some cases, `steps` is required; for example, when defining a [subworkflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows) or a [for loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
