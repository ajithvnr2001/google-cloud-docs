---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/completing/
title: Complete the execution of a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:44.782732+00:00
---

# Complete the execution of a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/completing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Complete the execution of a workflow Stay organized with collections  Save and categorize content based on your preferences. 

You can use `return` in the main workflow to stop a workflow's execution. You can also finish a workflow by simply completing the final step (assuming that the step doesn't jump to another).

A workflow's execution stops when one of the following occurs:

  * An [error is raised and not caught](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * After all steps have been executed
  * When the keywords `end` or `return` are used in the main workflow



## Use `end`

In the main workflow, you can use `next: end` to stop a workflow's execution if you don't need to return a value. A main workflow that executes a `next: end` step completes with `null` as the result.

In a subworkflow, you can use `next: end` in a step to make it the last step in the subworkflow and return `null`. It does not need to be in a separate step (unlike `return`) and can be used in any step. When using either `next: end` or `return`, control is returned to the calling subworkflow.

### YAML
    
    
      - STEP_NAME:
          ...
          next: end
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            ...
            "next": "end"
          }
        }
      ]
        

## Use `return`

Use `return` to stop a workflow's execution and return a value, variable, or expression:

### YAML
    
    
      - STEP_NAME:
          ...
          return: ${VARIABLE}
      

### JSON
    
    
      [
        {
          "STEP_NAME": {
            ...
            "return": "${VARIABLE}"
          }
        }
      ]
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
