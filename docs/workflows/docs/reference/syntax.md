---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/
title: Syntax overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:41.403201+00:00
---

# Syntax overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Syntax overview Stay organized with collections  Save and categorize content based on your preferences. 

To create a workflow, you use the _Workflows syntax_ to define the steps you want and their order of execution. For more information about creating workflows, see [Create and manage workflows](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow).

For other functions available in addition to the core syntax, refer to the [Standard library](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview) and [Connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis) references.

## File structure

Workflow source files have the following characteristics:

  * They contain only one [main workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows#main-block).
  * They might contain [subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows).
  * They are either a valid [YAML](https://yaml.org/) or [JSON](https://json.org/) file.

Code samples are provided in both YAML and the equivalent JSON.

**Note:** YAML indentation is meaningful and should be at least two spaces per indentation level. Insufficient indentation can cause errors, and a new level should be at least two spaces in from the _start of the text_ in the previous line. For more details, see [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting#indentation). 



## Search the syntax

You can search the Workflows syntax for its reserved words and other details. To see examples of the syntax in action, see the [cheat sheet](https://docs.cloud.google.com/workflows/docs/reference/syntax/syntax-cheat-sheet).

Reserved word | Description | Use with | See also | Examples  
---|---|---|---|---  
  
### `args`

| Pass arguments and their values when calling a function that accepts parameters.  | `call` steps  | `call`  
`result` | 

  * [Calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)

  
  
### `assign`

| Set the value of a variable.  | — |  —  | 

  * [Assign variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)

  
  
### `branches`

| Execute parallel branches concurrently and the steps in each branch sequentially.  |  `steps` | `parallel` | 

  * [Execute parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps)
  * [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [Replace experimental function with parallel step](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel)

  
  
### `break`

| Terminate iteration of a `for` loop.  |  `next` in `for` loops  | `continue` | 

  * [Use break/continue in a loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#break-in-loop)

  
  
### `call`

| Run a function and return a result. |  —  | `args`  
`result` | 

  * [Calls](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)

  
  
### `condition`

| Provide an expression to control if a step is executed (the first condition to evaluate as true).  | `switch` | — | 

  * [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)

  
  
### `continue`

| Terminate the current iteration of a `for` loop and continue with the next iteration.  |  `next` in `for` loops  | `break` | 

  * [Use break/continue in a loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#break-in-loop)

  
  
### `end`

| Stop a workflow's execution without returning a value.  | `next` | — | 

  * [Complete the execution of a workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing)

  
  
### `except`

| Catch and handle errors thrown during a workflow execution.  |  `try` | `retry` | 

  * [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)

  
`for` | Iterate over a sequence of numbers or through a collection of data, such as a list or map.  | `steps` | — | 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)

  
  
### `main`

| Define your main workflow. If a workflow has a subworkflow, or to receive runtime arguments, there must be a `main` block. |  Subworkflows  | — | 

  * [Main workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/main)

  
  
### `next`

| Define what step Workflows should execute next.  |  —  | `break`  
`continue` | 

  * [Jumps](https://docs.cloud.google.com/workflows/docs/reference/syntax/jumps)

  
  
### `parallel`

| Execute two or more steps concurrently.  |  `branches`  
`for` loops  
`steps` | — | 

  * [Execute parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps)
  * [Parallel steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [Replace experimental function with parallel step](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel)

  
  
### `params`

| Accept workflow execution arguments, or arguments passed to a subworkflow.  |  Subworkflows  | `main` | 

  * [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments)
  * [Runtime arguments](https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args)
  * [Subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows)

  
  
### `raise`

| Raise custom errors. | — |  `except`  
`retry`  
`try` | 

  * [Raise errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)

  
  
### `result`

| Assign the result from a call to this variable. | `call` steps  | `args` | 

  * [Assign responses from a call](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls#assign_responses_from_a_call)
  * [Store result from a call in a variable](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#store-result)

  
  
### `retry`

| Define the retry behavior and the number of retry attempts.  | `try` | — | 

  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)

  
  
### `return`

| Stop a workflow's execution and return a value or expression.  | — |  —  | 

  * [Complete the execution of a workflow](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing)

  
  
### `steps`

| Nest a series of steps.  |  `branches`  
`for` loops  
Subworkflows  
`try` | `main` | 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)
  * [Nested steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps#embedded-steps)
  * [Subworkflows](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows)

  
  
### `switch`

| Allow the value of an expression to control the flow of a workflow's execution.  |  —  | `condition` | 

  * [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)

  
  
### `try`

| Define a list of steps to retry if an error is raised, or catch and handle the error.  |  —  | `except`  
`retry` | 

  * [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)

  
  
### Example: ```args`

### YAML
    
    
      - STEP_NAME:
          call: ...
          **args** :
          ...
          result: VARIABLE
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "call": ...,
            "**args** ": {
              ...
            },
            "result": "VARIABLE"
          }
        }
      ]
        

OK

### Example: `assign`

### YAML
    
    
      - STEP_NAME:
          **assign** :
              - VARIABLE_NAME: VALUE
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "**assign** ": [
              {
                "VARIABLE_NAME": "VALUE"
              }
            ]
          }
        }
      ]
        

OK

### Example: `branches`

### YAML
    
    
      - PARALLEL_STEP_NAME:
          parallel:
              ...
              **branches** :
                - BRANCH_NAME_A:
                    steps:
                        ...
                - BRANCH_NAME_B:
                    steps:
                        ...
      

### JSON
    
    
       [
        {
          "PARALLEL_STEP_NAME": {
            "parallel": {
              ...
              "**branches** ": [
                {
                  "BRANCH_NAME_A": {
                    "steps":
                         ...
                  }
                },
                {
                  "BRANCH_NAME_B": {
                    "steps":
                         ...
                  }
                }
              ]
            }
          }
        }
      ]
      

OK

### Example: `break`

### YAML
    
    
      - FOR_LOOP_STEP_NAME_A:
          for:
              value: LOOP_VARIABLE_NAME_A
              in: ${LIST_EXPRESSION_A}    # or simply in: LIST_DEFINITION
              steps:
                  - STEP_NAME_A:
                      next: continue
      - FOR_LOOP_STEP_NAME_B:
          for:
              value: LOOP_VARIABLE_NAME_B
              range: [${BEGIN_EXPRESSION}, ${END_EXPRESSION}]
              steps:
                  - STEP_NAME_B:
                      next: **break**

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME_A": {
            "for": {
              "value": "LOOP_VARIABLE_NAME_A",
              "in": "${LIST_EXPRESSION_A}",
              "steps": [
                {
                  "STEP_NAME_A": {
                    "next": "continue"
                  }
                }
              ]
            }
          }
        },
        {
          "FOR_LOOP_STEP_NAME_B": {
            "for": {
              "value": "LOOP_VARIABLE_NAME_B",
              "range": [
                "${BEGIN_EXPRESSION}",
                "${END_EXPRESSION}"
              ],
              "steps": [
                {
                  "STEP_NAME_B": {
                    "next": "**break** "
                  }
                }
              ]
            }
          }
        }
      ]

