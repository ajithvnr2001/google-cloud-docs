---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptionsOrBuilder
title: Interface BuildOptionsOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:08.249160+00:00
---

# Interface BuildOptionsOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BuildOptionsOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface BuildOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAutomapSubstitutions()
    
    
    public abstract boolean getAutomapSubstitutions()

Option to include built-in and custom substitutions as env variables for all build steps.

`bool automap_substitutions = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The automapSubstitutions.  
  
### getDefaultLogsBucketBehavior()
    
    
    public abstract BuildOptions.DefaultLogsBucketBehavior getDefaultLogsBucketBehavior()

Optional. Option to specify how default logs buckets are setup.

` .google.devtools.cloudbuild.v1.BuildOptions.DefaultLogsBucketBehavior default_logs_bucket_behavior = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.DefaultLogsBucketBehavior](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.DefaultLogsBucketBehavior)` | The defaultLogsBucketBehavior.  
  
### getDefaultLogsBucketBehaviorValue()
    
    
    public abstract int getDefaultLogsBucketBehaviorValue()

Optional. Option to specify how default logs buckets are setup.

` .google.devtools.cloudbuild.v1.BuildOptions.DefaultLogsBucketBehavior default_logs_bucket_behavior = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for defaultLogsBucketBehavior.  
  
### getDiskSizeGb()
    
    
    public abstract long getDiskSizeGb()

Requested disk size for the VM that runs the build. Note that this is _NOT_ "disk free"; some of the space will be used by the operating system and build utilities. Also note that this is the minimum disk size that will be allocated for the build -- the build may run with a larger disk than requested. At present, the maximum disk size is 4000GB; builds that request more than the maximum are rejected with an error.

`int64 disk_size_gb = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskSizeGb.  
  
### getDynamicSubstitutions()
    
    
    public abstract boolean getDynamicSubstitutions()

Option to specify whether or not to apply bash style string operations to the substitutions.

NOTE: this is always enabled for triggered builds and cannot be overridden in the build configuration file.

`bool dynamic_substitutions = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dynamicSubstitutions.  
  
### getEnableStructuredLogging()
    
    
    public abstract boolean getEnableStructuredLogging()

Optional. Option to specify whether structured logging is enabled.

If true, JSON-formatted logs are parsed as structured logs.

`bool enable_structured_logging = 23 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableStructuredLogging.  
  
### getEnv(int index)
    
    
    public abstract String getEnv(int index)

A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 12;`

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

A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 12;`

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

A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of env.  
  
### getEnvList()
    
    
    public abstract List<String> getEnvList()

A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value.

The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

`repeated string env = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the env.  
  
### getLogStreamingOption()
    
    
    public abstract BuildOptions.LogStreamingOption getLogStreamingOption()

Option to define build log streaming behavior to Cloud Storage.

`.google.devtools.cloudbuild.v1.BuildOptions.LogStreamingOption log_streaming_option = 5; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.LogStreamingOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.LogStreamingOption)` | The logStreamingOption.  
  
### getLogStreamingOptionValue()
    
    
    public abstract int getLogStreamingOptionValue()

Option to define build log streaming behavior to Cloud Storage.

`.google.devtools.cloudbuild.v1.BuildOptions.LogStreamingOption log_streaming_option = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for logStreamingOption.  
  
### getLogging()
    
    
    public abstract BuildOptions.LoggingMode getLogging()

Option to specify the logging mode, which determines if and where build logs are stored.

`.google.devtools.cloudbuild.v1.BuildOptions.LoggingMode logging = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.LoggingMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.LoggingMode)` | The logging.  
  
### getLoggingValue()
    
    
    public abstract int getLoggingValue()

Option to specify the logging mode, which determines if and where build logs are stored.

`.google.devtools.cloudbuild.v1.BuildOptions.LoggingMode logging = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for logging.  
  
### getMachineType()
    
    
    public abstract BuildOptions.MachineType getMachineType()

Compute Engine machine type on which to run the build.

`.google.devtools.cloudbuild.v1.BuildOptions.MachineType machine_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.MachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.MachineType)` | The machineType.  
  
### getMachineTypeValue()
    
    
    public abstract int getMachineTypeValue()

Compute Engine machine type on which to run the build.

`.google.devtools.cloudbuild.v1.BuildOptions.MachineType machine_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for machineType.  
  
### getPool()
    
    
    public abstract BuildOptions.PoolOption getPool()

Optional. Specification for execution on a `WorkerPool`.

See [running builds in a private pool](https://cloud.google.com/build/docs/private-pools/run-builds-in-private-pool) for more information.

` .google.devtools.cloudbuild.v1.BuildOptions.PoolOption pool = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.PoolOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.PoolOption)` | The pool.  
  
### getPoolOrBuilder()
    
    
    public abstract BuildOptions.PoolOptionOrBuilder getPoolOrBuilder()

Optional. Specification for execution on a `WorkerPool`.

See [running builds in a private pool](https://cloud.google.com/build/docs/private-pools/run-builds-in-private-pool) for more information.

` .google.devtools.cloudbuild.v1.BuildOptions.PoolOption pool = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.PoolOptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.PoolOptionOrBuilder)` |   
  
### getRequestedVerifyOption()
    
    
    public abstract BuildOptions.VerifyOption getRequestedVerifyOption()

Requested verifiability options.

`.google.devtools.cloudbuild.v1.BuildOptions.VerifyOption requested_verify_option = 2; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.VerifyOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.VerifyOption)` | The requestedVerifyOption.  
  
### getRequestedVerifyOptionValue()
    
    
    public abstract int getRequestedVerifyOptionValue()

Requested verifiability options.

`.google.devtools.cloudbuild.v1.BuildOptions.VerifyOption requested_verify_option = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for requestedVerifyOption.  
  
