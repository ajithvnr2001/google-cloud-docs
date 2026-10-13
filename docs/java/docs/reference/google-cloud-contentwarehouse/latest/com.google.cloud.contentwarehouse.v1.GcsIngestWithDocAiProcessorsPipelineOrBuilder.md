---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GcsIngestWithDocAiProcessorsPipelineOrBuilder
title: Interface GcsIngestWithDocAiProcessorsPipelineOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:25.593593+00:00
---

# Interface GcsIngestWithDocAiProcessorsPipelineOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GcsIngestWithDocAiProcessorsPipelineOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GcsIngestWithDocAiProcessorsPipelineOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface GcsIngestWithDocAiProcessorsPipelineOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExtractProcessorInfos(int index)
    
    
    public abstract ProcessorInfo getExtractProcessorInfos(int index)

The extract processors information. One matched extract processor will be used to process documents based on the classify processor result. If no classify processor is specified, the first extract processor will be used.

`repeated .google.cloud.contentwarehouse.v1.ProcessorInfo extract_processor_infos = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ProcessorInfo)` |   
  
### getExtractProcessorInfosCount()
    
    
    public abstract int getExtractProcessorInfosCount()

The extract processors information. One matched extract processor will be used to process documents based on the classify processor result. If no classify processor is specified, the first extract processor will be used.

`repeated .google.cloud.contentwarehouse.v1.ProcessorInfo extract_processor_infos = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExtractProcessorInfosList()
    
    
    public abstract List<ProcessorInfo> getExtractProcessorInfosList()

The extract processors information. One matched extract processor will be used to process documents based on the classify processor result. If no classify processor is specified, the first extract processor will be used.

`repeated .google.cloud.contentwarehouse.v1.ProcessorInfo extract_processor_infos = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProcessorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ProcessorInfo)>` |   
  
### getExtractProcessorInfosOrBuilder(int index)
    
    
    public abstract ProcessorInfoOrBuilder getExtractProcessorInfosOrBuilder(int index)

The extract processors information. One matched extract processor will be used to process documents based on the classify processor result. If no classify processor is specified, the first extract processor will be used.

`repeated .google.cloud.contentwarehouse.v1.ProcessorInfo extract_processor_infos = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ProcessorInfoOrBuilder)` |   
  
### getExtractProcessorInfosOrBuilderList()
    
    
    public abstract List<? extends ProcessorInfoOrBuilder> getExtractProcessorInfosOrBuilderList()

The extract processors information. One matched extract processor will be used to process documents based on the classify processor result. If no classify processor is specified, the first extract processor will be used.

`repeated .google.cloud.contentwarehouse.v1.ProcessorInfo extract_processor_infos = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.contentwarehouse.v1.ProcessorInfoOrBuilder>` |   
  
### getInputPath()
    
    
    public abstract String getInputPath()

The input Cloud Storage folder. All files under this folder will be imported to Document Warehouse. Format: `gs://<bucket-name>/<folder-name>`.

`string input_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inputPath.  
  
### getInputPathBytes()
    
    
    public abstract ByteString getInputPathBytes()

The input Cloud Storage folder. All files under this folder will be imported to Document Warehouse. Format: `gs://<bucket-name>/<folder-name>`.

`string input_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inputPath.  
  
### getPipelineConfig()
    
    
    public abstract IngestPipelineConfig getPipelineConfig()

Optional. The config for the Cloud Storage Ingestion with DocAI Processors pipeline. It provides additional customization options to run the pipeline and can be skipped if it is not applicable.

` .google.cloud.contentwarehouse.v1.IngestPipelineConfig pipeline_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestPipelineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.IngestPipelineConfig)` | The pipelineConfig.  
  
### getPipelineConfigOrBuilder()
    
    
    public abstract IngestPipelineConfigOrBuilder getPipelineConfigOrBuilder()

Optional. The config for the Cloud Storage Ingestion with DocAI Processors pipeline. It provides additional customization options to run the pipeline and can be skipped if it is not applicable.

` .google.cloud.contentwarehouse.v1.IngestPipelineConfig pipeline_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestPipelineConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.IngestPipelineConfigOrBuilder)` |   
  
### getProcessorResultsFolderPath()
    
    
    public abstract String getProcessorResultsFolderPath()

The Cloud Storage folder path used to store the raw results from processors. Format: `gs://<bucket-name>/<folder-name>`.

`string processor_results_folder_path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The processorResultsFolderPath.  
  
### getProcessorResultsFolderPathBytes()
    
    
    public abstract ByteString getProcessorResultsFolderPathBytes()

The Cloud Storage folder path used to store the raw results from processors. Format: `gs://<bucket-name>/<folder-name>`.

`string processor_results_folder_path = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for processorResultsFolderPath.  
  
### getSkipIngestedDocuments()
    
    
    public abstract boolean getSkipIngestedDocuments()

The flag whether to skip ingested documents. If it is set to true, documents in Cloud Storage contains key "status" with value "status=ingested" in custom metadata will be skipped to ingest.

`bool skip_ingested_documents = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The skipIngestedDocuments.  
  
### getSplitClassifyProcessorInfo()
    
    
    public abstract ProcessorInfo getSplitClassifyProcessorInfo()

The split and classify processor information. The split and classify result will be used to find a matched extract processor.

`.google.cloud.contentwarehouse.v1.ProcessorInfo split_classify_processor_info = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ProcessorInfo)` | The splitClassifyProcessorInfo.  
  
### getSplitClassifyProcessorInfoOrBuilder()
    
    
    public abstract ProcessorInfoOrBuilder getSplitClassifyProcessorInfoOrBuilder()

The split and classify processor information. The split and classify result will be used to find a matched extract processor.

`.google.cloud.contentwarehouse.v1.ProcessorInfo split_classify_processor_info = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ProcessorInfoOrBuilder)` |   
  
### hasPipelineConfig()
    
    
    public abstract boolean hasPipelineConfig()

Optional. The config for the Cloud Storage Ingestion with DocAI Processors pipeline. It provides additional customization options to run the pipeline and can be skipped if it is not applicable.

` .google.cloud.contentwarehouse.v1.IngestPipelineConfig pipeline_config = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pipelineConfig field is set.  
  
### hasSplitClassifyProcessorInfo()
    
    
    public abstract boolean hasSplitClassifyProcessorInfo()

The split and classify processor information. The split and classify result will be used to find a matched extract processor.

`.google.cloud.contentwarehouse.v1.ProcessorInfo split_classify_processor_info = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the splitClassifyProcessorInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
