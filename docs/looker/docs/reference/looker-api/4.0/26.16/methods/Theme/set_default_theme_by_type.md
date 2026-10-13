---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Theme/set_default_theme_by_type/
title: Set Default Theme (with type) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:12.667662+00:00
---

# Set Default Theme (with type)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Theme/set_default_theme_by_type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Set Default Theme (with type) Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Set the global default theme by theme name

Only Admin users can call this function.

Only an active theme with no expiration (`end_at` not set) can be assigned as the default theme. As long as a theme has an active record with no expiration, it can be set as the default.

[Create Theme](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Theme/create) has detailed information on rules for default and active themes

Returns the new specified default theme object.

The optional `theme_type` parameter can specify the theme type to select for.

## Request

PUT /themes/default_theme 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

name

string 

Name of theme to set as default

theme_type

string 

Theme type.

## Response

### 200: Theme

Datatype

Description

(object)

[Theme](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Theme)

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

[ThemeSettings](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ThemeSettings)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationErrorDetail)[] 

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
