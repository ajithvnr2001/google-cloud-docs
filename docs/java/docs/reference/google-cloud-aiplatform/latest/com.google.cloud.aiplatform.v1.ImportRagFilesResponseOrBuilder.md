---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponseOrBuilder
title: Interface ImportRagFilesResponseOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:29.537408+00:00
---

# Interface ImportRagFilesResponseOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportRagFilesResponseOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface ImportRagFilesResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFailedRagFilesCount()
    
    
    public abstract long getFailedRagFilesCount()

The number of RagFiles that had failed while importing into the RagCorpus.

`int64 failed_rag_files_count = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The failedRagFilesCount.  
  
### getImportedRagFilesCount()
    
    
    public abstract long getImportedRagFilesCount()

The number of RagFiles that had been imported into the RagCorpus.

`int64 imported_rag_files_count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The importedRagFilesCount.  
  
### getPartialFailureSinkCase()
    
    
    public abstract ImportRagFilesResponse.PartialFailureSinkCase getPartialFailureSinkCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportRagFilesResponse.PartialFailureSinkCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportRagFilesResponse.PartialFailureSinkCase)` |   
  
### getPartialFailuresBigqueryTable()
    
    
    public abstract String getPartialFailuresBigqueryTable()

The BigQuery table into which the partial failures were written.

`string partial_failures_bigquery_table = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The partialFailuresBigqueryTable.  
  
### getPartialFailuresBigqueryTableBytes()
    
    
    public abstract ByteString getPartialFailuresBigqueryTableBytes()

The BigQuery table into which the partial failures were written.

`string partial_failures_bigquery_table = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for partialFailuresBigqueryTable.  
  
### getPartialFailuresGcsPath()
    
    
    public abstract String getPartialFailuresGcsPath()

The Google Cloud Storage path into which the partial failures were written.

`string partial_failures_gcs_path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The partialFailuresGcsPath.  
  
### getPartialFailuresGcsPathBytes()
    
    
    public abstract ByteString getPartialFailuresGcsPathBytes()

The Google Cloud Storage path into which the partial failures were written.

`string partial_failures_gcs_path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for partialFailuresGcsPath.  
  
### getSkippedRagFilesCount()
    
    
    public abstract long getSkippedRagFilesCount()

The number of RagFiles that was skipped while importing into the RagCorpus.

`int64 skipped_rag_files_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The skippedRagFilesCount.  
  
### hasPartialFailuresBigqueryTable()
    
    
    public abstract boolean hasPartialFailuresBigqueryTable()

The BigQuery table into which the partial failures were written.

`string partial_failures_bigquery_table = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partialFailuresBigqueryTable field is set.  
  
### hasPartialFailuresGcsPath()
    
    
    public abstract boolean hasPartialFailuresGcsPath()

The Google Cloud Storage path into which the partial failures were written.

`string partial_failures_gcs_path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partialFailuresGcsPath field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
