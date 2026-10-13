---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_element/
title: Update DashboardElement \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:52.490000+00:00
---

# Update DashboardElement  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_element/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update DashboardElement Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update the dashboard element with a specific id.

## Request

PATCH /dashboard_elements/{dashboard_element_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

dashboard_element_id

string 

Id of dashboard element

body

HTTP Body 

Expand HTTP Body definition... 

body

[DashboardElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardElement)

DashboardElement

Expand DashboardElement definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

body_text

string 

Text tile body text

body_text_as_html

_lock_

string 

Text tile body text as Html

dashboard_id

string 

Id of Dashboard

dashboard_layout_id

string 

Id of Dashboard Layout

group_id

_lock_

string 

ID of the group to place this element under in the layout

edit_uri

_lock_

string 

Relative path of URI of LookML file to edit the dashboard element (LookML dashboard only).

id

_lock_

string 

Unique Id

look

_lock_

[LookWithQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookWithQuery)

Look

look_id

string 

Id Of Look

lookml_link_id

_lock_

string 

LookML link ID

merge_result_id

string 

ID of merge result

note_display

string 

Note Display

note_state

string 

Note State

note_text

string 

Note Text

note_text_as_html

_lock_

string 

Note Text as Html

query

_lock_

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Query)

Query

query_id

string 

Id Of Query

filter_id

string 

ID of the filter this element represents

refresh_interval

string 

Refresh Interval

refresh_interval_to_i

_lock_

integer 

Refresh Interval as integer

result_maker

[ResultMakerWithIdVisConfigAndDynamicFields](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ResultMakerWithIdVisConfigAndDynamicFields)

Data about the result maker.

result_maker_id

string 

ID of the ResultMakerLookup entry.

subtitle_text

string 

Text tile subtitle text

title

string 

Title of dashboard element

title_hidden

boolean 

Whether title is hidden

title_text

string 

Text tile title

type

string 

Type

alert_count

_lock_

integer 

Count of Alerts associated to a dashboard element

rich_content_json

string 

JSON with all the properties required for rich editor and buttons elements

title_text_as_html

_lock_

string 

Text tile title text as Html

subtitle_text_as_html

_lock_

string 

Text tile subtitle text as Html

extension_id

string 

Extension ID

aria_description

string 

Custom ARIA description text

certification_metadata

_lock_

[Certification](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Certification)

Certification metadata

image_id

string 

ID of Dashboard Image

images

[Image](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Image)[] 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: DashboardElement

Datatype

Description

(object)

[DashboardElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardElement)

can

_lock_

object 

Operations the current user is able to perform on this object

body_text

string 

Text tile body text

body_text_as_html

_lock_

string 

Text tile body text as Html

dashboard_id

string 

Id of Dashboard

dashboard_layout_id

string 

Id of Dashboard Layout

group_id

_lock_

string 

ID of the group to place this element under in the layout

edit_uri

_lock_

string 

Relative path of URI of LookML file to edit the dashboard element (LookML dashboard only).

id

_lock_

string 

Unique Id

look

_lock_

[LookWithQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookWithQuery)

Look

Expand LookWithQuery definition... 

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

string 

Look Title

user_id

string 

User Id

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

content_favorite_id

_lock_

string 

Content Favorite Id

created_at

_lock_

string 

Time that the Look was created.

deleted

boolean 

Whether or not a look is 'soft' deleted.

deleted_at

_lock_

string 

Time that the Look was deleted.

deleter_id

_lock_

string 

Id of User that deleted the look.

description

string 

Description

embed_url

_lock_

string 

Embed Url

excel_file_url

_lock_

string 

Excel File Url

favorite_count

_lock_

integer 

Number of times favorited

google_spreadsheet_formula

_lock_

string 

Google Spreadsheet Formula

image_embed_url

_lock_

string 

Image Embed Url

is_run_on_load

boolean 

auto-run query when Look viewed

last_accessed_at

_lock_

string 

Time that the Look was last accessed by any user

last_updater_id

_lock_

string 

Id of User that last updated the look.

last_viewed_at

_lock_

string 

Time last viewed in the Looker web UI

model

_lock_

[LookModel](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookModel)

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

public

boolean 

Is Public

public_slug

_lock_

string 

Public Slug

public_url

_lock_

string 

Public Url

query_id

string 

Query Id

short_url

_lock_

string 

Short Url

folder

_lock_

[FolderBase](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/FolderBase)

Folder of this Look

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

folder_id

string 

Folder Id

updated_at

_lock_

string 

Time that the Look was updated.

user_name

_lock_

string 

Name of User that created the look.

view_count

_lock_

integer 

Number of times viewed in the Looker web UI

usage_count

_lock_

integer 

Number of queries executed on this look in the last N days

is_owner_disabled

_lock_

boolean 

Is the owner disabled

query

_lock_

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Query)

Query

Expand Query definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

model

string 

Model

view

string 

Explore Name

fields

string[] 

pivots

string[] 

fill_fields

string[] 

filters

object 

Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.

filter_expression

string 

Filter Expression

sorts

string[] 

limit

string 

Row limit. To download unlimited results, set the limit to -1 (negative one).

