---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob
title: Vertex AI v1 API - Class BatchPredictionJob (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:15.843972+00:00
---

# Vertex AI v1 API - Class BatchPredictionJob (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class BatchPredictionJob (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BatchPredictionJob : IMessage<BatchPredictionJob>, IEquatable<BatchPredictionJob>, IDeepCloneable<BatchPredictionJob>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1 API class BatchPredictionJob.

A job that uses a [Model][google.cloud.aiplatform.v1.BatchPredictionJob.model] to produce predictions on multiple [input instances][google.cloud.aiplatform.v1.BatchPredictionJob.input_config]. If predictions for significant portion of the instances fail, the job may finish without attempting predictions for all remaining instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchPredictionJob

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### BatchPredictionJob()
    
    
    public BatchPredictionJob()

### BatchPredictionJob(BatchPredictionJob)
    
    
    public BatchPredictionJob(BatchPredictionJob other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)`  
  
  
## Properties 

### BatchPredictionJobName
    
    
    public BatchPredictionJobName BatchPredictionJobName { get; set; }

[BatchPredictionJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJobName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob#Google_Cloud_AIPlatform_V1_BatchPredictionJob_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJobName)` |   
  
### CompletionStats
    
    
    public CompletionStats CompletionStats { get; set; }

Output only. Statistics on completed and failed prediction instances.

**Property Value**  
---  
**Type** | **Description**  
`[CompletionStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CompletionStats)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time when the BatchPredictionJob was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DedicatedResources
    
    
    public BatchDedicatedResources DedicatedResources { get; set; }

The config of resources used by the Model during the batch prediction. If the Model [supports][google.cloud.aiplatform.v1.Model.supported_deployment_resources_types] DEDICATED_RESOURCES this config may be provided (and the job will use these resources), if the Model doesn't support AUTOMATIC_RESOURCES, this config must be provided.

**Property Value**  
---  
**Type** | **Description**  
`[BatchDedicatedResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchDedicatedResources)` |   
  
### DisableContainerLogging
    
    
    public bool DisableContainerLogging { get; set; }

For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send `stderr` and `stdout` streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing).

User can disable container logging by setting this flag to true.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The user-defined name of this BatchPredictionJob.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EncryptionSpec
    
    
    public EncryptionSpec EncryptionSpec { get; set; }

Customer-managed encryption key options for a BatchPredictionJob. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EncryptionSpec)` |   
  
### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. Time when the BatchPredictionJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Error
    
    
    public Status Error { get; set; }

Output only. Only populated when the job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### ExplanationSpec
    
    
    public ExplanationSpec ExplanationSpec { get; set; }

Explanation configuration for this BatchPredictionJob. Can be specified only if [generate_explanation][google.cloud.aiplatform.v1.BatchPredictionJob.generate_explanation] is set to `true`.

This value overrides the value of [Model.explanation_spec][google.cloud.aiplatform.v1.Model.explanation_spec]. All fields of [explanation_spec][google.cloud.aiplatform.v1.BatchPredictionJob.explanation_spec] are optional in the request. If a field of the [explanation_spec][google.cloud.aiplatform.v1.BatchPredictionJob.explanation_spec] object is not populated, the corresponding field of the [Model.explanation_spec][google.cloud.aiplatform.v1.Model.explanation_spec] object is inherited.

**Property Value**  
---  
**Type** | **Description**  
`[ExplanationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ExplanationSpec)` |   
  
### GenerateExplanation
    
    
    public bool GenerateExplanation { get; set; }

Generate explanation with the batch prediction results.

When set to `true`, the batch prediction output changes based on the `predictions_format` field of the [BatchPredictionJob.output_config][google.cloud.aiplatform.v1.BatchPredictionJob.output_config] object:

  * `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [Explanation][google.cloud.aiplatform.v1.Explanation] object.
  * `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [Explanation][google.cloud.aiplatform.v1.Explanation] object.
  * `csv`: Generating explanations for CSV format is not supported.



If this field is set to true, either the [Model.explanation_spec][google.cloud.aiplatform.v1.Model.explanation_spec] or [explanation_spec][google.cloud.aiplatform.v1.BatchPredictionJob.explanation_spec] must be populated.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InputConfig
    
    
    public BatchPredictionJob.Types.InputConfig InputConfig { get; set; }

Required. Input configuration of the instances on which predictions are performed. The schema of any single instance may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri].

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InputConfig)` |   
  
### InstanceConfig
    
    
    public BatchPredictionJob.Types.InstanceConfig InstanceConfig { get; set; }

Configuration for how to convert batch prediction input instances to the prediction instances that are sent to the Model.

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[InstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.InstanceConfig)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

The labels with user-defined metadata to organize BatchPredictionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ManualBatchTuningParameters
    
    
    public ManualBatchTuningParameters ManualBatchTuningParameters { get; set; }

Immutable. Parameters configuring the batch behavior. Currently only applicable when [dedicated_resources][google.cloud.aiplatform.v1.BatchPredictionJob.dedicated_resources] are used (in other cases Vertex AI does the tuning itself).

**Property Value**  
---  
**Type** | **Description**  
`[ManualBatchTuningParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ManualBatchTuningParameters)` |   
  
### Model
    
    
    public string Model { get; set; }

The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set.

The model resource name may contain version id or version alias to specify the version. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` if no version is specified, the default version will be deployed.

