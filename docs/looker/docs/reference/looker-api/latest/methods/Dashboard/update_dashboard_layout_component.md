---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_layout_component/
title: Update DashboardLayoutComponent \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:54.574553+00:00
---

# Update DashboardLayoutComponent  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_layout_component/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update DashboardLayoutComponent Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update the dashboard element with a specific id.

## Request

PATCH /dashboard_layout_components/{dashboard_layout_component_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

dashboard_layout_component_id

string 

Id of dashboard layout component

body

HTTP Body 

Expand HTTP Body definition... 

body

[DashboardLayoutComponent](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardLayoutComponent)

DashboardLayoutComponent

Expand DashboardLayoutComponent definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

dashboard_layout_id

string 

Id of Dashboard Layout

dashboard_element_id

string 

Id Of Dashboard Element

row

integer 

Row

column

integer 

Column

width

integer 

Width

height

integer 

Height

deleted

boolean 

Whether or not the dashboard layout component is deleted

element_title

_lock_

string 

Dashboard element title, extracted from the Dashboard Element.

element_title_hidden

_lock_

boolean 

Whether or not the dashboard element title is displayed.

vis_type

_lock_

string 

Visualization type, extracted from a query's vis_config

granular_row

integer 

Row (granular layout)

granular_column

integer 

Column (granular layout)

granular_width

integer 

Width (granular layout)

granular_height

integer 

Height (granular layout)

group_id

string 

Id of parent Dashboard Layout Component group

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: DashboardLayoutComponent

Datatype

Description

(object)

[DashboardLayoutComponent](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardLayoutComponent)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

dashboard_layout_id

string 

Id of Dashboard Layout

dashboard_element_id

string 

Id Of Dashboard Element

row

integer 

Row

column

integer 

Column

width

integer 

Width

height

integer 

Height

deleted

boolean 

Whether or not the dashboard layout component is deleted

element_title

_lock_

string 

Dashboard element title, extracted from the Dashboard Element.

element_title_hidden

_lock_

boolean 

Whether or not the dashboard element title is displayed.

vis_type

_lock_

string 

Visualization type, extracted from a query's vis_config

granular_row

integer 

Row (granular layout)

granular_column

integer 

Column (granular layout)

granular_width

integer 

Width (granular layout)

granular_height

integer 

Height (granular layout)

group_id

string 

Id of parent Dashboard Layout Component group

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py#L97 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py#L119 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
