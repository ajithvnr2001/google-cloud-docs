---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildStepOrBuilder
title: Interface BuildStepOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:09.048574+00:00
---

# Interface BuildStepOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildStepOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BuildStepOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface BuildStepOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowExitCodes(int index)
    
    
    public abstract int getAllowExitCodes(int index)

Allow this build step to fail without failing the entire build if and only if the exit code is one of the specified codes. If allow_failure is also specified, this field will take precedence.

`repeated int32 allow_exit_codes = 18;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowExitCodes at the given index.  
  
### getAllowExitCodesCount()
    
    
    public abstract int getAllowExitCodesCount()

Allow this build step to fail without failing the entire build if and only if the exit code is one of the specified codes. If allow_failure is also specified, this field will take precedence.

`repeated int32 allow_exit_codes = 18;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowExitCodes.  
  
### getAllowExitCodesList()
    
    
    public abstract List<Integer> getAllowExitCodesList()

Allow this build step to fail without failing the entire build if and only if the exit code is one of the specified codes. If allow_failure is also specified, this field will take precedence.

`repeated int32 allow_exit_codes = 18;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the allowExitCodes.  
  
### getAllowFailure()
    
    
    public abstract boolean getAllowFailure()

Allow this build step to fail without failing the entire build.

If false, the entire build will fail if this step fails. Otherwise, the build will succeed, but this step will still have a failure status. Error information will be reported in the failure_detail field.

`bool allow_failure = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowFailure.  
  
### getArgs(int index)
    
    
    public abstract String getArgs(int index)

A list of arguments that will be presented to the step when it is started.

If the image used to run the step's container has an entrypoint, the `args` are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The args at the given index.  
  
### getArgsBytes(int index)
    
    
    public abstract ByteString getArgsBytes(int index)

A list of arguments that will be presented to the step when it is started.

If the image used to run the step's container has an entrypoint, the `args` are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.

`repeated string args = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the args at the given index.  
  
### getArgsCount()
    
    
    public abstract int getArgsCount()

A list of arguments that will be presented to the step when it is started.

If the image used to run the step's container has an entrypoint, the `args` are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of args.  
  
### getArgsList()
    
    
    public abstract List<String> getArgsList()

A list of arguments that will be presented to the step when it is started.

If the image used to run the step's container has an entrypoint, the `args` are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments.

`repeated string args = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the args.  
  
### getAutomapSubstitutions()
    
    
    public abstract boolean getAutomapSubstitutions()

Option to include built-in and custom substitutions as env variables for this build step. This option will override the global option in BuildOption.

`optional bool automap_substitutions = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The automapSubstitutions.  
  
### getDir()
    
    
    public abstract String getDir()

Working directory to use when running this step's container.

If this value is a relative path, it is relative to the build's working directory. If this value is absolute, it may be outside the build's working directory, in which case the contents of the path may not be persisted across build step executions, unless a `volume` for that path is specified.

If the build specifies a `RepoSource` with `dir` and a step with a `dir`, which specifies an absolute path, the `RepoSource` `dir` is ignored for the step's execution.

`string dir = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dir.  
  
### getDirBytes()
    
    
    public abstract ByteString getDirBytes()

Working directory to use when running this step's container.

If this value is a relative path, it is relative to the build's working directory. If this value is absolute, it may be outside the build's working directory, in which case the contents of the path may not be persisted across build step executions, unless a `volume` for that path is specified.

If the build specifies a `RepoSource` with `dir` and a step with a `dir`, which specifies an absolute path, the `RepoSource` `dir` is ignored for the step's execution.

`string dir = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dir.  
  
### getEntrypoint()
    
    
    public abstract String getEntrypoint()

Entrypoint to be used instead of the build step image's default entrypoint. If unset, the image's default entrypoint is used.

`string entrypoint = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The entrypoint.  
  
### getEntrypointBytes()
    
    
    public abstract ByteString getEntrypointBytes()

Entrypoint to be used instead of the build step image's default entrypoint. If unset, the image's default entrypoint is used.

`string entrypoint = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for entrypoint.  
  
### getEnv(int index)
    
    
    public abstract String getEnv(int index)

A list of environment variable definitions to be used when running a step.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The env at the given index.  
  
### getEnvBytes(int index)
    
    
    public abstract ByteString getEnvBytes(int index)

A list of environment variable definitions to be used when running a step.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the env at the given index.  
  
### getEnvCount()
    
    
    public abstract int getEnvCount()

A list of environment variable definitions to be used when running a step.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of env.  
  
### getEnvList()
    
    
    public abstract List<String> getEnvList()

A list of environment variable definitions to be used when running a step.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the env.  
  
### getExitCode()
    
    
    public abstract int getExitCode()

Output only. Return code from running the step.

`int32 exit_code = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The exitCode.  
  
### getId()
    
    
    public abstract String getId()

Unique identifier for this build step, used in `wait_for` to reference this build step as a dependency.

`string id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Unique identifier for this build step, used in `wait_for` to reference this build step as a dependency.

`string id = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getName()
    
    
    public abstract String getName()

Required. The name of the container image that will run this particular build step.

If the image is available in the host's Docker daemon's cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account's credentials if necessary.

The Docker daemon's cache will already have the latest versions of all of the officially supported build steps (<https://github.com/GoogleCloudPlatform/cloud-builders>). The Docker daemon will also have cached many of the layers for some popular images, like "ubuntu", "debian", but they will be refreshed at the time you attempt to use them.

If you built an image in a previous build step, it will be stored in the host's Docker daemon's cache and is available to use as the name for a later build step.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The name of the container image that will run this particular build step.

If the image is available in the host's Docker daemon's cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account's credentials if necessary.

