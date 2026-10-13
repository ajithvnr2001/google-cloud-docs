---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/search_user_login_lockouts/
title: Search User Login Lockouts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:20.662371+00:00
---

# Search User Login Lockouts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/search_user_login_lockouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Search User Login Lockouts Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Search currently locked-out users.

## Request

GET /user_login_lockouts/search 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Include only these fields in the response

page

integer 

DEPRECATED. Use limit and offset instead. Return only page N of paginated results

per_page

integer 

DEPRECATED. Use limit and offset instead. Return N rows of data per page

limit

integer 

Number of results to return. (used with offset and takes priority over page and per_page)

offset

integer 

Number of results to skip before returning any. (used with limit and takes priority over page and per_page)

sorts

string 

Fields to sort by.

auth_type

string 

Auth type user is locked out for (email, ldap, totp, api)

full_name

string 

Match name

email

string 

Match email

remote_id

string 

Match remote LDAP ID

filter_or

boolean 

Combine given search criteria in a boolean OR expression

## Response

### 200: User Login Lockout

Datatype

Description

(array)

[UserLoginLockout](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserLoginLockout)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

key

_lock_

string 

Hash of user's client id

auth_type

_lock_

string 

Authentication method for login failures

ip

_lock_

string 

IP address of most recent failed attempt

user_id

_lock_

string 

User ID

remote_id

_lock_

string 

Remote ID of user if using LDAP

full_name

_lock_

string 

User's name

email

_lock_

string 

Email address associated with the user's account

fail_count

_lock_

integer 

Number of failures that triggered the lockout

lockout_at

_lock_

string 

Time when lockout was triggered

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
