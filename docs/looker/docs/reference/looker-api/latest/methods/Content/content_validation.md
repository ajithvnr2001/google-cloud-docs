---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/content_validation/
title: Validate Content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:40.621063+00:00
---

# Validate Content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Content/content_validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Validate Content Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Validate All Content

Performs validation of all looks and dashboards Returns a list of errors found as well as metadata about the content validation run.

## Request

GET /content_validation 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

project_names

string[] 

space_ids

string[] 

## Response

### 200: Content validation results

Datatype

Description

(object)

[ContentValidation](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidation)

content_with_errors

[ContentValidatorError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidatorError)[] 

Expand ContentValidatorError definition... 

look

_lock_

[ContentValidationLook](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationLook)

Expand ContentValidationLook definition... 

id

_lock_

string 

Unique Id

title

string 

Look Title

short_url

_lock_

string 

Short Url

folder

_lock_

[ContentValidationFolder](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationFolder)

Folder of this Look

dashboard

_lock_

[ContentValidationDashboard](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationDashboard)

Expand ContentValidationDashboard definition... 

description

string 

Description

id

_lock_

string 

Unique Id

folder

_lock_

[ContentValidationFolder](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationFolder)

Folder

title

string 

Dashboard Title

url

_lock_

string 

Relative URL of the dashboard

dashboard_element

_lock_

[ContentValidationDashboardElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationDashboardElement)

Expand ContentValidationDashboardElement definition... 

body_text

string 

Text tile body text

dashboard_id

string 

Id of Dashboard

id

_lock_

string 

Unique Id

look_id

string 

Id Of Look

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

query_id

string 

Id Of Query

filter_id

string 

ID of the filter this element represents

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

rich_content_json

string 

JSON with all the properties required for rich editor and buttons elements

extension_id

string 

Extension ID

aria_description

string 

Custom ARIA description text

dashboard_filter

_lock_

[ContentValidationDashboardFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationDashboardFilter)

Expand ContentValidationDashboardFilter definition... 

id

_lock_

string 

Unique Id

dashboard_id

_lock_

string 

Id of Dashboard

name

string 

Name of filter

title

string 

Title of filter

type

string 

Type of filter: one of date, number, string, or field

default_value

string 

Default value of filter

model

string 

Model of filter (required if type = field)

explore

string 

Explore of filter (required if type = field)

dimension

string 

Dimension of filter (required if type = field)

scheduled_plan

_lock_

[ContentValidationScheduledPlan](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationScheduledPlan)

Expand ContentValidationScheduledPlan definition... 

name

string 

Name of this scheduled plan

look_id

string 

Id of a look

id

_lock_

string 

Unique Id

alert

_lock_

[ContentValidationAlert](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationAlert)

Expand ContentValidationAlert definition... 

id

string 

ID of the alert

lookml_dashboard_id

string 

ID of the LookML dashboard associated with the alert

lookml_link_id

string 

ID of the LookML dashboard element associated with the alert

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

lookml_dashboard

_lock_

[ContentValidationLookMLDashboard](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationLookMLDashboard)

Expand ContentValidationLookMLDashboard definition... 

id

_lock_

string 

ID of the LookML Dashboard

title

_lock_

string 

Title of the LookML Dashboard

space_id

_lock_

string 

ID of Space

lookml_dashboard_element

_lock_

[ContentValidationLookMLDashboardElement](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationLookMLDashboardElement)

Expand ContentValidationLookMLDashboardElement definition... 

lookml_link_id

_lock_

string 

Link ID of the LookML Dashboard Element

title

_lock_

string 

Title of the LookML Dashboard Element

errors

[ContentValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContentValidationError)[] 

Expand ContentValidationError definition... 

message

_lock_

string 

Error message

field_name

_lock_

string 

Name of the field involved in the error

model_name

_lock_

string 

Name of the model involved in the error

explore_name

_lock_

string 

Name of the explore involved in the error

removable

_lock_

boolean 

Whether this validation error is removable

id

_lock_

string 

An id unique to this piece of content for this validation run

computation_time

_lock_

number 

Duration of content validation in seconds

total_looks_validated

_lock_

integer 

The number of looks validated

total_dashboard_elements_validated

_lock_

integer 

The number of dashboard elements validated

total_dashboard_filters_validated

_lock_

integer 

The number of dashboard filters validated

total_scheduled_plans_validated

_lock_

integer 

The number of scheduled plans validated

total_alerts_validated

_lock_

integer 

The number of alerts validated

total_explores_validated

_lock_

integer 

The number of explores used across all content validated

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/content_validator_comparison.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/content_validator_comparison.py#L58 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/content_validator_comparison.py")  
---  
  
### Ruby

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_content.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_content.rb#L15 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_content.rb")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
