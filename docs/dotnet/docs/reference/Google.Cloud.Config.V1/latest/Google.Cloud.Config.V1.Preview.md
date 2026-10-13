---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview
title: Infrastructure Manager v1 API - Class Preview (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:10.170227+00:00
---

# Infrastructure Manager v1 API - Class Preview (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class Preview (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Preview : IMessage<Preview>, IEquatable<Preview>, IDeepCloneable<Preview>, IBufferMessage, IMessage

Reference documentation and code samples for the Infrastructure Manager v1 API class Preview.

A preview represents a set of actions Infra Manager would perform to move the resources towards the desired state as specified in the configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Preview

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### Preview()
    
    
    public Preview()

### Preview(Preview)
    
    
    public Preview(Preview other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Optional. Arbitrary key-value metadata storage e.g. to help client tools identify preview during automation. See <https://google.aip.dev/148#annotations> for details on format and size limitations.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ArtifactsGcsBucket
    
    
    public string ArtifactsGcsBucket { get; set; }

User-defined location of Cloud Build logs, artifacts, and in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default bucket will be bootstrapped if the field is not set or empty Default Bucket Format: `gs://<project number>-<region>-blueprint-config` Constraints:

  * The bucket needs to be in the same project as the deployment
  * The path cannot be within the path of `gcs_source` If omitted and deployment resource ref provided has artifacts_gcs_bucket defined, that artifact bucket is used.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BlueprintCase
    
    
    public Preview.BlueprintOneofCase BlueprintCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)[BlueprintOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.BlueprintOneofCase)` |   
  
### Build
    
    
    public string Build { get; set; }

Output only. Cloud Build instance UUID associated with this preview.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time the preview was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Deployment
    
    
    public string Deployment { get; set; }

Optional. Deployment reference. If specified, the preview will be performed using the provided deployment's current state and use any relevant fields from the deployment unless explicitly specified in the preview create request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DeploymentAsDeploymentName
    
    
    public DeploymentName DeploymentAsDeploymentName { get; set; }

[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentName)-typed view over the [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview#Google_Cloud_Config_V1_Preview_Deployment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.DeploymentName)` |   
  
### ErrorCode
    
    
    public Preview.Types.ErrorCode ErrorCode { get; set; }

Output only. Code describing any errors that may have occurred.

**Property Value**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types)[ErrorCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types.ErrorCode)` |   
  
### ErrorLogs
    
    
    public string ErrorLogs { get; set; }

Output only. Link to tf-error.ndjson file, which contains the full list of the errors encountered during a Terraform preview. Format: `gs://{bucket}/{object}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ErrorStatus
    
    
    public Status ErrorStatus { get; set; }

Output only. Additional information regarding the current state.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### HasArtifactsGcsBucket
    
    
    public bool HasArtifactsGcsBucket { get; }

Gets whether the "artifacts_gcs_bucket" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTfVersionConstraint
    
    
    public bool HasTfVersionConstraint { get; }

Gets whether the "tf_version_constraint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasWorkerPool
    
    
    public bool HasWorkerPool { get; }

Gets whether the "worker_pool" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. User-defined labels for the preview.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Logs
    
    
    public string Logs { get; set; }

Output only. Location of preview logs in `gs://{bucket}/{object}` format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Resource name of the preview. Resource name can be user provided or server generated ID if unspecified. Format: `projects/{project}/locations/{location}/previews/{preview}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PreviewArtifacts
    
    
    public PreviewArtifacts PreviewArtifacts { get; set; }

Output only. Artifacts from preview.

**Property Value**  
---  
**Type** | **Description**  
`[PreviewArtifacts](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.PreviewArtifacts)` |   
  
### PreviewMode
    
    
    public Preview.Types.PreviewMode PreviewMode { get; set; }

Optional. Current mode of preview.

**Property Value**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types)[PreviewMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types.PreviewMode)` |   
  
### PreviewName
    
    
    public PreviewName PreviewName { get; set; }

[PreviewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.PreviewName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview#Google_Cloud_Config_V1_Preview_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PreviewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.PreviewName)` |   
  
### ProviderConfig
    
    
    public ProviderConfig ProviderConfig { get; set; }

Optional. This field specifies the provider configurations.

**Property Value**  
---  
**Type** | **Description**  
`[ProviderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ProviderConfig)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

Required. User-specified Service Account (SA) credentials to be used when previewing resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountAsServiceAccountName
    
    
    public ServiceAccountName ServiceAccountAsServiceAccountName { get; set; }

[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ServiceAccountName)-typed view over the [ServiceAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview#Google_Cloud_Config_V1_Preview_ServiceAccount) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ServiceAccountName)` |   
  
### State
    
    
    public Preview.Types.State State { get; set; }

Output only. Current state of the preview.

**Property Value**  
---  
**Type** | **Description**  
`[Preview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview.Types.State)` |   
  
### TerraformBlueprint
    
    
    public TerraformBlueprint TerraformBlueprint { get; set; }

The terraform blueprint to preview.

**Property Value**  
---  
**Type** | **Description**  
`[TerraformBlueprint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformBlueprint)` |   
  
### TfErrors
    
    
    public RepeatedField<TerraformError> TfErrors { get; }

Output only. Summary of errors encountered during Terraform preview. It has a size limit of 10, i.e. only top 10 errors will be summarized here.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TerraformError](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.TerraformError)` |   
  
### TfVersion
    
    
    public string TfVersion { get; set; }

Output only. The current Terraform version set on the preview. It is in the format of "Major.Minor.Patch", for example, "1.3.10".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TfVersionConstraint
    
    
    public string TfVersionConstraint { get; set; }

The user-specified Terraform version constraint. Example: "=1.3.10".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkerPool
    
    
    public string WorkerPool { get; set; }

The user-specified Worker Pool resource in which the Cloud Build job will execute. Format projects/{project}/locations/{location}/workerPools/{workerPoolId} If this field is unspecified, the default Cloud Build worker pool will be used. If omitted and deployment resource ref provided has worker_pool defined, that worker pool is used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkerPoolAsWorkerPoolName
    
    
    public WorkerPoolName WorkerPoolAsWorkerPoolName { get; set; }

[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.WorkerPoolName)-typed view over the [WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.Preview#Google_Cloud_Config_V1_Preview_WorkerPool) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.WorkerPoolName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
