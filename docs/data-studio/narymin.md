---
url: https://docs.cloud.google.com/data-studio/narymin/
title: NARY_MIN \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:02.820810+00:00
---

# NARY_MIN  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/narymin/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  NARY_MIN Stay organized with collections  Save and categorize content based on your preferences. 

`NARY_MIN` is similar to `MIN`, except it lets you compare multiple values.

## Syntax
    
    
    NARY_MIN(X, Y, [,Z]*)
    

### Parameters

  * `X, Y, Z` \- fields or expressions to be evaluated.



## Examples

### Example 1

This example shows how you can mix fields, calculations, and literals in an `NARY_MIN` function:

`NARY_MIN(REVENUE, (COST * 2), 10, SESSIONS))`

### Example 2

Suppose you want to determine the minimum sales for your 3 sales regions by date and your data looks like this:

Date  |  Region 1 Sales  |  Region 2 Sales  |  Region 3 Sales   
---|---|---|---  
Date 1  |  100  |  200  |  150   
Date 2  |  75  |  130  |  150   
Date 3  |  225  |  185  |  230   
  
You could use the `NARY_MIN` function to determine the minimum sales for a given date:

Example formula |  Date  | Output  
---|---|---  
` NARY_MIN(Region 1 Sales, Region 2 Sales, Region 3 Sales,) ` |  Date 1  |  100   
Date 2  |  75   
Date 3  |  185   
  
### Notes

`NARY_MIN` requires at least 2 arguments. At least one argument must be a field or an expression containing a field.

`NARY_MIN` works on numeric fields or expressions only. If you apply this function to other data types, you'll get an error.

## Related resources

  * [NARY_MAX](https://docs.cloud.google.com/data-studio/narymax)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
