---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/strings/
title: Strings \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:57.112424+00:00
---

# Strings  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/strings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Strings Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows syntax supports a string data type with UTF‑8 encoding ([maximum length](https://docs.cloud.google.com/workflows/quotas#resource_limits)).

For information on conversion and built-in string functions, see [Data types, functions, operators](https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes).

For other text processing functions, see the Workflows standard library [`text` module reference](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview#module:-text).

## Assign a string variable

The value of a static string can be assigned to a variable. For example:

### YAML
    
    
      - step:
          assign:
            - string: "hello"
      

### JSON
    
    
      [
        {
          "step": {
            "assign": [
              {
                "string": "hello"
              }
            ]
          }
        }
      ]
        

## Concatenate using expressions

You can dynamically concatenate strings using expressions and the `+` operator. For example:

### YAML
    
    
        - step:
            assign:
              - outputVar: ${"Hello, " + firstName}
        

### JSON
    
    
        [
          {
            "step": {
              "assign": [
                {
                  "outputVar": "${\"Hello \" + firstName}"
                }
              ]
            }
          }
        ]

**Important:** In YAML, expressions containing colons can cause unexpected behaviour when the colon is interpreted as defining a map. You can resolve this issue by wrapping the YAML expression in single quotes: 

Recommended: `'${"thisVar: " + myVar}'`

Not recommended: `${"thisVar: " + myVar}`

For details, see [Expressions containing colons](https://docs.cloud.google.com/workflows/docs/troubleshooting#expressions-colons).

## Concatenate over multiple lines

Since each assignment is processed sequentially, you can concatenate a string over multiple lines by repeating the variable and splitting the assignment. For example:

### YAML
    
    
    main:
      steps:
        - assign_vars:
            assign:
              - concatLines: "say"
              - concatLines: ${concatLines+" "+"hello"}
              - concatLines: ${concatLines+" "+"to the world"}
        - returnOutput:
            return: ${concatLines}

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "assign_vars": {
              "assign": [
                {
                  "concatLines": "say"
                },
                {
                  "concatLines": "${concatLines+\" \"+\"hello\"}"
                },
                {
                  "concatLines": "${concatLines+\" \"+\"to the world\"}"
                }
              ]
            }
          },
          {
            "returnOutput": {
              "return": "${concatLines}"
            }
          }
        ]
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
