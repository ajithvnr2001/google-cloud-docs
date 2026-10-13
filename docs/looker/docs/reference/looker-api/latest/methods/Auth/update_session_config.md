---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_session_config/
title: Update Session Config \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:19.411908+00:00
---

# Update Session Config  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_session_config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update Session Config Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update session config.

## Request

PATCH /session_config 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[SessionConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SessionConfig)

Session Config

Expand SessionConfig definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

allow_persistent_sessions

boolean 

Allow users to have persistent sessions when they login

session_minutes

integer 

Number of minutes for user sessions. Must be between 5 and 43200

unlimited_sessions_per_user

boolean 

Allow users to have an unbounded number of concurrent sessions (otherwise, users will be limited to only one session at a time).

use_inactivity_based_logout

boolean 

Enforce session logout for sessions that are inactive for 15 minutes.

track_session_location

boolean 

Track location of session when user logs in.

## Response

### 200: Session Config

Datatype

Description

(object)

[SessionConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SessionConfig)

can

_lock_

object 

Operations the current user is able to perform on this object

allow_persistent_sessions

boolean 

Allow users to have persistent sessions when they login

session_minutes

integer 

Number of minutes for user sessions. Must be between 5 and 43200

unlimited_sessions_per_user

boolean 

Allow users to have an unbounded number of concurrent sessions (otherwise, users will be limited to only one session at a time).

use_inactivity_based_logout

boolean 

Enforce session logout for sessions that are inactive for 15 minutes.

track_session_location

boolean 

Track location of session when user logs in.

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
