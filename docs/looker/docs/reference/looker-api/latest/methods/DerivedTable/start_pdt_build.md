---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/start_pdt_build/
title: Start a PDT materialization \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:58.659450+00:00
---

# Start a PDT materialization  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/start_pdt_build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Start a PDT materialization Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Enqueue materialization for a PDT with the given model name and view name

## Request

GET /derived_table/{model_name}/{view_name}/start 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

model_name

string 

The model of the PDT to start building.

view_name

string 

The view name of the PDT to start building.

query

HTTP Query 

Expand HTTP Query definition... 

force_rebuild

string 

Force rebuild of required dependent PDTs, even if they are already materialized.

force_full_incremental

string 

Force involved incremental PDTs to fully re-materialize.

workspace

string 

Workspace in which to materialize selected PDT ('dev' or default 'production').

source

string 

The source of this request.

## Response

### 200: Derived Table

Datatype

Description

(object)

[MaterializePDT](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/MaterializePDT)

materialization_id

_lock_

string 

The ID of the enqueued materialization task

resp_text

_lock_

string 

Detailed response in text format

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
