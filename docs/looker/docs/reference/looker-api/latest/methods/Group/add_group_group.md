---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Group/add_group_group/
title: Add a Group to Group \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:38.482225+00:00
---

# Add a Group to Group  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Group/add_group_group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Add a Group to Group Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Adds a new group to a group.

## Request

POST /groups/{group_id}/groups 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

group_id

string 

Id of group

body

HTTP Body 

Expand HTTP Body definition... 

body

[GroupIdForGroupInclusion](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/GroupIdForGroupInclusion)

Group id to add

Expand GroupIdForGroupInclusion definition... 

group_id

_lock_

string 

Id of group

## Response

### 200: Added group.

Datatype

Description

(object)

[Group](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Group)

can

_lock_

object 

Operations the current user is able to perform on this object

can_add_to_content_metadata

boolean 

Group can be used in content access controls

contains_current_user

_lock_

boolean 

Currently logged in user is group member

external_group_id

_lock_

string 

External Id group if embed group

externally_managed

_lock_

boolean 

Group membership controlled outside of Looker

id

_lock_

string 

Unique Id

include_by_default

_lock_

boolean 

New users are added to this group by default

name

string 

Name of group

user_count

_lock_

integer 

Number of users included in this group

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

### 403: Permission Denied

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
