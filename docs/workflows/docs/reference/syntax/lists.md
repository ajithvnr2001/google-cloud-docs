---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/lists/
title: Lists \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:53.062774+00:00
---

# Lists  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/lists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Lists Stay organized with collections  Save and categorize content based on your preferences. 

Workflows supports lists (or arrays) for storing data. Lists can be defined in a workflow in two different ways. For information on iterating through a list, see [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration).

## List definition

Lists can be created in a workflow by being returned as the result of a step or by being defined in an `assign` step.

### List returned by a step

HTTP requests often return a JSON response as a list that we store as a variable in the workflow. In the following example, we make a request to an example API that returns a list of months. We store the list as a variable named `monthsList` and then return the third element of the list:

### YAML
    
    
      - step_a:
          call: http.get
          args:
              url: https://somewhere.com/getMonths
          result: monthsList
      - step_b:
          return: ${monthsList.body[2]}
      

### JSON
    
    
      [
        {
          "step_a": {
            "call": "http.get",
            "args": {
              "url": "https://somewhere.com/getMonths"
            },
            "result": "monthsList"
          }
        },
        {
          "step_b": {
            "return": "${monthsList.body[2]}"
          }
        }
      ]
        

### List defined in an assign step

To define a list, use an `assign` step:

### YAML
    
    
      - step_a:
          assign:
              - num_list: ["zero","one","two"]
      

### JSON
    
    
      [
        {
          "step_a": {
            "assign": [
              {
                "num_list": [
                  "zero",
                  "one",
                  "two"
                ]
              }
            ]
          }
        }
      ]
        

### List definition sample

This sample defines a few lists. List definitions can be made inline using square brackets or as a list with one item per line.

### YAML
    
    
    - first_step:
        assign:
          - my_list1: [1, 2, 3]
          - my_list2:
              - 1
              - 2
              - 3
          - my_list3: ["Grzegorz", "Irina", "Yufei"]

### JSON
    
    
    [
      {
        "first_step": {
          "assign": [
            {
              "my_list1": [
                1,
                2,
                3
              ]
            },
            {
              "my_list2": [
                1,
                2,
                3
              ]
            },
            {
              "my_list3": [
                "Grzegorz",
                "Irina",
                "Yufei"
              ]
            }
          ]
        }
      }
    ]

## Update list values

You can update the value at an index by using an `assign` step and index notation. Subscripts can address the elements of the list and support expressions, but they must evaluate to an integer value during execution.

### YAML
    
    
      - update_list:
          assign:
              - my_list: [0, 1, 2, 3, 4, 5]
              - idx: 0
              - my_list[0]: "Value0"
              - my_list[idx + 1]: "Value1"
              - my_list[len(my_list) - 1]: "LastValue"
              - number: 5
              - my_map: {"myKey": "myValue"}
              - my_list[2]: "${number+1}"  # Assigns result of an expression
              - my_list[3]:  # Clears fourth element
              - my_list[4]: "${my_map}" # Assigns map to fifth element in list
      - return_step:
          return: ${my_list}  # Returns ["Value0", "Value1", 6, null, {"myKey": "myValue"}, "LastValue"]
      

### JSON
    
    
      [
        {
          "update_list": {
            "assign": [
              {
                "my_list": [
                  0,
                  1,
                  2,
                  3,
                  4,
                  5
                ]
              },
              {
                "idx": 0
              },
              {
                "my_list[0]": "Value0"
              },
              {
                "my_list[idx + 1]": "Value1"
              },
              {
                "my_list[len(my_list) - 1]": "LastValue"
              },
              {
                "number": 5
              },
              {
                "my_map": {
                  "myKey": "myValue"
                }
              },
              {
                "my_list[2]": "${number+1}"
              },
              {
                "my_list[3]": null
              },
              {
                "my_list[4]": "${my_map}"
              }
            ]
          }
        },
        {
          "return_step": {
            "return": "${my_list}"
          }
        }
      ]

You can also update the values of multidimensional lists:

### YAML
    
    
      - update_2d_list:
          assign:
              - my_list: [[10, 11, 12], [20, 21, 22]]
              - my_list[0][1]: "Value11"
              - my_list[1][2]: "Value22"
      

