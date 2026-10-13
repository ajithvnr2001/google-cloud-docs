---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows/
title: Subworkflows \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:57.897692+00:00
---

# Subworkflows  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Subworkflows Stay organized with collections  Save and categorize content based on your preferences. 

You can use subworkflows to define a piece of logic or a set of steps you want to call multiple times, simplifying the workflow definition. Subworkflows are similar to a function or routine in a programming language. They can accept parameters and return values, allowing you to create more complex workflows with a broader range of applications.

For information on basic workflow tasks, see [Create and update an existing workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow) and [Execute a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow).

## Main block

If a workflow has a subworkflow, the main workflow must be placed in a `main` block. Subworkflows are always defined after the main body of the workflow definition:

### YAML
    
    
      main:
          steps:
              - STEP_NAME:
                  ...
              ...
    
      SUBWORKFLOW_NAME:
          params: [PARAMETER_1,PARAMETER_2...]
          steps:
              - SUBWORKFLOW_STEP_NAME:
              ...

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "STEP_NAME":
                ...
            }
            ...
          ]
        },
        "SUBWORKFLOW_NAME": {
          "params": "[PARAMETER_1,PARAMETER_2...]",
          "steps": [
            {
              "SUBWORKFLOW_STEP_NAME":
                ...
            }
          ]
        }
      }

If you don't need to pass parameters to the subworkflow, delete the `params` block. Note that any parameters must be enclosed in square brackets. For example:

`params: [Street, ZipCode, Country]`

Note that the `steps` block is required inside a `SUBWORKFLOW_NAME` block. It can contain the following:

  * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
  * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
  * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
  * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
  * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
  * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
  * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
  * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)



## Default parameters in subworkflows

Subworkflows support default values for parameters. The default parameter value is used only if a parameter isn't provided as part of a subworkflow call.

### YAML
    
    
      SUBWORKFLOW_NAME:
          params: [PARAMETER_1, PARAMETER_2: DEFAULT_VALUE2...]
          steps:
              - SUBWORKFLOW_STEP_NAME:
              ...

### JSON
    
    
      {
        "SUBWORKFLOW_NAME": {
          "params": "[PARAMETER_1,PARAMETER_2: DEFAULT_VALUE2...]",
          "steps": [
            {
              "SUBWORKFLOW_STEP_NAME":
                ...
            }
          ]
        }
      }

For example, the following workflow can be called with or without a Country parameter, and if the Country is not specified, it defaults to "United States".

### YAML
    
    
      build_address:
          params: [Street, ZipCode, Country: "United States"]
          steps:
              - concatenate:
                  return: ${Street + ", " + ZipCode + ", " + Country}

### JSON
    
    
      {
        "build_address": {
          "params": [
            "Street",
            "ZipCode",
            {
              "Country": "United States"
            }
          ],
          "steps": [
            {
              "concatenate": {
                "return": "${Street + \", \" + ZipCode + \", \" + Country}"
              }
            }
          ]
        }
      }

## Call a subworkflow

You call a subworkflow using the `call` field within a workflow step in the main workflow, optionally supplying arguments to pass to the subworkflow:

### YAML
    
    
       main:
           steps:
               - STEP_NAME:
                   call: SUBWORKFLOW_NAME
                   args:
                       ARG_1: VALUE_1
                       ARG_2: VALUE_2
                       ...
                   result: OUTPUT_VARIABLE
       SUBWORKFLOW_NAME:
            params: [PARAMETER_1,PARAMETER_2...]
            steps:
                - step_1:
                ...

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "STEP_NAME": {
                "call": "SUBWORKFLOW_NAME",
                "args": {
                  "ARG_1": "VALUE_1",
                  "ARG_2": "VALUE_2"
                },
                "result": "OUTPUT_VARIABLE"
              }
            }
          ]
        },
        "SUBWORKFLOW_NAME": {
          "params": ["PARAMETER_1,PARAMETER_2"...],
          "steps": [
            {
              "step_1":
              ...
            }
          ]
        }
      }

If the subworkflow accepts parameters, you can pass arguments (`ARG_1`, `ARG_2`) and their values (`VALUE_1`, `VALUE_2`) to the workflow. If the subworkflow returns anything, you can store the data in the `OUTPUT_VARIABLE`.

This example defines a subworkflow named `name_message` and calls it from the main workflow:

