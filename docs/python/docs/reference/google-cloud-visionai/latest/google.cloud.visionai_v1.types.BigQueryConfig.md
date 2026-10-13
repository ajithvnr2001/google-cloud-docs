---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.BigQueryConfig
title: Class BigQueryConfig (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:02.030732+00:00
---

# Class BigQueryConfig (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.BigQueryConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BigQueryConfig (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    BigQueryConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message of configurations for BigQuery processor.

## Attributes  
  
---  
**Name** | **Description**  
`table` |  `str`   
BigQuery table resource for Vision AI Platform to ingest annotations to.   
`cloud_function_mapping` |  `MutableMapping[str, str]`   
Data Schema By default, Vision AI Application will try to write annotations to the target BigQuery table using the following schema: ingestion_time: TIMESTAMP, the ingestion time of the original data. application: STRING, name of the application which produces the annotation. instance: STRING, Id of the instance which produces the annotation. node: STRING, name of the application graph node which produces the annotation. annotation: STRING or JSON, the actual annotation protobuf will be converted to json string with bytes field as 64 encoded string. It can be written to both String or Json type column. To forward annotation data to an existing BigQuery table, customer needs to make sure the compatibility of the schema. The map maps application node name to its corresponding cloud function endpoint to transform the annotations directly to the google.cloud.bigquery.storage.v1.AppendRowsRequest (only avro_rows or proto_rows should be set). If configured, annotations produced by corresponding application node will sent to the Cloud Function at first before be forwarded to BigQuery. If the default table schema doesn't fit, customer is able to transform the annotation output from Vision AI Application to arbitrary BigQuery table schema with CloudFunction. \- The cloud function will receive AppPlatformCloudFunctionRequest where the annotations field will be the json format of Vision AI annotation. \- The cloud function should return AppPlatformCloudFunctionResponse with AppendRowsRequest stored in the annotations field. \- To drop the annotation, simply clear the annotations field in the returned AppPlatformCloudFunctionResponse.   
`create_default_table_if_not_exists` |  `bool`   
If true, App Platform will create the BigQuery DataSet and the BigQuery Table with default schema if the specified table doesn't exist. This doesn't work if any cloud function customized schema is specified since the system doesn't know your desired schema. JSON column will be used in the default table created by App Platform.   
  
## Classes 

### CloudFunctionMappingEntry
    
    
    CloudFunctionMappingEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
