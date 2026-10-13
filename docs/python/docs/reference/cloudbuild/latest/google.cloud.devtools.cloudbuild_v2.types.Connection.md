---
url: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection
title: Class Connection (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:15.472688+00:00
---

# Class Connection (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Connection (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.1  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.3  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.2  3.23.3  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.1  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.1  3.10.0  3.9.3  3.8.3  3.7.1  3.6.0  3.5.2  3.4.0  3.3.2  3.2.1  3.1.1  3.0.2  2.0.2  1.1.2  1.0.0  0.1.0 
    
    
    Connection(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A connection to a SCM like GitHub, GitHub Enterprise, Bitbucket Data Center, Bitbucket Cloud or GitLab.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Server assigned timestamp for when the connection was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Server assigned timestamp for when the connection was updated.   
`github_config` |  `[google.cloud.devtools.cloudbuild_v2.types.GitHubConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubConfig)`   
Configuration for connections to github.com. This field is a member of `oneof`_ `connection_config`.   
`github_enterprise_config` |  `[google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig)`   
Configuration for connections to an instance of GitHub Enterprise. This field is a member of `oneof`_ `connection_config`.   
`gitlab_config` |  `[google.cloud.devtools.cloudbuild_v2.types.GitLabConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitLabConfig)`   
Configuration for connections to gitlab.com or an instance of GitLab Enterprise. This field is a member of `oneof`_ `connection_config`.   
`bitbucket_data_center_config` |  `[google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig)`   
Configuration for connections to Bitbucket Data Center. This field is a member of `oneof`_ `connection_config`.   
`bitbucket_cloud_config` |  `[google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig)`   
Configuration for connections to Bitbucket Cloud. This field is a member of `oneof`_ `connection_config`.   
`installation_state` |  `[google.cloud.devtools.cloudbuild_v2.types.InstallationState](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState)`   
Output only. Installation state of the Connection.   
`disabled` |  `bool`   
If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.   
`reconciling` |  `bool`   
Output only. Set to true when the connection is being set up or updated in the background.   
`annotations` |  `MutableMapping[str, str]`   
Allows clients to store small amounts of arbitrary data.   
`etag` |  `str`   
This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