### YAML
    
    
      main:
          steps:
              - call_subworkflow:
                  call: name_message
                  args:
                      first_name: "Ada"
                      last_name: "Lovelace"
                  result: output
              - call_subworkflow2:
                  call: name_message
                  args:
                      first_name: "Sherlock"
                      last_name: "Holmes"
                  result: output2
              - return_message:
                  return: ${output + " " + output2}
    
      name_message:
          params: [first_name, last_name, country: "England"]
          steps:
              - prepareMessage:
                  return: ${"Hello " + first_name + " " + last_name + " from " + country + "."}

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "call_subworkflow": {
                "call": "name_message",
                "args": {
                  "first_name": "Ada",
                  "last_name": "Lovelace"
                },
                "result": "output"
              }
            },
            {
              "call_subworkflow2": {
                "call": "name_message",
                "args": {
                  "first_name": "Sherlock",
                  "last_name": "Holmes"
                },
                "result": "output2"
              }
            },
            {
              "return_message": {
                "return": "${output + \" \" + output2}"
              }
            }
          ]
        },
        "name_message": {
          "params": [
            "first_name",
            "last_name",
            {
              "country": "England"
            }
          ],
          "steps": [
            {
              "prepareMessage": {
                "return": "${\"Hello \" + first_name + \" \" + last_name + \" from \" + country + \".\"}"
              }
            }
          ]
        }
      }

This workflow definition does the following:

  * The main workflow calls the `name_message` subworkflow twice, from the steps `call_subworkflow` and `call_subworkflow2`.
  * The two steps supply different inputs for the arguments `first_name` and `last_name`, which are then passed to the subworkflow.
  * The subworkflow `name_message` takes the arguments passed to it and constructs a simple message, supplying the default value of `England` for the `country` variable.
  * The subworkflow returns the message it constructs to the main workflow.
  * The steps in the main workflow store the results as `output` and `output2`, respectively.
  * The main workflow combines `output` and `output2` into a single message and returns the result: `Hello Ada Lovelace from England. Hello Sherlock Holmes from England.`



For more information, see [Calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls).

## Call a subworkflow in an expression

This example is identical to the preceding example except that the workflow calls the subworkflow using an [expression](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions). Note that expressions cannot contain calls to subworkflows with [blocking](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions#blocking-calls) steps.

### YAML
    
    
      main:
          steps:
              - call_subworkflow:
                  assign:
                    - output: ${name_message("Ada","Lovelace")}
              - call_subworkflow2:
                  assign:
                    - output2: ${name_message("Sherlock","Holmes")}
              - return_message:
                  return: ${output + " " + output2}
    
      name_message:
          params: [first_name, last_name, country: "England"]
          steps:
              - prepareMessage:
                  return: ${"Hello " + first_name + " " + last_name + " from " + country + "."}

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "call_subworkflow": {
                "assign": [
                  {
                    "output": "${name_message(\"Ada\",\"Lovelace\")}"
                  }
                ]
              }
            },
            {
              "call_subworkflow2": {
                "assign": [
                  {
                    "output2": "${name_message(\"Sherlock\",\"Holmes\")}"
                  }
                ]
              }
            },
            {
              "return_message": {
                "return": "${output + \" \" + output2}"
              }
            }
          ]
        },
        "name_message": {
          "params": [
            "first_name",
            "last_name",
            {
              "country": "England"
            }
          ],
          "steps": [
            {
              "prepareMessage": {
                "return": "${\"Hello \" + first_name + \" \" + last_name + \" from \" + country + \".\"}"
              }
            }
          ]
        }
      }

## Simple subworkflow

This sample implements a simple subworkflow. When a workflow has a subworkflow, the main workflow must be placed in a `main` block. Subworkflows are always defined after the main body of the workflow definition.

### YAML
    
    
    main:
      steps:
        - first:
            call: hello
            args:
              input: "Kristof"
            result: some_output
        - second:
            return: ${some_output}
    
    hello:
      params: [input]
      steps:
        - first:
            return: ${"Hello "+input}

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "first": {
              "call": "hello",
              "args": {
                "input": "Kristof"
              },
              "result": "some_output"
            }
          },
          {
            "second": {
              "return": "${some_output}"
            }
          }
        ]
      },
      "hello": {
        "params": [
          "input"
        ],
        "steps": [
          {
            "first": {
              "return": "${\"Hello \"+input}"
            }
          }
        ]
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
