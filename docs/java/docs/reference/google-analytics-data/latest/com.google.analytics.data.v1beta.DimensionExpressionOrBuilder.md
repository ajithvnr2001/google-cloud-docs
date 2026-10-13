---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpressionOrBuilder
title: Interface DimensionExpressionOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:29.814166+00:00
---

# Interface DimensionExpressionOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpressionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DimensionExpressionOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface DimensionExpressionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConcatenate()
    
    
    public abstract DimensionExpression.ConcatenateExpression getConcatenate()

Used to combine dimension values to a single dimension. For example, dimension "country, city": concatenate(country, ", ", city).

`.google.analytics.data.v1beta.DimensionExpression.ConcatenateExpression concatenate = 6; `

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.ConcatenateExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.ConcatenateExpression)` | The concatenate.  
  
### getConcatenateOrBuilder()
    
    
    public abstract DimensionExpression.ConcatenateExpressionOrBuilder getConcatenateOrBuilder()

Used to combine dimension values to a single dimension. For example, dimension "country, city": concatenate(country, ", ", city).

`.google.analytics.data.v1beta.DimensionExpression.ConcatenateExpression concatenate = 6; `

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.ConcatenateExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.ConcatenateExpressionOrBuilder)` |   
  
### getLowerCase()
    
    
    public abstract DimensionExpression.CaseExpression getLowerCase()

Used to convert a dimension value to lower case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression lower_case = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.CaseExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.CaseExpression)` | The lowerCase.  
  
### getLowerCaseOrBuilder()
    
    
    public abstract DimensionExpression.CaseExpressionOrBuilder getLowerCaseOrBuilder()

Used to convert a dimension value to lower case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression lower_case = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.CaseExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.CaseExpressionOrBuilder)` |   
  
### getOneExpressionCase()
    
    
    public abstract DimensionExpression.OneExpressionCase getOneExpressionCase()

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.OneExpressionCase](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.OneExpressionCase)` |   
  
### getUpperCase()
    
    
    public abstract DimensionExpression.CaseExpression getUpperCase()

Used to convert a dimension value to upper case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression upper_case = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.CaseExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.CaseExpression)` | The upperCase.  
  
### getUpperCaseOrBuilder()
    
    
    public abstract DimensionExpression.CaseExpressionOrBuilder getUpperCaseOrBuilder()

Used to convert a dimension value to upper case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression upper_case = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DimensionExpression.CaseExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.DimensionExpression.CaseExpressionOrBuilder)` |   
  
### hasConcatenate()
    
    
    public abstract boolean hasConcatenate()

Used to combine dimension values to a single dimension. For example, dimension "country, city": concatenate(country, ", ", city).

`.google.analytics.data.v1beta.DimensionExpression.ConcatenateExpression concatenate = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the concatenate field is set.  
  
### hasLowerCase()
    
    
    public abstract boolean hasLowerCase()

Used to convert a dimension value to lower case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression lower_case = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lowerCase field is set.  
  
### hasUpperCase()
    
    
    public abstract boolean hasUpperCase()

Used to convert a dimension value to upper case.

`.google.analytics.data.v1beta.DimensionExpression.CaseExpression upper_case = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the upperCase field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
