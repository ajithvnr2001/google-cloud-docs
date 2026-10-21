---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/
title: REST Resource: users \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:37.560223+00:00
---

# REST Resource: users  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  REST Resource: users Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: User
    * JSON representation
  * SqlUserType
  * UserPasswordValidationPolicy
    * JSON representation
  * PasswordStatus
    * JSON representation
  * DualPasswordType
  * IamStatus
  * Methods



## Resource: User

A Cloud SQL user resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "password": string,
      "etag": string,
      "name": string,
      "host": string,
      "instance": string,
      "project": string,
      "type": enum ([SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#SqlUserType)),
      "passwordPolicy": {
        object ([UserPasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#UserPasswordValidationPolicy))
      },
      "databaseRoles": [
        string
      ],
      "dualPasswordType": enum ([DualPasswordType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#DualPasswordType)),
      "iamStatus": enum ([IamStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#IamStatus))
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#user`.  
`password` |  `string` The password for the user.  
`etag` |  `string` This field is deprecated and will be removed from a future version of the API.  
`name` |  `string` The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.  
`host` |  `string` Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.  
`instance` |  `string` The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for **update** because it is already specified on the URL.  
`project` |  `string` The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for **update** because it is already specified on the URL.  
`type` |  `enum (`[SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#SqlUserType)`)` The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.  
`passwordPolicy` |  `object (`[UserPasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#UserPasswordValidationPolicy)`)` User level password validation policy.  
`databaseRoles[]` |  `string` Optional. Role memberships of the user  
`dualPasswordType` |  `enum (`[DualPasswordType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#DualPasswordType)`)` Dual password status for the user.  
`iamStatus` |  `enum (`[IamStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#IamStatus)`)` Indicates if a group is active or inactive for IAM database authentication.  
  
## SqlUserType

The user type.

Enums  
---  
`BUILT_IN` | The database's built-in user type.  
`CLOUD_IAM_USER` | Cloud IAM user.  
`CLOUD_IAM_SERVICE_ACCOUNT` | Cloud IAM service account.  
`CLOUD_IAM_GROUP` | Cloud IAM group. Not used for login.  
`CLOUD_IAM_GROUP_USER` | Read-only. Login for a user that belongs to the Cloud IAM group.  
`CLOUD_IAM_GROUP_SERVICE_ACCOUNT` | Read-only. Login for a service account that belongs to the Cloud IAM group.  
`CLOUD_IAM_WORKFORCE_IDENTITY` | Cloud IAM workforce identity managed by Workforce Identity Federation.  
  
## UserPasswordValidationPolicy

User level password validation policy.

JSON representation  
---  
      
    
    {
      "allowedFailedAttempts": integer,
      "passwordExpirationDuration": string,
      "enableFailedAttemptsCheck": boolean,
      "status": {
        object ([PasswordStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#PasswordStatus))
      },
      "enablePasswordVerification": boolean
    }  
  
Fields  
---  
`allowedFailedAttempts` |  `integer` Number of failed login attempts allowed before user get locked.  
`passwordExpirationDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Expiration duration after password is updated.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`enableFailedAttemptsCheck` |  `boolean` If true, failed login attempts check will be enabled.  
`status` |  `object (`[PasswordStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users#PasswordStatus)`)` Output only. Read-only password status.  
`enablePasswordVerification` |  `boolean` If true, the user must specify the current password before changing the password. This flag is supported only for MySQL.  
  
## PasswordStatus

Read-only password status.

JSON representation  
---  
      
    
    {
      "locked": boolean,
      "passwordExpirationTime": string
    }  
  
Fields  
---  
`locked` |  `boolean` If true, user does not have login privileges.  
`passwordExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The expiration time of the current password.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## DualPasswordType

The type of retained password.

Enums  
---  
`DUAL_PASSWORD_TYPE_UNSPECIFIED` | The default value.  
`NO_MODIFY_DUAL_PASSWORD` | Do not update the user's dual password status.  
`NO_DUAL_PASSWORD` | No dual password usable for connecting using this user.  
`DUAL_PASSWORD` | Dual password usable for connecting using this user.  
  
## IamStatus

Indicates if a group is available for IAM database authentication.

Enums  
---  
`IAM_STATUS_UNSPECIFIED` | The default value for users that are not of type CLOUD_IAM_GROUP. Only CLOUD_IAM_GROUP users will be inactive or active. Users with an IamStatus of IAM_STATUS_UNSPECIFIED will not display whether they are active or inactive as that is not applicable to them.  
`INACTIVE` | INACTIVE indicates a group is not available for IAM database authentication.  
`ACTIVE` | ACTIVE indicates a group is available for IAM database authentication.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/delete)`

|  Deletes a user from a Cloud SQL instance.  
  
### `[get](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/get)`

|  Retrieves a resource containing information about a user.  
  
### `[insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/insert)`

|  Creates a new user in a Cloud SQL instance.  
  
### `[list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/list)`

|  Lists users in the specified Cloud SQL instance.  
  
### `[update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update)`

|  Updates an existing user in a Cloud SQL instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
