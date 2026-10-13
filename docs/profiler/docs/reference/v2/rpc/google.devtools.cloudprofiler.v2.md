---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2
title: Package google.devtools.cloudprofiler.v2 \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:43.615094+00:00
---

# Package google.devtools.cloudprofiler.v2  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  Package google.devtools.cloudprofiler.v2 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ExportService](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ExportService)` (interface)
  * `[ProfilerService](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ProfilerService)` (interface)
  * `[CreateOfflineProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.CreateOfflineProfileRequest)` (message)
  * `[CreateProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.CreateProfileRequest)` (message)
  * `[Deployment](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Deployment)` (message)
  * `[ListProfilesRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ListProfilesRequest)` (message)
  * `[ListProfilesResponse](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ListProfilesResponse)` (message)
  * `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)` (message)
  * `[ProfileType](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ProfileType)` (enum)
  * `[UpdateProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.UpdateProfileRequest)` (message)



## ExportService

Service allows existing Cloud Profiler customers to export their profile data out of Google Cloud.

ListProfiles  
---  
` rpc ListProfiles(`[ListProfilesRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ListProfilesRequest)`) returns (`[ListProfilesResponse](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ListProfilesResponse)`) ` Lists profiles which have been collected so far and for which the caller has permission to view.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## ProfilerService

Manage the collection of continuous profiling data provided by profiling agents running in the cloud or by an offline provider of profiling data.

**The APIs listed in this service are intended for use within our profiler agents only.**

