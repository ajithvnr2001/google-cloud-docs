---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.BackupInstanceRequest
title: Class BackupInstanceRequest (0.5.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:58.667106+00:00
---

# Class BackupInstanceRequest (0.5.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.BackupInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupInstanceRequest (0.5.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.5 (latest)  0.5.4  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    BackupInstanceRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for `BackupInstance`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a Google Cloud region.   
`ttl` |  `google.protobuf.duration_pb2.Duration`   
Optional. TTL for the backup to expire. Value range is 1 day to 100 years. If not specified, the default value is 100 years.   
`backup_id` |  `str`   
Optional. The id of the backup to be created. If not specified, the default value ([YYYYMMDDHHMMSS]\\_[Shortened Instance UID] is used. This field is a member of `oneof`_ `_backup_id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
