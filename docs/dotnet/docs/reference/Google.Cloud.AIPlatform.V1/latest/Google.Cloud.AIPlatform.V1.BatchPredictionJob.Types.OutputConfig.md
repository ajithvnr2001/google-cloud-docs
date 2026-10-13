---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig
title: Vertex AI v1 API - Class BatchPredictionJob.Types.OutputConfig (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:16.541407+00:00
---

# Vertex AI v1 API - Class BatchPredictionJob.Types.OutputConfig (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class BatchPredictionJob.Types.OutputConfig (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BatchPredictionJob.Types.OutputConfig : IMessage<BatchPredictionJob.Types.OutputConfig>, IEquatable<BatchPredictionJob.Types.OutputConfig>, IDeepCloneable<BatchPredictionJob.Types.OutputConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class BatchPredictionJob.Types.OutputConfig.

Configures the output of [BatchPredictionJob][google.cloud.aiplatform.v1.BatchPredictionJob]. See [Model.supported_output_storage_formats][google.cloud.aiplatform.v1.Model.supported_output_storage_formats] for supported output formats, and how predictions are expressed via any of them.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchPredictionJob.Types.OutputConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### OutputConfig()
    
    
    public OutputConfig()

### OutputConfig(OutputConfig)
    
    
    public OutputConfig(BatchPredictionJob.Types.OutputConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig)`  
  
  
## Properties 

### BigqueryDestination
    
    
    public BigQueryDestination BigqueryDestination { get; set; }

The BigQuery project or dataset location where the output is to be written to. If project is provided, a new dataset is created with name `prediction_<model-display-name>_<job-create-time>` where <model-display-name> is made BigQuery-dataset-name compatible (for example, most special characters become underscores), and timestamp is in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. If the Model has both [instance][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri] and [prediction][google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri] schemata defined then the tables have columns as follows: The `predictions` table contains instances for which the prediction succeeded, it has columns as per a concatenation of the Model's instance and prediction schemata. The `errors` table contains rows for which the prediction has failed, it has instance columns, as per the instance schema, followed by a single "errors" column, which as values has [google.rpc.Status][google.rpc.Status] represented as a STRUCT, and containing only `code` and `message`.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BigQueryDestination)` |   
  
### DestinationCase
    
    
    public BatchPredictionJob.Types.OutputConfig.DestinationOneofCase DestinationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig)[DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig.DestinationOneofCase)` |   
  
### GcsDestination
    
    
    public GcsDestination GcsDestination { get; set; }

The Cloud Storage location of the directory where the output is to be written to. In the given directory a new directory is created. Its name is `prediction-<model-display-name>-<job-create-time>`, where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. Inside of it files `predictions_0001.<extension>`, `predictions_0002.<extension>`, ..., `predictions_N.<extension>` are created where `<extension>` depends on chosen [predictions_format][google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.predictions_format], and N may equal 0001 and depends on the total number of successfully predicted instances. If the Model has both [instance][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri] and [prediction][google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri] schemata defined then each such file contains predictions as per the [predictions_format][google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.predictions_format]. If prediction for any instance failed (partially or completely), then an additional `errors_0001.<extension>`, `errors_0002.<extension>`,..., `errors_N.<extension>` files are created (N depends on total number of failed predictions). These files contain the failed instances, as per their schema, followed by an additional `error` field which as value has [google.rpc.Status][google.rpc.Status] containing only `code` and `message` fields.

**Property Value**  
---  
**Type** | **Description**  
`[GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GcsDestination)` |   
  
### PredictionsFormat
    
    
    public string PredictionsFormat { get; set; }

Required. The format in which Vertex AI gives the predictions, must be one of the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [supported_output_storage_formats][google.cloud.aiplatform.v1.Model.supported_output_storage_formats].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VertexMultimodalDatasetDestination
    
    
    public VertexMultimodalDatasetDestination VertexMultimodalDatasetDestination { get; set; }

The details for a Vertex Multimodal Dataset that will be created for the output.

**Property Value**  
---  
**Type** | **Description**  
`[VertexMultimodalDatasetDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexMultimodalDatasetDestination)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
