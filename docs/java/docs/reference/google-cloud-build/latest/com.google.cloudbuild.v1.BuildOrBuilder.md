---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOrBuilder
title: Interface BuildOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:08.771317+00:00
---

# Interface BuildOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BuildOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface BuildOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsSubstitutions(String key)
    
    
    public abstract boolean containsSubstitutions(String key)

Substitutions data for `Build` resource.

`map<string, string> substitutions = 29;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsTiming(String key)
    
    
    public abstract boolean containsTiming(String key)

Output only. Stores timing information for phases of the build. Valid keys are:

  * BUILD: time to execute all build steps.
  * PUSH: time to push all artifacts including docker images and non docker artifacts.
  * FETCHSOURCE: time to fetch source.
  * SETUPBUILD: time to set up build.

If the build does not specify source or images, these keys will not be included.




` map<string, .google.devtools.cloudbuild.v1.TimeSpan> timing = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getApproval()
    
    
    public abstract BuildApproval getApproval()

Output only. Describes this build's approval configuration, status, and result.

` .google.devtools.cloudbuild.v1.BuildApproval approval = 44 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BuildApproval](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildApproval)` | The approval.  
  
### getApprovalOrBuilder()
    
    
    public abstract BuildApprovalOrBuilder getApprovalOrBuilder()

Output only. Describes this build's approval configuration, status, and result.

` .google.devtools.cloudbuild.v1.BuildApproval approval = 44 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BuildApprovalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildApprovalOrBuilder)` |   
  
### getArtifacts()
    
    
    public abstract Artifacts getArtifacts()

Artifacts produced by the build that should be uploaded upon successful completion of all build steps.

`.google.devtools.cloudbuild.v1.Artifacts artifacts = 37;`

**Returns**  
---  
**Type** | **Description**  
`[Artifacts](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts)` | The artifacts.  
  
### getArtifactsOrBuilder()
    
    
    public abstract ArtifactsOrBuilder getArtifactsOrBuilder()

Artifacts produced by the build that should be uploaded upon successful completion of all build steps.

`.google.devtools.cloudbuild.v1.Artifacts artifacts = 37;`

**Returns**  
---  
**Type** | **Description**  
`[ArtifactsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ArtifactsOrBuilder)` |   
  
### getAvailableSecrets()
    
    
    public abstract Secrets getAvailableSecrets()

Secrets and secret environment variables.

`.google.devtools.cloudbuild.v1.Secrets available_secrets = 47;`

**Returns**  
---  
**Type** | **Description**  
`[Secrets](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Secrets)` | The availableSecrets.  
  
### getAvailableSecretsOrBuilder()
    
    
    public abstract SecretsOrBuilder getAvailableSecretsOrBuilder()

Secrets and secret environment variables.

`.google.devtools.cloudbuild.v1.Secrets available_secrets = 47;`

**Returns**  
---  
**Type** | **Description**  
`[SecretsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.SecretsOrBuilder)` |   
  
### getBuildTriggerId()
    
    
    public abstract String getBuildTriggerId()

Output only. The ID of the `BuildTrigger` that triggered this build, if it was triggered automatically.

`string build_trigger_id = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The buildTriggerId.  
  
### getBuildTriggerIdBytes()
    
    
    public abstract ByteString getBuildTriggerIdBytes()

Output only. The ID of the `BuildTrigger` that triggered this build, if it was triggered automatically.

`string build_trigger_id = 22 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for buildTriggerId.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time at which the request to create the build was received.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time at which the request to create the build was received.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDependencies(int index)
    
    
    public abstract Dependency getDependencies(int index)

Optional. Dependencies that the Cloud Build worker will fetch before executing user steps.

` repeated .google.devtools.cloudbuild.v1.Dependency dependencies = 56 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dependency](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Dependency)` |   
  
### getDependenciesCount()
    
    
    public abstract int getDependenciesCount()

Optional. Dependencies that the Cloud Build worker will fetch before executing user steps.

