---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionFailureEvent.CloudStorageFailure
title: Class CloudStorageFailure (2.42.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:56.377228+00:00
---

# Class CloudStorageFailure (2.42.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionFailureEvent.CloudStorageFailure

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudStorageFailure (2.42.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.2  2.38.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.3  2.26.1  2.25.2  2.23.1  2.22.0  2.21.5  2.20.3  2.19.8  2.18.4  2.17.1  2.16.1  2.15.2  2.14.1  2.13.12  2.12.1  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.1  2.5.0  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.7.2  1.6.1  1.5.0  1.4.3  1.3.1  1.2.0  1.1.0  1.0.2  0.45.0  0.44.0  0.43.0 
    
    
    CloudStorageFailure(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Failure when ingesting from a Cloud Storage source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`bucket :noindex:` |  `str`   
Optional. Name of the Cloud Storage bucket used for ingestion.   
`object_name :noindex:` |  `str`   
Optional. Name of the Cloud Storage object which contained the section that couldn't be ingested.   
`object_generation :noindex:` |  `int`   
Optional. Generation of the Cloud Storage object which contained the section that couldn't be ingested.   
`avro_failure_reason :noindex:` |  `google.pubsub_v1.types.IngestionFailureEvent.AvroFailureReason`   
Optional. Failure encountered when parsing an Avro file. This field is a member of `oneof`_ `reason`.   
`api_violation_reason :noindex:` |  `google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason`   
Optional. The Pub/Sub API limits prevented the desired message from being published. This field is a member of `oneof`_ `reason`.   
`schema_violation_reason :noindex:` |  `google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason`   
Optional. The Pub/Sub message failed schema validation. This field is a member of `oneof`_ `reason`.   
`message_transformation_failure_reason :noindex:` |  `google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason`   
Optional. Failure encountered when applying a message transformation to the Pub/Sub message. This field is a member of `oneof`_ `reason`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
