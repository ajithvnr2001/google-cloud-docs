---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login_user/
title: Login user \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:08.282692+00:00
---

# Login user  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login_user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Login user Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Create an access token that runs as a given user.

This can only be called by an authenticated admin user. It allows that admin to generate a new authentication token for the user with the given user id. That token can then be used for subsequent API calls - which are then performed _as_ that target user.

The target user does _not_ need to have a pre-existing API client_id/client_secret pair. And, no such credentials are created by this call.

This allows for building systems where api user authentication for an arbitrary number of users is done outside of Looker and funneled through a single 'service account' with admin permissions. Note that a new access token is generated on each call. If target users are going to be making numerous API calls in a short period then it is wise to cache this authentication token rather than call this before each of those API calls.

See 'login' for more detail on the access token and how to use it.

In [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview) this call will be denied unless all of the following criteria are met:

  1. The calling user is an [API-only Service Account](https://docs.cloud.google.com/looker/docs/looker-core-user-management#creating_an_api-only_service_account) with the Admin role
  2. The target user is an [Embed User type](https://docs.cloud.google.com/looker/docs/r/single-sign-on-embedding) Regular user types can not be impersonated in [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview). If your application needs to call the API for these users, use OAuth authentication instead.



## Request

POST /login/{user_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

user_id

string 

Id of user.

## Response

### 200: Access token with metadata.

Datatype

Description

(object)

[AccessToken](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AccessToken)

access_token

_lock_

string 

Access Token used for API calls

token_type

_lock_

string 

Type of Token

expires_in

_lock_

integer 

Number of seconds before the token expires

refresh_token

_lock_

string 

Refresh token which can be used to obtain a new access token

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

## Examples

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L45 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