` repeated .google.devtools.cloudbuild.v1.Dependency dependencies = 56 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDependenciesList()
    
    
    public abstract List<Dependency> getDependenciesList()

Optional. Dependencies that the Cloud Build worker will fetch before executing user steps.

` repeated .google.devtools.cloudbuild.v1.Dependency dependencies = 56 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Dependency](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Dependency)>` |   
  
### getDependenciesOrBuilder(int index)
    
    
    public abstract DependencyOrBuilder getDependenciesOrBuilder(int index)

Optional. Dependencies that the Cloud Build worker will fetch before executing user steps.

` repeated .google.devtools.cloudbuild.v1.Dependency dependencies = 56 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DependencyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DependencyOrBuilder)` |   
  
### getDependenciesOrBuilderList()
    
    
    public abstract List<? extends DependencyOrBuilder> getDependenciesOrBuilderList()

Optional. Dependencies that the Cloud Build worker will fetch before executing user steps.

` repeated .google.devtools.cloudbuild.v1.Dependency dependencies = 56 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.DependencyOrBuilder>` |   
  
### getFailureInfo()
    
    
    public abstract Build.FailureInfo getFailureInfo()

Output only. Contains information about the build when status=FAILURE.

` .google.devtools.cloudbuild.v1.Build.FailureInfo failure_info = 51 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Build.FailureInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.FailureInfo)` | The failureInfo.  
  
### getFailureInfoOrBuilder()
    
    
    public abstract Build.FailureInfoOrBuilder getFailureInfoOrBuilder()

Output only. Contains information about the build when status=FAILURE.

` .google.devtools.cloudbuild.v1.Build.FailureInfo failure_info = 51 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Build.FailureInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.FailureInfoOrBuilder)` |   
  
### getFinishTime()
    
    
    public abstract Timestamp getFinishTime()

Output only. Time at which execution of the build was finished.

The difference between finish_time and start_time is the duration of the build's execution.

`.google.protobuf.Timestamp finish_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The finishTime.  
  
### getFinishTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getFinishTimeOrBuilder()

Output only. Time at which execution of the build was finished.

The difference between finish_time and start_time is the duration of the build's execution.

`.google.protobuf.Timestamp finish_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getGitConfig()
    
    
    public abstract GitConfig getGitConfig()

Optional. Configuration for git operations.

` .google.devtools.cloudbuild.v1.GitConfig git_config = 48 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GitConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitConfig)` | The gitConfig.  
  
### getGitConfigOrBuilder()
    
    
    public abstract GitConfigOrBuilder getGitConfigOrBuilder()

Optional. Configuration for git operations.

` .google.devtools.cloudbuild.v1.GitConfig git_config = 48 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GitConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitConfigOrBuilder)` |   
  
### getId()
    
    
    public abstract String getId()

Output only. Unique identifier of the build.

`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. Unique identifier of the build.

`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getImages(int index)
    
    
    public abstract String getImages(int index)

A list of images to be pushed upon the successful completion of all build steps.

The images are pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the `Build` resource's results field.

If any of the images fail to be pushed, the build status is marked `FAILURE`.

`repeated string images = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The images at the given index.  
  
### getImagesBytes(int index)
    
    
    public abstract ByteString getImagesBytes(int index)

A list of images to be pushed upon the successful completion of all build steps.

The images are pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the `Build` resource's results field.

If any of the images fail to be pushed, the build status is marked `FAILURE`.

`repeated string images = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the images at the given index.  
  
### getImagesCount()
    
    
    public abstract int getImagesCount()

A list of images to be pushed upon the successful completion of all build steps.

The images are pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the `Build` resource's results field.

If any of the images fail to be pushed, the build status is marked `FAILURE`.

`repeated string images = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of images.  
  
### getImagesList()
    
    
    public abstract List<String> getImagesList()

A list of images to be pushed upon the successful completion of all build steps.

The images are pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the `Build` resource's results field.

If any of the images fail to be pushed, the build status is marked `FAILURE`.

`repeated string images = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the images.  
  
### getLogUrl()
    
    
    public abstract String getLogUrl()

Output only. URL to logs for this build in Google Cloud Console.

`string log_url = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The logUrl.  
  
