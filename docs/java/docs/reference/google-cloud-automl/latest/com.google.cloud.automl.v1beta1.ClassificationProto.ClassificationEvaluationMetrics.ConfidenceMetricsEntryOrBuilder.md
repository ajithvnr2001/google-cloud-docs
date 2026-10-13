---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder
title: Interface ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:42.594596+00:00
---

# Interface ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 
    
    
    public static interface ClassificationProto.ClassificationEvaluationMetrics.ConfidenceMetricsEntryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfidenceThreshold()
    
    
    public abstract float getConfidenceThreshold()

Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value.

`float confidence_threshold = 1;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidenceThreshold.  
  
### getF1Score()
    
    
    public abstract float getF1Score()

Output only. The harmonic mean of recall and precision.

`float f1_score = 4;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The f1Score.  
  
### getF1ScoreAt1()
    
    
    public abstract float getF1ScoreAt1()

Output only. The harmonic mean of recall_at1 and precision_at1.

`float f1_score_at1 = 7;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The f1ScoreAt1.  
  
### getFalseNegativeCount()
    
    
    public abstract long getFalseNegativeCount()

Output only. The number of ground truth labels that are not matched by a model created label.

`int64 false_negative_count = 12;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The falseNegativeCount.  
  
### getFalsePositiveCount()
    
    
    public abstract long getFalsePositiveCount()

Output only. The number of model created labels that do not match a ground truth label.

`int64 false_positive_count = 11;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The falsePositiveCount.  
  
### getFalsePositiveRate()
    
    
    public abstract float getFalsePositiveRate()

Output only. False Positive Rate for the given confidence threshold.

`float false_positive_rate = 8;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The falsePositiveRate.  
  
### getFalsePositiveRateAt1()
    
    
    public abstract float getFalsePositiveRateAt1()

Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

`float false_positive_rate_at1 = 9;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The falsePositiveRateAt1.  
  
### getPositionThreshold()
    
    
    public abstract int getPositionThreshold()

Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold.

`int32 position_threshold = 14;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The positionThreshold.  
  
### getPrecision()
    
    
    public abstract float getPrecision()

Output only. Precision for the given confidence threshold.

`float precision = 3;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The precision.  
  
### getPrecisionAt1()
    
    
    public abstract float getPrecisionAt1()

Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

`float precision_at1 = 6;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The precisionAt1.  
  
### getRecall()
    
    
    public abstract float getRecall()

Output only. Recall (True Positive Rate) for the given confidence threshold.

`float recall = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The recall.  
  
### getRecallAt1()
    
    
    public abstract float getRecallAt1()

Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example.

`float recall_at1 = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The recallAt1.  
  
### getTrueNegativeCount()
    
    
    public abstract long getTrueNegativeCount()

Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label.

`int64 true_negative_count = 13;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The trueNegativeCount.  
  
### getTruePositiveCount()
    
    
    public abstract long getTruePositiveCount()

Output only. The number of model created labels that match a ground truth label.

`int64 true_positive_count = 10;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The truePositiveCount.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