column_limit

string 

Column Limit

total

boolean 

Total

row_total

string 

Raw Total

subtotals

string[] 

vis_config

object 

Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

filter_config

object 

The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

visible_ui_sections

string 

Visible UI Sections

slug

_lock_

string 

Slug

dynamic_fields

string 

Dynamic Fields

client_id

string 

Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

share_url

_lock_

string 

Share Url

expanded_share_url

_lock_

string 

Expanded Share Url

url

_lock_

string 

Expanded Url

query_timezone

string 

Query Timezone

has_table_calculations

_lock_

boolean 

Has Table Calculations

url

_lock_

string 

Url

look_id

string 

Id Of Look

lookml_link_id

_lock_

string 

LookML link ID

merge_result_id

string 

ID of merge result

note_display

string 

Note Display

note_state

string 

Note State

note_text

string 

Note Text

note_text_as_html

_lock_

string 

Note Text as Html

query

_lock_

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Query)

Query

Expand Query definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

model

string 

Model

view

string 

Explore Name

fields

string[] 

pivots

string[] 

fill_fields

string[] 

filters

object 

Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.

filter_expression

string 

Filter Expression

sorts

string[] 

limit

string 

Row limit. To download unlimited results, set the limit to -1 (negative one).

column_limit

string 

Column Limit

total

boolean 

Total

row_total

string 

Raw Total

subtotals

string[] 

vis_config

object 

Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

filter_config

object 

The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

visible_ui_sections

string 

Visible UI Sections

slug

_lock_

string 

Slug

dynamic_fields

string 

Dynamic Fields

client_id

string 

Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

share_url

_lock_

string 

Share Url

expanded_share_url

_lock_

string 

Expanded Share Url

url

_lock_

string 

Expanded Url

query_timezone

string 

Query Timezone

has_table_calculations

_lock_

boolean 

Has Table Calculations

query_id

string 

Id Of Query

filter_id

string 

ID of the filter this element represents

refresh_interval

string 

Refresh Interval

refresh_interval_to_i

_lock_

integer 

Refresh Interval as integer

result_maker

[ResultMakerWithIdVisConfigAndDynamicFields](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ResultMakerWithIdVisConfigAndDynamicFields)

Data about the result maker.

Expand ResultMakerWithIdVisConfigAndDynamicFields definition... 

id

_lock_

string 

Unique Id.

dynamic_fields

string 

JSON string of dynamic field information.

filterables

[ResultMakerFilterables](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ResultMakerFilterables)[] 

Expand ResultMakerFilterables definition... 

model

string 

The model this filterable comes from (used for field suggestions).

view

string 

The view this filterable comes from (used for field suggestions).

name

string 

The name of the filterable thing (Query or Merged Results).

listen

[ResultMakerFilterablesListen](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ResultMakerFilterablesListen)[] 

sorts

string[] 

merge_result_id

string 

ID of merge result if this is a merge_result.

total

boolean 

Total of the constituent Look, Query, or Merge Query

query_id

_lock_

string 

ID of query if this is a query.

sql_query_id

string 

ID of SQL Query if this is a SQL Runner Query

query

_lock_

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Query)

Query

Expand Query definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

model

string 

Model

view

string 

Explore Name

fields

string[] 

pivots

string[] 

fill_fields

string[] 

filters

object 

Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.

filter_expression

string 

Filter Expression

sorts

string[] 

limit

string 

Row limit. To download unlimited results, set the limit to -1 (negative one).

column_limit

string 

Column Limit

total

boolean 

Total

row_total

string 

Raw Total

subtotals

string[] 

vis_config

object 

Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

filter_config

object 

The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

visible_ui_sections

string 

Visible UI Sections

slug

_lock_

string 

Slug

dynamic_fields

string 

Dynamic Fields

client_id

string 

Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

share_url

_lock_

string 

Share Url

expanded_share_url

_lock_

string 

Expanded Share Url

url

_lock_

string 

Expanded Url

query_timezone

string 

Query Timezone

has_table_calculations

_lock_

boolean 

Has Table Calculations

vis_config

object 

Vis config of the constituent Query, or Merge Query.

result_maker_id

string 

ID of the ResultMakerLookup entry.

subtitle_text

string 

Text tile subtitle text

title

string 

Title of dashboard element

title_hidden

boolean 

Whether title is hidden

title_text

string 

Text tile title

type

string 

Type

alert_count

_lock_

integer 

Count of Alerts associated to a dashboard element

rich_content_json

string 

JSON with all the properties required for rich editor and buttons elements

title_text_as_html

_lock_

string 

Text tile title text as Html

subtitle_text_as_html

_lock_

string 

Text tile subtitle text as Html

extension_id

string 

Extension ID

aria_description

string 

Custom ARIA description text

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

image_id

string 

ID of Dashboard Image

images

[Image](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Image)[] 

Expand Image definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

file_name

_lock_

string 

Original file name

format

_lock_

string 

Image format (e.g. PNG, JPG)

label

string 

Accessibility label

url

_lock_

string 

URL of the image

created_at

_lock_

string 

Creation timestamp

updated_at

_lock_

string 

Update timestamp

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

## Examples

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py#L34 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
