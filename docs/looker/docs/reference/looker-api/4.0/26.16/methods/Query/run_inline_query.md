---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/run_inline_query/
title: Run Inline Query \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:20.619506+00:00
---

# Run Inline Query  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/run_inline_query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Run Inline Query Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Run the query that is specified inline in the posted body.

This allows running a query as defined in json in the posted body. This combines the two actions of posting & running a query into one step.

Here is an example body in json:
    
    
    {
      "model":"thelook",
      "view":"inventory_items",
      "fields":["category.name","inventory_items.days_in_inventory_tier","products.count"],
      "filters":{"category.name":"socks"},
      "sorts":["products.count desc 0"],
      "limit":"500",
      "query_timezone":"America/Los_Angeles"
    }
    

When using the Ruby SDK this would be passed as a Ruby hash like:
    
    
    {
     :model=>"thelook",
     :view=>"inventory_items",
     :fields=>
      ["category.name",
       "inventory_items.days_in_inventory_tier",
       "products.count"],
     :filters=>{:"category.name"=>"socks"},
     :sorts=>["products.count desc 0"],
     :limit=>"500",
     :query_timezone=>"America/Los_Angeles",
    }
    

This will return the result of running the query in the format specified by the 'result_format' parameter.

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

POST /queries/run/{result_format} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

result_format

string 

Format of result

body

HTTP Body 

Expand HTTP Body definition... 

body

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Query)

inline query

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

### 200: Query Result

Datatype

Description

(string)

string 

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

### 403: Database OAuth Error

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

## Examples

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/run_look_with_filters.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/run_look_with_filters.py#L62 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/run_look_with_filters.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L330 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L340 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L248 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
### TSX

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-tile-playground/src/components/DashboardTile/DashboardTile.tsx ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-tile-playground/src/components/DashboardTile/DashboardTile.tsx#L66 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/extension-tile-playground/src/components/DashboardTile/DashboardTile.tsx")  
---  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L795 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L806 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L725 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L736 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