### getSecretEnv(int index)
    
    
    public abstract String getSecretEnv(int index)

A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`. These variables will be available to all build steps in this build.

`repeated string secret_env = 13;`

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

A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`. These variables will be available to all build steps in this build.

`repeated string secret_env = 13;`

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

A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`. These variables will be available to all build steps in this build.

`repeated string secret_env = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of secretEnv.  
  
### getSecretEnvList()
    
    
    public abstract List<String> getSecretEnvList()

A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's `Secret`. These variables will be available to all build steps in this build.

`repeated string secret_env = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the secretEnv.  
  
### getSourceProvenanceHash(int index)
    
    
    public abstract Hash.HashType getSourceProvenanceHash(int index)

Requested hash for SourceProvenance.

`repeated .google.devtools.cloudbuild.v1.Hash.HashType source_provenance_hash = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Hash.HashType](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Hash.HashType)` | The sourceProvenanceHash at the given index.  
  
### getSourceProvenanceHashCount()
    
    
    public abstract int getSourceProvenanceHashCount()

Requested hash for SourceProvenance.

`repeated .google.devtools.cloudbuild.v1.Hash.HashType source_provenance_hash = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of sourceProvenanceHash.  
  
### getSourceProvenanceHashList()
    
    
    public abstract List<Hash.HashType> getSourceProvenanceHashList()

Requested hash for SourceProvenance.

`repeated .google.devtools.cloudbuild.v1.Hash.HashType source_provenance_hash = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HashType](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Hash.HashType)>` | A list containing the sourceProvenanceHash.  
  
### getSourceProvenanceHashValue(int index)
    
    
    public abstract int getSourceProvenanceHashValue(int index)

Requested hash for SourceProvenance.

`repeated .google.devtools.cloudbuild.v1.Hash.HashType source_provenance_hash = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of sourceProvenanceHash at the given index.  
  
### getSourceProvenanceHashValueList()
    
    
    public abstract List<Integer> getSourceProvenanceHashValueList()

Requested hash for SourceProvenance.

`repeated .google.devtools.cloudbuild.v1.Hash.HashType source_provenance_hash = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for sourceProvenanceHash.  
  
### getSubstitutionOption()
    
    
    public abstract BuildOptions.SubstitutionOption getSubstitutionOption()

Option to specify behavior when there is an error in the substitution checks.

NOTE: this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file.

`.google.devtools.cloudbuild.v1.BuildOptions.SubstitutionOption substitution_option = 4; `

**Returns**  
---  
**Type** | **Description**  
`[BuildOptions.SubstitutionOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOptions.SubstitutionOption)` | The substitutionOption.  
  
### getSubstitutionOptionValue()
    
    
    public abstract int getSubstitutionOptionValue()

Option to specify behavior when there is an error in the substitution checks.

NOTE: this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file.

`.google.devtools.cloudbuild.v1.BuildOptions.SubstitutionOption substitution_option = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for substitutionOption.  
  
### getVolumes(int index)
    
    
    public abstract Volume getVolumes(int index)

Global list of volumes to mount for ALL build steps

Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.

Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 14;`

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

Global list of volumes to mount for ALL build steps

Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.

Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 14;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVolumesList()
    
    
    public abstract List<Volume> getVolumesList()

Global list of volumes to mount for ALL build steps

Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.

Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 14;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Volume)>` |   
  
### getVolumesOrBuilder(int index)
    
    
    public abstract VolumeOrBuilder getVolumesOrBuilder(int index)

Global list of volumes to mount for ALL build steps

Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.

Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 14;`

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

Global list of volumes to mount for ALL build steps

Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step.

Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration.

`repeated .google.devtools.cloudbuild.v1.Volume volumes = 14;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.VolumeOrBuilder>` |   
  
### getWorkerPool() (deprecated)
    
    
    public abstract String getWorkerPool()

**Deprecated.** _google.devtools.cloudbuild.v1.BuildOptions.worker_pool is deprecated. See google/devtools/cloudbuild/v1/cloudbuild.proto;l=2579_

This field deprecated; please use `pool.name` instead.

`string worker_pool = 7 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workerPool.  
  
### getWorkerPoolBytes() (deprecated)
    
    
    public abstract ByteString getWorkerPoolBytes()

**Deprecated.** _google.devtools.cloudbuild.v1.BuildOptions.worker_pool is deprecated. See google/devtools/cloudbuild/v1/cloudbuild.proto;l=2579_

This field deprecated; please use `pool.name` instead.

`string worker_pool = 7 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for workerPool.  
  
### hasPool()
    
    
    public abstract boolean hasPool()

Optional. Specification for execution on a `WorkerPool`.

See [running builds in a private pool](https://cloud.google.com/build/docs/private-pools/run-builds-in-private-pool) for more information.

` .google.devtools.cloudbuild.v1.BuildOptions.PoolOption pool = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pool field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
