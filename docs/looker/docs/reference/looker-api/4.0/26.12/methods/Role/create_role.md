---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Role/create_role/
title: Create Role \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:11.880274+00:00
---

# Create Role  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Role/create_role/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create Role Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Create a role with the specified information.

## Request

POST /roles 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Role)

Role

Expand Role definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of Role

permission_set

_lock_

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/PermissionSet)

(Read only) Permission set

permission_set_id

string 

(Write-Only) Id of permission set

model_set

_lock_

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ModelSet)

(Read only) Model set

model_set_id

string 

(Write-Only) Id of model set

internal

_lock_

boolean 

Is this a Looker internal role

url

_lock_

string 

Link to get this item

users_url

_lock_

string 

Link to get list of users with this role

## Response

### 200: Role

Datatype

Description

(object)

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Role)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of Role

permission_set

_lock_

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/PermissionSet)

(Read only) Permission set

Expand PermissionSet definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

all_access

_lock_

boolean 

built_in

_lock_

boolean 

id

_lock_

string 

Unique Id

name

string 

Name of PermissionSet

permissions

string[] 

url

_lock_

string 

Link to get this item

permission_set_id

string 

(Write-Only) Id of permission set

model_set

_lock_

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ModelSet)

(Read only) Model set

Expand ModelSet definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

all_access

_lock_

boolean 

built_in

_lock_

boolean 

id

_lock_

string 

Unique Id

models

string[] 

name

string 

Name of ModelSet

url

_lock_

string 

Link to get this item

model_set_id

string 

(Write-Only) Id of model set

internal

_lock_

boolean 

Is this a Looker internal role

url

_lock_

string 

Link to get this item

users_url

_lock_

string 

Link to get list of users with this role

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 405: Resource Can't Be Modified

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 409: Resource Already Exists

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationErrorDetail)[] 

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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
