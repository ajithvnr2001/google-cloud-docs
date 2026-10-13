---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig
title: Class InsightsConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:09.135381+00:00
---

# Class InsightsConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InsightsConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    InsightsConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`app_hub_application` |  `str`   
Optional. The name of the App Hub Application. Format: projects/{project}/locations/{location}/applications/{application} This field is a member of `oneof`_ `insights_config_context`.   
`projects` |  `[google.cloud.developerconnect_v1.types.Projects](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Projects)`   
Optional. The projects to track with the InsightsConfig. This field is a member of `oneof`_ `insights_config_context`.   
`name` |  `str`   
Identifier. The name of the InsightsConfig. Format: projects/{project}/locations/{location}/insightsConfigs/{insightsConfig}   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create timestamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update timestamp.   
`runtime_configs` |  `MutableSequence[[google.cloud.developerconnect_v1.types.RuntimeConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig)]`   
Output only. The runtime configurations where the application is deployed.   
`artifact_configs` |  `MutableSequence[[google.cloud.developerconnect_v1.types.ArtifactConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactConfig)]`   
Optional. The artifact configurations of the artifacts that are deployed.   
`state` |  `[google.cloud.developerconnect_v1.types.InsightsConfig.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig.State)`   
Optional. Output only. The state of the InsightsConfig.   
`annotations` |  `MutableMapping[str, str]`   
Optional. User specified annotations. See https://google.aip.dev/148#annotations for more details such as format and size limitations.   
`labels` |  `MutableMapping[str, str]`   
Optional. Set of labels associated with an InsightsConfig.   
`reconciling` |  `bool`   
Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of InsightsConfig does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.   
`errors` |  `MutableSequence[google.rpc.status_pb2.Status]`   
Output only. Any errors that occurred while setting up the InsightsConfig. Each error will be in the format: `field_name: error_message`, e.g. GetAppHubApplication: Permission denied while getting App Hub application. Please grant permissions to the P4SA.   
  
## Classes 

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### State
    
    
    State(value)

The state of the InsightsConfig.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
