---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/User/user_credentials_embed/
title: Get Embedding Credential \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:44.597993+00:00
---

# Get Embedding Credential  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/User/user_credentials_embed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get Embedding Credential Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Embed login information for the specified user.

**NOTE** : Calls to this endpoint require [Embedding](https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed) to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.

## Request

GET /users/{user_id}/credentials_embed/{credentials_embed_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

user_id

string 

Id of user

credentials_embed_id

string 

Id of Embedding Credential

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Embedding Credential

Datatype

Description

(object)

[CredentialsEmbed](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/CredentialsEmbed)

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

external_group_id

_lock_

string 

Embedder's id for a group to which this user was added during the most recent login

external_user_id

_lock_

string 

Embedder's unique id for the user

id

_lock_

string 

Unique Id

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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
