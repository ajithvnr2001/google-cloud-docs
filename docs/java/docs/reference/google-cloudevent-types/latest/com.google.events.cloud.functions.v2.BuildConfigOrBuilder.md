---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.BuildConfigOrBuilder
title: Interface BuildConfigOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:54.618936+00:00
---

# Interface BuildConfigOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.BuildConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BuildConfigOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.BuildConfigOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.functions.v2.BuildConfigOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.functions.v2.BuildConfigOrBuilder)


    
    
    public interface BuildConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsEnvironmentVariables(String key)
    
    
    public abstract boolean containsEnvironmentVariables(String key)

User-provided build-time environment variables for the function

`map<string, string> environment_variables = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBuild()
    
    
    public abstract String getBuild()

Output only. The Cloud Build name of the latest successful deployment of the function.

`string build = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The build.  
  
### getBuildBytes()
    
    
    public abstract ByteString getBuildBytes()

Output only. The Cloud Build name of the latest successful deployment of the function.

`string build = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for build.  
  
### getBuildpackStack()
    
    
    public abstract String getBuildpackStack()

Specifies one of the Google provided buildpack stacks.

`string buildpack_stack = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The buildpackStack.  
  
### getBuildpackStackBytes()
    
    
    public abstract ByteString getBuildpackStackBytes()

Specifies one of the Google provided buildpack stacks.

`string buildpack_stack = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for buildpackStack.  
  
### getDockerRegistry()
    
    
    public abstract BuildConfig.DockerRegistry getDockerRegistry()

Optional. Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry. If `docker_repository` field is specified, this field will be automatically set as `ARTIFACT_REGISTRY`. If unspecified, it currently defaults to `CONTAINER_REGISTRY`. This field may be overridden by the backend for eligible deployments.

`.google.events.cloud.functions.v2.BuildConfig.DockerRegistry docker_registry = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BuildConfig.DockerRegistry](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.BuildConfig.DockerRegistry)` | The dockerRegistry.  
  
### getDockerRegistryValue()
    
    
    public abstract int getDockerRegistryValue()

Optional. Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry. If `docker_repository` field is specified, this field will be automatically set as `ARTIFACT_REGISTRY`. If unspecified, it currently defaults to `CONTAINER_REGISTRY`. This field may be overridden by the backend for eligible deployments.

`.google.events.cloud.functions.v2.BuildConfig.DockerRegistry docker_registry = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for dockerRegistry.  
  
### getDockerRepository()
    
    
    public abstract String getDockerRepository()

User managed repository created in Artifact Registry optionally with a customer managed encryption key. This is the repository to which the function docker image will be pushed after it is built by Cloud Build. If unspecified, GCF will create and use a repository named 'gcf-artifacts' for every deployed region. It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`. Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be 'DOCKER'.

`string docker_repository = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dockerRepository.  
  
### getDockerRepositoryBytes()
    
    
    public abstract ByteString getDockerRepositoryBytes()

User managed repository created in Artifact Registry optionally with a customer managed encryption key. This is the repository to which the function docker image will be pushed after it is built by Cloud Build. If unspecified, GCF will create and use a repository named 'gcf-artifacts' for every deployed region. It must match the pattern `projects/{project}/locations/{location}/repositories/{repository}`. Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be 'DOCKER'.

`string docker_repository = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dockerRepository.  
  
### getEntryPoint()
    
    
    public abstract String getEntryPoint()

The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.

`string entry_point = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The entryPoint.  
  
### getEntryPointBytes()
    
    
    public abstract ByteString getEntryPointBytes()

The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in `source_location`.

`string entry_point = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for entryPoint.  
  
### getEnvironmentVariables()
    
    
    public abstract Map<String,String> getEnvironmentVariables()

Use [#getEnvironmentVariablesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.BuildConfigOrBuilder#com_google_events_cloud_functions_v2_BuildConfigOrBuilder_getEnvironmentVariablesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getEnvironmentVariablesCount()
    
    
    public abstract int getEnvironmentVariablesCount()

User-provided build-time environment variables for the function

`map<string, string> environment_variables = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEnvironmentVariablesMap()
    
    
    public abstract Map<String,String> getEnvironmentVariablesMap()

User-provided build-time environment variables for the function

`map<string, string> environment_variables = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getEnvironmentVariablesOrDefault(String key, String defaultValue)
    
    
    public abstract String getEnvironmentVariablesOrDefault(String key, String defaultValue)

User-provided build-time environment variables for the function

`map<string, string> environment_variables = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getEnvironmentVariablesOrThrow(String key)
    
    
    public abstract String getEnvironmentVariablesOrThrow(String key)

User-provided build-time environment variables for the function

`map<string, string> environment_variables = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRuntime()
    
    
    public abstract String getRuntime()

The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).

`string runtime = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The runtime.  
  
### getRuntimeBytes()
    
    
    public abstract ByteString getRuntimeBytes()

The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [`gcloud` command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime).

`string runtime = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for runtime.  
  
### getSource()
    
    
    public abstract Source getSource()

The location of the function source code.

`.google.events.cloud.functions.v2.Source source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.Source)` | The source.  
  
### getSourceOrBuilder()
    
    
    public abstract SourceOrBuilder getSourceOrBuilder()

The location of the function source code.

`.google.events.cloud.functions.v2.Source source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.SourceOrBuilder)` |   
  
### getSourceProvenance()
    
    
    public abstract SourceProvenance getSourceProvenance()

Output only. A permanent fixed identifier for source.

`.google.events.cloud.functions.v2.SourceProvenance source_provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.SourceProvenance)` | The sourceProvenance.  
  
### getSourceProvenanceOrBuilder()
    
    
    public abstract SourceProvenanceOrBuilder getSourceProvenanceOrBuilder()

Output only. A permanent fixed identifier for source.

`.google.events.cloud.functions.v2.SourceProvenance source_provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[SourceProvenanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.functions.v2.SourceProvenanceOrBuilder)` |   
  
### getWorkerPool()
    
    
    public abstract String getWorkerPool()

Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project.

`string worker_pool = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workerPool.  
  
### getWorkerPoolBytes()
    
    
    public abstract ByteString getWorkerPoolBytes()

Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is `projects/{project}/locations/{region}/workerPools/{workerPool}` where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project.

`string worker_pool = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for workerPool.  
  
### hasSource()
    
    
    public abstract boolean hasSource()

The location of the function source code.

`.google.events.cloud.functions.v2.Source source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the source field is set.  
  
### hasSourceProvenance()
    
    
    public abstract boolean hasSourceProvenance()

Output only. A permanent fixed identifier for source.

`.google.events.cloud.functions.v2.SourceProvenance source_provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceProvenance field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
