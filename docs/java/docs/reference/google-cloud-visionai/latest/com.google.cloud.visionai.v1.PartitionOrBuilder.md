---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PartitionOrBuilder
title: Interface PartitionOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:28.377496+00:00
---

# Interface PartitionOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.PartitionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PartitionOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface PartitionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getRelativeTemporalPartition()
    
    
    public abstract Partition.RelativeTemporalPartition getRelativeTemporalPartition()

Partition of asset in time.

` .google.cloud.visionai.v1.Partition.RelativeTemporalPartition relative_temporal_partition = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Partition.RelativeTemporalPartition](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.RelativeTemporalPartition)` | The relativeTemporalPartition.  
  
### getRelativeTemporalPartitionOrBuilder()
    
    
    public abstract Partition.RelativeTemporalPartitionOrBuilder getRelativeTemporalPartitionOrBuilder()

Partition of asset in time.

` .google.cloud.visionai.v1.Partition.RelativeTemporalPartition relative_temporal_partition = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Partition.RelativeTemporalPartitionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.RelativeTemporalPartitionOrBuilder)` |   
  
### getSpatialPartition()
    
    
    public abstract Partition.SpatialPartition getSpatialPartition()

Partition of asset in space.

`.google.cloud.visionai.v1.Partition.SpatialPartition spatial_partition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Partition.SpatialPartition](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.SpatialPartition)` | The spatialPartition.  
  
### getSpatialPartitionOrBuilder()
    
    
    public abstract Partition.SpatialPartitionOrBuilder getSpatialPartitionOrBuilder()

Partition of asset in space.

`.google.cloud.visionai.v1.Partition.SpatialPartition spatial_partition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Partition.SpatialPartitionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.SpatialPartitionOrBuilder)` |   
  
### getTemporalPartition()
    
    
    public abstract Partition.TemporalPartition getTemporalPartition()

Partition of asset in time.

`.google.cloud.visionai.v1.Partition.TemporalPartition temporal_partition = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Partition.TemporalPartition](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.TemporalPartition)` | The temporalPartition.  
  
### getTemporalPartitionOrBuilder()
    
    
    public abstract Partition.TemporalPartitionOrBuilder getTemporalPartitionOrBuilder()

Partition of asset in time.

`.google.cloud.visionai.v1.Partition.TemporalPartition temporal_partition = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Partition.TemporalPartitionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Partition.TemporalPartitionOrBuilder)` |   
  
### hasRelativeTemporalPartition()
    
    
    public abstract boolean hasRelativeTemporalPartition()

Partition of asset in time.

` .google.cloud.visionai.v1.Partition.RelativeTemporalPartition relative_temporal_partition = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the relativeTemporalPartition field is set.  
  
### hasSpatialPartition()
    
    
    public abstract boolean hasSpatialPartition()

Partition of asset in space.

`.google.cloud.visionai.v1.Partition.SpatialPartition spatial_partition = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the spatialPartition field is set.  
  
### hasTemporalPartition()
    
    
    public abstract boolean hasTemporalPartition()

Partition of asset in time.

`.google.cloud.visionai.v1.Partition.TemporalPartition temporal_partition = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the temporalPartition field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
