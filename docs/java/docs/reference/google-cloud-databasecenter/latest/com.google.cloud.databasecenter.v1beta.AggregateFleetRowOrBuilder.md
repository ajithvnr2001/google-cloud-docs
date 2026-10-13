---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.AggregateFleetRowOrBuilder
title: Interface AggregateFleetRowOrBuilder (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:22.627093+00:00
---

# Interface AggregateFleetRowOrBuilder (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.AggregateFleetRowOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AggregateFleetRowOrBuilder (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AggregateFleetRowOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDeltaDetails()
    
    
    public abstract DeltaDetails getDeltaDetails()

Optional. Delta counts and details of resources which were added to/deleted from fleet.

` optional .google.cloud.databasecenter.v1beta.DeltaDetails delta_details = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DeltaDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.DeltaDetails)` | The deltaDetails.  
  
### getDeltaDetailsOrBuilder()
    
    
    public abstract DeltaDetailsOrBuilder getDeltaDetailsOrBuilder()

Optional. Delta counts and details of resources which were added to/deleted from fleet.

` optional .google.cloud.databasecenter.v1beta.DeltaDetails delta_details = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DeltaDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.DeltaDetailsOrBuilder)` |   
  
### getDimension(int index)
    
    
    public abstract Dimension getDimension(int index)

Group by dimension.

`repeated .google.cloud.databasecenter.v1beta.Dimension dimension = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dimension](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Dimension)` |   
  
### getDimensionCount()
    
    
    public abstract int getDimensionCount()

Group by dimension.

`repeated .google.cloud.databasecenter.v1beta.Dimension dimension = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionList()
    
    
    public abstract List<Dimension> getDimensionList()

Group by dimension.

`repeated .google.cloud.databasecenter.v1beta.Dimension dimension = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Dimension](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.Dimension)>` |   
  
### getDimensionOrBuilder(int index)
    
    
    public abstract DimensionOrBuilder getDimensionOrBuilder(int index)

Group by dimension.

`repeated .google.cloud.databasecenter.v1beta.Dimension dimension = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-databasecenter/latest/com.google.cloud.databasecenter.v1beta.DimensionOrBuilder)` |   
  
### getDimensionOrBuilderList()
    
    
    public abstract List<? extends DimensionOrBuilder> getDimensionOrBuilderList()

Group by dimension.

`repeated .google.cloud.databasecenter.v1beta.Dimension dimension = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.databasecenter.v1beta.DimensionOrBuilder>` |   
  
### getResourceGroupsCount()
    
    
    public abstract int getResourceGroupsCount()

Number of resource groups that have a particular dimension.

`int32 resource_groups_count = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The resourceGroupsCount.  
  
### getResourcesCount()
    
    
    public abstract int getResourcesCount()

Number of resources that have a particular dimension.

`int32 resources_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The resourcesCount.  
  
### hasDeltaDetails()
    
    
    public abstract boolean hasDeltaDetails()

Optional. Delta counts and details of resources which were added to/deleted from fleet.

` optional .google.cloud.databasecenter.v1beta.DeltaDetails delta_details = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deltaDetails field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
