---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.CloudStorageConfig
title: Class CloudStorageConfig (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:40.420041+00:00
---

# Class CloudStorageConfig (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.CloudStorageConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudStorageConfig (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.2  2.38.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.3  2.26.1  2.25.2  2.23.1  2.22.0  2.21.5  2.20.3  2.19.8  2.18.4  2.17.1  2.16.1  2.15.2  2.14.1  2.13.12  2.12.1  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.1  2.5.0  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.7.2  1.6.1  1.5.0  1.4.3  1.3.1  1.2.0  1.1.0  1.0.2  0.45.0  0.44.0  0.43.0 
    
    
    CloudStorageConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for a Cloud Storage subscription.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`bucket :noindex:` |  `str`   
Required. User-provided name for the Cloud Storage bucket. The bucket must be created by the user. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements] (https://cloud.google.com/storage/docs/buckets#naming).   
`filename_prefix :noindex:` |  `str`   
Optional. User-provided prefix for Cloud Storage filename. See the `object naming requirements   
`filename_suffix :noindex:` |  `str`   
Optional. User-provided suffix for Cloud Storage filename. See the `object naming requirements   
`filename_datetime_format :noindex:` |  `str`   
Optional. User-provided format string specifying how to represent datetimes in Cloud Storage filenames. See the `datetime format guidance   
`text_config :noindex:` |  `google.pubsub_v1.types.CloudStorageConfig.TextConfig`   
Optional. If set, message data will be written to Cloud Storage in text format. This field is a member of `oneof`_ `output_format`.   
`avro_config :noindex:` |  `google.pubsub_v1.types.CloudStorageConfig.AvroConfig`   
Optional. If set, message data will be written to Cloud Storage in Avro format. This field is a member of `oneof`_ `output_format`.   
`max_duration :noindex:` |  `google.protobuf.duration_pb2.Duration`   
Optional. The maximum duration that can elapse before a new Cloud Storage file is created. Min 1 minute, max 10 minutes, default 5 minutes. May not exceed the subscription's acknowledgment deadline.   
`max_bytes :noindex:` |  `int`   
Optional. The maximum bytes that can be written to a Cloud Storage file before a new file is created. Min 1 KB, max 10 GiB. The max_bytes limit may be exceeded in cases where messages are larger than the limit.   
`max_messages :noindex:` |  `int`   
Optional. The maximum number of messages that can be written to a Cloud Storage file before a new file is created. Min 1000 messages.   
`state :noindex:` |  `google.pubsub_v1.types.CloudStorageConfig.State`   
Output only. An output-only field that indicates whether or not the subscription can receive messages.   
`service_account_email :noindex:` |  `str`   
Optional. The service account to use to write to Cloud Storage. The subscription creator or updater that specifies this field must have `iam.serviceAccounts.actAs` permission on the service account. If not specified, the Pub/Sub `service agent   
  
## Classes 

### AvroConfig
    
    
    AvroConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for writing message data in Avro format. Message payloads and metadata will be written to files as an Avro binary.

### State
    
    
    State(value)

Possible states for a Cloud Storage subscription.

### TextConfig
    
    
    TextConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for writing message data in text format. Message payloads will be written to files as raw text, separated by a newline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
