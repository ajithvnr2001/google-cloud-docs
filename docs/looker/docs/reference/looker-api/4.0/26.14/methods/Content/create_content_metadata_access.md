---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Content/create_content_metadata_access/
title: Create Content Metadata Access \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:50.037792+00:00
---

# Create Content Metadata Access  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Content/create_content_metadata_access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create Content Metadata Access Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Create content metadata access.

## Request

POST /content_metadata_access 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[ContentMetaGroupUser](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ContentMetaGroupUser)

Content Metadata Access

Expand ContentMetaGroupUser definition... 

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

query

HTTP Query 

Expand HTTP Query definition... 

send_boards_notification_email

boolean 

Optionally sends notification email when granting access to a board.

## Response

### 200: Content Metadata Access

Datatype

Description

(object)

[ContentMetaGroupUser](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ContentMetaGroupUser)

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

### 409: Resource Already Exists

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

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ValidationErrorDetail)[] 

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