CreateOfflineProfile  
---  
` rpc CreateOfflineProfile(`[CreateOfflineProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.CreateOfflineProfileRequest)`) returns (`[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)`) ` CreateOfflineProfile creates a new profile resource in the offline mode. The client provides the profile to create along with the profile bytes, the server records it._Direct use of this API is discouraged, please use a[supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateProfile  
---  
` rpc CreateProfile(`[CreateProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.CreateProfileRequest)`) returns (`[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)`) ` CreateProfile creates a new profile resource in the online mode._Direct use of this API is discouraged, please use a[supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._The server ensures that the new profiles are created at a constant rate per deployment, so the creation request may hang for some time until the next profile session is available.The request may fail with ABORTED error if the creation is not available within ~1m, the response will indicate the duration of the backoff the client should take before attempting creating a profile again. The backoff duration is returned in google.rpc.RetryInfo extension on the response status. To a gRPC client, the extension will be return as a binary-serialized proto in the trailing metadata item named "google.rpc.retryinfo-bin".

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateProfile  
---  
` rpc UpdateProfile(`[UpdateProfileRequest](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.UpdateProfileRequest)`) returns (`[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)`) ` UpdateProfile updates the profile bytes and labels on the profile resource created in the online mode. Updating the bytes for profiles created in the offline mode is currently not supported: the profile content must be provided at the time of the profile creation._Direct use of this API is discouraged, please use a[supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## CreateOfflineProfileRequest

CreateOfflineProfileRequest describes a profile resource offline creation request.

Fields  
---  
`parent` |  `string` Parent project to create the profile in. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudprofiler.profiles.create`

  
`profile` |  `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)` Contents of the profile to create.  
  
## CreateProfileRequest

CreateProfileRequest describes a profile resource online creation request. The deployment field must be populated. The profile_type specifies the list of profile types supported by the agent. The creation call will hang until a profile of one of these types needs to be collected.

Fields  
---  
`parent` |  `string` Parent project to create the profile in. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudprofiler.profiles.create`

  
`deployment` |  `[Deployment](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Deployment)` Deployment details. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `deployment`:

  * `cloudprofiler.profiles.create`

  
`profile_type[]` |  `[ProfileType](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ProfileType)` One or more profile types that the agent is capable of providing.  
  
## Deployment

Deployment contains the deployment identification information.

Fields  
---  
`project_id` |  `string` Project ID is the ID of a cloud project. Validation regex: `^[a-z][-a-z0-9:.]{4,61}[a-z0-9]$`.  
`target` |  `string` Target is the service name used to group related deployments: * Service name for App Engine Flex / Standard. * Cluster and container name for GKE. * User-specified string for direct Compute Engine profiling (e.g. Java). * Job name for Dataflow. Validation regex: `^[a-z0-9]([-a-z0-9_.]{0,253}[a-z0-9])?$`.  
`labels` |  `map<string, string>` Labels identify the deployment within the user universe and same target. Validation regex for label names: `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`. Value for an individual label must be <= 512 bytes, the total size of all label names and values must be <= 1024 bytes.Label named "language" can be used to record the programming language of the profiled deployment. The standard choices for the value include "java", "go", "python", "ruby", "nodejs", "php", "dotnet".For deployments running on Google Cloud Platform, "zone" or "region" label should be present describing the deployment location. An example of a zone is "us-central1-a", an example of a region is "us-central1" or "us-central".  
  
## ListProfilesRequest

ListProfilesRequest contains request parameters for listing profiles for deployments in projects which the user has permissions to view.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of profiles. Format: projects/{user_project_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudprofiler.profiles.list`

  
`page_size` |  `int32` Optional. The maximum number of items to return. Default page_size is 1000. Max limit is 1000.  
`page_token` |  `string` Optional. The token to continue pagination and get profiles from a particular page. When paginating, all other parameters provided to `ListProfiles` must match the call that provided the page token.  
  
## ListProfilesResponse

ListProfileResponse contains the list of collected profiles for deployments in projects which the user has permissions to view.

Fields  
---  
`profiles[]` |  `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)` List of profiles fetched.  
`next_page_token` |  `string` Token to receive the next page of results. This field maybe empty if there are no more profiles to fetch.  
`skipped_profiles` |  `int32` Number of profiles that were skipped in the current page since they were not able to be fetched successfully. This should typically be zero. A non-zero value may indicate a transient failure, in which case if the number is too high for your use case, the call may be retried.  
  
## Profile

Profile resource.

Fields  
---  
`name` |  `string` Output only. Opaque, server-assigned, unique ID for this profile.  
`profile_type` |  `[ProfileType](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.ProfileType)` Type of profile. For offline mode, this must be specified when creating the profile. For online mode it is assigned and returned by the server.  
`deployment` |  `[Deployment](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Deployment)` Deployment this profile corresponds to.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Duration of the profiling session. Input (for the offline mode) or output (for the online mode). The field represents requested profiling duration. It may slightly differ from the effective profiling duration, which is recorded in the profile data, in case the profiling can't be stopped immediately (e.g. in case stopping the profiling is handled asynchronously).  
`profile_bytes` |  `bytes` Input only. Profile bytes, as a gzip compressed serialized proto, the format is <https://github.com/google/pprof/blob/master/proto/profile.proto>.  
`labels` |  `map<string, string>` Input only. Labels associated to this specific profile. These labels will get merged with the deployment labels for the final data set. See documentation on deployment labels for validation rules and limits.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Start time for the profile. This output is only present in response from the ListProfiles method.  
  
## ProfileType

ProfileType is type of profiling data. NOTE: the enumeration member names are used (in lowercase) as unique string identifiers of profile types, so they must not be renamed.

Enums  
---  
`PROFILE_TYPE_UNSPECIFIED` | Unspecified profile type.  
`CPU` | Thread CPU time sampling.  
`WALL` | Wallclock time sampling. More expensive as stops all threads.  
`HEAP` | In-use heap profile. Represents a snapshot of the allocations that are live at the time of the profiling.  
`THREADS` | Single-shot collection of all thread stacks.  
`CONTENTION` | Synchronization contention profile.  
`PEAK_HEAP` | Peak heap profile.  
`HEAP_ALLOC` | Heap allocation profile. It represents the aggregation of all allocations made over the duration of the profile. All allocations are included, including those that might have been freed by the end of the profiling interval. The profile is in particular useful for garbage collecting languages to understand which parts of the code create most of the garbage collection pressure to see if those can be optimized.  
  
## UpdateProfileRequest

UpdateProfileRequest contains the profile to update.

Fields  
---  
`profile` |  `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rpc/google.devtools.cloudprofiler.v2#google.devtools.cloudprofiler.v2.Profile)` Profile to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `profile`:

  * `cloudprofiler.profiles.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Field mask used to specify the fields to be overwritten. Currently only profile_bytes and labels fields are supported by UpdateProfile, so only those fields can be specified in the mask. When no mask is provided, all fields are overwritten.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
