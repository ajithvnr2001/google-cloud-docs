---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.ScoreSourceOrBuilder
title: Interface QaScorecardResult.ScoreSourceOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:27.701447+00:00
---

# Interface QaScorecardResult.ScoreSourceOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.ScoreSourceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QaScorecardResult.ScoreSourceOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.10  2.2.7 
    
    
    public static interface QaScorecardResult.ScoreSourceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNormalizedScore()
    
    
    public abstract double getNormalizedScore()

The normalized score, which is the score divided by the potential score.

`optional double normalized_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The normalizedScore.  
  
### getPotentialScore()
    
    
    public abstract double getPotentialScore()

The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.

`optional double potential_score = 3;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The potentialScore.  
  
### getQaTagResults(int index)
    
    
    public abstract QaScorecardResult.QaTagResult getQaTagResults(int index)

Collection of tags and their scores.

` repeated .google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult qa_tag_results = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QaScorecardResult.QaTagResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult)` |   
  
### getQaTagResultsCount()
    
    
    public abstract int getQaTagResultsCount()

Collection of tags and their scores.

` repeated .google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult qa_tag_results = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getQaTagResultsList()
    
    
    public abstract List<QaScorecardResult.QaTagResult> getQaTagResultsList()

Collection of tags and their scores.

` repeated .google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult qa_tag_results = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[QaTagResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult)>` |   
  
### getQaTagResultsOrBuilder(int index)
    
    
    public abstract QaScorecardResult.QaTagResultOrBuilder getQaTagResultsOrBuilder(int index)

Collection of tags and their scores.

` repeated .google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult qa_tag_results = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QaScorecardResult.QaTagResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResultOrBuilder)` |   
  
### getQaTagResultsOrBuilderList()
    
    
    public abstract List<? extends QaScorecardResult.QaTagResultOrBuilder> getQaTagResultsOrBuilderList()

Collection of tags and their scores.

` repeated .google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResult qa_tag_results = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.contactcenterinsights.v1.QaScorecardResult.QaTagResultOrBuilder>` |   
  
### getScore()
    
    
    public abstract double getScore()

The overall numerical score of the result.

`optional double score = 2;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The score.  
  
### getSourceType()
    
    
    public abstract QaScorecardResult.ScoreSource.SourceType getSourceType()

What created the score.

` .google.cloud.contactcenterinsights.v1.QaScorecardResult.ScoreSource.SourceType source_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[QaScorecardResult.ScoreSource.SourceType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardResult.ScoreSource.SourceType)` | The sourceType.  
  
### getSourceTypeValue()
    
    
    public abstract int getSourceTypeValue()

What created the score.

` .google.cloud.contactcenterinsights.v1.QaScorecardResult.ScoreSource.SourceType source_type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sourceType.  
  
### hasNormalizedScore()
    
    
    public abstract boolean hasNormalizedScore()

The normalized score, which is the score divided by the potential score.

`optional double normalized_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the normalizedScore field is set.  
  
### hasPotentialScore()
    
    
    public abstract boolean hasPotentialScore()

The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.

`optional double potential_score = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the potentialScore field is set.  
  
### hasScore()
    
    
    public abstract boolean hasScore()

The overall numerical score of the result.

`optional double score = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the score field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
