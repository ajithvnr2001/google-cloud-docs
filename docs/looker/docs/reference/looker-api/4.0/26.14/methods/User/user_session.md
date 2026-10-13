---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/User/user_session/
title: Get Web Login Session \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:47.184471+00:00
---

# Get Web Login Session  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/User/user_session/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get Web Login Session Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Web login session for the specified user.

## Request

GET /users/{user_id}/sessions/{session_id} 

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

session_id

string 

Id of Web Login Session

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Web Login Session

Datatype

Description

(object)

[Session](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Session)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

ip_address

_lock_

string 

IP address of user when this session was initiated

browser

_lock_

string 

User's browser type

operating_system

_lock_

string 

User's Operating System

city

_lock_

string 

City component of user location (derived from IP address)

state

_lock_

string 

State component of user location (derived from IP address)

country

_lock_

string 

Country component of user location (derived from IP address)

credentials_type

_lock_

string 

Type of credentials used for logging in this session

extended_at

_lock_

string 

Time when this session was last extended by the user

extended_count

_lock_

integer 

Number of times this session was extended

sudo_user_id

_lock_

string 

Actual user in the case when this session represents one user sudo'ing as another

created_at

_lock_

string 

Time when this session was initiated

expires_at

_lock_

string 

Time when this session will expire

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
