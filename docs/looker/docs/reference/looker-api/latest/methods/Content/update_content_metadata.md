---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/update_content_metadata/
title: Update Content Metadata \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:38.236351+00:00
---

# Update Content Metadata  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/update_content_metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update Content Metadata Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Move a piece of content.

## Request

PATCH /content_metadata/{content_metadata_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

content_metadata_id

string 

Id of content metadata

body

HTTP Body 

Expand HTTP Body definition... 

body

[ContentMeta](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentMeta)

Content Metadata

Expand ContentMeta definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

_lock_

string 

Name or title of underlying content

parent_id

_lock_

string 

Id of Parent Content

dashboard_id

_lock_

string 

Id of associated dashboard when content_type is "dashboard"

look_id

_lock_

string 

Id of associated look when content_type is "look"

folder_id

_lock_

string 

Id of associated folder when content_type is "space"

homepage_id

_lock_

string 

Id of associated board when content_type is "board"

agent_id

_lock_

string 

Id of associated agent when content_type is "agent"

content_type

_lock_

string 

Content Type ("dashboard", "look", or "folder")

inherits

boolean 

Whether content inherits its access levels from parent. Can be false only if the associated content is a folder, an agent or a board.

inheriting_id

_lock_

string 

Id of Inherited Content

slug

_lock_

string 

Content Slug

## Response

### 200: Content Metadata

Datatype

Description

(object)

[ContentMeta](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentMeta)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

_lock_

string 

Name or title of underlying content

parent_id

_lock_

string 

Id of Parent Content

dashboard_id

_lock_

string 

Id of associated dashboard when content_type is "dashboard"

look_id

_lock_

string 

Id of associated look when content_type is "look"

folder_id

_lock_

string 

Id of associated folder when content_type is "space"

homepage_id

_lock_

string 

Id of associated board when content_type is "board"

agent_id

_lock_

string 

Id of associated agent when content_type is "agent"

content_type

_lock_

string 

Content Type ("dashboard", "look", or "folder")

inherits

boolean 

Whether content inherits its access levels from parent. Can be false only if the associated content is a folder, an agent or a board.

inheriting_id

_lock_

string 

Id of Inherited Content

slug

_lock_

string 

Content Slug

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
