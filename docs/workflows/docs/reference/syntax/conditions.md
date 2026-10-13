---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions/
title: Conditions \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:45.779276+00:00
---

# Conditions  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Conditions Stay organized with collections  Save and categorize content based on your preferences. 

You can use a `switch` block as a selection mechanism that allows the value of an expression to control the flow of a workflow's execution. If a value matches, that condition's statement is executed.

If no matching expression is found, the workflow looks for an optional default condition: `- condition: true`. This should be the last condition in the `switch` block as they are evaluated in order and the first match found is executed. If there is neither a match nor a default condition, the workflow continues execution with the step that immediately follows.

Each `switch` block can include a maximum of 50 conditions. Each expression must evaluate to true or false. (Learn how to define and use [expressions](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions).)

For example, you can control the order of a workflow's execution by using a `switch` block to [jump](https://docs.cloud.google.com/workflows/docs/reference/syntax/jumps) between steps based on a conditional expression:

### YAML
    
    
      - STEP_NAME_A:
          switch:
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
            "switch": [
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
        

You can also nest multiple steps inside a `switch` block:

### YAML
    
    
      - STEP_NAME_A:
          switch:
              - condition: ${EXPRESSION}
                steps:
                    - STEP_NAME_B:
                        ...
                    - STEP_NAME_C:
                        ...
          next: STEP_NAME_D
      

### JSON
    
    
      [
        {
          "STEP_NAME_A": {
            "switch": [
              {
                "condition": "${EXPRESSION}",
                "steps": [
                  {
                    "STEP_NAME_B": {
                      ...
                    }
                  },
                  {
                    "STEP_NAME_C": {
                      ...
                    }
                  }
                ]
              }
            ],
            "next": "STEP_NAME_D"
          }
        }
      ]
        

Note that the `steps` block is optional. It can contain the following:

  * [`assign`](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step)
  * [`call`](https://docs.cloud.google.com/workflows/docs/reference/syntax/calls)
  * [`for`](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration#for-in)
  * [`parallel`](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps)
  * [`raise`](https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors)
  * [`return`](https://docs.cloud.google.com/workflows/docs/reference/syntax/completing#using-return)
  * [`steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps)
  * [`switch`](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)
  * [`try`](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)



For more information about defining a workflow's order of execution, see [Jumps](https://docs.cloud.google.com/workflows/docs/reference/syntax/jumps) and [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order).

## Samples

These samples demonstrate the syntax.

### Conditional jumps to specific steps

You might want a workflow to jump to a specific step when a condition is met. These two samples execute steps depending on the value returned by the first step of the workflow.

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

### JSON
    
    
    [
      {
        "first_step": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/callA"
          },
          "result": "first_result"
        }
      },
      {
        "where_to_jump": {
          "switch": [
            {
              "condition": "${first_result.body.SomeField < 10}",
              "next": "small"
            },
            {
              "condition": "${first_result.body.SomeField < 100}",
              "next": "medium"
            }
          ],
          "next": "large"
        }
      },
      {
        "small": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/SmallFunc"
          },
          "next": "end"
        }
      },
      {
        "medium": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/MediumFunc"
          },
          "next": "end"
        }
      },
      {
        "large": {
          "call": "http.get",
          "args": {
            "url": "https://www.example.com/LargeFunc"
          },
          "next": "end"
        }
      }
    ]

### YAML
    
    
    - getCurrentTime:
        call: http.get
        args:
          url: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam
        result: currentTime
    - conditionalSwitch:
        switch:
          - condition: ${currentTime.body.dayOfWeek == "Friday"}
            next: friday
          - condition: ${currentTime.body.dayOfWeek == "Saturday" or currentTime.body.dayOfWeek == "Sunday"}
            next: weekend
        next: workWeek
    - friday:
        return: "It's Friday! Almost the weekend!"
    - weekend:
        return: "It's the weekend!"
    - workWeek:
        return: "It's the work week."

### JSON
    
    
    [
      {
        "getCurrentTime": {
          "call": "http.get",
          "args": {
            "url": "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam"
          },
          "result": "currentTime"
        }
      },
      {
        "conditionalSwitch": {
          "switch": [
            {
              "condition": "${currentTime.body.dayOfWeek == \"Friday\"}",
              "next": "friday"
            },
            {
              "condition": "${currentTime.body.dayOfWeek == \"Saturday\" or currentTime.body.dayOfWeek == \"Sunday\"}",
              "next": "weekend"
            }
          ],
          "next": "workWeek"
        }
      },
      {
        "friday": {
          "return": "It's Friday! Almost the weekend!"
        }
      },
      {
        "weekend": {
          "return": "It's the weekend!"
        }
      },
      {
        "workWeek": {
          "return": "It's the work week."
        }
      }
    ]

### Switch structure with embedded steps

A switch structure can also be used to support direct execution of steps when a condition is met, without jumping to other steps. This improves the readability of a workflow by reducing the number of steps in the workflow definition.

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

### JSON
    
    
    [
      {
        "step1": {
          "assign": [
            {
              "a": 1
            }
          ]
        }
      },
      {
        "step2": {
          "switch": [
            {
              "condition": "${a==1}",
              "steps": [
                {
                  "stepA": {
                    "assign": [
                      {
                        "a": "${a+7}"
                      }
                    ]
                  }
                },
                {
                  "stepB": {
                    "return": "${\"increase a to:\"+string(a)}"
                  }
                }
              ]
            }
          ]
        }
      },
      {
        "step3": {
          "return": "${\"default a=\"+string(a)}"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
