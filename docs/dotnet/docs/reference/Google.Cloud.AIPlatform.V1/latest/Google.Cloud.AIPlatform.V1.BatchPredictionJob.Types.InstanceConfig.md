---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig
title: Vertex AI v1 API - Class BatchPredictionJob.Types.InstanceConfig (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:16.147904+00:00
---

# Vertex AI v1 API - Class BatchPredictionJob.Types.InstanceConfig (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class BatchPredictionJob.Types.InstanceConfig (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BatchPredictionJob.Types.InstanceConfig : IMessage<BatchPredictionJob.Types.InstanceConfig>, IEquatable<BatchPredictionJob.Types.InstanceConfig>, IDeepCloneable<BatchPredictionJob.Types.InstanceConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class BatchPredictionJob.Types.InstanceConfig.

Configuration defining how to transform batch prediction input instances to the instances that the Model accepts.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchPredictionJob.Types.InstanceConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### InstanceConfig()
    
    
    public InstanceConfig()

### InstanceConfig(InstanceConfig)
    
    
    public InstanceConfig(BatchPredictionJob.Types.InstanceConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig)`  
  
  
## Properties 

### ExcludedFields
    
    
    public RepeatedField<string> ExcludedFields { get; }

Fields that will be excluded in the prediction instance that is sent to the Model.

Excluded will be attached to the batch prediction output if [key_field][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.key_field] is not specified.

When excluded_fields is populated, [included_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.included_fields] must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IncludedFields
    
    
    public RepeatedField<string> IncludedFields { get; }

Fields that will be included in the prediction instance that is sent to the Model.

If [instance_type][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.instance_type] is `array`, the order of field names in included_fields also determines the order of the values in the array.

When included_fields is populated, [excluded_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.excluded_fields] must be empty.

The input must be JSONL with objects at each line, BigQuery or TfRecord.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceType
    
    
    public string InstanceType { get; set; }

The format of the instance that the Model accepts. Vertex AI will convert compatible [batch prediction input instance formats][google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.instances_format] to the specified format.

Supported values are:

  * `object`: Each input is converted to JSON object format.

    * For `bigquery`, each row is converted to an object.
    * For `jsonl`, each line of the JSONL input must be an object.
    * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.
  * `array`: Each input is converted to JSON array format.

    * For `bigquery`, each row is converted to an array. The order of columns is determined by the BigQuery column order, unless [included_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.included_fields] is populated. [included_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.included_fields] must be populated for specifying field orders.
    * For `jsonl`, if each line of the JSONL input is an object, [included_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.included_fields] must be populated for specifying field orders.
    * Does not apply to `csv`, `file-list`, `tf-record`, or `tf-record-gzip`.



If not specified, Vertex AI converts the batch prediction input as follows:

  * For `bigquery` and `csv`, the behavior is the same as `array`. The order of columns is the same as defined in the file or table, unless [included_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.included_fields] is populated.
  * For `jsonl`, the prediction instance format is determined by each line of the input.
  * For `tf-record`/`tf-record-gzip`, each record will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the record.
  * For `file-list`, each file in the list will be converted to an object in the format of `{"b64": <value>}`, where `<value>` is the Base64-encoded string of the content of the file.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KeyField
    
    
    public string KeyField { get; set; }

The name of the field that is considered as a key.

The values identified by the key field is not included in the transformed instances that is sent to the Model. This is similar to specifying this name of the field in [excluded_fields][google.cloud.aiplatform.v1.BatchPredictionJob.InstanceConfig.excluded_fields]. In addition, the batch prediction output will not include the instances. Instead the output will only include the value of the key field, in a field named `key` in the output:

  * For `jsonl` output format, the output will have a `key` field instead of the `instance` field.
  * For `csv`/`bigquery` output format, the output will have have a `key` column instead of the instance feature columns.



The input must be JSONL with objects at each line, CSV, BigQuery or TfRecord.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