### getLogUrlBytes()
    
    
    public abstract ByteString getLogUrlBytes()

Output only. URL to logs for this build in Google Cloud Console.

`string log_url = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for logUrl.  
  
### getLogsBucket()
    
    
    public abstract String getLogsBucket()

Cloud Storage bucket where logs should be written (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). Logs file names will be of the format `${logs_bucket}/log-${build_id}.txt`.

`string logs_bucket = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The logsBucket.  
  
### getLogsBucketBytes()
    
    
    public abstract ByteString getLogsBucketBytes()

Cloud Storage bucket where logs should be written (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). Logs file names will be of the format `${logs_bucket}/log-${build_id}.txt`.

`string logs_bucket = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for logsBucket.  
  
### getName()
    
    
    public abstract String getName()

Output only. The 'Build' name with format: `projects/{project}/locations/{location}/builds/{build}`, where {build} is a unique identifier generated by the service.

`string name = 45 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The 'Build' name with format: `projects/{project}/locations/{location}/builds/{build}`, where {build} is a unique identifier generated by the service.

`string name = 45 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOptions()
    
    
    public abstract BuildOptions getOptions()

Special options for this build.

`.google.devtools.cloudbuild.v1.BuildOptions options = 23;`

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions)` | The options.  
  
### getOptionsOrBuilder()
    
    
    public abstract BuildOptionsOrBuilder getOptionsOrBuilder()

Special options for this build.

`.google.devtools.cloudbuild.v1.BuildOptions options = 23;`

**Returns**  
---  
**Type** | **Description**  
`[BuildOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptionsOrBuilder)` |   
  
### getProjectId()
    
    
    public abstract String getProjectId()

Output only. ID of the project.

`string project_id = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The projectId.  
  
### getProjectIdBytes()
    
    
    public abstract ByteString getProjectIdBytes()

Output only. ID of the project.

`string project_id = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for projectId.  
  
### getQueueTtl()
    
    
    public abstract Duration getQueueTtl()

TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be `EXPIRED`.

The TTL starts ticking from create_time.

`.google.protobuf.Duration queue_ttl = 40;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The queueTtl.  
  
### getQueueTtlOrBuilder()
    
    
    public abstract DurationOrBuilder getQueueTtlOrBuilder()

TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be `EXPIRED`.

The TTL starts ticking from create_time.

`.google.protobuf.Duration queue_ttl = 40;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getResults()
    
    
    public abstract Results getResults()

Output only. Results of the build.

` .google.devtools.cloudbuild.v1.Results results = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Results](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Results)` | The results.  
  
### getResultsOrBuilder()
    
    
    public abstract ResultsOrBuilder getResultsOrBuilder()

Output only. Results of the build.

` .google.devtools.cloudbuild.v1.Results results = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResultsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ResultsOrBuilder)` |   
  
### getSecrets(int index)
    
    
    public abstract Secret getSecrets(int index)

Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: <https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets>

`repeated .google.devtools.cloudbuild.v1.Secret secrets = 32;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Secret)` |   
  
### getSecretsCount()
    
    
    public abstract int getSecretsCount()

Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: <https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets>

`repeated .google.devtools.cloudbuild.v1.Secret secrets = 32;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSecretsList()
    
    
    public abstract List<Secret> getSecretsList()

Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: <https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets>

`repeated .google.devtools.cloudbuild.v1.Secret secrets = 32;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Secret)>` |   
  
### getSecretsOrBuilder(int index)
    
    
    public abstract SecretOrBuilder getSecretsOrBuilder(int index)

Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: <https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets>

`repeated .google.devtools.cloudbuild.v1.Secret secrets = 32;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecretOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.SecretOrBuilder)` |   
  
### getSecretsOrBuilderList()
    
    
    public abstract List<? extends SecretOrBuilder> getSecretsOrBuilderList()

Secrets to decrypt using Cloud Key Management Service. Note: Secret Manager is the recommended technique for managing sensitive data with Cloud Build. Use `available_secrets` to configure builds to access secrets from Secret Manager. For instructions, see: <https://cloud.google.com/cloud-build/docs/securing-builds/use-secrets>

`repeated .google.devtools.cloudbuild.v1.Secret secrets = 32;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.SecretOrBuilder>` |   
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

IAM service account whose credentials will be used at build runtime. Must be of the format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. ACCOUNT can be email address or uniqueId of the service account.

`string service_account = 42 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

