---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/run_look/
title: Run Look \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:29.996867+00:00
---

# Run Look  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/run_look/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Run Look Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Run a Look

Runs a given look's query and returns the results in the requested format.

Supported formats:

result_format | Description  
---|---  
json | Plain json  
json_bi | (_RECOMMENDED_) Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query. See JsonBi type for schema  
json_detail | (_LEGACY_) Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query  
csv | Comma separated values with a header  
txt | Tab separated values with a header  
html | Simple html  
md | Simple markdown  
xlsx | MS Excel spreadsheet  
sql | Returns the generated SQL rather than running the query  
png | A PNG image of the visualization of the query  
jpg | A JPG image of the visualization of the query  
  
**Note** : Streaming queries only write results to the cache when using the `json_detail` format. Queries in other formats only populate the cache if they cannot be streamed (such as when table calculations or row totals are present). Once cached, all result formats can retrieve results from the cache.

## Request

GET /looks/{look_id}/run/{result_format} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

look_id

string 

Id of look

result_format

string 

Format of result

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

image_width

integer 

Render width for image formats.

image_height

integer 

Render height for image formats.

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

## Response

### 200: Look

Datatype

Description

(string)

string 

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py#L28 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py#L33 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/lookersdk-flask/app/looker.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L480 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L483 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L486 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
  
### Ruby

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb#L27 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb#L28 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb#L36 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb#L37 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/dev_vs_prod.rb")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/rerun_failed_email_schedules.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/rerun_failed_email_schedules.rb#L15 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/rerun_failed_email_schedules.rb")  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts#L184 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/kotlin.gen.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts#L921 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/python.gen.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts#L319 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts#L396 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-codegen/src/typescript.gen.spec.ts")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
