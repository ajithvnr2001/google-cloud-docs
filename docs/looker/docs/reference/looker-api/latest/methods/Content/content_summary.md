---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/content_summary/
title: Search Content Summaries \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:39.552510+00:00
---

# Search Content Summaries  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/content_summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Search Content Summaries Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get Content Summary

Retrieves a collection of content items related to user activity and engagement, such as recently viewed content, favorites and scheduled items.

## Request

GET /content_summary 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Comma-delimited names of fields to return in responses. Omit for all fields

limit

integer 

Number of results to return. (used with offset)

offset

integer 

Number of results to skip before returning any. (used with limit)

target_group_id

string 

Match group id

target_user_id

string 

Match user id

target_content_type

string 

Content type to match, options are: look, dashboard. Can be provided as a comma delimited list.

sorts

string 

Fields to sort by

## Response

### 200: Content Summary

Datatype

Description

(array)

[ContentSummary](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentSummary)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique id

content_type

_lock_

string 

Content type

content_id

_lock_

string 

Content id

content_slug

_lock_

string 

Content slug

content_url

_lock_

string 

Content url

title

_lock_

string 

Content title

description

_lock_

string 

Content Description

last_viewed_at

_lock_

string 

Last time viewed by current user

user_id

_lock_

string 

ID of user who created the content

user_full_name

_lock_

string 

Full name of user who created the content

is_scheduled

_lock_

boolean 

If the content is scheduled by the current user

favorite_count

_lock_

integer 

Number of favorites

view_count

_lock_

integer 

Number of views

favorite_id

_lock_

string 

Corresponding favorite id if item is favorited by current user

weighted_score

_lock_

number 

group_weighted_score

_lock_

number 

suggestion_score

_lock_

number 

preferred_viewer

_lock_

string 

The preferred route for viewing this content (ie: dashboards or dashboards-next)

certification_metadata

_lock_

[Certification](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Certification)

Certification metadata

Expand Certification definition... 

certification_status

string 

Certification status: "certified" or "revoked" Valid values are: "certified", "revoked".

ui_status

_lock_

string 

Indicates whether the underlying model is ungoverned

user_name

_lock_

string 

Display name of user who certified the content, derived from user_id

notes

string 

Certification notes

updated_at

_lock_

string 

Timestamp of certification

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
