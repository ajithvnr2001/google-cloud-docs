---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder
title: Interface FilterExpressionOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:31.708087+00:00
---

# Interface FilterExpressionOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FilterExpressionOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface FilterExpressionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAndGroup()
    
    
    public abstract FilterExpressionList getAndGroup()

The FilterExpressions in and_group have an AND relationship.

`.google.analytics.data.v1beta.FilterExpressionList and_group = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionList](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionList)` | The andGroup.  
  
### getAndGroupOrBuilder()
    
    
    public abstract FilterExpressionListOrBuilder getAndGroupOrBuilder()

The FilterExpressions in and_group have an AND relationship.

`.google.analytics.data.v1beta.FilterExpressionList and_group = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionListOrBuilder)` |   
  
### getExprCase()
    
    
    public abstract FilterExpression.ExprCase getExprCase()

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression.ExprCase](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression.ExprCase)` |   
  
### getFilter()
    
    
    public abstract Filter getFilter()

A primitive filter. In the same FilterExpression, all of the filter's field names need to be either all dimensions or all metrics.

`.google.analytics.data.v1beta.Filter filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Filter](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.Filter)` | The filter.  
  
### getFilterOrBuilder()
    
    
    public abstract FilterOrBuilder getFilterOrBuilder()

A primitive filter. In the same FilterExpression, all of the filter's field names need to be either all dimensions or all metrics.

`.google.analytics.data.v1beta.Filter filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterOrBuilder)` |   
  
### getNotExpression()
    
    
    public abstract FilterExpression getNotExpression()

The FilterExpression is NOT of not_expression.

`.google.analytics.data.v1beta.FilterExpression not_expression = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpression)` | The notExpression.  
  
### getNotExpressionOrBuilder()
    
    
    public abstract FilterExpressionOrBuilder getNotExpressionOrBuilder()

The FilterExpression is NOT of not_expression.

`.google.analytics.data.v1beta.FilterExpression not_expression = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionOrBuilder)` |   
  
### getOrGroup()
    
    
    public abstract FilterExpressionList getOrGroup()

The FilterExpressions in or_group have an OR relationship.

`.google.analytics.data.v1beta.FilterExpressionList or_group = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionList](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionList)` | The orGroup.  
  
### getOrGroupOrBuilder()
    
    
    public abstract FilterExpressionListOrBuilder getOrGroupOrBuilder()

The FilterExpressions in or_group have an OR relationship.

`.google.analytics.data.v1beta.FilterExpressionList or_group = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FilterExpressionListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.FilterExpressionListOrBuilder)` |   
  
### hasAndGroup()
    
    
    public abstract boolean hasAndGroup()

The FilterExpressions in and_group have an AND relationship.

`.google.analytics.data.v1beta.FilterExpressionList and_group = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the andGroup field is set.  
  
### hasFilter()
    
    
    public abstract boolean hasFilter()

A primitive filter. In the same FilterExpression, all of the filter's field names need to be either all dimensions or all metrics.

`.google.analytics.data.v1beta.Filter filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filter field is set.  
  
### hasNotExpression()
    
    
    public abstract boolean hasNotExpression()

The FilterExpression is NOT of not_expression.

`.google.analytics.data.v1beta.FilterExpression not_expression = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the notExpression field is set.  
  
### hasOrGroup()
    
    
    public abstract boolean hasOrGroup()

The FilterExpressions in or_group have an OR relationship.

`.google.analytics.data.v1beta.FilterExpressionList or_group = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the orGroup field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
