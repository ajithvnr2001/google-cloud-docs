---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.OperationMetadata
title: Class OperationMetadata (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:45.608128+00:00
---

# Class OperationMetadata (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.OperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OperationMetadata (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    OperationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the metadata of the long-running operation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`deployment_metadata` |  `[google.cloud.config_v1.types.DeploymentOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentOperationMetadata)`   
Output only. Metadata about the deployment operation state. This field is a member of `oneof`_ `resource_metadata`.   
`preview_metadata` |  `[google.cloud.config_v1.types.PreviewOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewOperationMetadata)`   
Output only. Metadata about the preview operation state. This field is a member of `oneof`_ `resource_metadata`.   
`provision_deployment_group_metadata` |  `[google.cloud.config_v1.types.ProvisionDeploymentGroupOperationMetadata](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ProvisionDeploymentGroupOperationMetadata)`   
Output only. Metadata about ProvisionDeploymentGroup operation state. This field is a member of `oneof`_ `resource_metadata`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the operation was created.   
`end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the operation finished running.   
`target` |  `str`   
Output only. Server-defined resource path for the target of the operation.   
`verb` |  `str`   
Output only. Name of the verb executed by the operation.   
`status_message` |  `str`   
Output only. Human-readable status of the operation, if any.   
`requested_cancellation` |  `bool`   
Output only. Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have `google.longrunning.Operation.error][google.longrunning.Operation.error]` value with a `google.rpc.Status.code][google.rpc.Status.code]` of `1`, corresponding to `Code.CANCELLED`.   
`api_version` |  `str`   
Output only. API version used to start the operation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
