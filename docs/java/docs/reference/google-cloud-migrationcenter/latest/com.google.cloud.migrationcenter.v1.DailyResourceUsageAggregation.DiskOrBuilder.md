---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.DiskOrBuilder
title: Interface DailyResourceUsageAggregation.DiskOrBuilder (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:56.382348+00:00
---

# Interface DailyResourceUsageAggregation.DiskOrBuilder (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.DiskOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DailyResourceUsageAggregation.DiskOrBuilder (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface DailyResourceUsageAggregation.DiskOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIops()
    
    
    public abstract DailyResourceUsageAggregation.Stats getIops()

Disk I/O operations per second.

`.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.Stats iops = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DailyResourceUsageAggregation.Stats](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.Stats)` | The iops.  
  
### getIopsOrBuilder()
    
    
    public abstract DailyResourceUsageAggregation.StatsOrBuilder getIopsOrBuilder()

Disk I/O operations per second.

`.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.Stats iops = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DailyResourceUsageAggregation.StatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.StatsOrBuilder)` |   
  
### hasIops()
    
    
    public abstract boolean hasIops()

Disk I/O operations per second.

`.google.cloud.migrationcenter.v1.DailyResourceUsageAggregation.Stats iops = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iops field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
