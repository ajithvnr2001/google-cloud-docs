---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput/
title: ModelMonitoringInput \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:50.677509+00:00
---

# ModelMonitoringInput  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ModelMonitoringInput Stay organized with collections  Save and categorize content based on your preferences. 

Model monitoring data input spec.

Fields  
  
`dataset` `Union type`  
  
Dataset source. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`columnizedDataset` `object (`[ModelMonitoringDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringDataset)`)` Columnized dataset. | `batchPredictionOutput` `object (`[BatchPredictionOutput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#BatchPredictionOutput)`)` Agent Platform Batch prediction Job. | `vertexEndpointLogs` `object (`[VertexEndpointLogs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#VertexEndpointLogs)`)` Agent Platform Endpoint request & response logging. End of mutually exclusive fields. | `time_spec` `Union type`  
  
Time specification for the dataset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`timeInterval` `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval)`)` The time interval (pair of startTime and endTime) for which results should be returned. | `timeOffset` `object (`[TimeOffset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#TimeOffset)`)` The time offset setting for which results should be returned. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // dataset
      "columnizedDataset": {
        object ([ModelMonitoringDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringDataset))
      },
      "batchPredictionOutput": {
        object ([BatchPredictionOutput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#BatchPredictionOutput))
      },
      "vertexEndpointLogs": {
        object ([VertexEndpointLogs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#VertexEndpointLogs))
      }
      // Union type
    
      // time_spec
      "timeInterval": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Interval))
      },
      "timeOffset": {
        object ([TimeOffset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#TimeOffset))
      }
      // Union type
    }  
  
## ModelMonitoringDataset

Input dataset spec.

Fields  
  
`timestampField` `string` The timestamp field. Usually for serving data. | `data_location` `Union type`  
  
Choose one of supported data location for columnized dataset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`vertexDataset` `string` Resource name of the Agent Platform managed dataset. | `gcsSource` `object (`[ModelMonitoringGcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringGcsSource)`)` Google Cloud Storage data source. | `bigquerySource` `object (`[ModelMonitoringBigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringBigQuerySource)`)` BigQuery data source. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "timestampField": string,
    
      // data_location
      "vertexDataset": string,
      "gcsSource": {
        object ([ModelMonitoringGcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringGcsSource))
      },
      "bigquerySource": {
        object ([ModelMonitoringBigQuerySource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#ModelMonitoringBigQuerySource))
      }
      // Union type
    }  
  
## ModelMonitoringGcsSource

Dataset spec for data stored in Google Cloud Storage.

Fields  
  
`gcsUri` `string` Google Cloud Storage URI to the input file(s). May contain wildcards. For more information on wildcards, see <https://cloud.google.com/storage/docs/wildcards>. | `format` `enum (`[DataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#DataFormat)`)` data format of the dataset. | JSON representation  
---  
      
    
    {
      "gcsUri": string,
      "format": enum ([DataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelMonitoringInput#DataFormat))
    }  
  
## DataFormat

Supported data format.

Enums  
---  
`DATA_FORMAT_UNSPECIFIED` | data format unspecified, used when this field is unset.  
`CSV` | CSV files.  
`TF_RECORD` | TfRecord files  
`JSONL` | JsonL files.  
  
## ModelMonitoringBigQuerySource

Dataset spec for data sotred in BigQuery.

Fields  
  
`connection` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`tableUri` `string` BigQuery URI to a table, up to 2000 characters long. All the columns in the table will be selected. Accepted forms:

  * BigQuery path. For example: `bq://projectId.bqDatasetId.bqTableId`.

| `query` `string` Standard SQL to be used instead of the `tableUri`. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // connection
      "tableUri": string,
      "query": string
      // Union type
    }  
  
## BatchPredictionOutput

data from Agent Platform Batch prediction job output.

Fields  
  
`batchPredictionJob` `string` Agent Platform Batch prediction job resource name. The job must match the model version specified in [ModelMonitor].[modelMonitoringTarget]. | JSON representation  
---  
      
    
    {
      "batchPredictionJob": string
    }  
  
## VertexEndpointLogs

data from Agent Platform Endpoint request response logging.

Fields  
  
`endpoints[]` `string` List of endpoint resource names. The endpoints must enable the logging with the [Endpoint].[requestResponseLoggingConfig], and must contain the deployed model corresponding to the model version specified in [ModelMonitor].[modelMonitoringTarget]. | JSON representation  
---  
      
    
    {
      "endpoints": [
        string
      ]
    }  
  
## TimeOffset

time offset setting.

Fields  
  
`offset` `string` [offset] is the time difference from the cut-off time. For scheduled jobs, the cut-off time is the scheduled time. For non-scheduled jobs, it's the time when the job was created. Currently we support the following format: 'w|W': Week, 'd|D': Day, 'h|H': Hour E.g. '1h' stands for 1 hour, '2d' stands for 2 days. | `window` `string` [window] refers to the scope of data selected for analysis. It allows you to specify the quantity of data you wish to examine. Currently we support the following format: 'w|W': Week, 'd|D': Day, 'h|H': Hour E.g. '1h' stands for 1 hour, '2d' stands for 2 days. | JSON representation  
---  
      
    
    {
      "offset": string,
      "window": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
