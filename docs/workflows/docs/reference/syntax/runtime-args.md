---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args/
title: Runtime arguments \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:54.983457+00:00
---

# Runtime arguments  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Runtime arguments Stay organized with collections  Save and categorize content based on your preferences. 

You can access data passed at runtime by adding a `params` field to your workflow, which names the argument the workflow uses to store the data you pass in. If passing in a JSON object, you can then use dot notation to access the arguments. For example:

### YAML
    
    
      main:
          params: [ARG_NAME]
          steps:
            - step1:
                return: ${ARG_NAME.PARAM_NAME}
      

### JSON
    
    
      {
        "main": {
          "params": ["ARG_NAME",]
          "steps": [
            {
              "step1": {
                "return": "${ARG_NAME.PARAM_NAME}"
              }
            }
          ]
        }
      }
        

Note the following:

  * For a workflow to receive runtime arguments there must be a `main` block.

  * The `main` block accepts a single argument that is the name of any valid JSON data type: an array, an object, or a string.

  * As a best practice, passing in an object with multiple, named arguments makes it easier to understand their purpose, and to add arguments. You can also then use dot notation to access the arguments.

  * Other subworkflows can have multiple arguments.




The following workflow returns a "Hello" greeting to a person whose first and last name you pass as a string in JSON format to the workflow in an execution request. For example, if you pass in the argument `{"firstName":"Workflows","lastName":"User"}`, the results of the execution should include the output "Hello, Workflows User".

### YAML
    
    
        main:
          params: [person]
          steps:
            - step1:
                assign:
                  - outputVar: ${"Hello, " + person.firstName + " " + person.lastName}
            - step2:
                return: ${outputVar}
        

### JSON
    
    
        {
          "main": {
            "params": [
              "person"
            ],
            "steps": [
              {
                "step1": {
                  "assign": [
                    {
                      "outputVar": "${"Hello " + person.firstName + " " + person.lastName}"
                    }
                  ]
                }
              },
              {
                "step2": {
                  "return": "${outputVar}"
                }
              }
            ]
          }
        }
          

For more information about using runtime arguments, see [Pass runtime arguments in an execution request](https://docs.cloud.google.com/workflows/docs/passing-runtime-arguments).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
