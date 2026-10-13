---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_dashboard_filters/
title: Get All Dashboard Filters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:53.937606+00:00
---

# Get All Dashboard Filters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_dashboard_filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get All Dashboard Filters Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get information about all the dashboard filters on a dashboard with a specific id.

## Request

GET /dashboards/{dashboard_id}/dashboard_filters 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

dashboard_id

string 

Id of dashboard

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Dashboard Filter

Datatype

Description

(array)

[DashboardFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardFilter)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

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

field

_lock_

object 

Field information

row

integer 

Display order of this filter relative to other filters

listens_to_filters

string[] 

allow_multiple_values

boolean 

Whether the filter allows multiple filter values (deprecated in the latest version of dashboards)

required

boolean 

Whether the filter requires a value to run the dashboard

ui_config

object 

The visual configuration for this filter. Used to set up how the UI for this filter should appear.

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
