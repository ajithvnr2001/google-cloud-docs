---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig
title: Class TransferConfig (3.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:04.793745+00:00
---

# Class TransferConfig (3.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TransferConfig (3.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.24.0 (latest)  3.23.0  3.22.0  3.21.0  3.20.0  3.19.2  3.18.0  3.17.1  3.16.0  3.15.7  3.14.1  3.13.0  3.12.1  3.11.2  3.10.1  3.9.0  3.8.0  3.7.3  3.6.2  3.5.0  3.4.1  3.3.4  3.2.0  3.1.1  3.0.1  2.1.2  2.0.0  1.1.3  1.0.0  0.4.1 
    
    
    TransferConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a data transfer configuration. A transfer configuration contains all metadata needed to perform a data transfer. For example, `destination_dataset_id` specifies where data should be stored. When a new transfer configuration is created, the specified `destination_dataset_id` is created when needed and shared with the appropriate data source service account.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the transfer config. Transfer config names have the form either `projects/{project_id}/locations/{region}/transferConfigs/{config_id}` or `projects/{project_id}/transferConfigs/{config_id}`, where `config_id` is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config.   
`destination_dataset_id` |  `str`   
The BigQuery target dataset id. This field is a member of `oneof`_ `destination`.   
`display_name` |  `str`   
User specified display name for the data transfer.   
`data_source_id` |  `str`   
Data source ID. This cannot be changed once data transfer is created. The full list of available data source IDs can be returned through an API call: https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.locations.dataSources/list   
`params` |  `google.protobuf.struct_pb2.Struct`   
Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq   
`schedule` |  `str`   
Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: The minimum interval time between recurring transfers depends on the data source; refer to the documentation for your data source.   
`schedule_options` |  `[google.cloud.bigquery_datatransfer_v1.types.ScheduleOptions](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.ScheduleOptions)`   
Options customizing the data transfer schedule.   
`schedule_options_v2` |  `[google.cloud.bigquery_datatransfer_v1.types.ScheduleOptionsV2](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.ScheduleOptionsV2)`   
Options customizing different types of data transfer schedule. This field replaces "schedule" and "schedule_options" fields. ScheduleOptionsV2 cannot be used together with ScheduleOptions/Schedule.   
`data_refresh_window_days` |  `int`   
The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value.   
`disabled` |  `bool`   
Is this config disabled. When set to true, no runs will be scheduled for this transfer config.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Data transfer modification time. Ignored by server on input.   
`next_run_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Next time when data transfer will run.   
`state` |  `[google.cloud.bigquery_datatransfer_v1.types.TransferState](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferState)`   
Output only. State of the most recently updated transfer run.   
`user_id` |  `int`   
Deprecated. Unique ID of the user on whose behalf transfer is done.   
`dataset_region` |  `str`   
Output only. Region in which BigQuery dataset is located.   
`notification_pubsub_topic` |  `str`   
Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish. The format for specifying a pubsub topic is: `projects/{project_id}/topics/{topic_id}`  
`email_preferences` |  `[google.cloud.bigquery_datatransfer_v1.types.EmailPreferences](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.EmailPreferences)`   
Email notifications will be sent according to these preferences to the email address of the user who owns this transfer config.   
`owner_info` |  `[google.cloud.bigquery_datatransfer_v1.types.UserInfo](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.UserInfo)`   
Output only. Information about the user whose credentials are used to transfer data. Populated only for `transferConfigs.get` requests. In case the user information is not available, this field will not be populated. This field is a member of `oneof`_ `_owner_info`.   
`encryption_configuration` |  `[google.cloud.bigquery_datatransfer_v1.types.EncryptionConfiguration](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.EncryptionConfiguration)`   
The encryption configuration part. Currently, it is only used for the optional KMS key name. The BigQuery service account of your project must be granted permissions to use the key. Read methods will return the key name applied in effect. Write methods will apply the key if it is present, or otherwise try to apply project default keys if it is absent.   
`error` |  `google.rpc.status_pb2.Status`   
Output only. Error code with detailed information about reason of the latest config failure.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
