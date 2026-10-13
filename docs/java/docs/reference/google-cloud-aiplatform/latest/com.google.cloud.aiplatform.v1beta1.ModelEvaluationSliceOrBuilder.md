---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelEvaluationSliceOrBuilder
title: Interface ModelEvaluationSliceOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:11.957006+00:00
---

# Interface ModelEvaluationSliceOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelEvaluationSliceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelEvaluationSliceOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ModelEvaluationSliceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Timestamp when this ModelEvaluationSlice was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when this ModelEvaluationSlice was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMetrics()
    
    
    public abstract Value getMetrics()

Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri

`.google.protobuf.Value metrics = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` | The metrics.  
  
### getMetricsOrBuilder()
    
    
    public abstract ValueOrBuilder getMetricsOrBuilder()

Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri

`.google.protobuf.Value metrics = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getMetricsSchemaUri()
    
    
    public abstract String getMetricsSchemaUri()

Output only. Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject).

`string metrics_schema_uri = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metricsSchemaUri.  
  
### getMetricsSchemaUriBytes()
    
    
    public abstract ByteString getMetricsSchemaUriBytes()

Output only. Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject).

`string metrics_schema_uri = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metricsSchemaUri.  
  
### getModelExplanation()
    
    
    public abstract ModelExplanation getModelExplanation()

Output only. Aggregated explanation metrics for the Model's prediction output over the data this ModelEvaluation uses. This field is populated only if the Model is evaluated with explanations, and only for tabular Models.

` .google.cloud.aiplatform.v1beta1.ModelExplanation model_explanation = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelExplanation)` | The modelExplanation.  
  
### getModelExplanationOrBuilder()
    
    
    public abstract ModelExplanationOrBuilder getModelExplanationOrBuilder()

Output only. Aggregated explanation metrics for the Model's prediction output over the data this ModelEvaluation uses. This field is populated only if the Model is evaluated with explanations, and only for tabular Models.

` .google.cloud.aiplatform.v1beta1.ModelExplanation model_explanation = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelExplanationOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The resource name of the ModelEvaluationSlice.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The resource name of the ModelEvaluationSlice.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSlice()
    
    
    public abstract ModelEvaluationSlice.Slice getSlice()

Output only. The slice of the test data that is used to evaluate the Model.

` .google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice slice = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice)` | The slice.  
  
### getSliceOrBuilder()
    
    
    public abstract ModelEvaluationSlice.SliceOrBuilder getSliceOrBuilder()

Output only. The slice of the test data that is used to evaluate the Model.

` .google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice slice = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.SliceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.SliceOrBuilder)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Timestamp when this ModelEvaluationSlice was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasMetrics()
    
    
    public abstract boolean hasMetrics()

Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri

`.google.protobuf.Value metrics = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metrics field is set.  
  
### hasModelExplanation()
    
    
    public abstract boolean hasModelExplanation()

Output only. Aggregated explanation metrics for the Model's prediction output over the data this ModelEvaluation uses. This field is populated only if the Model is evaluated with explanations, and only for tabular Models.

` .google.cloud.aiplatform.v1beta1.ModelExplanation model_explanation = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelExplanation field is set.  
  
### hasSlice()
    
    
    public abstract boolean hasSlice()

Output only. The slice of the test data that is used to evaluate the Model.

` .google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice slice = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the slice field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
