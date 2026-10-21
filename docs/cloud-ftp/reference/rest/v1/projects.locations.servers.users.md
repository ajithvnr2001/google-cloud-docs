---
url: https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users
title: REST Resource: projects.locations.servers.users \u00a0|\u00a0 Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:43.068961+00:00
---

# REST Resource: projects.locations.servers.users  |  Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ APIs & Reference ](https://docs.cloud.google.com/cloud-ftp/apis)



Send feedback 

#  REST Resource: projects.locations.servers.users Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: User
    * JSON representation
  * State
  * UserCredential
    * JSON representation
  * Type
  * StorageDirectoryMapping
    * JSON representation
  * Permission
  * Methods



## Resource: User

Message describing User object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "username": string,
      "customerServiceAccount": string,
      "state": enum ([State](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#State)),
      "userCredentials": [
        {
          object ([UserCredential](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#UserCredential))
        }
      ],
      "storageDirectoryMappings": [
        {
          object ([StorageDirectoryMapping](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#StorageDirectoryMapping))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. User-friendly name via which User will be identified. projects/{project}/locations/{location}/servers/{server}/users/{user}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`username` |  `string` Output only. [Output only] The username of the user.  
`customerServiceAccount` |  `string` Required. Service account in customer project attached to this SFTP User.  
`state` |  `enum (`[State](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#State)`)` Output only. Tracks user creation.  
`userCredentials[]` |  `object (`[UserCredential](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#UserCredential)`)` Required. User credential for the user. The maximum number of user credentials is 10.  
`storageDirectoryMappings[]` |  `object (`[StorageDirectoryMapping](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#StorageDirectoryMapping)`)` Required. Mapping of Cloud Storage buckets to directories where the user will land in the SFTP server.  
  
## State

Tracks user creation.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`CREATING` | User is being created.  
`ACTIVE` | User is ready to be used.  
`ERROR` | User creation failed.  
`UPDATING` | The resource is being updated.  
`DELETING` | The resource is being deleted.  
  
## UserCredential

Message describing UserCredential object

JSON representation  
---  
      
    
    {
      "credentialName": string,
      "credentialType": enum ([Type](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#Type)),
      "sshPublicKeyBody": string
    }  
  
Fields  
---  
`credentialName` |  `string` Required. Name of the user credential.  
`credentialType` |  `enum (`[Type](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#Type)`)` Required. Type of credential.  
`sshPublicKeyBody` |  `string` Optional. SSH public key body in OpenSSH format. Example: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ..."  
  
## Type

Type of credential.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`PUBLIC_KEY` | Public key credential.  
  
## StorageDirectoryMapping

Mapping of backing Cloud Storage path to the directory where the user lands in the SFTP server. If directory is not specified, it'll default to '/'.

Eg 1 - (bucket_name: bucket, bucketPrefix: path1/path2, directory: /abc/def/username)

The user will land at /abcd/def/username, and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1' and there will be no such directory in the view.

Eg 2 - (bucket_name: bucket, bucketPrefix: path1/path2, directory: '')

The user will land at '/', and the view there will match that of /bucket/path1/path2. The user will not be aware of Cloud Storage prefix '/bucket/path1/path2' and there will be no such directory in the view.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "bucketPrefix": string,
      "directory": string,
      "permission": enum ([Permission](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#Permission))
    }  
  
Fields  
---  
`bucket` |  `string` Required. Name of the bucket.  
`bucketPrefix` |  `string` Optional. Prefix inside the bucket.  
`directory` |  `string` Required. Directory where the user lands in the SFTP server.  
`permission` |  `enum (`[Permission](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users#Permission)`)` Required. Permission to the bucket.  
  
## Permission

Tracks read/write access to the bucket.

Enums  
---  
`PERMISSION_UNSPECIFIED` | Permission unspecified.  
`READ_ONLY` | Read only permission.  
`READ_WRITE` | Read write permission.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/create)`

|  Creates a new User in a given project and location and Server.  
  
### `[delete](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/delete)`

|  Deletes a single User.  
  
### `[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/get)`

|  Gets details of a single User.  
  
### `[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/list)`

|  Lists Users in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers.users/patch)`

|  Updates the parameters of a single User.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
