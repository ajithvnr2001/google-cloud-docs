---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Theme/search_themes/
title: Search Themes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:26.661185+00:00
---

# Search Themes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Theme/search_themes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Search Themes Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Search all themes for matching criteria.

Returns an **array of theme objects** that match the specified search criteria.

Search Parameters | Description  
---|---  
`begin_at` only | Find themes active at or after `begin_at`  
`end_at` only | Find themes active at or before `end_at`  
both set | Find themes with an active inclusive period between `begin_at` and `end_at`  
  
Note: Range matching requires boolean AND logic. When using `begin_at` and `end_at` together, do not use `filter_or`=TRUE

If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match _all_ search param criteria will be returned.

If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.

String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example="dan%" will match "danger" and "Danzig" but not "David" example="D_m%" will match "Damage" and "dump"

Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.

Most search params can accept "IS NULL" and "NOT NULL" as special expressions to match or exclude (respectively) rows where the column is null.

Boolean search params accept only "true" and "false" as values.

Get a **single theme** by id with [Theme](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Theme/theme)

**Note** : Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or <https://console.cloud.google.com/support/cases/> to update your license for this feature.

## Request

GET /themes/search 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

id

string 

Match theme id.

name

string 

Match theme name.

begin_at

string 

Timestamp for activation.

end_at

string 

Timestamp for expiration.

limit

integer 

Number of results to return (used with `offset`).

offset

integer 

Number of results to skip before returning any (used with `limit`).

sorts

string 

Fields to sort by.

fields

string 

Requested fields.

filter_or

boolean 

Combine given search criteria in a boolean OR expression

theme_type

string 

Match theme type ('internal', 'embed', or 'all').

## Response

### 200: Themes

Datatype

Description

(array)

[Theme](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Theme)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

begin_at

string 

Timestamp for when this theme becomes active. Null=always

end_at

string 

Timestamp for when this theme expires. Null=never

id

_lock_

string 

Unique Id

name

string 

Name of theme. Can only be alphanumeric and underscores.

settings

[ThemeSettings](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ThemeSettings)

Hash of name/value pairs for theme settings. These names get validated.

Expand ThemeSettings definition... 

background_color

string 

Default background color

background_image_url

string 

URL for background image

background_image_id

string 

Optional. ID of theme background image.

background_opacity

number 

Background image opacity (0.0 to 1.0).

base_font_size

string 

Base font size for scaling fonts (only supported by legacy dashboards)

color_collection_id

string 

Optional. ID of color collection to use with the theme. Use an empty string for none.

font_color

string 

Default font color

font_family

string 

Primary font family

font_source

string 

Source specification for font

info_button_color

string 

(DEPRECATED) Info button color

primary_button_color

string 

Primary button color

show_filters_bar

boolean 

Toggle to show filters. Defaults to true.

show_title

boolean 

Toggle to show the title. Defaults to true.

text_tile_text_color

string 

Text color for text tiles

tile_background_color

string 

Background color for tiles

text_tile_background_color

string 

Background color for text tiles

tile_text_color

string 

Text color for tiles

title_color

string 

Color for titles

warn_button_color

string 

(DEPRECATED) Warning button color

tile_title_alignment

string 

The text alignment of tile titles (New Dashboards)

tile_shadow

boolean 

Toggles the tile shadow (not supported)

show_last_updated_indicator

boolean 

Toggle to show the dashboard last updated indicator. Defaults to true.

show_reload_data_icon

boolean 

Toggle to show reload data icon/button. Defaults to true.

show_dashboard_menu

boolean 

Toggle to show the dashboard actions menu. Defaults to true.

show_filters_toggle

boolean 

Toggle to show the filters icon/toggle. Defaults to true.

show_dashboard_header

boolean 

Toggle to show the dashboard header. Defaults to true.

center_dashboard_title

boolean 

Toggle to center the dashboard title. Defaults to false.

dashboard_title_font_size

string 

Dashboard title font size.

box_shadow

string 

Default box shadow.

page_margin_top

string 

Dashboard page margin top.

page_margin_bottom

string 

Dashboard page margin bottom.

page_margin_sides

string 

Dashboard page margin left and right.

show_explore_header

boolean 

Toggle to show the explore page header. Defaults to true.

show_explore_title

boolean 

Toggle to show the explore page title. Defaults to true.

show_explore_last_run

boolean 

Toggle to show the explore page last run. Defaults to true.

show_explore_timezone

boolean 

Toggle to show the explore page timezone. Defaults to true.

show_explore_run_stop_button

boolean 

Toggle to show the explore page run button. Defaults to true.

show_explore_actions_button

boolean 

Toggle to show the explore page actions button. Defaults to true.

show_look_header

boolean 

Toggle to show the look page header. Defaults to true.

show_look_title

boolean 

Toggle to show the look page title. Defaults to true.

show_look_last_run

boolean 

Toggle to show the look page last run. Defaults to true.

show_look_timezone

boolean 

Toggle to show the look page timezone Defaults to true.

show_look_run_stop_button

boolean 

Toggle to show the look page run button. Defaults to true.

show_look_actions_button

boolean 

Toggle to show the look page actions button. Defaults to true.

tile_title_font_size

string 

Font size for tiles.

column_gap_size

string 

The vertical gap/gutter size between tiles.

row_gap_size

string 

The horizontal gap/gutter size between tiles.

border_radius

string 

The border radius for tiles.

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