### JSON
    
    
      [
        {
          "update_2d_list": {
            "assign": [
              {
                "my_list": [
                  [
                    10,
                    11,
                    12
                  ],
                  [
                    20,
                    21,
                    22
                  ]
                ]
              },
              {
                "my_list[0][1]": "Value11"
              },
              {
                "my_list[1][2]": "Value22"
              }
            ]
          }
        }
      ]
        

## Add a new element to the end of a list

You can create a copy of a list with a new element concatenated at the end by using the `list.concat` [function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/concat).

**Note:** To avoid conflicting with the standard library namespace, don't use `list` as a list name. (In the following example, the list name is `listVar`.)

### YAML
    
    
      assign:
          - listVar: ${list.concat(listVar, "new item")}
      

### JSON
    
    
        {
          "assign": [
            {
              "listVar": "${list.concat(listVar, \"new item\")}"
            }
          ]
        }
        

## Check existence of a key in a list

To check whether a given key is present in a list, use the following expression: 
    
    
    ${KEY in LIST}

For example:

### YAML
    
    
      main:
          params: [input]
          steps:
          - init:
              assign:
                  - list:
                      - "Alex"
                      - "Izumi"
                      - "Nur"
          - check:
              switch:
                  - condition: ${"Nur" in list}
                    return: true
                  - condition: true
                    return: false

### JSON
    
    
      {
        "main": {
          "params": [
            "input"
          ],
          "steps": [
            {
              "init": {
                "assign": [
                  {
                    "list": [
                      "Alex",
                      "Izumi",
                      "Nur"
                    ]
                  }
                ]
              }
            },
            {
              "check": {
                "switch": [
                  {
                    "condition": "${\"Nur\" in list}",
                    "return": true
                  },
                  {
                    "condition": true,
                    "return": false
                  }
                ]
              }
            }
          ]
        }
      }

To check whether a key is not in a list, use the `not()` function:

### YAML
    
    
      - check:
          switch:
            - condition: ${not("Nur" in list)}
              next: NameMissing
      

### JSON
    
    
      [
        {
          "check": {
            "switch": [
              {
                "condition": "${not(\"Nur\" in list)}",
                "next": "NameMissing"
              }
            ]
          }
        }
      ]
        

## Get the length of a list

You can get the length of a list by using the `len()` [expression helper](https://docs.cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#data_type_functions). This built-in function accepts an attribute of type `list` and returns the number of elements in the list as an integer. For example, the following sample returns `4`:

### YAML
    
    
      - init:
          assign:
            - my_list: ["zero","one","two","three"]
      - returnStep:
          return: ${len(my_list)}  # returns `4`

### JSON
    
    
      [
        {
          "init": {
            "assign": [
              {
                "my_list": [
                  "zero",
                  "one",
                  "two",
                  "three"
                ]
              }
            ]
          }
        },
        {
          "returnStep": {
            "return": "${len(my_list)}"
          }
        }
      ]

## Reverse elements in a list

You can use a [`for` loop](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration) and the [`list.prepend` function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/prepend) to reverse the order of elements in a list:

### YAML
    
    
    # Reverse the order of elements in a list
    # Expected output: `[3,2,1]`
    main:
      steps:
        - call_reverse_list:
            call: reverse_list
            args:
              source: [1, 2, 3]
            result: output
        - return_message:
            return: ${output}
    
    reverse_list:
      params: [source]
      steps:
        - init:
            assign:
              - dst: []
        - reverse:
            for:
              value: entry
              in: ${source}
              steps:
                - prepend_value:
                    assign:
                      - dst: ${list.prepend(dst, entry)}
        - return_destination:
            return: ${dst}

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "call_reverse_list": {
              "call": "reverse_list",
              "args": {
                "source": [
                  1,
                  2,
                  3
                ]
              },
              "result": "output"
            }
          },
          {
            "return_message": {
              "return": "${output}"
            }
          }
        ]
      },
      "reverse_list": {
        "params": [
          "source"
        ],
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "dst": []
                }
              ]
            }
          },
          {
            "reverse": {
              "for": {
                "value": "entry",
                "in": "${source}",
                "steps": [
                  {
                    "prepend_value": {
                      "assign": [
                        {
                          "dst": "${list.prepend(dst, entry)}"
                        }
                      ]
                    }
                  }
                ]
              }
            }
          },
          {
            "return_destination": {
              "return": "${dst}"
            }
          }
        ]
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
