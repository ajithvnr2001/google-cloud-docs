---
url: https://docs.cloud.google.com/data-studio/avg/
title: AVG \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:50.477993+00:00
---

# AVG  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/avg/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  AVG Stay organized with collections  Save and categorize content based on your preferences. 

The `AVG` function calculates the average value of a numeric field.

## Syntax

`AVG(X)`

### Parameters

  * `X` \- a field or expression that evaluates to an unaggregated number.



## How the `AVG` function works

The `AVG` function takes 1 parameter, which must be the name of a numeric field, or a numeric expression. `AVG` returns the average for all values of that field or expression.

You can't apply this function to a pre-aggregated field (Aggregation equals `Auto`), or to an expression which is the result of another aggregation function. For example, a formula such as `AVG(SUM(x))` will produce an error.

**Note:** This function can be applied in one of the following ways: 

  * In a data source, change a field's Aggregation to `Average`.
  * In a report, [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports) in a chart.



## Examples

In these examples, the parameters passed to `AVG` are unaggregated numeric dimensions (i.e., they have an **Aggregation** type of **None** ).

Example formula | Input | Output  
---|---|---  
`AVG(Latency)` | 

  * 0.02
  * 0.07
  * 0.09

| 0.06  
`AVG(CASE WHEN My Dimension < 1 THEN.5 WHEN My Dimension >= 1 AND My Dimension < 5 THEN 1 ELSE 2 END)` | 

  * 0
  * 0.5
  * 3
  * 5

| 1  
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
