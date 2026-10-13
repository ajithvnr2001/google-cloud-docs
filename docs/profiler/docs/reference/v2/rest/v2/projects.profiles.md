---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles
title: REST Resource: projects.profiles \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:42.755311+00:00
---

# REST Resource: projects.profiles  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  REST Resource: projects.profiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Profile
    * JSON representation
  * ProfileType
  * Deployment
    * JSON representation
  * Methods



## Resource: Profile

Profile resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "profileType": enum ([ProfileType](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#ProfileType)),
      "deployment": {
        object ([Deployment](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Deployment))
      },
      "duration": string,
      "profileBytes": string,
      "labels": {
        string: string,
        ...
      },
      "startTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Opaque, server-assigned, unique ID for this profile.  
`profileType` |  `enum (`[ProfileType](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#ProfileType)`)` Type of profile. For offline mode, this must be specified when creating the profile. For online mode it is assigned and returned by the server.  
`deployment` |  `object (`[Deployment](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Deployment)`)` Deployment this profile corresponds to.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration of the profiling session. Input (for the offline mode) or output (for the online mode). The field represents requested profiling duration. It may slightly differ from the effective profiling duration, which is recorded in the profile data, in case the profiling can't be stopped immediately (e.g. in case stopping the profiling is handled asynchronously).  
`profileBytes` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Input only. Profile bytes, as a gzip compressed serialized proto, the format is <https://github.com/google/pprof/blob/master/proto/profile.proto>.  
`labels` |  `map (key: string, value: string)` Input only. Labels associated to this specific profile. These labels will get merged with the deployment labels for the final data set. See documentation on deployment labels for validation rules and limits.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Start time for the profile. This output is only present in response from the profiles.list method.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
## Deployment

Deployment contains the deployment identification information.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "target": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`projectId` |  `string` Project ID is the ID of a cloud project. Validation regex: `^[a-z][-a-z0-9:.]{4,61}[a-z0-9]$`.  
`target` |  `string` Target is the service name used to group related deployments: * Service name for App Engine Flex / Standard. * Cluster and container name for GKE. * User-specified string for direct Compute Engine profiling (e.g. Java). * Job name for Dataflow. Validation regex: `^[a-z0-9]([-a-z0-9_.]{0,253}[a-z0-9])?$`.  
`labels` |  `map (key: string, value: string)` Labels identify the deployment within the user universe and same target. Validation regex for label names: `^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$`. Value for an individual label must be <= 512 bytes, the total size of all label names and values must be <= 1024 bytes.Label named "language" can be used to record the programming language of the profiled deployment. The standard choices for the value include "java", "go", "python", "ruby", "nodejs", "php", "dotnet".For deployments running on Google Cloud Platform, "zone" or "region" label should be present describing the deployment location. An example of a zone is "us-central1-a", an example of a region is "us-central1" or "us-central".  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/create)`

|  CreateProfile creates a new profile resource in the online mode.  
  
### `[createOffline](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/createOffline)`

|  CreateOfflineProfile creates a new profile resource in the offline mode.  
  
### `[list](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/list)`

|  Lists profiles which have been collected so far and for which the caller has permission to view.  
  
### `[patch](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/patch)`

|  UpdateProfile updates the profile bytes and labels on the profile resource created in the online mode.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-12 UTC."],[],[]] 
