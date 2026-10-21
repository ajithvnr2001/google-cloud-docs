---
url: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users/
title: MCP Tools Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:43.891577+00:00
---

# MCP Tools Reference: cloud-sql  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  MCP Tools Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_users`

List all database users for a Cloud SQL instance.

The following code sample shows how to use `curl` to call the `list_users` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_users",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

### SqlUsersListRequest

JSON representation  
---  
      
    
    {
      "instance": string,
      "project": string,
      "location": string
    }  
  
Fields  
---  
`instance` |  `string` Database instance ID. This does not include the project ID.  
`project` |  `string` Project ID of the project that contains the instance.  
`location` |  `string` Optional. Region of the Cloud SQL instance.  
  
## Output Schema

User list response.

### UsersListResponse

JSON representation  
---  
      
    
    {
      "kind": string,
      "items": [
        {
          object ([User](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.User))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#usersList`.  
`items[]` |  `object (`[User](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.User)`)` List of user resources in the instance.  
`nextPageToken  
**(deprecated)**` |  `string` This item is deprecated!Unused.  
  
### User

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
      "type": enum ([SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user#Input.Schema.SqlUserType)),
      "iamEmail": string,
      "passwordPolicy": {
        object ([UserPasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.UserPasswordValidationPolicy))
      },
      "databaseRoles": [
        string
      ],
      "serverRoles": [
        string
      ],
    
      // Union field user_details can be only one of the following:
      "sqlserverUserDetails": {
        object ([SqlServerUserDetails](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.SqlServerUserDetails))
      }
      // End of list of possible types for union field user_details.
    
      // Union field _dual_password_type can be only one of the following:
      "dualPasswordType": enum ([DualPasswordType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.DualPasswordType))
      // End of list of possible types for union field _dual_password_type.
    
      // Union field _iam_status can be only one of the following:
      "iamStatus": enum ([IamStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.IamStatus))
      // End of list of possible types for union field _iam_status.
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#user`.  
`password` |  `string` The password for the user.  
`etag` |  `string` This field is deprecated and will be removed from a future version of the API.  
`name` |  `string` The name of the user in the Cloud SQL instance. Can be omitted for `update` because it is already specified in the URL.  
`host` |  `string` Optional. The host from which the user can connect. For `insert` operations, host defaults to an empty string. For `update` operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it's required; for a PostgreSQL or SQL Server instance, it's optional.  
`instance` |  `string` The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for `update` because it is already specified on the URL.  
`project` |  `string` The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for `update` because it is already specified on the URL.  
`type` |  `enum (`[SqlUserType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user#Input.Schema.SqlUserType)`)` The user type. It determines the method to authenticate the user during login. The default is the database's built-in user type.  
`iamEmail` |  `string` Optional. The full email for an IAM user. For normal database users, this will not be filled. Only applicable to MySQL database users.  
`passwordPolicy` |  `object (`[UserPasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.UserPasswordValidationPolicy)`)` User level password validation policy.  
`databaseRoles[]` |  `string` Optional. Role memberships of the user  
`serverRoles[]` |  `string` Optional. The server roles for the SQL Server login.  
Union field `user_details`. User details for specific database type `user_details` can be only one of the following:  
`sqlserverUserDetails` |  `object (`[SqlServerUserDetails](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.SqlServerUserDetails)`)`  
Union field `_dual_password_type`.`_dual_password_type` can be only one of the following:  
`dualPasswordType` |  `enum (`[DualPasswordType](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.DualPasswordType)`)` Dual password status for the user.  
Union field `_iam_status`.`_iam_status` can be only one of the following:  
`iamStatus` |  `enum (`[IamStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.IamStatus)`)` Indicates if a group is active or inactive for IAM database authentication.  
  
### SqlServerUserDetails

JSON representation  
---  
      
    
    {
      "disabled": boolean,
      "serverRoles": [
        string
      ]
    }  
  
Fields  
---  
`disabled` |  `boolean` Indicates if the user has been disabled.  
`serverRoles[]` |  `string` Indicates the server roles for this user.  
  
### UserPasswordValidationPolicy

JSON representation  
---  
      
    
    {
      "allowedFailedAttempts": integer,
      "passwordExpirationDuration": string,
      "enableFailedAttemptsCheck": boolean,
      "status": {
        object ([PasswordStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.PasswordStatus))
      },
      "enablePasswordVerification": boolean
    }  
  
Fields  
---  
`allowedFailedAttempts` |  `integer` Number of failed login attempts allowed before user get locked.  
`passwordExpirationDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Expiration duration after password is updated.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`enableFailedAttemptsCheck` |  `boolean` If true, failed login attempts check will be enabled.  
`status` |  `object (`[PasswordStatus](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users#Output.Schema.PasswordStatus)`)` Output only. Read-only password status.  
`enablePasswordVerification` |  `boolean` If true, the user must specify the current password before changing the password. This flag is supported only for MySQL.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### PasswordStatus

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
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### SqlUserType

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
`ENTRAID_USER` | Microsoft Entra ID user.  
  
### DualPasswordType

The type of retained password.

Enums  
---  
`DUAL_PASSWORD_TYPE_UNSPECIFIED` | The default value.  
`NO_MODIFY_DUAL_PASSWORD` | Do not update the user's dual password status.  
`NO_DUAL_PASSWORD` | No dual password usable for connecting using this user.  
`DUAL_PASSWORD` | Dual password usable for connecting using this user.  
  
### IamStatus

Indicates if a group is available for IAM database authentication.

Enums  
---  
`IAM_STATUS_UNSPECIFIED` | The default value for users that are not of type CLOUD_IAM_GROUP. Only CLOUD_IAM_GROUP users will be inactive or active. Users with an IamStatus of IAM_STATUS_UNSPECIFIED will not display whether they are active or inactive as that is not applicable to them.  
`INACTIVE` | INACTIVE indicates a group is not available for IAM database authentication.  
`ACTIVE` | ACTIVE indicates a group is available for IAM database authentication.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