IAM service account whose credentials will be used at build runtime. Must be of the format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`. ACCOUNT can be email address or uniqueId of the service account.

`string service_account = 42 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getSource()
    
    
    public abstract Source getSource()

Optional. The location of the source files to build.

` .google.devtools.cloudbuild.v1.Source source = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Source)` | The source.  
  
### getSourceOrBuilder()
    
    
    public abstract SourceOrBuilder getSourceOrBuilder()

Optional. The location of the source files to build.

` .google.devtools.cloudbuild.v1.Source source = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.SourceOrBuilder)` |   
  
### getSourceProvenance()
    
    
    public abstract SourceProvenance getSourceProvenance()

Output only. A permanent fixed identifier for source.

` .google.devtools.cloudbuild.v1.SourceProvenance source_provenance = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceProvenance](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.SourceProvenance)` | The sourceProvenance.  
  
### getSourceProvenanceOrBuilder()
    
    
    public abstract SourceProvenanceOrBuilder getSourceProvenanceOrBuilder()

Output only. A permanent fixed identifier for source.

` .google.devtools.cloudbuild.v1.SourceProvenance source_provenance = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceProvenanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.SourceProvenanceOrBuilder)` |   
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. Time at which execution of the build was started.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. Time at which execution of the build was started.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStatus()
    
    
    public abstract Build.Status getStatus()

Output only. Status of the build.

` .google.devtools.cloudbuild.v1.Build.Status status = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Build.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.Status)` | The status.  
  
### getStatusDetail()
    
    
    public abstract String getStatusDetail()

Output only. Customer-readable message about the current status.

`string status_detail = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The statusDetail.  
  
### getStatusDetailBytes()
    
    
    public abstract ByteString getStatusDetailBytes()

Output only. Customer-readable message about the current status.

`string status_detail = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for statusDetail.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Output only. Status of the build.

` .google.devtools.cloudbuild.v1.Build.Status status = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getSteps(int index)
    
    
    public abstract BuildStep getSteps(int index)

Required. The operations to be performed on the workspace.

`repeated .google.devtools.cloudbuild.v1.BuildStep steps = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BuildStep](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildStep)` |   
  
### getStepsCount()
    
    
    public abstract int getStepsCount()

Required. The operations to be performed on the workspace.

`repeated .google.devtools.cloudbuild.v1.BuildStep steps = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStepsList()
    
    
    public abstract List<BuildStep> getStepsList()

Required. The operations to be performed on the workspace.

`repeated .google.devtools.cloudbuild.v1.BuildStep steps = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BuildStep](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildStep)>` |   
  
### getStepsOrBuilder(int index)
    
    
    public abstract BuildStepOrBuilder getStepsOrBuilder(int index)

Required. The operations to be performed on the workspace.

`repeated .google.devtools.cloudbuild.v1.BuildStep steps = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BuildStepOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildStepOrBuilder)` |   
  
### getStepsOrBuilderList()
    
    
    public abstract List<? extends BuildStepOrBuilder> getStepsOrBuilderList()

Required. The operations to be performed on the workspace.

`repeated .google.devtools.cloudbuild.v1.BuildStep steps = 11;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.BuildStepOrBuilder>` |   
  
### getSubstitutions() (deprecated)
    
    
    public abstract Map<String,String> getSubstitutions()

