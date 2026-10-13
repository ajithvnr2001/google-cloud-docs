---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/versions/
title: Get ApiVersion \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:30.438191+00:00
---

# Get ApiVersion  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get ApiVersion Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get information about all API versions supported by this Looker instance.

## Request

GET /versions 

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

### 200: ApiVersion

Datatype

Description

(object)

[ApiVersion](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ApiVersion)

looker_release_version

_lock_

string 

Current Looker release version number

current_version

_lock_

[ApiVersionElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ApiVersionElement)

Current version for this Looker instance

Expand ApiVersionElement definition... 

version

_lock_

string 

Version number as it appears in '/api/xxx/' urls

full_version

_lock_

string 

Full version number including minor version

status

_lock_

string 

Status of this version

swagger_url

_lock_

string 

Url for swagger.json for this version

supported_versions

[ApiVersionElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ApiVersionElement)[] 

Expand ApiVersionElement definition... 

version

_lock_

string 

Version number as it appears in '/api/xxx/' urls

full_version

_lock_

string 

Full version number including minor version

status

_lock_

string 

Status of this version

swagger_url

_lock_

string 

Url for swagger.json for this version

api_server_url

_lock_

string 

API server base url

web_server_url

_lock_

string 

Web server base url

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

### TSX

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-api-explorer/src/ExtensionApiExplorer.tsx ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-api-explorer/src/ExtensionApiExplorer.tsx#L45 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-api-explorer/src/ExtensionApiExplorer.tsx")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
