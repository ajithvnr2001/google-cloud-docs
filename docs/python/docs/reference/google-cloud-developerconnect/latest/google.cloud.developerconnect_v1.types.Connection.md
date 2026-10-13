---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection
title: Class Connection (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:42.760153+00:00
---

# Class Connection (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.Connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Connection (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    Connection(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing Connection object

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`github_config` |  `[google.cloud.developerconnect_v1.types.GitHubConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubConfig)`   
Configuration for connections to github.com. This field is a member of `oneof`_ `connection_config`.   
`github_enterprise_config` |  `[google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitHubEnterpriseConfig)`   
Configuration for connections to an instance of GitHub Enterprise. This field is a member of `oneof`_ `connection_config`.   
`gitlab_config` |  `[google.cloud.developerconnect_v1.types.GitLabConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabConfig)`   
Configuration for connections to gitlab.com. This field is a member of `oneof`_ `connection_config`.   
`gitlab_enterprise_config` |  `[google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitLabEnterpriseConfig)`   
Configuration for connections to an instance of GitLab Enterprise. This field is a member of `oneof`_ `connection_config`.   
`bitbucket_data_center_config` |  `[google.cloud.developerconnect_v1.types.BitbucketDataCenterConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketDataCenterConfig)`   
Configuration for connections to an instance of Bitbucket Data Center. This field is a member of `oneof`_ `connection_config`.   
`bitbucket_cloud_config` |  `[google.cloud.developerconnect_v1.types.BitbucketCloudConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketCloudConfig)`   
Configuration for connections to an instance of Bitbucket Clouds. This field is a member of `oneof`_ `connection_config`.   
`secure_source_manager_instance_config` |  `[google.cloud.developerconnect_v1.types.SecureSourceManagerInstanceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.SecureSourceManagerInstanceConfig)`   
Configuration for connections to an instance of Secure Source Manager. This field is a member of `oneof`_ `connection_config`.   
`http_config` |  `[google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig)`   
Optional. Configuration for connections to an HTTP service provider. This field is a member of `oneof`_ `connection_config`.   
`name` |  `str`   
Identifier. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create timestamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update timestamp   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Delete timestamp   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels as key value pairs   
`installation_state` |  `[google.cloud.developerconnect_v1.types.InstallationState](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InstallationState)`   
Output only. Installation state of the Connection.   
`disabled` |  `bool`   
Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.   
`reconciling` |  `bool`   
Output only. Set to true when the connection is being set up or updated in the background.   
`annotations` |  `MutableMapping[str, str]`   
Optional. Allows clients to store small amounts of arbitrary data.   
`etag` |  `str`   
Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
`uid` |  `str`   
Output only. A system-assigned unique identifier for the Connection.   
`crypto_key_config` |  `[google.cloud.developerconnect_v1.types.CryptoKeyConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CryptoKeyConfig)`   
Optional. The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.   
`git_proxy_config` |  `[google.cloud.developerconnect_v1.types.GitProxyConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GitProxyConfig)`   
Optional. Configuration for the git proxy feature. Enabling the git proxy allows clients to perform git operations on the repositories linked in the connection.   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