Use [#getSubstitutionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOrBuilder#com_google_cloudbuild_v1_BuildOrBuilder_getSubstitutionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSubstitutionsCount()
    
    
    public abstract int getSubstitutionsCount()

Substitutions data for `Build` resource.

`map<string, string> substitutions = 29;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSubstitutionsMap()
    
    
    public abstract Map<String,String> getSubstitutionsMap()

Substitutions data for `Build` resource.

`map<string, string> substitutions = 29;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSubstitutionsOrDefault(String key, String defaultValue)
    
    
    public abstract String getSubstitutionsOrDefault(String key, String defaultValue)

Substitutions data for `Build` resource.

`map<string, string> substitutions = 29;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSubstitutionsOrThrow(String key)
    
    
    public abstract String getSubstitutionsOrThrow(String key)

Substitutions data for `Build` resource.

`map<string, string> substitutions = 29;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTags(int index)
    
    
    public abstract String getTags(int index)

Tags for annotation of a `Build`. These are not docker tags.

`repeated string tags = 31;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public abstract ByteString getTagsBytes(int index)

Tags for annotation of a `Build`. These are not docker tags.

`repeated string tags = 31;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

Tags for annotation of a `Build`. These are not docker tags.

`repeated string tags = 31;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public abstract List<String> getTagsList()

Tags for annotation of a `Build`. These are not docker tags.

`repeated string tags = 31;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tags.  
  
### getTimeout()
    
    
    public abstract Duration getTimeout()

Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be `TIMEOUT`.

`timeout` starts ticking from `startTime`.

Default time is 60 minutes.

`.google.protobuf.Duration timeout = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The timeout.  
  
### getTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getTimeoutOrBuilder()

Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be `TIMEOUT`.

`timeout` starts ticking from `startTime`.

Default time is 60 minutes.

`.google.protobuf.Duration timeout = 12;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getTiming() (deprecated)
    
    
    public abstract Map<String,TimeSpan> getTiming()

Use [#getTimingMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOrBuilder#com_google_cloudbuild_v1_BuildOrBuilder_getTimingMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)>` |   
  
### getTimingCount()
    
    
    public abstract int getTimingCount()

Output only. Stores timing information for phases of the build. Valid keys are:

  * BUILD: time to execute all build steps.
  * PUSH: time to push all artifacts including docker images and non docker artifacts.
  * FETCHSOURCE: time to fetch source.
  * SETUPBUILD: time to set up build.

If the build does not specify source or images, these keys will not be included.




` map<string, .google.devtools.cloudbuild.v1.TimeSpan> timing = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTimingMap()
    
    
    public abstract Map<String,TimeSpan> getTimingMap()

Output only. Stores timing information for phases of the build. Valid keys are:

  * BUILD: time to execute all build steps.
  * PUSH: time to push all artifacts including docker images and non docker artifacts.
  * FETCHSOURCE: time to fetch source.
  * SETUPBUILD: time to set up build.

If the build does not specify source or images, these keys will not be included.




` map<string, .google.devtools.cloudbuild.v1.TimeSpan> timing = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)>` |   
  
### getTimingOrDefault(String key, TimeSpan defaultValue)
    
    
    public abstract TimeSpan getTimingOrDefault(String key, TimeSpan defaultValue)

Output only. Stores timing information for phases of the build. Valid keys are:

  * BUILD: time to execute all build steps.
  * PUSH: time to push all artifacts including docker images and non docker artifacts.
  * FETCHSOURCE: time to fetch source.
  * SETUPBUILD: time to set up build.

If the build does not specify source or images, these keys will not be included.




` map<string, .google.devtools.cloudbuild.v1.TimeSpan> timing = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)` |   
  
### getTimingOrThrow(String key)
    
    
    public abstract TimeSpan getTimingOrThrow(String key)

Output only. Stores timing information for phases of the build. Valid keys are:

  * BUILD: time to execute all build steps.
  * PUSH: time to push all artifacts including docker images and non docker artifacts.
  * FETCHSOURCE: time to fetch source.
  * SETUPBUILD: time to set up build.

If the build does not specify source or images, these keys will not be included.




` map<string, .google.devtools.cloudbuild.v1.TimeSpan> timing = 33 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)` |   
  
### getWarnings(int index)
    
    
    public abstract Build.Warning getWarnings(int index)

Output only. Non-fatal problems encountered during the execution of the build.

` repeated .google.devtools.cloudbuild.v1.Build.Warning warnings = 49 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Build.Warning](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.Warning)` |   
  
### getWarningsCount()
    
    
    public abstract int getWarningsCount()

Output only. Non-fatal problems encountered during the execution of the build.

` repeated .google.devtools.cloudbuild.v1.Build.Warning warnings = 49 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWarningsList()
    
    
    public abstract List<Build.Warning> getWarningsList()

