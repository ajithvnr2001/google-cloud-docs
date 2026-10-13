---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/prepend/
title: Function: list.prepend \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:14.851649+00:00
---

# Function: list.prepend  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/list/prepend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: list.prepend Stay organized with collections  Save and categorize content based on your preferences. 

Creates a copy of a list with a new element added to the beginning.

## Arguments

Arguments  
---  
`objs` |  `list` The source list. Note that this list is not modified.  
`val` |  `any` The element that will be prepended to the beginning.  
  
## Returns

A copy of `objs` with `val` added to the beginning.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `objs` is not a list.  
  
## Examples
    
    
    # Prepend `val` to start of copy of `my_list`
    # Returns `["three","zero","one","two"]`
    - init:
        assign:
          - my_list: ["zero","one","two"]
          - val: "three"
    - returnStep:
        return: ${list.prepend(my_list, val)}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
