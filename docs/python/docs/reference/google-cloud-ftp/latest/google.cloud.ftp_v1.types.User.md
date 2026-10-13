---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.User
title: Class User (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:02.595269+00:00
---

# Class User (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.User

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class User (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    User(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing User object

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. User-friendly name via which User will be identified. projects/{project}/locations/{location}/servers/{server}/users/{user}   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update time stamp   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels as key value pairs   
`username` |  `str`   
Output only. [Output only] The username of the user.   
`customer_service_account` |  `str`   
Required. Service account in customer project attached to this SFTP User.   
`state` |  `[google.cloud.ftp_v1.types.User.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.User.State)`   
Output only. Tracks user creation.   
`user_credentials` |  `MutableSequence[[google.cloud.ftp_v1.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UserCredential)]`   
Required. User credential for the user. The maximum number of user credentials is 10.   
`storage_directory_mappings` |  `MutableSequence[[google.cloud.ftp_v1.types.StorageDirectoryMapping](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.StorageDirectoryMapping)]`   
Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.   
  
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

Tracks user creation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
