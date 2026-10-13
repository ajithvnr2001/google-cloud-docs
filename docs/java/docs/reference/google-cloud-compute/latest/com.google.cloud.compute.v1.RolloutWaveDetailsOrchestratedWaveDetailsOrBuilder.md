---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder
title: Interface RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:35.438145+00:00
---

# Interface RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLocationStatus(String key)
    
    
    public abstract boolean containsLocationStatus(String key)

Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".

` map<string, .google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> location_status = 19007420; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCompletedResourcesCount()
    
    
    public abstract long getCompletedResourcesCount()

Output only. Resource completed so far.

`optional int64 completed_resources_count = 208328833;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The completedResourcesCount.  
  
### getEstimatedCompletionTime()
    
    
    public abstract String getEstimatedCompletionTime()

Output only. Estimated timestamp at which the wave will complete. Extrapolated from current progress.

`optional string estimated_completion_time = 102305613;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The estimatedCompletionTime.  
  
### getEstimatedCompletionTimeBytes()
    
    
    public abstract ByteString getEstimatedCompletionTimeBytes()

Output only. Estimated timestamp at which the wave will complete. Extrapolated from current progress.

`optional string estimated_completion_time = 102305613;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for estimatedCompletionTime.  
  
### getEstimatedTotalResourcesCount()
    
    
    public abstract long getEstimatedTotalResourcesCount()

Output only. Estimated total count of resources.

`optional int64 estimated_total_resources_count = 457594807;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The estimatedTotalResourcesCount.  
  
### getFailedLocations(int index)
    
    
    public abstract String getFailedLocations(int index)

Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.

`repeated string failed_locations = 30506460;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The failedLocations at the given index.  
  
### getFailedLocationsBytes(int index)
    
    
    public abstract ByteString getFailedLocationsBytes(int index)

Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.

`repeated string failed_locations = 30506460;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the failedLocations at the given index.  
  
### getFailedLocationsCount()
    
    
    public abstract int getFailedLocationsCount()

Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.

`repeated string failed_locations = 30506460;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of failedLocations.  
  
### getFailedLocationsList()
    
    
    public abstract List<String> getFailedLocationsList()

Output only. Locations that failed during orchestration, and ProgressiveRollout stopped retrying. There may be some successful resources rolled out in the wave as the location may have failed later in the Rollout.

`repeated string failed_locations = 30506460;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the failedLocations.  
  
### getFailedResourcesCount()
    
    
    public abstract long getFailedResourcesCount()

Output only. Resources failed.

`optional int64 failed_resources_count = 391795315;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The failedResourcesCount.  
  
### getLocationStatus() (deprecated)
    
    
    public abstract Map<String,RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> getLocationStatus()

Use [#getLocationStatusMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder#com_google_cloud_compute_v1_RolloutWaveDetailsOrchestratedWaveDetailsOrBuilder_getLocationStatusMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus)>` |   
  
### getLocationStatusCount()
    
    
    public abstract int getLocationStatusCount()

Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".

` map<string, .google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> location_status = 19007420; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLocationStatusMap()
    
    
    public abstract Map<String,RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> getLocationStatusMap()

Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".

` map<string, .google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> location_status = 19007420; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus)>` |   
  
### getLocationStatusOrDefault(String key, RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus defaultValue)
    
    
    public abstract RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus getLocationStatusOrDefault(String key, RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus defaultValue)

Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".

` map<string, .google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> location_status = 19007420; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus)` |   
  
### getLocationStatusOrThrow(String key)
    
    
    public abstract RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus getLocationStatusOrThrow(String key)

Output only. Status of each location in the wave. Map keys (locations) must be specified like "us-east1" or "asia-west1-a".

` map<string, .google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus> location_status = 19007420; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus)` |   
  
### hasCompletedResourcesCount()
    
    
    public abstract boolean hasCompletedResourcesCount()

Output only. Resource completed so far.

`optional int64 completed_resources_count = 208328833;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the completedResourcesCount field is set.  
  
### hasEstimatedCompletionTime()
    
    
    public abstract boolean hasEstimatedCompletionTime()

Output only. Estimated timestamp at which the wave will complete. Extrapolated from current progress.

`optional string estimated_completion_time = 102305613;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the estimatedCompletionTime field is set.  
  
### hasEstimatedTotalResourcesCount()
    
    
    public abstract boolean hasEstimatedTotalResourcesCount()

Output only. Estimated total count of resources.

`optional int64 estimated_total_resources_count = 457594807;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the estimatedTotalResourcesCount field is set.  
  
### hasFailedResourcesCount()
    
    
    public abstract boolean hasFailedResourcesCount()

Output only. Resources failed.

`optional int64 failed_resources_count = 391795315;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the failedResourcesCount field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
