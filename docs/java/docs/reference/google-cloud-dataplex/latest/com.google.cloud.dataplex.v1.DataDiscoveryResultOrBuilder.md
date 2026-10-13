---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResultOrBuilder
title: Interface DataDiscoveryResultOrBuilder (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:19.472547+00:00
---

# Interface DataDiscoveryResultOrBuilder (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataDiscoveryResultOrBuilder (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public interface DataDiscoveryResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBigqueryPublishing()
    
    
    public abstract DataDiscoveryResult.BigQueryPublishing getBigqueryPublishing()

Output only. Configuration for metadata publishing.

` .google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishing bigquery_publishing = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDiscoveryResult.BigQueryPublishing](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishing)` | The bigqueryPublishing.  
  
### getBigqueryPublishingOrBuilder()
    
    
    public abstract DataDiscoveryResult.BigQueryPublishingOrBuilder getBigqueryPublishingOrBuilder()

Output only. Configuration for metadata publishing.

` .google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishing bigquery_publishing = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDiscoveryResult.BigQueryPublishingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishingOrBuilder)` |   
  
### getScanStatistics()
    
    
    public abstract DataDiscoveryResult.ScanStatistics getScanStatistics()

Output only. Describes result statistics of a data scan discovery job.

` .google.cloud.dataplex.v1.DataDiscoveryResult.ScanStatistics scan_statistics = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDiscoveryResult.ScanStatistics](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResult.ScanStatistics)` | The scanStatistics.  
  
### getScanStatisticsOrBuilder()
    
    
    public abstract DataDiscoveryResult.ScanStatisticsOrBuilder getScanStatisticsOrBuilder()

Output only. Describes result statistics of a data scan discovery job.

` .google.cloud.dataplex.v1.DataDiscoveryResult.ScanStatistics scan_statistics = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DataDiscoveryResult.ScanStatisticsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataDiscoveryResult.ScanStatisticsOrBuilder)` |   
  
### hasBigqueryPublishing()
    
    
    public abstract boolean hasBigqueryPublishing()

Output only. Configuration for metadata publishing.

` .google.cloud.dataplex.v1.DataDiscoveryResult.BigQueryPublishing bigquery_publishing = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryPublishing field is set.  
  
### hasScanStatistics()
    
    
    public abstract boolean hasScanStatistics()

Output only. Describes result statistics of a data scan discovery job.

` .google.cloud.dataplex.v1.DataDiscoveryResult.ScanStatistics scan_statistics = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scanStatistics field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
