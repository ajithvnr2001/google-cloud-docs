---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation
title: Class Curation (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:33.658710+00:00
---

# Class Curation (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Curation (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    Curation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A curation resource in the API Hub.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the curation. Format: `projects/{project}/locations/{location}/curations/{curation}`  
`display_name` |  `str`   
Required. The display name of the curation.   
`description` |  `str`   
Optional. The description of the curation.   
`endpoint` |  `[google.cloud.apihub_v1.types.Endpoint](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Endpoint)`   
Required. The endpoint to be triggered for curation.   
`plugin_instance_actions` |  `MutableSequence[[google.cloud.apihub_v1.types.Curation.PluginInstanceActionID](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation.PluginInstanceActionID)]`   
Output only. The plugin instances and associated actions that are using the curation. Note: A particular curation could be used by multiple plugin instances or multiple actions in a plugin instance.   
`last_execution_state` |  `[google.cloud.apihub_v1.types.Curation.LastExecutionState](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation.LastExecutionState)`   
Output only. The last execution state of the curation.   
`last_execution_error_code` |  `[google.cloud.apihub_v1.types.Curation.ErrorCode](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Curation.ErrorCode)`   
Output only. The error code of the last execution of the curation. The error code is populated only when the last execution state is failed.   
`last_execution_error_message` |  `str`   
Output only. Error message describing the failure, if any, during the last execution of the curation.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the curation was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the curation was last updated.   
  
## Classes 

### ErrorCode
    
    
    ErrorCode(value)

The error codes for failed executions.

### LastExecutionState
    
    
    LastExecutionState(value)

The state of the last execution of the curation.

### PluginInstanceActionID
    
    
    PluginInstanceActionID(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The plugin instance and associated action that is using the curation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
