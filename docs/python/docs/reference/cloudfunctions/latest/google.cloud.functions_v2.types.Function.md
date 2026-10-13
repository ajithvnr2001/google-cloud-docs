---
url: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function
title: Class Function (1.25.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:06.872336+00:00
---

# Class Function (1.25.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Function (1.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.0 (latest)  1.24.0  1.23.0  1.22.0  1.21.0  1.20.4  1.19.0  1.18.1  1.16.5  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.0  1.8.3  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.1  1.0.4  0.7.2  0.6.1  0.5.1  0.4.0  0.1.0 
    
    
    Function(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulates function and trigger configurations.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*`  
`description` |  `str`   
User-provided description of a function.   
`build_config` |  `[google.cloud.functions_v2.types.BuildConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.BuildConfig)`   
Describes the Build step of the function that builds a container from the given source.   
`service_config` |  `[google.cloud.functions_v2.types.ServiceConfig](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.ServiceConfig)`   
Describes the Service being deployed. Currently deploys services to Cloud Run (fully managed).   
`event_trigger` |  `[google.cloud.functions_v2.types.EventTrigger](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.EventTrigger)`   
An Eventarc trigger managed by Google Cloud Functions that fires events in response to a condition in another service.   
`state` |  `[google.cloud.functions_v2.types.Function.State](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Function.State)`   
Output only. State of the function.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last update timestamp of a Cloud Function.   
`labels` |  `MutableMapping[str, str]`   
Labels associated with this Cloud Function.   
`state_messages` |  `MutableSequence[[google.cloud.functions_v2.types.StateMessage](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.StateMessage)]`   
Output only. State Messages for this Cloud Function.   
`environment` |  `[google.cloud.functions_v2.types.Environment](https://docs.cloud.google.com/python/docs/reference/cloudfunctions/latest/google.cloud.functions_v2.types.Environment)`   
Describe whether the function is 1st Gen or 2nd Gen.   
`url` |  `str`   
Output only. The deployed url for the function.   
`kms_key_name` |  `str`   
Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The create timestamp of a Cloud Function. This is only applicable to 2nd Gen functions.   
  
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
  
### State
    
    
    State(value)

Describes the current state of the function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
