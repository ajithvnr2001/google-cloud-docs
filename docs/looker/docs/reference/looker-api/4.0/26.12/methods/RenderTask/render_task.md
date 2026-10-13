---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/RenderTask/render_task/
title: Get Render Task \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:57.601280+00:00
---

# Get Render Task  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/RenderTask/render_task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get Render Task Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Get information about a render task.

Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/RenderTask/get_render_task_results).

## Request

GET /render_tasks/{render_task_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

render_task_id

string 

Id of render task

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Render Task

Datatype

Description

(object)

[RenderTask](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/RenderTask)

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Date/Time render task was created

dashboard_filters

_lock_

string 

Filter values to apply to the dashboard queries, in URL query format

dashboard_id

_lock_

string 

Id of dashboard to render

dashboard_style

_lock_

string 

Dashboard layout style: single_column or tiled

finalized_at

_lock_

string 

Date/Time render task was completed

height

_lock_

integer 

Output height in pixels. Flowed layouts may ignore this value.

id

_lock_

string 

Id of this render task

look_id

_lock_

string 

Id of look to render

lookml_dashboard_id

_lock_

string 

Id of lookml dashboard to render

query_id

_lock_

string 

Id of query to render

dashboard_element_id

_lock_

string 

Id of dashboard element to render: UDD dashboard element would be numeric and LookML dashboard element would be model_name::dashboard_title::lookml_link_id

query_runtime

_lock_

number 

Number of seconds elapsed running queries

render_runtime

_lock_

number 

Number of seconds elapsed rendering data

result_format

_lock_

string 

Output format: pdf, png, or jpg

runtime

_lock_

number 

Total seconds elapsed for render task

status

_lock_

string 

Render task status: enqueued_for_query, querying, enqueued_for_render, rendering, success, failure

status_detail

_lock_

string 

Additional information about the current status

user_id

_lock_

string 

The user account permissions in which the render task will execute

width

_lock_

integer 

Output width in pixels

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_pdf.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_pdf.py#L87 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_pdf.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_look.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_look.py#L65 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_look.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_tile.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_tile.py#L54 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_tile.py")  
  
### Ruby

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/render_look_png.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/render_look_png.rb#L16 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/render_look_png.rb")  
---  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/utils.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/utils.ts#L150 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/typescript/utils.ts")  
---  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/KotlinExample.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/KotlinExample.kt#L46 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/KotlinExample.kt")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
