---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetricOrBuilder
title: Interface MetricOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:16.342175+00:00
---

# Interface MetricOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MetricOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MetricOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface MetricOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAggregationMetrics(int index)
    
    
    public abstract Metric.AggregationMetric getAggregationMetrics(int index)

Optional. The aggregation metrics to use.

` repeated .google.cloud.aiplatform.v1.Metric.AggregationMetric aggregation_metrics = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Metric.AggregationMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Metric.AggregationMetric)` | The aggregationMetrics at the given index.  
  
### getAggregationMetricsCount()
    
    
    public abstract int getAggregationMetricsCount()

Optional. The aggregation metrics to use.

` repeated .google.cloud.aiplatform.v1.Metric.AggregationMetric aggregation_metrics = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of aggregationMetrics.  
  
### getAggregationMetricsList()
    
    
    public abstract List<Metric.AggregationMetric> getAggregationMetricsList()

Optional. The aggregation metrics to use.

` repeated .google.cloud.aiplatform.v1.Metric.AggregationMetric aggregation_metrics = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AggregationMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Metric.AggregationMetric)>` | A list containing the aggregationMetrics.  
  
### getAggregationMetricsValue(int index)
    
    
    public abstract int getAggregationMetricsValue(int index)

Optional. The aggregation metrics to use.

` repeated .google.cloud.aiplatform.v1.Metric.AggregationMetric aggregation_metrics = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of aggregationMetrics at the given index.  
  
### getAggregationMetricsValueList()
    
    
    public abstract List<Integer> getAggregationMetricsValueList()

Optional. The aggregation metrics to use.

` repeated .google.cloud.aiplatform.v1.Metric.AggregationMetric aggregation_metrics = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for aggregationMetrics.  
  
### getBleuSpec()
    
    
    public abstract BleuSpec getBleuSpec()

Spec for bleu metric.

`.google.cloud.aiplatform.v1.BleuSpec bleu_spec = 5;`

**Returns**  
---  
**Type** | **Description**  
`[BleuSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BleuSpec)` | The bleuSpec.  
  
### getBleuSpecOrBuilder()
    
    
    public abstract BleuSpecOrBuilder getBleuSpecOrBuilder()

Spec for bleu metric.

`.google.cloud.aiplatform.v1.BleuSpec bleu_spec = 5;`

**Returns**  
---  
**Type** | **Description**  
`[BleuSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BleuSpecOrBuilder)` |   
  
### getComputationBasedMetricSpec()
    
    
    public abstract ComputationBasedMetricSpec getComputationBasedMetricSpec()

Spec for a computation based metric.

`.google.cloud.aiplatform.v1.ComputationBasedMetricSpec computation_based_metric_spec = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ComputationBasedMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ComputationBasedMetricSpec)` | The computationBasedMetricSpec.  
  
### getComputationBasedMetricSpecOrBuilder()
    
    
    public abstract ComputationBasedMetricSpecOrBuilder getComputationBasedMetricSpecOrBuilder()

Spec for a computation based metric.

`.google.cloud.aiplatform.v1.ComputationBasedMetricSpec computation_based_metric_spec = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ComputationBasedMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ComputationBasedMetricSpecOrBuilder)` |   
  
### getExactMatchSpec()
    
    
    public abstract ExactMatchSpec getExactMatchSpec()

Spec for exact match metric.

`.google.cloud.aiplatform.v1.ExactMatchSpec exact_match_spec = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ExactMatchSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExactMatchSpec)` | The exactMatchSpec.  
  
### getExactMatchSpecOrBuilder()
    
    
    public abstract ExactMatchSpecOrBuilder getExactMatchSpecOrBuilder()

Spec for exact match metric.

`.google.cloud.aiplatform.v1.ExactMatchSpec exact_match_spec = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ExactMatchSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExactMatchSpecOrBuilder)` |   
  
### getLlmBasedMetricSpec()
    
    
    public abstract LLMBasedMetricSpec getLlmBasedMetricSpec()

Spec for an LLM based metric.

`.google.cloud.aiplatform.v1.LLMBasedMetricSpec llm_based_metric_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[LLMBasedMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LLMBasedMetricSpec)` | The llmBasedMetricSpec.  
  
### getLlmBasedMetricSpecOrBuilder()
    
    
    public abstract LLMBasedMetricSpecOrBuilder getLlmBasedMetricSpecOrBuilder()

Spec for an LLM based metric.

`.google.cloud.aiplatform.v1.LLMBasedMetricSpec llm_based_metric_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[LLMBasedMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LLMBasedMetricSpecOrBuilder)` |   
  
### getMetricSpecCase()
    
    
    public abstract Metric.MetricSpecCase getMetricSpecCase()

**Returns**  
---  
**Type** | **Description**  
`[Metric.MetricSpecCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Metric.MetricSpecCase)` |   
  
### getPairwiseMetricSpec()
    
    
    public abstract PairwiseMetricSpec getPairwiseMetricSpec()

Spec for pairwise metric.

`.google.cloud.aiplatform.v1.PairwiseMetricSpec pairwise_metric_spec = 3;`

**Returns**  
---  
**Type** | **Description**  
`[PairwiseMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PairwiseMetricSpec)` | The pairwiseMetricSpec.  
  
### getPairwiseMetricSpecOrBuilder()
    
    
    public abstract PairwiseMetricSpecOrBuilder getPairwiseMetricSpecOrBuilder()

Spec for pairwise metric.

`.google.cloud.aiplatform.v1.PairwiseMetricSpec pairwise_metric_spec = 3;`

**Returns**  
---  
**Type** | **Description**  
`[PairwiseMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PairwiseMetricSpecOrBuilder)` |   
  
### getPointwiseMetricSpec()
    
    
    public abstract PointwiseMetricSpec getPointwiseMetricSpec()

Spec for pointwise metric.

`.google.cloud.aiplatform.v1.PointwiseMetricSpec pointwise_metric_spec = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PointwiseMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PointwiseMetricSpec)` | The pointwiseMetricSpec.  
  
### getPointwiseMetricSpecOrBuilder()
    
    
    public abstract PointwiseMetricSpecOrBuilder getPointwiseMetricSpecOrBuilder()

Spec for pointwise metric.

`.google.cloud.aiplatform.v1.PointwiseMetricSpec pointwise_metric_spec = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PointwiseMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PointwiseMetricSpecOrBuilder)` |   
  
### getPredefinedMetricSpec()
    
    
    public abstract PredefinedMetricSpec getPredefinedMetricSpec()

The spec for a pre-defined metric.

`.google.cloud.aiplatform.v1.PredefinedMetricSpec predefined_metric_spec = 8;`

**Returns**  
---  
**Type** | **Description**  
`[PredefinedMetricSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedMetricSpec)` | The predefinedMetricSpec.  
  
### getPredefinedMetricSpecOrBuilder()
    
    
    public abstract PredefinedMetricSpecOrBuilder getPredefinedMetricSpecOrBuilder()

The spec for a pre-defined metric.

`.google.cloud.aiplatform.v1.PredefinedMetricSpec predefined_metric_spec = 8;`

**Returns**  
---  
**Type** | **Description**  
`[PredefinedMetricSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedMetricSpecOrBuilder)` |   
  
### getRougeSpec()
    
    
    public abstract RougeSpec getRougeSpec()

Spec for rouge metric.

`.google.cloud.aiplatform.v1.RougeSpec rouge_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RougeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RougeSpec)` | The rougeSpec.  
  
### getRougeSpecOrBuilder()
    
    
    public abstract RougeSpecOrBuilder getRougeSpecOrBuilder()

Spec for rouge metric.

`.google.cloud.aiplatform.v1.RougeSpec rouge_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RougeSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RougeSpecOrBuilder)` |   
  
### hasBleuSpec()
    
    
    public abstract boolean hasBleuSpec()

Spec for bleu metric.

`.google.cloud.aiplatform.v1.BleuSpec bleu_spec = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bleuSpec field is set.  
  
