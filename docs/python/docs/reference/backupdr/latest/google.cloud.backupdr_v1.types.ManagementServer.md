---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer
title: Class ManagementServer (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:04.831814+00:00
---

# Class ManagementServer (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ManagementServer (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    ManagementServer(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ManagementServer describes a single BackupDR ManagementServer instance.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. The resource name.   
`description` |  `str`   
Optional. The description of the ManagementServer instance (2048 characters or less).   
`labels` |  `MutableMapping[str, str]`   
Optional. Resource labels to represent user provided metadata. Labels currently defined: 1\. migrate_from_go=  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated.   
`type_` |  `[google.cloud.backupdr_v1.types.ManagementServer.InstanceType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer.InstanceType)`   
Optional. The type of the ManagementServer resource.   
`management_uri` |  `[google.cloud.backupdr_v1.types.ManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementURI)`   
Output only. The hostname or ip address of the exposed AGM endpoints, used by clients to connect to AGM/RD graphical user interface and APIs.   
`workforce_identity_based_management_uri` |  `[google.cloud.backupdr_v1.types.WorkforceIdentityBasedManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedManagementURI)`   
Output only. The hostnames of the exposed AGM endpoints for both types of user i.e. 1p and 3p, used to connect AGM/RM UI.   
`state` |  `[google.cloud.backupdr_v1.types.ManagementServer.InstanceState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer.InstanceState)`   
Output only. The ManagementServer state.   
`networks` |  `MutableSequence[[google.cloud.backupdr_v1.types.NetworkConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkConfig)]`   
Optional. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. This field is optional if MS is created without PSA   
`etag` |  `str`   
Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other.   
`oauth2_client_id` |  `str`   
Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the 'aud' field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken).   
`workforce_identity_based_oauth2_client_id` |  `[google.cloud.backupdr_v1.types.WorkforceIdentityBasedOAuth2ClientID](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedOAuth2ClientID)`   
Output only. The OAuth client IDs for both types of user i.e. 1p and 3p.   
`ba_proxy_uri` |  `MutableSequence[str]`   
Output only. The hostname or ip address of the exposed AGM endpoints, used by BAs to connect to BA proxy.   
`satisfies_pzs` |  `google.protobuf.wrappers_pb2.BoolValue`   
Output only. Reserved for future use.   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use.   
  
## Classes 

### InstanceState
    
    
    InstanceState(value)

State of Management server instance.

### InstanceType
    
    
    InstanceType(value)

Type of backup service resource.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
