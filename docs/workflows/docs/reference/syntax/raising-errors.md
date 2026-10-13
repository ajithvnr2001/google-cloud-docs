---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors/
title: Raise errors \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:48.987475+00:00
---

# Raise errors  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/raising-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Raise errors Stay organized with collections  Save and categorize content based on your preferences. 

You can raise custom errors using the `raise` syntax, and you can catch and handle errors using a [`try/except` block](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors).

Errors can be either a string or a map. You can use user-defined keys:

### YAML
    
    
      - STEP_NAME:
          raise:
              KEY_1: VALUE_1
              KEY_2: VALUE_2

### JSON
    
    
      [
        {
          "STEP_NAME": {
            "raise": {
              "KEY_1": "VALUE_1",
              "KEY_2": "VALUE_2"
            }
          }
        }
      ]

## Examples

**String**

### YAML
    
    
      - step_a:
          raise: "Something went wrong."

### JSON
    
    
      [
        {
          "step_a": {
            "raise": "Something went wrong."
          }
        }
      ]

**Map**

### YAML
    
    
      - step_a:
          raise:
              code: 55
              message: "Something went wrong."

### JSON
    
    
      [
        {
          "step_a": {
            "raise": {
              "code": 55,
              "message": "Something went wrong."
            }
          }
        }
      ]

## What's next

  * [Workflow errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/error-types)
  * [Catch errors](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors)
  * [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
