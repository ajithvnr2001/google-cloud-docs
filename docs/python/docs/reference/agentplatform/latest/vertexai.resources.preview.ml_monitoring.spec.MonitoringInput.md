---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.MonitoringInput
title: Class MonitoringInput (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:40.892956+00:00
---

# Class MonitoringInput (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.spec.MonitoringInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MonitoringInput (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    MonitoringInput(
        vertex_dataset: typing.Optional[str] = None,
        gcs_uri: typing.Optional[str] = None,
        data_format: typing.Optional[str] = None,
        table_uri: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        timestamp_field: typing.Optional[str] = None,
        batch_prediction_job: typing.Optional[str] = None,
        endpoints: typing.Optional[typing.List[str]] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        offset: typing.Optional[str] = None,
        window: typing.Optional[str] = None,
    )

Model monitoring data input spec.

## Attributes  
  
---  
**Name** | **Description**  
`vertex_dataset` |  `str`   
Optional. Resource name of the Vertex AI managed dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}` At least one source of dataset should be provided, and if one of the fields is set, no need to set other sources (vertex_dataset, gcs_uri, table_uri, query, batch_prediction_job, endpoints).   
`gcs_uri` |  `str`   
Optional. Google Cloud Storage URI to the input file(s). May contain wildcards.   
`data_format` |  `str`   
Optional. Data format of Google Cloud Storage file(s). Should be provided if a gcs_uri is set. Supported formats: "csv", "jsonl", "tf-record"   
`table_uri` |  `str`   
Optonal. BigQuery URI to a table, up to 2000 characters long. All the columns in the table will be selected. Accepted forms: \- BigQuery path. For example: `bq://projectId.bqDatasetId.bqTableId`.   
`query` |  `str`   
Optional. Standard SQL for BigQuery to be used instead of the `table_uri`.   
`timestamp_field` |  `str`   
Optional. The timestamp field in the dataset. the `timestamp_field` must be specified if you'd like to use `start_time`, `end_time`, `offset` or `window`. If you use `query` to specify the dataset, make sure the `timestamp_field` is in the selection fields.   
`batch_prediction_job` |  `str`   
Optional. Vertex AI Batch Prediction Job resource name. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
`endpoints` |  `List[str]`   
Optional. List of Vertex AI Endpoint resource names. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`start_time` |  `timestamp_pb2.Timestamp`   
Optional. Inclusive start of the time interval for which results should be returned. Should be set together with `end_time`.   
`end_time` |  `timestamp_pb2.Timestamp`   
Optional. Exclusive end of the time interval for which results should be returned. Should be set together with `start_time`.`   
`offset` |  `str`   
Optional. Offset is the time difference from the cut-off time. For scheduled jobs, the cut-off time is the scheduled time. For non-scheduled jobs, it's the time when the job was created. Currently we support the following format: 'w|W': Week, 'd|D': Day, 'h|H': Hour E.g. '1h' stands for 1 hour, '2d' stands for 2 days.   
`window` |  `str`   
Optional. Window refers to the scope of data selected for analysis. It allows you to specify the quantity of data you wish to examine. It refers to the data time window prior to the cut-off time or the cut-off time minus the offset. Currently we support the following format: 'w|W': Week, 'd|D': Day, 'h|H': Hour E.g. '1h' stands for 1 hour, '2d' stands for 2 days.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
