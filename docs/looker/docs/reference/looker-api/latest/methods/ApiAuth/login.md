---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login/
title: Login \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:07.513628+00:00
---

# Login  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Login Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Present client credentials to obtain an authorization token

Looker API implements the OAuth2 [Resource Owner Password Credentials Grant](https://docs.cloud.google.com/looker/docs/r/api/outh2_resource_owner_pc) pattern. The client credentials required for this login must be obtained by creating an API key on a user account in the Looker Admin console. The API key consists of a public `client_id` and a private `client_secret`.

The access token returned by `login` must be used in the HTTP Authorization header of subsequent API requests, like this:
    
    
    Authorization: token 4QDkCyCtZzYgj4C2p2cj3csJH7zqS5RzKs2kTnG4
    

Replace "4QDkCy..." with the `access_token` value returned by `login`. The word `token` is a string literal and must be included exactly as shown.

Example of passing credentials in the HTTP request body:
    
    
    POST HTTP /login
    Content-Type: application/x-www-form-urlencoded
    
    client_id=CGc9B7v7J48dQSJvxxx&client_secret=nNVS9cSS3xNpSC9JdsBvvvvv
    

_NOTICE_

Pass 'client_id' and 'client_secret' as body parameters.

The ability to use query parameters for `client_id` and `client_secret` will be deprecated before the end of 2026.

## Request

POST /login 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

client_id

string 

client_id part of API Key.

client_secret

string 

client_secret part of API Key.

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