OK

### Example: `call`

### YAML
    
    
      - STEP_NAME:
          **call** : ...
          args:
          ...
          result: VARIABLE
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "**call** ": ...,
            "args": {
              ...
            },
            "result": "VARIABLE"
          }
        }
      ]
        

OK

### Example: `condition`

### YAML
    
    
      - STEP_NAME_A:
          switch:
              - **condition** : ${EXPRESSION_A}
                next: STEP_NAME_B
              - **condition** : ${EXPRESSION_B}
                next: STEP_NAME_C
              - **condition** : true
                next: STEP_NAME_C
          next: STEP_NAME_D
      

### JSON
    
    
      [
        {
          "STEP_NAME_A": {
            "switch": [
              {
                "**condition** ": "${EXPRESSION_A}",
                "next": "STEP_NAME_B"
              },
              {
                "**condition** ": "${EXPRESSION_B}",
                "next": "STEP_NAME_C"
              }
              {
                "**condition** ": true,
                "next": "STEP_NAME_C"
              }
            ],
            "next": "STEP_NAME_D"
          }
        }
      ]
        

OK

### Example: `continue`

### YAML
    
    
      - FOR_LOOP_STEP_NAME_A:
          for:
              value: LOOP_VARIABLE_NAME_A
              in: ${LIST_EXPRESSION_A}    # or simply in: LIST_DEFINITION
              steps:
                  - STEP_NAME_A:
                      next: **continue**
      - FOR_LOOP_STEP_NAME_B:
          for:
              value: LOOP_VARIABLE_NAME_B
              range: [${BEGIN_EXPRESSION}, ${END_EXPRESSION}]
              steps:
                  - STEP_NAME_B:
                      next: break

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME_A": {
            "for": {
              "value": "LOOP_VARIABLE_NAME_A",
              "in": "${LIST_EXPRESSION_A}",
              "steps": [
                {
                  "STEP_NAME_A": {
                    "next": "**continue** "
                  }
                }
              ]
            }
          }
        },
        {
          "FOR_LOOP_STEP_NAME_B": {
            "for": {
              "value": "LOOP_VARIABLE_NAME_B",
              "range": [
                "${BEGIN_EXPRESSION}",
                "${END_EXPRESSION}"
              ],
              "steps": [
                {
                  "STEP_NAME_B": {
                    "next": "break"
                  }
                }
              ]
            }
          }
        }
      ]

