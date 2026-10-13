---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Content/search_content_favorites/
title: Search Favorite Contents \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:28.758676+00:00
---

# Search Favorite Contents  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Content/search_content_favorites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Search Favorite Contents Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Search Favorite Content

If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match _all_ search param criteria will be returned.

If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.

String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example="dan%" will match "danger" and "Danzig" but not "David" example="D_m%" will match "Damage" and "dump"

Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.

Most search params can accept "IS NULL" and "NOT NULL" as special expressions to match or exclude (respectively) rows where the column is null.

Boolean search params accept only "true" and "false" as values.

## Request

GET /content_favorite/search 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

id

string 

Match content favorite id(s)

user_id

string 

Match user id(s). To create a list of multiple ids, use commas as separators

content_metadata_id

string 

Match content metadata id(s). To create a list of multiple ids, use commas as separators

dashboard_id

string 

Match dashboard id(s). To create a list of multiple ids, use commas as separators

look_id

string 

Match look id(s). To create a list of multiple ids, use commas as separators

board_id

string 

Match board id(s). To create a list of multiple ids, use commas as separators

lookml_dashboard_id

string 

Match lookml dashboard id(s). To create a list of multiple ids, use commas as separators

include_board_items

boolean 

If true, and board_id is provided, returns the content favorites for all items on the board. If false, returns the content favorite for the board itself.

limit

integer 

Number of results to return. (used with offset)

offset

integer 

Number of results to skip before returning any. (used with limit)

sorts

string 

Fields to sort by.

fields

string 

Requested fields.

filter_or

boolean 

Combine given search criteria in a boolean OR expression

## Response

### 200: Favorite Content

Datatype

Description

(array)

[ContentFavorite](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ContentFavorite)[] 

id

_lock_

string 

Unique Id

user_id

string 

User Id which owns this ContentFavorite

content_metadata_id

string 

Content Metadata Id associated with this ContentFavorite

look_id

_lock_

string 

Id of a look

dashboard_id

_lock_

string 

Id of a dashboard

look

_lock_

[LookBasic](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookBasic)

Associated Look

Expand LookBasic definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

content_metadata_id

_lock_

string 

Id of content metadata

id

_lock_

string 

Unique Id

title

_lock_

string 

Look Title

user_id

string 

User Id

certification_metadata

_lock_

[Certification](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Certification)

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

dashboard

_lock_

[DashboardBase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DashboardBase)

Associated Dashboard

Expand DashboardBase definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

content_favorite_id

_lock_

string 

Content Favorite Id

content_metadata_id

_lock_

string 

Id of content metadata

description

_lock_

string 

Description

hidden

_lock_

boolean 

Is Hidden

id

_lock_

string 

Unique Id

model

_lock_

[LookModel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookModel)

Model

Expand LookModel definition... 

id

_lock_

string 

Model Id

label

_lock_

string 

Model Label

query_timezone

_lock_

string 

Timezone in which the Dashboard will run by default.

readonly

_lock_

boolean 

Is Read-only

refresh_interval

_lock_

string 

Refresh Interval, as a time duration phrase like "2 hours 30 minutes". A number with no time units will be interpreted as whole seconds.

refresh_interval_to_i

_lock_

integer 

Refresh Interval in milliseconds

folder

_lock_

[FolderBase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/FolderBase)

Folder

Expand FolderBase definition... 

name

string 

Unique Name

parent_id

string 

Id of Parent. If the parent id is null, this is a root-level entry

id

_lock_

string 

Unique Id

content_metadata_id

_lock_

string 

Id of content metadata

created_at

_lock_

string 

Time the folder was created

creator_id

_lock_

string 

User Id of Creator

child_count

_lock_

integer 

Children Count

external_id

_lock_

string 

Embedder's Id if this folder was autogenerated as an embedding shared folder via 'external_group_id' in an SSO embed login

is_embed

_lock_

boolean 

Folder is an embed folder

is_embed_shared_root

_lock_

boolean 

Folder is the root embed shared folder

is_embed_users_root

_lock_

boolean 

Folder is the root embed users folder

is_personal

_lock_

boolean 

Folder is a user's personal folder

is_personal_descendant

_lock_

boolean 

Folder is descendant of a user's personal folder

is_shared_root

_lock_

boolean 

Folder is the root shared folder

is_users_root

_lock_

boolean 

Folder is the root user folder

can

_lock_

object 

Operations the current user is able to perform on this object

title

_lock_

string 

Dashboard Title

user_id

_lock_

string 

Id of User

slug

_lock_

string 

Content Metadata Slug

preferred_viewer

_lock_

string 

The preferred route for viewing this dashboard (ie: dashboards or dashboards-next)

certification_metadata

_lock_

[Certification](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Certification)

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

board_id

_lock_

string 

Id of a board

lookml_dashboard_id

_lock_

string 

Id of a lookml dashboard

lookml_dashboard

_lock_

[DashboardBase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DashboardBase)

Associated LookML Dashboard

Expand DashboardBase definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

content_favorite_id

_lock_

string 

Content Favorite Id

content_metadata_id

_lock_

string 

Id of content metadata

description

_lock_

string 

Description

hidden

_lock_

boolean 

Is Hidden

id

_lock_

string 

Unique Id

model

_lock_

[LookModel](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookModel)

Model

Expand LookModel definition... 

id

_lock_

string 

Model Id

label

_lock_

string 

Model Label

query_timezone

_lock_

string 

Timezone in which the Dashboard will run by default.

readonly

_lock_

boolean 

Is Read-only

refresh_interval

_lock_

string 

Refresh Interval, as a time duration phrase like "2 hours 30 minutes". A number with no time units will be interpreted as whole seconds.

refresh_interval_to_i

_lock_

integer 

Refresh Interval in milliseconds

folder

_lock_

[FolderBase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/FolderBase)

Folder

Expand FolderBase definition... 

name

string 

Unique Name

parent_id

string 

Id of Parent. If the parent id is null, this is a root-level entry

id

_lock_

string 

Unique Id

content_metadata_id

_lock_

string 

Id of content metadata

created_at

_lock_

string 

Time the folder was created

creator_id

_lock_

string 

User Id of Creator

child_count

_lock_

integer 

Children Count

external_id

_lock_

string 

Embedder's Id if this folder was autogenerated as an embedding shared folder via 'external_group_id' in an SSO embed login

is_embed

_lock_

boolean 

Folder is an embed folder

is_embed_shared_root

_lock_

boolean 

Folder is the root embed shared folder

is_embed_users_root

_lock_

boolean 

Folder is the root embed users folder

is_personal

_lock_

boolean 

Folder is a user's personal folder

is_personal_descendant

_lock_

boolean 

Folder is descendant of a user's personal folder

is_shared_root

_lock_

boolean 

Folder is the root shared folder

is_users_root

_lock_

boolean 

Folder is the root user folder

can

_lock_

object 

Operations the current user is able to perform on this object

title

_lock_

string 

Dashboard Title

user_id

_lock_

string 

Id of User

slug

_lock_

string 

Content Metadata Slug

preferred_viewer

_lock_

string 

The preferred route for viewing this dashboard (ie: dashboards or dashboards-next)

certification_metadata

_lock_

[Certification](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Certification)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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
