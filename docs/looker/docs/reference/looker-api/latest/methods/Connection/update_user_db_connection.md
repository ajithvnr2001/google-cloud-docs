---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/update_user_db_connection/
title: Update User DB Connection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:36.266643+00:00
---

# Update User DB Connection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/update_user_db_connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update User DB Connection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update User DB Connection

Updates an existing user DB connection (only enabling/disabling is allowed via the write limits in UserDbConnectionMapper).

## Request

PATCH /user_db_connections/{user_db_connection_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

user_db_connection_id

string 

Id of user DB connection

body

HTTP Body 

Expand HTTP Body definition... 

body

[UserDbConnection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserDbConnection)

User DB Connection

Expand UserDbConnection definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

ID of the connection

name

_lock_

string 

Name of the connection (must match virtual namespace pattern)

label

_lock_

string 

User-specified display label for the connection

user_id

_lock_

integer 

ID of the user who owns the connection

dialect

_lock_

string 

Database dialect name

auth_type

_lock_

string 

Authentication type (oauth, service_account, password)

host

_lock_

string 

Host name/address of server

port

_lock_

string 

Port number on server

database

_lock_

string 

Database name

schema

_lock_

string 

Schema name

jdbc_additional_params

_lock_

string 

Additional JDBC parameters

oauth_application_id

_lock_

integer 

OAuth application ID (if auth_type is oauth)

enabled

boolean 

Whether this connection is enabled

created_at

_lock_

string 

When the connection was created

updated_at

_lock_

string 

When the connection was last updated

## Response

### 200: User DB Connection

Datatype

Description

(object)

[UserDbConnection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserDbConnection)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

ID of the connection

name

_lock_

string 

Name of the connection (must match virtual namespace pattern)

label

_lock_

string 

User-specified display label for the connection

user_id

_lock_

integer 

ID of the user who owns the connection

dialect

_lock_

string 

Database dialect name

auth_type

_lock_

string 

Authentication type (oauth, service_account, password)

host

_lock_

string 

Host name/address of server

port

_lock_

string 

Port number on server

database

_lock_

string 

Database name

schema

_lock_

string 

Schema name

jdbc_additional_params

_lock_

string 

Additional JDBC parameters

oauth_application_id

_lock_

integer 

OAuth application ID (if auth_type is oauth)

enabled

boolean 

Whether this connection is enabled

created_at

_lock_

string 

When the connection was created

updated_at

_lock_

string 

When the connection was last updated

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 403: Permission Denied

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
