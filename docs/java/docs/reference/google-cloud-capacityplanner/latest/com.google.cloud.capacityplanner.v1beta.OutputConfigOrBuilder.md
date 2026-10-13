---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OutputConfigOrBuilder
title: Interface OutputConfigOrBuilder (0.22.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:03.733864+00:00
---

# Interface OutputConfigOrBuilder (0.22.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OutputConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OutputConfigOrBuilder (0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.18.0  0.17.0  0.16.0  0.14.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface OutputConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBigqueryDestination()
    
    
    public abstract BigQueryDestination getBigqueryDestination()

Destination on BigQuery.

`.google.cloud.capacityplanner.v1beta.BigQueryDestination bigquery_destination = 2;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestination)` | The bigqueryDestination.  
  
### getBigqueryDestinationOrBuilder()
    
    
    public abstract BigQueryDestinationOrBuilder getBigqueryDestinationOrBuilder()

Destination on BigQuery.

`.google.cloud.capacityplanner.v1beta.BigQueryDestination bigquery_destination = 2;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDestinationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestinationOrBuilder)` |   
  
### getDestinationCase()
    
    
    public abstract OutputConfig.DestinationCase getDestinationCase()

**Returns**  
---  
**Type** | **Description**  
`[OutputConfig.DestinationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.OutputConfig.DestinationCase)` |   
  
### getGcsDestination()
    
    
    public abstract GcsDestination getGcsDestination()

Destination on Cloud Storage.

`.google.cloud.capacityplanner.v1beta.GcsDestination gcs_destination = 1;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.GcsDestination)` | The gcsDestination.  
  
### getGcsDestinationOrBuilder()
    
    
    public abstract GcsDestinationOrBuilder getGcsDestinationOrBuilder()

Destination on Cloud Storage.

`.google.cloud.capacityplanner.v1beta.GcsDestination gcs_destination = 1;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.GcsDestinationOrBuilder)` |   
  
### hasBigqueryDestination()
    
    
    public abstract boolean hasBigqueryDestination()

Destination on BigQuery.

`.google.cloud.capacityplanner.v1beta.BigQueryDestination bigquery_destination = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryDestination field is set.  
  
### hasGcsDestination()
    
    
    public abstract boolean hasGcsDestination()

Destination on Cloud Storage.

`.google.cloud.capacityplanner.v1beta.GcsDestination gcs_destination = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsDestination field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
