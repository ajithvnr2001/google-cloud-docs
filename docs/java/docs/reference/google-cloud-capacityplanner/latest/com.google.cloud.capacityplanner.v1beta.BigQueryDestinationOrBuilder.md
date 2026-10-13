---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestinationOrBuilder
title: Interface BigQueryDestinationOrBuilder (0.22.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:25.346756+00:00
---

# Interface BigQueryDestinationOrBuilder (0.22.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestinationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BigQueryDestinationOrBuilder (0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.18.0  0.17.0  0.16.0  0.14.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface BigQueryDestinationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateDisposition()
    
    
    public abstract BigQueryDestination.CreateDisposition getCreateDisposition()

Optional. Specifies the action that occurs if the destination table does not exist

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.CreateDisposition create_disposition = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDestination.CreateDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestination.CreateDisposition)` | The createDisposition.  
  
### getCreateDispositionValue()
    
    
    public abstract int getCreateDispositionValue()

Optional. Specifies the action that occurs if the destination table does not exist

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.CreateDisposition create_disposition = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for createDisposition.  
  
### getDataset()
    
    
    public abstract String getDataset()

Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.

`string dataset = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataset.  
  
### getDatasetBytes()
    
    
    public abstract ByteString getDatasetBytes()

Required. The BigQuery dataset in format "projects/{projectId}/datasets/{datasetId}", to which the snapshot result should be exported. If this dataset does not exist, the export call returns an INVALID_ARGUMENT error.

`string dataset = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataset.  
  
### getGcsLocation()
    
    
    public abstract String getGcsLocation()

Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'.

`string gcs_location = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gcsLocation.  
  
### getGcsLocationBytes()
    
    
    public abstract ByteString getGcsLocationBytes()

Optional. Specifies the Cloud Storage location. Users can choose to provide a location for Cloud Storage bucket to store the exported data. (as it is possible that some locations are restricted via org policy for that project) Temporary Cloud Storage bucket creation is an interim step for BigQuery upload. If no value is provided, the default location used will be 'US'.

`string gcs_location = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gcsLocation.  
  
### getPartitionKey()
    
    
    public abstract BigQueryDestination.PartitionKey getPartitionKey()

Optional. The partition key for BigQuery partitioned table.

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.PartitionKey partition_key = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDestination.PartitionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestination.PartitionKey)` | The partitionKey.  
  
### getPartitionKeyValue()
    
    
    public abstract int getPartitionKeyValue()

Optional. The partition key for BigQuery partitioned table.

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.PartitionKey partition_key = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for partitionKey.  
  
### getTable()
    
    
    public abstract String getTable()

Required. The BigQuery table to which the snapshot result should be written.

`string table = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The table.  
  
### getTableBytes()
    
    
    public abstract ByteString getTableBytes()

Required. The BigQuery table to which the snapshot result should be written.

`string table = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for table.  
  
### getWriteDisposition()
    
    
    public abstract BigQueryDestination.WriteDisposition getWriteDisposition()

Optional. Specifies the action that occurs if the destination table or partition already exists.

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.WriteDisposition write_disposition = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDestination.WriteDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.BigQueryDestination.WriteDisposition)` | The writeDisposition.  
  
### getWriteDispositionValue()
    
    
    public abstract int getWriteDispositionValue()

Optional. Specifies the action that occurs if the destination table or partition already exists.

` .google.cloud.capacityplanner.v1beta.BigQueryDestination.WriteDisposition write_disposition = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for writeDisposition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
