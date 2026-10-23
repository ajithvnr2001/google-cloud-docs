---
url: https://docs.cloud.google.com/data-studio/cast/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:01.954093+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/cast/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CAST

Converts a field or expression from one type to another type.

## Sample usage

  * `CAST(Number_field AS TEXT)`
  * `CAST(Text_field AS NUMBER)`
  * `CAST(Date_field as DATETIME)`



## Syntax
    
    
    CAST field_expression AS type
    

### Parameters

  * `field_expression` \- a field or expression.

  * `type` \- a data type literal.




### `CAST` data type literals

You can cast from or to the following types:

From type  |  To type   
---|---  
Text  | 

  * `DATE`
  * `DATETIME`
  * `NUMBER`

  
Number  | 

  * `TEXT`

  
Date  | 

  * `DATETIME`
  * `TEXT`

  
Date & Time  | 

  * `DATETIME`
  * `TEXT`

  
  
## Examples

**Goal** : Count website sessions longer than _N_ seconds.

In a Google Analytics data source, **Session Duration** is a text dimension. The first step to counting sessions longer than _N_ is to convert this to a number using `CAST`. The second step is to use the `CASE` statement to identify sessions longer than a certain value—we'll say 60 seconds for this example. We'll combine `CASE` with `SUM` to do the counting.

**Step 1** : Create a new calculated field **Session Duration (number)** with the following formula:

`CAST(Session Duration AS NUMBER)`

**Step 2** : Create a new calculated field **Long Sessions** _:_

`SUM(CASE WHEN Session Duration > 60 THEN 1 ELSE 0 END)`

## Notes

You cannot  `CAST` aggregated fields.

  * Casts from `[DATE|DATETIME]` to `TEXT` return the canonical string formats shown following. To return a different format, use the `FORMAT_DATETIME` function.
  * Casts from `TEXT` to `[DATE|DATETIME]` accept only the canonical string format. To parse a different format, use the `PARSE_*` functions.

Type  |  Canonical STRING format   
---|---  
DATE  |  ` YYYY-\[M\]M-\[D\]D `  
DATETIME  |  ` YYYY-\[M\]M-\[D\]D \[\[H\]H:\[M\]M:\[S\]S\[.DDDDDD\]\] `  
  
### Coercion to text

When an expression requires a text string, Data Studio coerces (implicitly converts) non-string values to a string data type.

Type  |  Canonical STRING format   
---|---  
DATE  |  ` YYYY-MM-DD `  
DATETIME  |  ` YYYY-MM-DD HH:MM:SS\[.DDD\[DDD\]\] `  
  
For example, suppose we have a `created_datetime` field of type DATETIME and the following formula:
    
    
    CONCAT("Created on ", created_datetime)
    

This formula returns the following:
    
    
    Created on 2019-11-22 16:30:00.739182
    

This formula doesn't require an explicit `CAST(created_datetime AS TEXT)`.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [CASE expression](https://docs.cloud.google.com/data-studio/case-searched)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