OK

### Example: `end`

### YAML
    
    
      - STEP_NAME:
          ...
          next: **end**
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            ...
            "next": "**end** "
          }
        }
      ]
        

OK

### Example: `except`

### YAML
    
    
      - STEP_NAME:
         try:
             call: http.get
             ...
         **except** :
             as: ERROR_MAP
             steps:
                 ...
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "try": {
              "call": "http.get"
              ...
            },
            "**except** ": {
              "as": "ERROR_MAP",
              "steps":
                  ...
            }
          }
        }
      ]
        

OK

### Example: `for`

### YAML
    
    
      - FOR_LOOP_STEP_NAME:
          **for** :
              value: LOOP_VARIABLE_NAME
              index: INDEX_VARIABLE_NAME
              in: ${LIST_EXPRESSION}
              steps:
                  - STEP_NAME_A:
                    ...

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME": {
            "**for** ": {
              "value": "LOOP_VARIABLE_NAME",
              "index": "INDEX_VARIABLE_NAME",
              "in": "${LIST_EXPRESSION}",
              "steps": [
                {
                  "STEP_NAME_A":
                    ...
                }
              ]
            }
          }
        }
      ]

OK

### Example: `main`

### YAML
    
    
      **main** :
          params: [MAP_NAME]
          steps:
              - STEP_NAME:
                  ...
              ...
      

### JSON
    
    
        {
          "**main** ": {
            "params": [
              "MAP_NAME"
            ],
            "steps": [
              {
                "STEP_NAME": {
                  ...
                }
              },
              ...
            ]
          }
        }
        

OK

### Example: `next`

### YAML
    
    
      - STEP_NAME:
          ...
          **next** : STEP_NAME_TO_JUMP_TO
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            ...
            "**next** ": "STEP_NAME_TO_JUMP_TO"
          }
        }
      ]
        

OK

### Example: `params`

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
            **params** : [PARAMETER_1,PARAMETER_2...]
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
          "**params** ": ["PARAMETER_1,PARAMETER_2"...],
          "steps": [
            {
              "step_1":
              ...
            }
          ]
        }
      }
        

OK

### Example: `parallel`

### YAML
    
    
      - PARALLEL_STEP_NAME:
          **parallel** :
              exception_policy: POLICY
              shared: [VARIABLE_A, VARIABLE_B, ...]
              BRANCHES_OR_FOR:
                 ...

### JSON
    
    
      [
        {
          "PARALLEL_STEP_NAME": {
            "**parallel** ": {
              "exception_policy": "POLICY",
              "shared": [
                "VARIABLE_A",
                "VARIABLE_B",
                ...
              ],
              "BRANCHES_OR_FOR":
              ...
            }
          }
        }
      ]
        

OK

### Example: `raise`

### YAML
    
    
      - step_a:
          **raise** : "Something went wrong."
      

### JSON
    
    
      [
        {
          "step_a": {
            "**raise** ": "Something went wrong."
          }
        }
      ]
        

OK

### Example: `result`