The model resource could also be a publisher model. Example: `publishers/{publisher}/models/{model}` or `projects/{project}/locations/{location}/publishers/{publisher}/models/{model}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ModelAsModelName
    
    
    public ModelName ModelAsModelName { get; set; }

[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelName)-typed view over the [Model](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob#Google_Cloud_AIPlatform_V1_BatchPredictionJob_Model) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelName)` |   
  
### ModelParameters
    
    
    public Value ModelParameters { get; set; }

The parameters that govern the predictions. The schema of the parameters may be specified via the [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [parameters_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.parameters_schema_uri].

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### ModelVersionId
    
    
    public string ModelVersionId { get; set; }

Output only. The version ID of the Model that produces the predictions via this job.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Resource name of the BatchPredictionJob.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OutputConfig
    
    
    public BatchPredictionJob.Types.OutputConfig OutputConfig { get; set; }

Required. The Configuration specifying where output predictions should be written. The schema of any single prediction may be specified as a concatenation of [Model's][google.cloud.aiplatform.v1.BatchPredictionJob.model] [PredictSchemata's][google.cloud.aiplatform.v1.Model.predict_schemata] [instance_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.instance_schema_uri] and [prediction_schema_uri][google.cloud.aiplatform.v1.PredictSchemata.prediction_schema_uri].

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputConfig)` |   
  
### OutputInfo
    
    
    public BatchPredictionJob.Types.OutputInfo OutputInfo { get; set; }

Output only. Information further describing the output of this job.

**Property Value**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types)[OutputInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.BatchPredictionJob.Types.OutputInfo)` |   
  
### PartialFailures
    
    
    public RepeatedField<Status> PartialFailures { get; }

Output only. Partial failures encountered. For example, single files that can't be read. This field never exceeds 20 entries. Status details fields contain standard Google Cloud error details.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### ResourcesConsumed
    
    
    public ResourcesConsumed ResourcesConsumed { get; set; }

Output only. Information about resources that had been consumed by this job. Provided in real time at best effort basis, as well as a final value once the job completes.

Note: This field currently may be not populated for batch predictions that use AutoML Models.

**Property Value**  
---  
**Type** | **Description**  
`[ResourcesConsumed](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ResourcesConsumed)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

The service account that the DeployedModel's container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources.

Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. Time when the BatchPredictionJob for the first time entered the `JOB_STATE_RUNNING` state.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### State
    
    
    public JobState State { get; set; }

Output only. The detailed state of the job.

**Property Value**  
---  
**Type** | **Description**  
`[JobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.JobState)` |   
  
### UnmanagedContainerModel
    
    
    public UnmanagedContainerModel UnmanagedContainerModel { get; set; }

Contains model information necessary to perform batch prediction without requiring uploading to model registry. Exactly one of model and unmanaged_container_model must be set.

**Property Value**  
---  
**Type** | **Description**  
`[UnmanagedContainerModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UnmanagedContainerModel)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time when the BatchPredictionJob was most recently updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
