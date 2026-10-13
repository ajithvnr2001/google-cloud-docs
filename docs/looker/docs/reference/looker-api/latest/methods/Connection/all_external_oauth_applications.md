---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_external_oauth_applications/
title: Get All External OAuth Applications \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:33.372490+00:00
---

# Get All External OAuth Applications  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_external_oauth_applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get All External OAuth Applications Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get all External OAuth Applications.

This is an OAuth Application which Looker uses to access external systems.

## Request

GET /external_oauth_applications 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

name

string 

Application name

client_id

string 

Application Client ID

## Response

### 200: External OAuth Application

Datatype

Description

(array)

[ExternalOauthApplication](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ExternalOauthApplication)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

ID of this OAuth Application

name

string 

The name of this application. For Snowflake connections, this should be the name of the host database.

client_id

string 

The OAuth Client ID for this application

client_secret

string 

(Write-Only) The OAuth Client Secret for this application

tenant_id

string 

The OAuth Tenant ID for this application

dialect_name

string 

The database dialect for this application.

provider

string 

The OAuth provider for this application (e.g., 'entra'). Null for standard dialect OAuth.

scopes

string 

Space-delimited OAuth scopes to request when authorizing users. Required when provider is 'entra': the Snowflake resource application's scope, e.g. 'api:///session:role-any' (offline_access is added automatically).

bi_directional_data_access

boolean 

Whether this application supports bi-directional data access.

created_at

_lock_

string 

Creation time for this application

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L230 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
