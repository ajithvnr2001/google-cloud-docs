---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration/
title: Iteration \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:52.459642+00:00
---

# Iteration  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Iteration Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Workflows syntax to iterate through a [list](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists).

You can use a `for` loop to iterate over a sequence of numbers or through a collection of data, such as a list or [map](https://docs.cloud.google.com/workflows/docs/reference/syntax/maps).

You can walk through every item in a list or map using item-based iteration. If you have a specific range of numeric values to iterate through, you can use range-based iteration.

**Note:** There is a known issue where the placement of `for` directly after `try` causes an error. For details and the workaround, see [Known issues](https://docs.cloud.google.com/workflows/docs/issues).

## for loops for lists

The following syntax shows an index-based iteration in Workflows:

### YAML
    
    
      - FOR_LOOP_STEP_NAME:
          for:
              value: LOOP_VARIABLE_NAME
              index: INDEX_VARIABLE_NAME
              in: ${LIST_EXPRESSION}      # or simply in: LIST_DEFINITION
    
              steps:
                  - STEP_NAME_A:
                    ...

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME": {
            "for": {
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

Replace the following:

  * `LOOP_VARIABLE_NAME`: refers to the value of the currently iterated element. The variable name must not be used in assignments or expressions outside of the loop. The same name can be used in multiple loops, as long as they are not nested.
  * `INDEX_VARIABLE_NAME` (optional): contains the value to the current offset of the iteration. This always starts at 0 and goes to `len(${LIST_EXPRESSION}) - 1`. The variable name must not be used in assignments or expressions outside of the loop. The same name can be used in multiple loops, as long as they are not nested.
  * `LIST_EXPRESSION`: an expression that evaluates into a list or a [list definition](https://docs.cloud.google.com/workflows/docs/reference/syntax/lists#list-definition).



Notes:

  * `for`: required. This is the top-level element indicating the beginning of a for loop.
  * `steps`: required. Each iteration the `steps` will be executed.
  * The 4-space indentation before `value`, `index`, `in`, and `steps` are required.
  * The ordering of `value`, `index`, `in`, and `steps` does not matter.
  * Do not assign new values in the loop to variables used in the loop expression. This is an undefined behaviour.
  * When iterating over maps, `${keys(map)}` can be used to obtain a list of keys. `keys()` always returns a sorted list.
  * All loop variables (for example, `INDEX_VARIABLE_NAME`, `LOOP_VARIABLE_NAME`, or any variable that is not assigned to outside of the loop) have loop-level scope. These variables are cleared after exiting the loop and accessing them outside of the loop will raise an error when deploying the workflow. For more information, see [Variable scope](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#variable-scope). The following sample demonstrates how any variable created in a loop does not exist outside of that loop:

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




## Examples

These examples demonstrate the syntax.

### List iteration

### YAML
    
    
    - assignStep:
        assign:
          - list: [1, 2, 3, 4, 5]
          - sum: 0
    - loopStep:
        for:
          value: v                          # required, v = 1, 2, …, 5
          in: ${list}
          steps:
            - getStep:
                assign:
                  - sum: ${sum + v}
    - returnStep:
        return: ${sum}                      # sum is 15

### JSON
    
    
    [
      {
        "assignStep": {
          "assign": [
            {
              "list": [
                1,
                2,
                3,
                4,
                5
              ]
            },
            {
              "sum": 0
            }
          ]
        }
      },
      {
        "loopStep": {
          "for": {
            "value": "v",
            "in": "${list}",
            "steps": [
              {
                "getStep": {
                  "assign": [
                    {
                      "sum": "${sum + v}"
                    }
                  ]
                }
              }
            ]
          }
        }
      },
      {
        "returnStep": {
          "return": "${sum}"
        }
      }
    ]

### Map iteration

### YAML
    
    
    - assignStep:
        assign:
          - map:
              1: 10
              2: 20
              3: 30
          - sum: 0
    - loopStep:
        for:
          value: key                        # key = 1, 2, 3
          in: ${keys(map)}                  # [1, 2, 3]
          steps:
            - sumStep:
                assign:
                  - sum: ${sum + map[key]}
    - returnStep:
        return: ${sum}                      # sum is 60

### JSON
    
    
    [
      {
        "assignStep": {
          "assign": [
            {
              "map": {
                "1": 10,
                "2": 20,
                "3": 30
              }
            },
            {
              "sum": 0
            }
          ]
        }
      },
      {
        "loopStep": {
          "for": {
            "value": "key",
            "in": "${keys(map)}",
            "steps": [
              {
                "sumStep": {
                  "assign": [
                    {
                      "sum": "${sum + map[key]}"
                    }
                  ]
                }
              }
            ]
          }
        }
      },
      {
        "returnStep": {
          "return": "${sum}"
        }
      }
    ]

### Make HTTP requests in a for-in loop

### YAML
    
    
    - getUserIDs:
        call: http.get
        args:
          url: https://example.com/getUserIDs
        result: userIds
    - saveUserInfo:
        for:
          value: uid
          in: ${userIds}
          steps:
            - tryStep:
                try:
                  steps:
                    - get:
                        call: http.get
                        args:
                          url: ${"https://example.com/getUserInfo?userId=" + string(uid)}
                        result: userInfo
                    - post:
                        call: http.post
                        args:
                          url: ${"https://example.com/saveUserInfo?userId=" + string(uid)}
                          body: ${userInfo}
                except:
                  as: e
                  steps:
                    - knownErrors:
                        switch:
                          - condition: ${not("HttpError" in e.tags)}
                            return: '${"Connection problem with userID: " + string(uid)}'
                    - unhandledErrors:
                        raise: ${e}

### JSON
    
    
    [
      {
        "getUserIDs": {
          "call": "http.get",
          "args": {
            "url": "https://example.com/getUserIDs"
          },
          "result": "userIds"
        }
      },
      {
        "saveUserInfo": {
          "for": {
            "value": "uid",
            "in": "${userIds}",
            "steps": [
              {
                "tryStep": {
                  "try": {
                    "steps": [
                      {
                        "get": {
                          "call": "http.get",
                          "args": {
                            "url": "${\"https://example.com/getUserInfo?userId=\" + string(uid)}"
                          },
                          "result": "userInfo"
                        }
                      },
                      {
                        "post": {
                          "call": "http.post",
                          "args": {
                            "url": "${\"https://example.com/saveUserInfo?userId=\" + string(uid)}",
                            "body": "${userInfo}"
                          }
                        }
                      }
                    ]
                  },
                  "except": {
                    "as": "e",
                    "steps": [
                      {
                        "knownErrors": {
                          "switch": [
                            {
                              "condition": "${not(\"HttpError\" in e.tags)}",
                              "return": "${\"Connection problem with userID: \" + string(uid)}"
                            }
                          ]
                        }
                      },
                      {
                        "unhandledErrors": {
                          "raise": "${e}"
                        }
                      }
                    ]
                  }
                }
              }
            ]
          }
        }
      }
    ]

### Use Google Translate in a for-in loop

### YAML
    
    
    - init:
        assign:
          - textAndSourceLang:
              "Hello": "en"
              "Ciao": "it"
              "Auf wiedersehen": "de"
              "Goodbye": "en"
              "Bonjour": "fr"
              "lkajshflkj": "unknown"
          - allowedSourceLang: ["en", "de", "it", "fr"]
    - translateToFrench:
        for:
          value: text
          in: ${keys(textAndSourceLang)}
          steps:
            - verifySource:
                switch:
                  - condition: ${not(textAndSourceLang[text] in allowedSourceLang)}
                    next: continue
                  - condition: ${textAndSourceLang[text] == "fr"}
                    next: skipFrenchTranslation
            - translate:
                call: googleapis.translate.v2.translations.translate
                args:
                  q: ${text}
                  target: "fr"
                  format: "text"
                  source: ${textAndSourceLang[text]}
                result: translation
            - getTranslation:
                assign:
                  - translated: ${translation.data.translations[0].translatedText}
                next: print
            - skipFrenchTranslation:
                assign:
                  - translated: ${text}
            - print:
                call: sys.log
                args:
                  text: '${"Original: " + text + ", Translation: " + translated}'

### JSON
    
    
    [
      {
        "init": {
          "assign": [
            {
              "textAndSourceLang": {
                "Hello": "en",
                "Ciao": "it",
                "Auf wiedersehen": "de",
                "Goodbye": "en",
                "Bonjour": "fr",
                "lkajshflkj": "unknown"
              }
            },
            {
              "allowedSourceLang": [
                "en",
                "de",
                "it",
                "fr"
              ]
            }
          ]
        }
      },
      {
        "translateToFrench": {
          "for": {
            "value": "text",
            "in": "${keys(textAndSourceLang)}",
            "steps": [
              {
                "verifySource": {
                  "switch": [
                    {
                      "condition": "${not(textAndSourceLang[text] in allowedSourceLang)}",
                      "next": "continue"
                    },
                    {
                      "condition": "${textAndSourceLang[text] == \"fr\"}",
                      "next": "skipFrenchTranslation"
                    }
                  ]
                }
              },
              {
                "translate": {
                  "call": "googleapis.translate.v2.translations.translate",
                  "args": {
                    "q": "${text}",
                    "target": "fr",
                    "format": "text",
                    "source": "${textAndSourceLang[text]}"
                  },
                  "result": "translation"
                }
              },
              {
                "getTranslation": {
                  "assign": [
                    {
                      "translated": "${translation.data.translations[0].translatedText}"
                    }
                  ],
                  "next": "print"
                }
              },
              {
                "skipFrenchTranslation": {
                  "assign": [
                    {
                      "translated": "${text}"
                    }
                  ]
                }
              },
              {
                "print": {
                  "call": "sys.log",
                  "args": {
                    "text": "${\"Original: \" + text + \", Translation: \" + translated}"
                  }
                }
              }
            ]
          }
        }
      }
    ]

## for loops for number ranges

The following syntax shows a range-based iteration in Workflows:

### YAML
    
    
      - FOR_LOOP_STEP_NAME:
          for:
              value: LOOP_VARIABLE_NAME
              range: ${[BEGIN_EXPRESSION, END_EXPRESSION]}
              steps:
                  - STEP_NAME_A:
                    ...

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME": {
            "for": {
              "value": "LOOP_VARIABLE_NAME",
              "range": "${[BEGIN_EXPRESSION, END_EXPRESSION]}",
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

  * `for`: Required. This is the top-level element indicating the beginning of a for loop.
  * `value`: Required. The variable named in `LOOP_VARIABLE_NAME` refers to the value of the currently iterated element. The variable name must not be used in assignments or expressions outside of the loop. The same name can be used in multiple loops, as long as they are not nested.
  * `range`: Required. A list of two expressions, specifying the beginning and end of the range, both **inclusive**.

    * The expressions must evaluate into incrementable values; that is, integer or double.
    * Negative values are allowed. For example, `range: [-10, -1]` will result in 10 iterations.
    * Floating point values are allowed. Floating point values are not rounded. For example, `range: [-1.1, -1]` will result in 1 iteration starting at -1.1.
    * If `END_EXPRESSION` is evaluated to be smaller than `BEGIN_EXPRESSION`, the loop will have 0 iterations.
**Note:** Make sure that you do not use multiple expressions inside a list like this: `[${rangeStart}, ${rangeEnd}])`. See [Troubleshoot issues](https://docs.cloud.google.com/workflows/docs/troubleshooting#expressions-in-list).
  * `steps`: Required. Each iteration the `steps` will be executed.

  * Each iteration increments the loop counter by 1, or when doubles are provided by 1.0. For example, `range: [1.1, 2.8]` causes the loop to have two iterations.

  * The 4-space indentation before `value`, `range`, and `steps` are required.

  * The ordering of `value` ,`range`, and `steps` does not matter.

  * All loop variables (for example, `LOOP_VARIABLE_NAME` or any variable that is not assigned to outside of the loop) have loop-level scope. These variables are cleared after exiting the loop and accessing them outside of the loop will raise an error when deploying the workflow. For more information, see [Variable scope](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#variable-scope).




## Examples

These examples demonstrate the syntax.

### Basic for-range

### YAML
    
    
    - assignStep:
        assign:
          - sum: 0
    - loopStep:
        for:
          value: v                    # required, v = 1, 2, …, 9
          range: [1, 9]               # inclusive beginning and ending values
          steps:
            - sumStep:
                assign:
                  - sum: ${sum + v}   # v = 1, 2, … 9
    - returnStep:
        return: ${sum}                # sum is 45

### JSON
    
    
    [
      {
        "assignStep": {
          "assign": [
            {
              "sum": 0
            }
          ]
        }
      },
      {
        "loopStep": {
          "for": {
            "value": "v",
            "range": [
              1,
              9
            ],
            "steps": [
              {
                "sumStep": {
                  "assign": [
                    {
                      "sum": "${sum + v}"
                    }
                  ]
                }
              }
            ]
          }
        }
      },
      {
        "returnStep": {
          "return": "${sum}"
        }
      }
    ]

### for-range to make HTTP requests

### YAML
    
    
    - init:
        assign:
          - minTemp: -14.5
          - maxTemp: 42.8
    - storeNormalBodyTemp:
        for:
          value: temp
          range: ${[minTemp, maxTemp]}
          steps:
            - checkTemp:
                call: http.get
                args:
                  url: ${"https://example.com/isBodyTempNormal?temp=" + string(temp)}
                result: isNormal
            - storeOrBreak:
                switch:
                  - condition: ${isNormal}
                    next: storeTemp
                next: break
            - storeTemp:
                call: http.post
                args:
                  url: ${"https://example.com/storeTemp?temp=" + string(temp)}
                  body: ${temp}

### JSON
    
    
    [
      {
        "init": {
          "assign": [
            {
              "minTemp": -14.5
            },
            {
              "maxTemp": 42.8
            }
          ]
        }
      },
      {
        "storeNormalBodyTemp": {
          "for": {
            "value": "temp",
            "range": "${[minTemp, maxTemp]}",
            "steps": [
              {
                "checkTemp": {
                  "call": "http.get",
                  "args": {
                    "url": "${\"https://example.com/isBodyTempNormal?temp=\" + string(temp)}"
                  },
                  "result": "isNormal"
                }
              },
              {
                "storeOrBreak": {
                  "switch": [
                    {
                      "condition": "${isNormal}",
                      "next": "storeTemp"
                    }
                  ],
                  "next": "break"
                }
              },
              {
                "storeTemp": {
                  "call": "http.post",
                  "args": {
                    "url": "${\"https://example.com/storeTemp?temp=\" + string(temp)}",
                    "body": "${temp}"
                  }
                }
              }
            ]
          }
        }
      }
    ]

## Jump within a loop

Only jumping between named steps belonging to the same for loop is allowed. Jumping in or out of a for loop, or between two different for loops, is not allowed.

### YAML
    
    
      - FOR_LOOP_STEP_NAME:
          for:
              value: LOOP_VARIABLE_NAME
              in: ${LIST_EXPRESSION_A}    # or simply in: LIST_DEFINITION
              steps:
                  - STEP_NAME_A:
                      next: STEP_NAME_C
                  - STEP_NAME_B:
                      next: STEP_NAME_C
                  - STEP_NAME_C:
                      ...

### JSON
    
    
      [
        {
          "FOR_LOOP_STEP_NAME": {
            "for": {
              "value": "LOOP_VARIABLE_NAME",
              "in": "${LIST_EXPRESSION_A}",
              "steps": [
                {
                  "STEP_NAME_A": {
                    "next": "STEP_NAME_C"
                  }
                },
                {
                  "STEP_NAME_B": {
                    "next": "STEP_NAME_C"
                  }
                },
                {
                  "STEP_NAME_C":
                    ...
                }
              ]
            }
          }
        }
      ]

## Use break/continue in a loop

To change the flow of a for loop, you can use `next: break` or `next: continue`. Note that `break` and `continue` are reserved jump targets defined implicitly within a loop. Named steps called `break` or `continue` within a for loop are not allowed; however, they are allowed outside of a for loop.

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
              range: ${[BEGIN_EXPRESSION, END_EXPRESSION]}
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
              "range": "${[BEGIN_EXPRESSION, END_EXPRESSION]}",
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

## Iterate through a list

This sample shows how you can use a combination of conditional jumps, variables, and the `len()` function to iterate through a list.

### YAML
    
    
    - define:
        assign:
          - array: ["foo", "ba", "r"]
          - result: ""
          - i: 0
    - check_condition:
        switch:
          - condition: ${len(array) > i}
            next: iterate
        next: exit_loop
    - iterate:
        assign:
          - result: ${result + array[i]}
          - i: ${i+1}
        next: check_condition
    - exit_loop:
        return:
          concat_result: ${result}

### JSON
    
    
    [
      {
        "define": {
          "assign": [
            {
              "array": [
                "foo",
                "ba",
                "r"
              ]
            },
            {
              "result": ""
            },
            {
              "i": 0
            }
          ]
        }
      },
      {
        "check_condition": {
          "switch": [
            {
              "condition": "${len(array) > i}",
              "next": "iterate"
            }
          ],
          "next": "exit_loop"
        }
      },
      {
        "iterate": {
          "assign": [
            {
              "result": "${result + array[i]}"
            },
            {
              "i": "${i+1}"
            }
          ],
          "next": "check_condition"
        }
      },
      {
        "exit_loop": {
          "return": {
            "concat_result": "${result}"
          }
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
