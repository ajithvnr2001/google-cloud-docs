---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/User/create_embed_user/
title: Create an embed user from an external user ID \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:28.806570+00:00
---

# Create an embed user from an external user ID  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/User/create_embed_user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create an embed user from an external user ID Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Create an embed user from an external user ID

**NOTE** : Calls to this endpoint require [Embedding](https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed) to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.

## Request

POST /users/embed_user 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[CreateEmbedUserRequest](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/CreateEmbedUserRequest)

Expand CreateEmbedUserRequest definition... 

external_user_id

string 

## Response

### 200: Created embed user

Datatype

Description

(object)

[UserPublic](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/UserPublic)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

first_name

_lock_

string 

First Name

last_name

_lock_

string 

Last Name

display_name

_lock_

string 

Full name for display (available only if both first_name and last_name are set)

avatar_url

_lock_

string 

URL for the avatar image (may be generic)

url

_lock_

string 

Link to get this item

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
