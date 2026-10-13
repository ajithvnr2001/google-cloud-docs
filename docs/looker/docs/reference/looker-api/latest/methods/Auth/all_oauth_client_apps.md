---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/all_oauth_client_apps/
title: Get All OAuth Client Apps \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:13.347632+00:00
---

# Get All OAuth Client Apps  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/all_oauth_client_apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get All OAuth Client Apps Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### List All OAuth Client Apps

Lists all applications registered to use OAuth2 login with this Looker instance, including enabled and disabled apps.

Results are filtered to include only the apps that the caller (current user) has permission to see.

## Request

GET /oauth_client_apps 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: OAuth Client App

Datatype

Description

(array)

[OauthClientApp](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/OauthClientApp)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

client_guid

_lock_

string 

The globally unique id of this application

redirect_uri

string 

(DEPRECATED) The uri with which this application will receive an auth code by browser redirect. (DEPRECATED: Use redirect_uris instead)

redirect_uris

string[] 

display_name

string 

The application's display name

description

string 

A description of the application that will be displayed to users

enabled

boolean 

When enabled is true, OAuth2 and API requests will be accepted from this app. When false, all requests from this app will be refused. Setting disabled invalidates existing tokens.

group_id

string 

If set, only Looker users who are members of this group can use this web app with Looker. If group_id is not set, any Looker user may use this app to access this Looker instance

tokens_invalid_before

_lock_

string 

All auth codes, access tokens, and refresh tokens issued for this application prior to this date-time for ALL USERS will be invalid.

activated_users

[UserPublic](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserPublic)[] 

Expand UserPublic definition... 

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

is_service_account

_lock_

boolean 

Indicates if this user is a service account.

is_embed_user

_lock_

boolean 

Indicates if this user is an embed user.

url

_lock_

string 

Link to get this item

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

## Examples

### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L179 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
