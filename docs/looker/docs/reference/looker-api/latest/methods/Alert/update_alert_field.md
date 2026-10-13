---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/update_alert_field/
title: Update select fields on an alert \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:05.963563+00:00
---

# Update select fields on an alert  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/update_alert_field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update select fields on an alert Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update select alert fields

# Available fields: `owner_id`, `is_disabled`, `disabled_reason`, `is_public`, `threshold`, `enhancements`

# 

## Request

PATCH /alerts/{alert_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

alert_id

string 

ID of an alert

body

HTTP Body 

Expand HTTP Body definition... 

body

[AlertPatch](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertPatch)

Alert

Expand AlertPatch definition... 

owner_id

string 

New owner ID of the alert

is_disabled

boolean 

Set alert enabled or disabled

disabled_reason

string 

The reason this alert is disabled

is_public

boolean 

Set alert public or private

threshold

number 

New threshold value

enhancements

string 

Enum of additional alert properties. Valid values are: "NONE", "STRATEGIC_NARRATIVE".

## Response

### 200: The alert is saved.

Datatype

Description

(object)

[Alert](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Alert)

applied_dashboard_filters

[AlertAppliedDashboardFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertAppliedDashboardFilter)[] 

Expand AlertAppliedDashboardFilter definition... 

filter_title

string 

Field Title. Refer to `DashboardFilter.title` in [DashboardFilter](#!/types/DashboardFilter). Example `Name`

field_name

string 

Field Name. Refer to `DashboardFilter.dimension` in [DashboardFilter](#!/types/DashboardFilter). Example `distribution_centers.name`

filter_value

string 

Field Value. [Filter Expressions](https://docs.cloud.google.com/looker/docs/reference/filter-expressions). Example `Los Angeles CA`

filter_description

_lock_

string 

Human Readable Filter Description. This may be null or auto-generated. Example `is Los Angeles CA`

comparison_type

string 

This property informs the check what kind of comparison we are performing. Only certain condition types are valid for time series alerts. For details, refer to [Setting Alert Conditions](https://docs.cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts#setting_alert_conditions) Valid values are: "EQUAL_TO", "GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO", "LESS_THAN", "LESS_THAN_OR_EQUAL_TO", "INCREASES_BY", "DECREASES_BY", "CHANGES_BY".

cron

string 

Vixie-Style crontab specification when to run. At minimum, it has to be longer than 15 minute intervals

query_id

string 

ID of the query

custom_url_base

string 

Domain for the custom url selected by the alert creator from the admin defined domain allowlist

custom_url_params

string 

Parameters and path for the custom url defined by the alert creator

custom_url_label

string 

Label for the custom url defined by the alert creator

show_custom_url

boolean 

Boolean to determine if the custom url should be used

custom_title

string 

An optional, user-defined title for the alert

dashboard_element_id

string 

ID of the dashboard element associated with the alert. Refer to [dashboard_element()](#!/Dashboard/DashboardElement)

description

string 

An optional description for the alert. This supplements the title

enhancements

string 

Enum of additional alert properties. Valid values are: "NONE", "STRATEGIC_NARRATIVE".

destinations

[AlertDestination](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertDestination)[] 

Expand AlertDestination definition... 

destination_type

string 

Type of destination that the alert will be sent to Valid values are: "EMAIL", "ACTION_HUB".

email_address

string 

Email address for the 'email' type

action_hub_integration_id

string 

Action hub integration id for the 'action_hub' type. [Integration](#!/types/Integration)

action_hub_form_params_json

string 

Action hub form params json for the 'action_hub' type [IntegrationParam](#!/types/IntegrationParam)

field

[AlertField](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertField)

The field the alert threshold is compared against when determining when to send notifications

Expand AlertField definition... 

title

string 

Field's title. Usually auto-generated to reflect field name and its filters

name

string 

Field's name. Has the format `.` Refer to [docs](https://docs.cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts) for more details

filter

[AlertFieldFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertFieldFilter)[] 

Expand AlertFieldFilter definition... 

field_name

string 

Field Name. Has format `.`

field_value

any 

Field Value. Depends on the type of field - numeric or string. For [location](https://docs.cloud.google.com/looker/docs/reference/field-reference/dimension-type-reference#location) type, it's a list of floats. Example `[1.0, 56.0]`

filter_value

string 

Filter Value. Usually null except for [location](https://docs.cloud.google.com/looker/docs/reference/field-reference/dimension-type-reference#location) type. It'll be a string of lat,long ie `'1.0,56.0'`

followed

_lock_

boolean 

Whether or not the user follows this alert.

followable

_lock_

boolean 

Whether or not the alert is followable

id

_lock_

string 

ID of the alert

is_disabled

boolean 

Whether or not the alert is disabled

disabled_reason

string 

Reason for disabling alert

is_public

boolean 

Whether or not the alert is public

investigative_content_type

string 

The type of the investigative content Valid values are: "dashboard".

investigative_content_id

string 

The ID of the investigative content. For dashboards, this will be the dashboard ID

investigative_content_title

_lock_

string 

The title of the investigative content.

lookml_dashboard_id

string 

ID of the LookML dashboard associated with the alert

lookml_link_id

string 

ID of the LookML dashboard element associated with the alert

owner_id

string 

User id of alert owner

owner_display_name

_lock_

string 

Alert owner's display name

threshold

number 

Value of the alert threshold

time_series_condition_state

[AlertConditionState](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertConditionState)

(Write-Only) (Optional) Only used when first creating time series alerts. It's used to pick a starting time reference from which alerts will be evaluated again. Without it, alerts be run against all time series data. Refer to [docs](https://docs.cloud.google.com/looker/docs/sharing-and-publishing/creating-alerts) for details. Example `{ latest_time_series_id: '2020-09-17', previous_time_series_id: '2020-09-16' }`.

Expand AlertConditionState definition... 

previous_time_series_id

string 

(Write-Only) The second latest time string the alert has seen.

latest_time_series_id

string 

(Write-Only) Latest time string the alert has seen.

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