The Docker daemon's cache will already have the latest versions of all of the officially supported build steps (<https://github.com/GoogleCloudPlatform/cloud-builders>). The Docker daemon will also have cached many of the layers for some popular images, like "ubuntu", "debian", but they will be refreshed at the time you attempt to use them.

If you built an image in a previous build step, it will be stored in the host's Docker daemon's cache and is available to use as the name for a later build step.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPullTiming()
    
    
    public abstract TimeSpan getPullTiming()

Output only. Stores timing information for pulling this build step's builder image only.

` .google.devtools.cloudbuild.v1.TimeSpan pull_timing = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)` | The pullTiming.  
  
### getPullTimingOrBuilder()
    
    
    public abstract TimeSpanOrBuilder getPullTimingOrBuilder()

Output only. Stores timing information for pulling this build step's builder image only.

` .google.devtools.cloudbuild.v1.TimeSpan pull_timing = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSpanOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpanOrBuilder)` |   
  
### getScript()
    
    
    public abstract String getScript()

A shell script to be executed in the step.

When script is provided, the user cannot specify the entrypoint or args.

`string script = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The script.  
  
### getScriptBytes()
    
    
    public abstract ByteString getScriptBytes()

A shell script to be executed in the step.

When script is provided, the user cannot specify the entrypoint or args.

`string script = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for script.  
  
### getSecretEnv(int index)
    
    
    public abstract String getSecretEnv(int index)

A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`.

`repeated string secret_env = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The secretEnv at the given index.  
  
### getSecretEnvBytes(int index)
    
    
    public abstract ByteString getSecretEnvBytes(int index)

A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`.

`repeated string secret_env = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the secretEnv at the given index.  
  
### getSecretEnvCount()
    
    
    public abstract int getSecretEnvCount()

A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`.

`repeated string secret_env = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of secretEnv.  
  
### getSecretEnvList()
    
    
    public abstract List<String> getSecretEnvList()

A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`.

`repeated string secret_env = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the secretEnv.  
  
### getStatus()
    
    
    public abstract Build.Status getStatus()

Output only. Status of the build step. At this time, build step status is only updated on build completion; step status is not updated in real-time as the build progresses.

` .google.devtools.cloudbuild.v1.Build.Status status = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Build.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build.Status)` | The status.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Output only. Status of the build step. At this time, build step status is only updated on build completion; step status is not updated in real-time as the build progresses.

` .google.devtools.cloudbuild.v1.Build.Status status = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getTimeout()
    
    
    public abstract Duration getTimeout()

Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out.

`.google.protobuf.Duration timeout = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The timeout.  
  
### getTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getTimeoutOrBuilder()

Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out.

`.google.protobuf.Duration timeout = 11;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getTiming()
    
    
    public abstract TimeSpan getTiming()

Output only. Stores timing information for executing this build step.

` .google.devtools.cloudbuild.v1.TimeSpan timing = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSpan](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpan)` | The timing.  
  
### getTimingOrBuilder()
    
    
    public abstract TimeSpanOrBuilder getTimingOrBuilder()

Output only. Stores timing information for executing this build step.

` .google.devtools.cloudbuild.v1.TimeSpan timing = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimeSpanOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.TimeSpanOrBuilder)` |   
  
### getVolumes(int index)
    
    
    public abstract Volume getVolumes(int index)

List of volumes to mount into the build step.

Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.

Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Volume)` |   
  
### getVolumesCount()
    
    
    public abstract int getVolumesCount()

List of volumes to mount into the build step.

Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.

Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVolumesList()
    
    
    public abstract List<Volume> getVolumesList()

List of volumes to mount into the build step.

Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.

Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Volume)>` |   
  
### getVolumesOrBuilder(int index)
    
    
    public abstract VolumeOrBuilder getVolumesOrBuilder(int index)

List of volumes to mount into the build step.

Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.

Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VolumeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.VolumeOrBuilder)` |   
  
### getVolumesOrBuilderList()
    
    
    public abstract List<? extends VolumeOrBuilder> getVolumesOrBuilderList()

List of volumes to mount into the build step.

Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded.

Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.VolumeOrBuilder>` |   
  
### getWaitFor(int index)
    
    
    public abstract String getWaitFor(int index)

The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.

`repeated string wait_for = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The waitFor at the given index.  
  
### getWaitForBytes(int index)
    
    
    public abstract ByteString getWaitForBytes(int index)

The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.

`repeated string wait_for = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the waitFor at the given index.  
  
### getWaitForCount()
    
    
    public abstract int getWaitForCount()

The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.

`repeated string wait_for = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of waitFor.  
  
### getWaitForList()
    
    
    public abstract List<String> getWaitForList()

The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in `wait_for` have completed successfully. If `wait_for` is empty, this build step will start when all previous build steps in the `Build.Steps` list have completed successfully.

`repeated string wait_for = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the waitFor.  
  
### hasAutomapSubstitutions()
    
    
    public abstract boolean hasAutomapSubstitutions()

Option to include built-in and custom substitutions as env variables for this build step. This option will override the global option in BuildOption.

`optional bool automap_substitutions = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automapSubstitutions field is set.  
  
### hasPullTiming()
    
    
    public abstract boolean hasPullTiming()

Output only. Stores timing information for pulling this build step's builder image only.

` .google.devtools.cloudbuild.v1.TimeSpan pull_timing = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pullTiming field is set.  
  
### hasTimeout()
    
    
    public abstract boolean hasTimeout()

Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out.

`.google.protobuf.Duration timeout = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeout field is set.  
  
### hasTiming()
    
    
    public abstract boolean hasTiming()

Output only. Stores timing information for executing this build step.

` .google.devtools.cloudbuild.v1.TimeSpan timing = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timing field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
