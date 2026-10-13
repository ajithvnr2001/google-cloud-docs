---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetricsOrBuilder
title: Interface Evaluation.MultiConfidenceMetricsOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:49.241924+00:00
---

# Interface Evaluation.MultiConfidenceMetricsOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetricsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Evaluation.MultiConfidenceMetricsOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static interface Evaluation.MultiConfidenceMetricsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuprc()
    
    
    public abstract float getAuprc()

The calculated area under the precision recall curve (AUPRC), computed by integrating over all confidence thresholds.

`float auprc = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The auprc.  
  
### getAuprcExact()
    
    
    public abstract float getAuprcExact()

The AUPRC for metrics with fuzzy matching disabled, i.e., exact matching only.

`float auprc_exact = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The auprcExact.  
  
### getConfidenceLevelMetrics(int index)
    
    
    public abstract Evaluation.ConfidenceLevelMetrics getConfidenceLevelMetrics(int index)

Metrics across confidence levels with fuzzy matching enabled.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation.ConfidenceLevelMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics)` |   
  
### getConfidenceLevelMetricsCount()
    
    
    public abstract int getConfidenceLevelMetricsCount()

Metrics across confidence levels with fuzzy matching enabled.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConfidenceLevelMetricsExact(int index)
    
    
    public abstract Evaluation.ConfidenceLevelMetrics getConfidenceLevelMetricsExact(int index)

Metrics across confidence levels with only exact matching.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics_exact = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation.ConfidenceLevelMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics)` |   
  
### getConfidenceLevelMetricsExactCount()
    
    
    public abstract int getConfidenceLevelMetricsExactCount()

Metrics across confidence levels with only exact matching.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics_exact = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConfidenceLevelMetricsExactList()
    
    
    public abstract List<Evaluation.ConfidenceLevelMetrics> getConfidenceLevelMetricsExactList()

Metrics across confidence levels with only exact matching.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics_exact = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConfidenceLevelMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics)>` |   
  
### getConfidenceLevelMetricsExactOrBuilder(int index)
    
    
    public abstract Evaluation.ConfidenceLevelMetricsOrBuilder getConfidenceLevelMetricsExactOrBuilder(int index)

Metrics across confidence levels with only exact matching.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics_exact = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation.ConfidenceLevelMetricsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetricsOrBuilder)` |   
  
### getConfidenceLevelMetricsExactOrBuilderList()
    
    
    public abstract List<? extends Evaluation.ConfidenceLevelMetricsOrBuilder> getConfidenceLevelMetricsExactOrBuilderList()

Metrics across confidence levels with only exact matching.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics_exact = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetricsOrBuilder>` |   
  
### getConfidenceLevelMetricsList()
    
    
    public abstract List<Evaluation.ConfidenceLevelMetrics> getConfidenceLevelMetricsList()

Metrics across confidence levels with fuzzy matching enabled.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ConfidenceLevelMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics)>` |   
  
### getConfidenceLevelMetricsOrBuilder(int index)
    
    
    public abstract Evaluation.ConfidenceLevelMetricsOrBuilder getConfidenceLevelMetricsOrBuilder(int index)

Metrics across confidence levels with fuzzy matching enabled.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation.ConfidenceLevelMetricsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetricsOrBuilder)` |   
  
### getConfidenceLevelMetricsOrBuilderList()
    
    
    public abstract List<? extends Evaluation.ConfidenceLevelMetricsOrBuilder> getConfidenceLevelMetricsOrBuilderList()

Metrics across confidence levels with fuzzy matching enabled.

` repeated .google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetrics confidence_level_metrics = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.documentai.v1beta3.Evaluation.ConfidenceLevelMetricsOrBuilder>` |   
  
### getEstimatedCalibrationError()
    
    
    public abstract float getEstimatedCalibrationError()

The Estimated Calibration Error (ECE) of the confidence of the predicted entities.

`float estimated_calibration_error = 3;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedCalibrationError.  
  
### getEstimatedCalibrationErrorExact()
    
    
    public abstract float getEstimatedCalibrationErrorExact()

The ECE for the predicted entities with fuzzy matching disabled, i.e., exact matching only.

`float estimated_calibration_error_exact = 6;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedCalibrationErrorExact.  
  
### getMetricsType()
    
    
    public abstract Evaluation.MultiConfidenceMetrics.MetricsType getMetricsType()

The metrics type for the label.

` .google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics.MetricsType metrics_type = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Evaluation.MultiConfidenceMetrics.MetricsType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics.MetricsType)` | The metricsType.  
  
### getMetricsTypeValue()
    
    
    public abstract int getMetricsTypeValue()

The metrics type for the label.

` .google.cloud.documentai.v1beta3.Evaluation.MultiConfidenceMetrics.MetricsType metrics_type = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for metricsType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
