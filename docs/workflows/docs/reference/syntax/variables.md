---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/variables/
title: Variables \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:58.618018+00:00
---

# Variables  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Variables Stay organized with collections  Save and categorize content based on your preferences. 

You can assign variables in a workflow by using an assign step or by assigning them as the result of a call step. Assigning a variable creates a variable in the current scope (in this document, see Variable scope). You can also access HTTP response information stored in a variable using the built-in parser.

For more information about invoking an HTTP endpoint or accessing HTTP response data, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

## Variable names

Variable names must start with a letter or underscore, and must consist of only letters, digits, and underscores.

## Memory usage

The maximum amount of memory that you can use applies to the cumulative size of all variables defined in a single execution of a workflow. For more information, see [Resource limits](https://docs.cloud.google.com/workflows/quotas#resource_limits).

The memory usage for local variables is computed as follows:

Data type | Size  
---|---  
Integer, double, boolean | 8 bytes  
String, byte, array | 8 bytes + size of `EACH_ELEMENT` *  
Map (dict) | 8 bytes + size of `EACH_KEY` \+ size of `EACH_VALUE`  
  
* Applied recursively to each substructure. 

### Passing by value

When you assign one variable to another, you create a separate, independent copy of the variable's value instead of a reference. This action doubles the memory usage. For example:
    
    
    - assign:
      - a: "This is a string of 28 bytes"
      - b: ${a}  # Creates a copy of `a` and not a reference to `a`

Because a string's size is 8 bytes + size of `EACH_ELEMENT`, the `a` and `b` variables together use 36 + 36 = 72 bytes of memory.

## Variable scope

A variable created inside a [`for` loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration) belongs to the _local scope_ of that loop, and is accessible only in that scope. For example, the variable is cleared after exiting the loop, and accessing it outside of the loop will raise an error when deploying the workflow. This local scoping also applies to any variable created inside an [`except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors).

This sample demonstrates how any variable created in a loop does not exist outside of that loop:

### YAML
    
    
    - init:
        assign:
          - workflowScope: foo
    - outerLoop:
        for:
          value: outerLoopValue  # outerLoopValue does not exist outside of outerLoop step
          in: [1, 2, 3, 4]
          steps:
            - outerLoopAssign:
                assign:
                  - outerLoopScope: ${workflowScope}  # outerLoopScope is a new variable and does not exist outside of outerLoop step
            - innerLoop:
                for:
                  value: innerLoopValue  # innerLoopValue does not exist outside of innerLoop step
                  in: [5, 6, 7, 8]
                  steps:
                    - innerLoopAssign:
                        assign:
                          - workflowScope: ${innerLoopValue}
                          - innerLoopScope: ${outerLoopScope}  # innerLoopScope is a new variable and does not exist outside of innerLoop step
    - final:
        return:
          - ${workflowScope}  # allowed
          # - ${outerLoopScope}  # not allowed
          # - ${innerLoopScope}  # not allowed
          # - ${outerLoopValue}  # not allowed

### JSON
    
    
    [
      {
        "init": {
          "assign": [
            {
              "workflowScope": "foo"
            }
          ]
        }
      },
      {
        "outerLoop": {
          "for": {
            "value": "outerLoopValue",
            "in": [
              1,
              2,
              3,
              4
            ],
            "steps": [
              {
                "outerLoopAssign": {
                  "assign": [
                    {
                      "outerLoopScope": "${workflowScope}"
                    }
                  ]
                }
              },
              {
                "innerLoop": {
                  "for": {
                    "value": "innerLoopValue",
                    "in": [
                      5,
                      6,
                      7,
                      8
                    ],
                    "steps": [
                      {
                        "innerLoopAssign": {
                          "assign": [
                            {
                              "workflowScope": "${innerLoopValue}"
                            },
                            {
                              "innerLoopScope": "${outerLoopScope}"
                            }
                          ]
                        }
                      }
                    ]
                  }
                }
              }
            ]
          }
        }
      },
      {
        "final": {
          "return": [
            "${workflowScope}"
          ]
        }
      }
    ]

Variables assigned in a _parent scope_ are accessible in any _child scopes_. For example, a variable created inside the `main` block of a workflow is accessible in any child `for` loop.

Using [nested `steps`](https://docs.cloud.google.com/workflows/docs/reference/syntax/steps#embedded-steps) does _not_ create a new variable scope. Variables declared in a `steps` block have workflow-level scope and can be accessed outside of the block.

### Subworkflows

Subworkflows don't have access to any variables from the `main` block of a workflow or other subworkflows. A subworkflow receives values passed in a call, and assigns those values to new variables in the subworkflow scope. Note the following points:

  * All step names in a subworkflow must be unique, even if they are in a scope.
  * When calling a subworkflow, a copy of all input data is created for the subworkflow's execution scope. To avoid exceeding [memory limits](https://docs.cloud.google.com/workflows/quotas#resource_limits), pay attention to the size of the data you are passing to subworkflows.



### Share a variable before an `except` block

If you are assigning a variable inside an `except` block and want to access the variable outside of the block, assign the variable _before_ the block to place it in the surrounding scope. For example, the following workflow generates a deployment error:

### YAML
    
    
      main:
        steps:
        - fail:
            try:
                call: http.get
                args:
                    url: https://foo.bar
                result: nope
            except:
                as: e
        - returnError:
                return: ${e}

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "fail": {
                "try": {
                  "call": "http.get",
                  "args": {
                    "url": "https://foo.bar"
                  },
                  "result": "nope"
                },
                "except": {
                  "as": "e"
                }
              }
            },
            {
              "returnError": {
                "return": "${e}"
              }
            }
          ]
        }
      }

The deployment error will be similar to the following:
    
    
    Could not deploy workflow: failed to build: error in step returnError: error
    evaluating return value: symbol 'e' is neither a variable nor a sub-workflow
    name (Code: 3)

To fix this issue, assign the exception variable `e` outside the `except` block so that it is a shared variable in the outer scope. For example:

### YAML
    
    
      main:
          steps:
          - init:
              assign:
              - e: null
          - fail:
              try:
                  call: http.get
                  args:
                      url: https://foo.bar
                  result: nope
              except:
                  as: e
          - returnError:
                  return: ${e}

### JSON
    
    
      {
        "main": {
          "steps": [
            {
              "init": {
                "assign": [
                  {
                    "e": null
                  }
                ]
              }
            },
            {
              "fail": {
                "try": {
                  "call": "http.get",
                  "args": {
                    "url": "https://foo.bar"
                  },
                  "result": "nope"
                },
                "except": {
                  "as": "e"
                }
              }
            },
            {
              "returnError": {
                "return": "${e}"
              }
            }
          ]
        }
      }

## Assign variables

To initialize variables or update existing variables, use a variable assignment step.

### YAML
    
    
      - STEP_NAME:
          assign:
              - VARIABLE_NAME: VALUE

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "assign": [
              {
                "VARIABLE_NAME": "VALUE"
              }
            ]
          }
        }
      ]

You can perform up to 50 assignments in a single step. Variables can be assigned to a particular value or to the result of an expression. For example:

### YAML
    
    
      - assign_vars:
          assign:
              - number: 5
              - number_plus_one: ${number+1}
              - other_number: 10
              - string: "hello"

### JSON
    
    
      [
        {
          "assign_vars": {
            "assign": [
              {
                "number": 5
              },
              {
                "number_plus_one": "${number+1}"
              },
              {
                "other_number": 10
              },
              {
                "string": "hello"
              }
            ]
          }
        }
      ]

Since each assignment is processed sequentially, you can concatenate a string over multiple lines by repeating the variable and splitting the assignment. For example:

### YAML
    
    
      - assign_vars:
          assign:
              - string: "say"
              - string: ${string+" "+"hello"}
              - string: ${string+" "+"to the world"}

### JSON
    
    
      [
        {
          "assign_vars": {
            "assign": [
              {
                "string": "say"
              },
              {
                "string": "${string+" "+"hello"}"
              },
              {
                "string": "${string+" "+"to the world"}"
              }
            ]
          }
        }
      ]

## Clear variables

You can clear a variable by assigning `null`. In YAML, you can also assign an empty value or `~` to a variable. This identifies memory that can be safely reclaimed and lets you free up memory needed for subsequent steps. For example:

### YAML
    
    
      - step:
          assign:
            - bigVar:

### JSON
    
    
      [
        {
          "step": {
            "assign": [
              {
                "bigVar": null
              }
            ]
          }
        }
      ]

If you are working with large datasets from external sources, consider paginating or limiting the result size of the response to avoid loading large amounts of data into memory at once. For example, you can use a page token in a workflow to [paginate a BigQuery result set](https://docs.cloud.google.com/workflows/docs/paginate-bigquery-results).

## Store result from a call in a variable

You can store the result of a `call` step to a variable.

### YAML
    
    
      - STEP_NAME:
          call: ...
          args:
          ...
          result: VARIABLE

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "call": ...,
            "args":
            ...,
            "result": "VARIABLE"
          }
        }
      ]

## Samples

These samples demonstrate the syntax.

### Assign variables

This sample assigns string and number values to variables. Variable assignments are executed sequentially.

### YAML
    
    
    - first_step:
        assign:
          - SomeName: "Sherlock"
          - AnotherName: "Ada"
          - SomeIntegerNumber: 27
          - SomeDoubleNumber: 4.1

### JSON
    
    
    [
      {
        "first_step": {
          "assign": [
            {
              "SomeName": "Sherlock"
            },
            {
              "AnotherName": "Ada"
            },
            {
              "SomeIntegerNumber": 27
            },
            {
              "SomeDoubleNumber": 4.1
            }
          ]
        }
      }
    ]

### Evaluate an expression with type casting

This sample uses an expression to assign the value of a variable. The `full_name` variable uses the `name` and `last_name` variables previously defined.

### YAML
    
    
    - get_message:
        assign:
          - name: "Harsha"
          - last_name: "Kapoor"
          - full_name: ${name+" "+last_name}
          - temperature_C: 27
          - temperature_F: ${temperature_C * 9/5 + 32}
          - temperature_msg: ${"Current temperature is "+string(temperature_F)+" F"}
    - return_value:
        return: ${temperature_msg}

### JSON
    
    
    [
      {
        "get_message": {
          "assign": [
            {
              "name": "Harsha"
            },
            {
              "last_name": "Kapoor"
            },
            {
              "full_name": "${name+\" \"+last_name}"
            },
            {
              "temperature_C": 27
            },
            {
              "temperature_F": "${temperature_C * 9/5 + 32}"
            },
            {
              "temperature_msg": "${\"Current temperature is \"+string(temperature_F)+\" F\"}"
            }
          ]
        }
      },
      {
        "return_value": {
          "return": "${temperature_msg}"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