Output only. Non-fatal problems encountered during the execution of the build.

` repeated .google.devtools.cloudbuild.v1.Build.Warning warnings = 49 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Warning](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.Warning)>` |   
  
### getWarningsOrBuilder(int index)
    
    
    public abstract Build.WarningOrBuilder getWarningsOrBuilder(int index)

Output only. Non-fatal problems encountered during the execution of the build.

` repeated .google.devtools.cloudbuild.v1.Build.Warning warnings = 49 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Build.WarningOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.WarningOrBuilder)` |   
  
### getWarningsOrBuilderList()
    
    
    public abstract List<? extends Build.WarningOrBuilder> getWarningsOrBuilderList()

Output only. Non-fatal problems encountered during the execution of the build.

` repeated .google.devtools.cloudbuild.v1.Build.Warning warnings = 49 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.Build.WarningOrBuilder>` |   
  
### hasApproval()
    
    
    public abstract boolean hasApproval()

Output only. Describes this build's approval configuration, status, and result.

` .google.devtools.cloudbuild.v1.BuildApproval approval = 44 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the approval field is set.  
  
### hasArtifacts()
    
    
    public abstract boolean hasArtifacts()

Artifacts produced by the build that should be uploaded upon successful completion of all build steps.

`.google.devtools.cloudbuild.v1.Artifacts artifacts = 37;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the artifacts field is set.  
  
### hasAvailableSecrets()
    
    
    public abstract boolean hasAvailableSecrets()

Secrets and secret environment variables.

`.google.devtools.cloudbuild.v1.Secrets available_secrets = 47;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availableSecrets field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time at which the request to create the build was received.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasFailureInfo()
    
    
    public abstract boolean hasFailureInfo()

Output only. Contains information about the build when status=FAILURE.

` .google.devtools.cloudbuild.v1.Build.FailureInfo failure_info = 51 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the failureInfo field is set.  
  
### hasFinishTime()
    
    
    public abstract boolean hasFinishTime()

Output only. Time at which execution of the build was finished.

The difference between finish_time and start_time is the duration of the build's execution.

`.google.protobuf.Timestamp finish_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the finishTime field is set.  
  
### hasGitConfig()
    
    
    public abstract boolean hasGitConfig()

Optional. Configuration for git operations.

` .google.devtools.cloudbuild.v1.GitConfig git_config = 48 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gitConfig field is set.  
  
### hasOptions()
    
    
    public abstract boolean hasOptions()

Special options for this build.

`.google.devtools.cloudbuild.v1.BuildOptions options = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the options field is set.  
  
### hasQueueTtl()
    
    
    public abstract boolean hasQueueTtl()

TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be `EXPIRED`.

The TTL starts ticking from create_time.

`.google.protobuf.Duration queue_ttl = 40;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queueTtl field is set.  
  
### hasResults()
    
    
    public abstract boolean hasResults()

Output only. Results of the build.

` .google.devtools.cloudbuild.v1.Results results = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the results field is set.  
  
### hasSource()
    
    
    public abstract boolean hasSource()

Optional. The location of the source files to build.

` .google.devtools.cloudbuild.v1.Source source = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the source field is set.  
  
### hasSourceProvenance()
    
    
    public abstract boolean hasSourceProvenance()

Output only. A permanent fixed identifier for source.

` .google.devtools.cloudbuild.v1.SourceProvenance source_provenance = 21 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceProvenance field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. Time at which execution of the build was started.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
### hasTimeout()
    
    
    public abstract boolean hasTimeout()

Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be `TIMEOUT`.

`timeout` starts ticking from `startTime`.

Default time is 60 minutes.

`.google.protobuf.Duration timeout = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeout field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
