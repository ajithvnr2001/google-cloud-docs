---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.UserSequenceStepOrBuilder
title: Interface UserSequenceStepOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:08.469274+00:00
---

# Interface UserSequenceStepOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.UserSequenceStepOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UserSequenceStepOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface UserSequenceStepOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIsDirectlyFollowedBy()
    
    
    public abstract boolean getIsDirectlyFollowedBy()

If true, the event satisfying this step must be the very next event after the event satifying the last step. If false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. `isDirectlyFollowedBy` must be false for the first step.

`bool is_directly_followed_by = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isDirectlyFollowedBy.  
  
### getSegmentFilterExpression()
    
    
    public abstract SegmentFilterExpression getSegmentFilterExpression()

A user matches this sequence step if their events match this expression. Expressions express criteria on dimension, metrics, and/or parameters.

`.google.analytics.data.v1alpha.SegmentFilterExpression segment_filter_expression = 3; `

**Returns**  
---  
**Type** | **Description**  
`[SegmentFilterExpression](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.SegmentFilterExpression)` | The segmentFilterExpression.  
  
### getSegmentFilterExpressionOrBuilder()
    
    
    public abstract SegmentFilterExpressionOrBuilder getSegmentFilterExpressionOrBuilder()

A user matches this sequence step if their events match this expression. Expressions express criteria on dimension, metrics, and/or parameters.

`.google.analytics.data.v1alpha.SegmentFilterExpression segment_filter_expression = 3; `

**Returns**  
---  
**Type** | **Description**  
`[SegmentFilterExpressionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.SegmentFilterExpressionOrBuilder)` |   
  
### getStepScoping()
    
    
    public abstract UserCriteriaScoping getStepScoping()

This sequence step must be satisfied in the scoping for the user to match the sequence. For example if `sequenceScoping = WITHIN_SAME_SESSION`, this sequence steps must complete within one session for the user to match the sequence. `stepScoping = ACROSS_ALL_SESSIONS` is only allowed if the `sequenceScoping = ACROSS_ALL_SESSIONS`.

Optional. If unspecified, `stepScoping` uses the same `UserCriteriaScoping` as the `sequenceScoping`.

`.google.analytics.data.v1alpha.UserCriteriaScoping step_scoping = 2;`

**Returns**  
---  
**Type** | **Description**  
`[UserCriteriaScoping](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1alpha.UserCriteriaScoping)` | The stepScoping.  
  
### getStepScopingValue()
    
    
    public abstract int getStepScopingValue()

This sequence step must be satisfied in the scoping for the user to match the sequence. For example if `sequenceScoping = WITHIN_SAME_SESSION`, this sequence steps must complete within one session for the user to match the sequence. `stepScoping = ACROSS_ALL_SESSIONS` is only allowed if the `sequenceScoping = ACROSS_ALL_SESSIONS`.

Optional. If unspecified, `stepScoping` uses the same `UserCriteriaScoping` as the `sequenceScoping`.

`.google.analytics.data.v1alpha.UserCriteriaScoping step_scoping = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for stepScoping.  
  
### hasSegmentFilterExpression()
    
    
    public abstract boolean hasSegmentFilterExpression()

A user matches this sequence step if their events match this expression. Expressions express criteria on dimension, metrics, and/or parameters.

`.google.analytics.data.v1alpha.SegmentFilterExpression segment_filter_expression = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the segmentFilterExpression field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
