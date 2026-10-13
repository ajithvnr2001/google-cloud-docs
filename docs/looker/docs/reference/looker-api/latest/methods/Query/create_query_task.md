---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_query_task/
title: Run Query Async \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:50.595534+00:00
---

# Run Query Async  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_query_task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Run Query Async Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Create an async query task

Creates a query task (job) to run a previously created query asynchronously. Returns a Query Task ID.

Use [query_task(query_task_id)](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query_task) to check the execution status of the query task. After the query task status reaches "Complete", use [query_task_results(query_task_id)](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query_task_results) to fetch the results of the query.

**Note** : Streaming queries only write results to the cache when using the `json_detail` format. Queries in other formats only populate the cache if they cannot be streamed (such as when table calculations or row totals are present). Once cached, all result formats can retrieve results from the cache.

## Request

POST /query_tasks 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[CreateQueryTask](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CreateQueryTask)

Query parameters

Expand CreateQueryTask definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

query_id

string 

Id of query to run

result_format

string 

Desired async query result format. Valid values are: "inline_json", "json", "json_detail", "json_fe", "json_bi", "csv", "html", "md", "txt", "xlsx", "gsxml", "sql", "odc".

source

string 

Source of query task

deferred

boolean 

Create the task but defer execution

look_id

string 

Id of look associated with query.

dashboard_id

string 

Id of dashboard associated with query.

query

HTTP Query 

Expand HTTP Query definition... 

limit

integer 

Row limit (may override the limit in the saved query).

apply_formatting

boolean 

Apply model-specified formatting to each result.

apply_vis

boolean 

Apply visualization options to results.

cache

boolean 

Get results from cache if available.

generate_drill_links

boolean 

Generate drill links (only applicable to 'json_detail' format.

force_production

boolean 

Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used.

cache_only

boolean 

Retrieve any results from cache even if the results have expired.

path_prefix

string 

Prefix to use for drill links (url encoded).

rebuild_pdts

boolean 

Rebuild PDTS used in query.

server_table_calcs

boolean 

Perform table calculations on query results

fields

string 

Requested fields

## Response

### 200: query_task

Datatype

Description

(object)

[QueryTask](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/QueryTask)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

query_id

string 

Id of query

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

generate_links

boolean 

whether or not to generate links in the query response.

force_production

boolean 

Use production models to run query (even is user is in dev mode).

path_prefix

string 

Prefix to use for drill links.

cache

boolean 

Whether or not to use the cache

server_table_calcs

boolean 

Whether or not to run table calculations on the server

cache_only

boolean 

Retrieve any results from cache even if the results have expired.

cache_key

_lock_

string 

cache key used to cache query.

status

string 

Status of query task.

source

string 

Source of query task.

runtime

_lock_

number 

Runtime of prior queries.

rebuild_pdts

boolean 

Rebuild PDTS used in query.

result_source

_lock_

string 

Source of the results of the query.

look_id

string 

Id of look associated with query.

dashboard_id

string 

Id of dashboard associated with query.

result_format

_lock_

string 

The data format of the query results.

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

### 409: Resource Already Exists

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_csv.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_csv.py#L74 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/download_dashboard_csv.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py#L33 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py#L70 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L233 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L130 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
---  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts#L198 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts#L980 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts#L422 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
