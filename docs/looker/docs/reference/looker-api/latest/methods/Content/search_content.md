---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/search_content/
title: Search Content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:39.077851+00:00
---

# Search Content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/search_content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Search Content Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Search across looks, dashboards, and lookml dashboards. The terms field will be matched against the

title and description of the content and the closest results are returned. Content that has been frequently viewed and those pieces of content stored in public folders will be ranked more highly in the results.

This endpoint does not return a full description of these content types. For more specific information about each type please refer to the individual content specific API endpoints.

Get the **full details** of a specific dashboard (or lookml dashboard) by id with [dashboard()](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard) Get the **full details** of a specific look by id with [look()](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/look)

## Request

GET /content/{terms} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

terms

string 

Search terms

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

types

string 

Content types requested (dashboard, look, lookml_dashboard).

limit

integer 

Number of results to return. (used with offset and takes priority over page and per_page)

offset

integer 

Number of results to skip before returning any. (used with limit and takes priority over page and per_page)

page

integer 

DEPRECATED. Use limit and offset instead. Return only page N of paginated results

per_page

integer 

DEPRECATED. Use limit and offset instead. Return N rows of data per page

## Response

### 200: Matching content

Datatype

Description

(array)

[ContentSearch](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentSearch)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

content_id

_lock_

string 

Primary id associated with the content

type

_lock_

string 

Type of content

title

_lock_

string 

Content title

description

_lock_

string 

Content description

folder_id

_lock_

string 

Id of the folder where the content is saved

folder_name

_lock_

string 

Name of the folder where the content is saved

view_count

_lock_

integer 

Number of times the content has been viewed

preferred_viewer

_lock_

string 

Preferred way of viewing the content (only applies to dashboards)

model

_lock_

string 

Name of the model the explore belongs to

created_by_id

_lock_

integer 

Creator Id of the content

certification_status

_lock_

string 

Certification status of the content

parent_folder_name

_lock_

string 

Name of the parent folder of the content

parent_project_name

_lock_

string 

Name of the parent project of the content

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
