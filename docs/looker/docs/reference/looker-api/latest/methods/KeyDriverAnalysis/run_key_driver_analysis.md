---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/KeyDriverAnalysis/run_key_driver_analysis/
title: Analyze Key Drivers \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:12.202983+00:00
---

# Analyze Key Drivers  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/KeyDriverAnalysis/run_key_driver_analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Analyze Key Drivers Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Analyze Key Drivers

Identifies the dimensional segments that most significantly drove a metric's change between two time periods.

Given a data source (a saved query or a model/explore pair), a contribution metric, and a list of dimensions to analyse, this endpoint compares a test (breach) period against a control (baseline) period and returns a ranked list of segment-level insights. Each insight reports the metric value in both periods, the absolute and relative difference, the unexpected deviation (how much a segment over or under-performed relative to the overall trend), its proportional contribution to the total change, and its a-priori support (what share of total volume that segment represents).

## Request

POST /internal/kda/analyze 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[KdaRequestPayload](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/KdaRequestPayload)

Analysis parameters

Expand KdaRequestPayload definition... 

data_source

[KdaDataSource](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/KdaDataSource)

Defines the Looker dataset. Must provide either query_id OR (model_name + explore_name).

contribution_metric

string 

The LookML measure to analyze (e.g., 'orders.total_revenue').

dimensions

string[] 

base_filters

object 

Optional Looker-syntax filters to scope the entire dataset (e.g., {'users.country': 'India'}).

baseline_filters

object 

Defines the EXPECTED, PAST, or NORMAL group (State A). For time KDA, put the past date filter here (e.g., {'orders.created_date': 'last week'}). For cohort KDA, put the baseline segment here (e.g., {'users.status': 'Active'}).

breach_filters

object 

Defines the ANOMALOUS, CURRENT, or COMPARISON group (State B). For time KDA, put the current date here. For 'Rest of Population' cohort comparisons, use a minus sign to negate the baseline (e.g., {'users.status': '-Active'}).

## Response

### 200: Analysis result as JSON

Datatype

Description

(object)

[KdaResponsePayload](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/KdaResponsePayload)

status

_lock_

string 

Status of the analysis (e.g., 'SUCCESS', 'FAILED')

dimensions

string[] 

drivers

any[] 

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
