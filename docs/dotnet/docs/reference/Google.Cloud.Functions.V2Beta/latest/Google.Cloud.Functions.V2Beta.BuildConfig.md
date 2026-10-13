---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig
title: Cloud Functions v2beta API - Class BuildConfig (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:21.568430+00:00
---

# Cloud Functions v2beta API - Class BuildConfig (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class BuildConfig (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.BuildConfig)


    
    
    public sealed class BuildConfig : IMessage<BuildConfig>, IEquatable<BuildConfig>, IDeepCloneable<BuildConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2beta API class BuildConfig.

Describes the Build step of the function that builds a container from the given source.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BuildConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### BuildConfig()
    
    
    public BuildConfig()

### BuildConfig(BuildConfig)
    
    
    public BuildConfig(BuildConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig)`  
  
  
## Properties 

### AutomaticUpdatePolicy
    
    
    public AutomaticUpdatePolicy AutomaticUpdatePolicy { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[AutomaticUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.AutomaticUpdatePolicy)` |   
  
### Build
    
    
    public string Build { get; set; }

Output only. The Cloud Build name of the latest successful deployment of the function.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BuildAsBuildName
    
    
    public BuildName BuildAsBuildName { get; set; }

[BuildName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildName)-typed view over the [Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig#Google_Cloud_Functions_V2Beta_BuildConfig_Build) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BuildName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildName)` |   
  
### DockerRegistry
    
    
    public BuildConfig.Types.DockerRegistry DockerRegistry { get; set; }

Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry.

If unspecified, it defaults to `ARTIFACT_REGISTRY`. If `docker_repository` field is specified, this field should either be left unspecified or set to `ARTIFACT_REGISTRY`.

**Property Value**  
---  
**Type** | **Description**  
`[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig.Types)[DockerRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig.Types.DockerRegistry)` |   
  
### DockerRepository
    
    
    public string DockerRepository { get; set; }

Repository in Artifact Registry to which the function docker image will be pushed after it is built by Cloud Build. If specified by user, it is created and managed by user with a customer managed encryption key. Otherwise, GCF will create and use a repository named 'gcf-artifacts' for every deployed region.

It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`.

Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be 'DOCKER'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DockerRepositoryAsRepositoryName
    
    
    public RepositoryName DockerRepositoryAsRepositoryName { get; set; }

[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.RepositoryName)-typed view over the [DockerRepository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig#Google_Cloud_Functions_V2Beta_BuildConfig_DockerRepository) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.RepositoryName)` |   
  
### EntryPoint
    
    
    public string EntryPoint { get; set; }

The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnvironmentVariables
    
    
    public MapField<string, string> EnvironmentVariables { get; }

User-provided build-time environment variables for the function

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OnDeployUpdatePolicy
    
    
    public OnDeployUpdatePolicy OnDeployUpdatePolicy { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[OnDeployUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.OnDeployUpdatePolicy)` |   
  
### Runtime
    
    
    public string Runtime { get; set; }

The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RuntimeUpdatePolicyCase
    
    
    public BuildConfig.RuntimeUpdatePolicyOneofCase RuntimeUpdatePolicyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BuildConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig)[RuntimeUpdatePolicyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig.RuntimeUpdatePolicyOneofCase)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

Service account to be used for building the container. The format of this field is `projects/{projectId}/serviceAccounts/{serviceAccountEmail}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Source
    
    
    public Source Source { get; set; }

The location of the function source code.

**Property Value**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Source)` |   
  
### SourceProvenance
    
    
    public SourceProvenance SourceProvenance { get; set; }

Output only. A permanent fixed identifier for source.

**Property Value**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.SourceProvenance)` |   
  
### WorkerPool
    
    
    public string WorkerPool { get; set; }

Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool.

If the project id is not the same as the function, then the Cloud Functions Service Agent (service-&lt;project_number&gt;@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkerPoolAsWorkerPoolName
    
    
    public WorkerPoolName WorkerPoolAsWorkerPoolName { get; set; }

[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.WorkerPoolName)-typed view over the [WorkerPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.BuildConfig#Google_Cloud_Functions_V2Beta_BuildConfig_WorkerPool) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkerPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.WorkerPoolName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
