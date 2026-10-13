---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.OperationMetadata
title: Class OperationMetadata (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:31.292697+00:00
---

# Class OperationMetadata (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.OperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OperationMetadata (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    OperationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata used across all long running operations returned by AutoML API.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`delete_details` |  `[google.cloud.automl_v1.types.DeleteOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeleteOperationMetadata)`   
Details of a Delete operation. This field is a member of `oneof`_ `details`.   
`deploy_model_details` |  `[google.cloud.automl_v1.types.DeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.DeployModelOperationMetadata)`   
Details of a DeployModel operation. This field is a member of `oneof`_ `details`.   
`undeploy_model_details` |  `[google.cloud.automl_v1.types.UndeployModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.UndeployModelOperationMetadata)`   
Details of an UndeployModel operation. This field is a member of `oneof`_ `details`.   
`create_model_details` |  `[google.cloud.automl_v1.types.CreateModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateModelOperationMetadata)`   
Details of CreateModel operation. This field is a member of `oneof`_ `details`.   
`create_dataset_details` |  `[google.cloud.automl_v1.types.CreateDatasetOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.CreateDatasetOperationMetadata)`   
Details of CreateDataset operation. This field is a member of `oneof`_ `details`.   
`import_data_details` |  `[google.cloud.automl_v1.types.ImportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImportDataOperationMetadata)`   
Details of ImportData operation. This field is a member of `oneof`_ `details`.   
`batch_predict_details` |  `[google.cloud.automl_v1.types.BatchPredictOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictOperationMetadata)`   
Details of BatchPredict operation. This field is a member of `oneof`_ `details`.   
`export_data_details` |  `[google.cloud.automl_v1.types.ExportDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportDataOperationMetadata)`   
Details of ExportData operation. This field is a member of `oneof`_ `details`.   
`export_model_details` |  `[google.cloud.automl_v1.types.ExportModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExportModelOperationMetadata)`   
Details of ExportModel operation. This field is a member of `oneof`_ `details`.   
`progress_percent` |  `int`   
Output only. Progress of operation. Range: [0, 100]. Not used currently.   
`partial_failures` |  `MutableSequence[google.rpc.status_pb2.Status]`   
Output only. Partial failures encountered. E.g. single files that couldn't be read. This field should never exceed 20 entries. Status details field will contain standard GCP error details.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the operation was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the operation was updated for the last time.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
