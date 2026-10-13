---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/generate_tokens_for_cookieless_session/
title: Generate tokens for cookieless embed session \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:10.805710+00:00
---

# Generate tokens for cookieless embed session  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/generate_tokens_for_cookieless_session/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Generate tokens for cookieless embed session Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Generate api and navigation tokens for a cookieless embed session

The generate tokens endpoint is used to create new tokens of type:

  * Api token.
  * Navigation token. The generate tokens endpoint should be called every time the Looker client asks for a token (except for the first time when the tokens returned by the acquire_session endpoint should be used).



#### Embed session expiration handling

This endpoint does NOT return an error when the embed session expires. This is to simplify processing in the caller as errors can happen for non session expiration reasons. Instead the endpoint returns the session time to live in the `session_reference_token_ttl` response property. If this property contains a zero, the embed session has expired.

**NOTE** : Calls to this endpoint require [Embedding](https://docs.cloud.google.com/looker/docs/r/looker-core-feature-embed) to be enabled. Usage of this endpoint is not authorized for Looker Core Standard and Looker Core Enterprise.

## Request

PUT /embed/cookieless_session/generate_tokens 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[EmbedCookielessSessionGenerateTokens](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedCookielessSessionGenerateTokens)

Embed session reference token

Expand EmbedCookielessSessionGenerateTokens definition... 

session_reference_token

string 

Token referencing the embed session and is used to generate new authentication, navigation and api tokens.

navigation_token

string 

Token used to load and navigate between Looker pages.

api_token

string 

Token to used to call Looker APIs. 

## Response

### 200: Generated api and navigations tokens for the cookieless embed session.

Datatype

Description

(object)

[EmbedCookielessSessionGenerateTokensResponse](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedCookielessSessionGenerateTokensResponse)

navigation_token

string 

Token used to load and navigate between Looker pages.

navigation_token_ttl

integer 

Navigation token time to live in seconds.

api_token

string 

Token to used to call Looker APIs. 

api_token_ttl

integer 

Api token time to live in seconds.

session_reference_token

string 

Token referencing the embed session and is used to generate new authentication, navigation and api tokens.

session_reference_token_ttl

integer 

Session reference token time to live in seconds. Note that this is the same as actual session.

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
