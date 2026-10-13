---
url: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session
title: Class Session (5.31.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:52.207652+00:00
---

# Class Session (5.31.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Session (5.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.31.0 (latest)  5.30.0  5.29.0  5.28.0  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.18.1  5.17.1  5.16.0  5.15.1  5.14.0  5.13.0  5.12.0  5.10.2  5.9.3  5.8.0  5.7.0  5.6.0  5.5.1  5.4.3  5.3.0  5.2.0  5.1.0  5.0.3  4.0.3  3.3.2  3.2.0  3.1.1  3.0.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.0.2  1.1.3  1.0.1  0.8.2  0.7.0  0.6.1  0.5.0 
    
    
    Session(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A representation of a session.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the session.   
`uuid` |  `str`   
Output only. A session UUID (Unique Universal Identifier). The service generates this value when it creates the session.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the session was created.   
`jupyter_session` |  `[google.cloud.dataproc_v1.types.JupyterConfig](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.JupyterConfig)`   
Optional. Jupyter session config. This field is a member of `oneof`_ `session_config`.   
`spark_connect_session` |  `[google.cloud.dataproc_v1.types.SparkConnectConfig](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.SparkConnectConfig)`   
Optional. Spark connect session config. This field is a member of `oneof`_ `session_config`.   
`runtime_info` |  `[google.cloud.dataproc_v1.types.RuntimeInfo](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.RuntimeInfo)`   
Output only. Runtime information about session execution.   
`state` |  `[google.cloud.dataproc_v1.types.Session.State](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.State)`   
Output only. A state of the session.   
`state_message` |  `str`   
Output only. Session state details, such as the failure description if the state is `FAILED`.   
`state_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the session entered the current state.   
`creator` |  `str`   
Output only. The email address of the user who created the session.   
`labels` |  `MutableMapping[str, str]`   
Optional. The labels to associate with the session. Label **keys** must contain 1 to 63 characters, and must conform to `RFC 1035 `__. Label **values** may be empty, but, if present, must contain 1 to 63 characters, and must conform to `RFC 1035   
`runtime_config` |  `[google.cloud.dataproc_v1.types.RuntimeConfig](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.RuntimeConfig)`   
Optional. Runtime configuration for the session execution.   
`environment_config` |  `[google.cloud.dataproc_v1.types.EnvironmentConfig](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.EnvironmentConfig)`   
Optional. Environment configuration for the session execution.   
`user` |  `str`   
Optional. The email address of the user who owns the session.   
`state_history` |  `MutableSequence[[google.cloud.dataproc_v1.types.Session.SessionStateHistory](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.SessionStateHistory)]`   
Output only. Historical state information for the session.   
`session_template` |  `str`   
Optional. The session template used by the session. Only resource names, including project ID and location, are valid. Example: \- `https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]` \- `projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]` The template must be in the same project and Dataproc region as the session.   
  
## Classes 

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
  
### SessionStateHistory
    
    
    SessionStateHistory(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Historical state information.

### State
    
    
    State(value)

The session state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
