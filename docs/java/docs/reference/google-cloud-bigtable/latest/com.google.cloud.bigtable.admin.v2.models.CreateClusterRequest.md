---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest
title: Class CreateClusterRequest (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:01.947714+00:00
---

# Class CreateClusterRequest (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CreateClusterRequest (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public final class CreateClusterRequest

Parameters for creating a new Bigtable cluster.

A cluster represents the actual Cloud Bigtable service. Each cluster belongs to a single Cloud Bigtable instance. When your application sends requests to a Cloud Bigtable instance, those requests are actually handled by one of the clusters in the instance.

Each cluster is located in a single zone. An instance's clusters must be in unique zones that are within the same region. For example, if the first cluster is in us-east1-b, then us-east1-c is a valid zone for the second cluster. For a list of zones and regions where Cloud Bigtable is available, see [Cloud Bigtable Locations](https://cloud.google.com/bigtable/docs/locations).

Examples:
    
    
     // Small production instance:
     CreateClusterRequest clusterRequest = CreateClusterRequest.of("my-existing-instance", "my-cluster")
       .setZone("us-east1-c")
       .setServeNodes(3)
       .setStorageType(StorageType.SSD);
     

See Also: [For more details](https://cloud.google.com/bigtable/docs/instances-clusters-nodes#clusters)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CreateClusterRequest

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### of(String instanceId, String clusterId)
    
    
    public static CreateClusterRequest of(String instanceId, String clusterId)

Builds a new request to create a new cluster to the specified instance with the specified cluster id.

**Parameters**  
---  
**Name** | **Description**  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`clusterId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
## Methods 

### setKmsKeyName(String kmsKeyName)
    
    
    public CreateClusterRequest setKmsKeyName(String kmsKeyName)

Sets the Google Cloud Key Management Service (KMS) key for a CMEK-protected Bigtable. This requires the full resource name of the Cloud KMS key, in the format `projects/{key_project_id}/locations/{location}/keyRings/{ring_name}/cryptoKeys/{key_name}`

**Parameter**  
---  
**Name** | **Description**  
`kmsKeyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### setScalingMode(ClusterAutoscalingConfig autoscalingConfig)
    
    
    public CreateClusterRequest setScalingMode(ClusterAutoscalingConfig autoscalingConfig)

Sets the scaling mode to autoscaling by accepting an AutoscalingConfig where min nodes, max nodes, CPU utilization percent target, and storage utilization gib per node are set.

**Parameter**  
---  
**Name** | **Description**  
`autoscalingConfig` | `[ClusterAutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.ClusterAutoscalingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### setScalingMode(StaticClusterSize staticClusterSize)
    
    
    public CreateClusterRequest setScalingMode(StaticClusterSize staticClusterSize)

Sets the scaling node to manual and sets the number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.

**Parameter**  
---  
**Name** | **Description**  
`staticClusterSize` | `[StaticClusterSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.StaticClusterSize)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### setServeNodes(int numNodes) (deprecated)
    
    
    public CreateClusterRequest setServeNodes(int numNodes)

**Deprecated.** _Please use CreateClusterRequest#setScalingMode instead_

Sets the number of nodes allocated to this cluster. More nodes enable higher throughput and more consistent performance.

**Parameter**  
---  
**Name** | **Description**  
`numNodes` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### setStorageType(StorageType storageType)
    
    
    public CreateClusterRequest setStorageType(StorageType storageType)

Sets the type of storage used by this cluster to serve its parent instance's tables. Defaults to `SSD`.

**Parameter**  
---  
**Name** | **Description**  
`storageType` | `[StorageType](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.StorageType)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### setZone(String zone)
    
    
    public CreateClusterRequest setZone(String zone)

Sets the zone where the new cluster will be located. Must be different from the existing cluster.

**Parameter**  
---  
**Name** | **Description**  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateClusterRequest)` |   
  
### toProto(String projectId)
    
    
    public CreateClusterRequest toProto(String projectId)

**Internal Only** : This feature is not stable for application use.

Creates the request protobuf. This method is considered an internal implementation detail and not meant to be used by applications.

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.bigtable.admin.v2.CreateClusterRequest` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