### hasComputationBasedMetricSpec()
    
    
    public abstract boolean hasComputationBasedMetricSpec()

Spec for a computation based metric.

`.google.cloud.aiplatform.v1.ComputationBasedMetricSpec computation_based_metric_spec = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computationBasedMetricSpec field is set.  
  
### hasExactMatchSpec()
    
    
    public abstract boolean hasExactMatchSpec()

Spec for exact match metric.

`.google.cloud.aiplatform.v1.ExactMatchSpec exact_match_spec = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the exactMatchSpec field is set.  
  
### hasLlmBasedMetricSpec()
    
    
    public abstract boolean hasLlmBasedMetricSpec()

Spec for an LLM based metric.

`.google.cloud.aiplatform.v1.LLMBasedMetricSpec llm_based_metric_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the llmBasedMetricSpec field is set.  
  
### hasPairwiseMetricSpec()
    
    
    public abstract boolean hasPairwiseMetricSpec()

Spec for pairwise metric.

`.google.cloud.aiplatform.v1.PairwiseMetricSpec pairwise_metric_spec = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pairwiseMetricSpec field is set.  
  
### hasPointwiseMetricSpec()
    
    
    public abstract boolean hasPointwiseMetricSpec()

Spec for pointwise metric.

`.google.cloud.aiplatform.v1.PointwiseMetricSpec pointwise_metric_spec = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pointwiseMetricSpec field is set.  
  
### hasPredefinedMetricSpec()
    
    
    public abstract boolean hasPredefinedMetricSpec()

The spec for a pre-defined metric.

`.google.cloud.aiplatform.v1.PredefinedMetricSpec predefined_metric_spec = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predefinedMetricSpec field is set.  
  
### hasRougeSpec()
    
    
    public abstract boolean hasRougeSpec()

Spec for rouge metric.

`.google.cloud.aiplatform.v1.RougeSpec rouge_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rougeSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
