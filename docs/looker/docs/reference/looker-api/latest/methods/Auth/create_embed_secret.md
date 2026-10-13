---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_embed_secret/
title: Create Embed Secret \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:09.409812+00:00
---

# Create Embed Secret  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_embed_secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Create Embed Secret Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Create an embed secret using the specified information.

The value of the `secret` field will be set by Looker and returned.

**NOTE** : Calls to this endpoint require [Embedding](https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed) to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.

## Request

POST /embed_config/secrets 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[EmbedSecret](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedSecret)

embed secret

Expand EmbedSecret definition... 

algorithm

string 

Signing algorithm to use with this secret. Either `hmac/sha-256`(default) or `hmac/sha-1`

created_at

_lock_

string 

When secret was created

enabled

boolean 

Is this secret currently enabled

id

_lock_

string 

Unique Id

secret

_lock_

string 

Secret for use with SSO embedding

user_id

_lock_

string 

Id of user who created this secret

secret_type

string 

Field to distinguish between SSO secrets and JWT secrets Valid values are: "SSO", "JWT".

## Response

### 200: embed secret

Datatype

Description

(object)

[EmbedSecret](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedSecret)

algorithm

string 

Signing algorithm to use with this secret. Either `hmac/sha-256`(default) or `hmac/sha-1`

created_at

_lock_

string 

When secret was created

enabled

boolean 

Is this secret currently enabled

id

_lock_

string 

Unique Id

secret

_lock_

string 

Secret for use with SSO embedding

user_id

_lock_

string 

Id of user who created this secret

secret_type

string 

Field to distinguish between SSO secrets and JWT secrets Valid values are: "SSO", "JWT".

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

### 409: Resource Already Exists

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
