---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/floor/
title: Function: math.floor \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:18.540335+00:00
---

# Function: math.floor  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/math/floor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: math.floor Stay organized with collections  Save and categorize content based on your preferences. 

Returns the floor of a number.

Rounds down to the largest integer less than or equal to a given number.

## Arguments

Arguments  
---  
`x` | An integer or floating-point number.  
  
## Raised exceptions

Exceptions  
---  
`TypeError` | If `x` is not an integer or floating-point number.  
  
## Examples

### Example 1
    
    
    # Return floor of a number
    # For example, returns `23` 
    - returnStep:
        return: ${math.floor(23.67)}

### Example 2
    
    
    # Return floor of a number
    # For example, returns `-24` 
    - returnStep:
        return: ${math.floor(-23.67)}

### Example 3
    
    
    # Return floor of a number
    # For example, returns `0` 
    - returnStep:
        return: ${math.floor(0)}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
