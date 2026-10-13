---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/all_content_metadata_accesses/
title: Get All Content Metadata Accesses \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:38.784411+00:00
---

# Get All Content Metadata Accesses  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/all_content_metadata_accesses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get All Content Metadata Accesses Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### All content metadata access records for a content metadata item.

## Request

GET /content_metadata_access 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

content_metadata_id

string 

Id of content metadata

fields

string 

Requested fields.

## Response

### 200: Content Metadata Access

Datatype

Description

(array)

[ContentMetaGroupUser](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentMetaGroupUser)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

content_metadata_id

_lock_

string 

Id of associated Content Metadata

permission_type

_lock_

string 

Type of permission: "view" or "edit" Valid values are: "view", "edit".

group_id

_lock_

string 

ID of associated group

user_id

_lock_

string 

ID of associated user

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

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/folder_permission_access.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/folder_permission_access.py#L50 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/folder_permission_access.py")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