### YAML
    
    
      - STEP_NAME:
          call: ...
          args:
          ...
          **result** : VARIABLE
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "call": ...,
            "args":
            ...,
            "**result** ": "VARIABLE"
          }
        }
      ]
        

OK

### Example: `retry`

### YAML
    
    
      - step_name:
          try:
              steps:
                  ...
          **retry** : RETRY_POLICY
              predicate: RETRY_PREDICATE
              max_retries: NUMBER_OF_RETRIES
              backoff:
                  initial_delay: DELAY_SECONDS
                  max_delay: MAX_DELAY_SECONDS
                  multiplier: DELAY_MULTIPLIER
      

### JSON
    
    
      [
        {
          "step_name": {
            "try": {
               "steps": [
                   ...
        ]
            },
            "**retry** ": "RETRY_POLICY"
              "predicate": "RETRY_PREDICATE",
              "max_retries": NUMBER_OF_RETRIES,
              "backoff": {
                "initial_delay": DELAY_SECONDS,
                "max_delay": MAX_DELAY_SECONDS,
                "multiplier": DELAY_MULTIPLIER
              }
            }
          }
      ]
        

OK

### Example: `return`

### YAML
    
    
      - STEP_NAME:
          ...
          **return** : ${VARIABLE}
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            ...
            "**return** ": "${VARIABLE}"
          }
        }
      ]
        

OK

### Example: `steps`

### YAML
    
    
      - STEP_NAME:
        **steps** :
          - STEP_NAME_1:
              **steps** :
                  - STEP_NAME_A:
                      ...
                  - STEP_NAME_B:
                      ...
          - STEP_NAME_2:
              **steps** :
                  - STEP_NAME_C:
                      ...
      

### JSON
    
    
        {
          STEP_NAME: {
          "**steps** ": [
            {
              STEP_NAME_1: {
                "**steps** ": [
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
                "**steps** ": [
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
        

OK

### Example: `switch`

### YAML
    
    
      - STEP_NAME_A:
          **switch** :
              - condition: ${EXPRESSION_A}
                next: STEP_NAME_B
              - condition: ${EXPRESSION_B}
                next: STEP_NAME_C
              - condition: true
                next: STEP_NAME_C
          next: STEP_NAME_D
      

### JSON
    
    
      [
        {
          "STEP_NAME_A": {
            "**switch** ": [
              {
                "condition": "${EXPRESSION_A}",
                "next": "STEP_NAME_B"
              },
              {
                "condition": "${EXPRESSION_B}",
                "next": "STEP_NAME_C"
              }
              {
                "condition": true,
                "next": "STEP_NAME_C"
              }
            ],
            "next": "STEP_NAME_D"
          }
        }
      ]
        

OK

### Example: `try`

### YAML
    
    
      - STEP_NAME:
         **try** :
             call: http.get
             ...
         except:
             as: ERROR_MAP
             steps:
                 ...
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "**try** ": {
              "call": "http.get"
              ...
            },
            "except": {
              "as": "ERROR_MAP",
              "steps":
                  ...
            }
          }
        }
      ]
        

OK

### Example: `stub`

OK

## Using code samples

For all samples that communicate with other Google Cloud resources, your workflow must be associated with a service account that has sufficient privileges to access those resources. To learn more about granting roles to service accounts, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). To learn how to change the service account associated with a workflow, see [update a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow). For more information about authentication, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).

Some samples might require that you first enable a Google Cloud API. Learn more about [listing services](https://docs.cloud.google.com/service-usage/docs/list-services) and [enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

**Caution:** Some samples use placeholder URLs for Google Cloud resources and external APIs. Because of this, **samples in this reference might not execute without modifications**. When a sample includes the URL for a Cloud Run functions function, a Cloud Run app, or an API, you must replace that URL with the URL of your own function, app, or API.

See [all Workflows code samples](https://docs.cloud.google.com/workflows/docs/samples).

## Notation key

Notation | Description  
---|---  
`[]` Square brackets | Optional; if the brackets themselves must be typed, this is indicated  
`{}` Braces | Required  
`|` Vertical bar | Separator for mutually exclusive items; choose one  
`...` Ellipsis | Items that can be repeated; or indicates an omission to improve clarity and shorten the length of the example  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
