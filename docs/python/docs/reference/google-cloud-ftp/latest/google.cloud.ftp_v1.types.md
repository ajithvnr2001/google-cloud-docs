---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types
title: Package types (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:10.169483+00:00
---

# Package types (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

API documentation for `ftp_v1.types` package.

## Classes 

### [CreateServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.CreateServerRequest)

Message for creating a Server

### [CreateUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.CreateUserRequest)

Message for creating a User

### [DeleteServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.DeleteServerRequest)

Message for deleting a Server Note: Cascading delete is not supported. Any nested User resources under this Server must be deleted before the Server itself can be deleted. Attempting to delete a Server with active User resources will result in an error.

### [DeleteUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.DeleteUserRequest)

Message for deleting a User

### [ExternalServerConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ExternalServerConfig)

Configuration for external server.

### [GetServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.GetServerRequest)

Message for getting a Server

### [GetUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.GetUserRequest)

Message for getting a User

### [InternalServerConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.InternalServerConfig)

Configuration for private server accessible via PSC.

### [ListServersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListServersRequest)

Message for requesting list of Servers

### [ListServersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListServersResponse)

Message for response to listing Servers

### [ListUsersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListUsersRequest)

Message for requesting list of Users

### [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListUsersResponse)

Message for response to listing Users

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [Server](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.Server)

Message describing Server object

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServerCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ServerCredential)

Represents credentials of an FTP Server.

### [ServerView](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ServerView)

View for Server resource.

### [StartServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.StartServerRequest)

Request message for starting a Server.

### [StopServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.StopServerRequest)

Request message for stopping a Server.

### [StorageDirectoryMapping](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.StorageDirectoryMapping)

Mapping of backing Cloud Storage path to the directory where the user lands in the SFTP server. If directory is not specified, it'll default to '/'.

Eg 1 - (bucket_name: bucket, bucket_prefix: path1/path2, directory: /abc/def/username)

The user will land at /abcd/def/username, and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1' and there will be no such directory in the view.

Eg 2 - (bucket_name: bucket, bucket_prefix: path1/path2, directory: '')

The user will land at '/', and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1/path2' and there will be no such directory in the view.

### [UpdateServerRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UpdateServerRequest)

Message for updating a Server

### [UpdateUserRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UpdateUserRequest)

Message for updating a User

### [User](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.User)

Message describing User object

### [UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UserCredential)

Message describing UserCredential object

### [UserView](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.UserView)

View for User resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
