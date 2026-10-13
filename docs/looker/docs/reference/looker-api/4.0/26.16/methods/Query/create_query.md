---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/create_query/
title: Create Query \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:10.491953+00:00
---

# Create Query  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/create_query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create Query Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Create a query.

This allows you to create a new query that you can later run. Looker queries are immutable once created and are not deleted. If you create a query that is exactly like an existing query then the existing query will be returned and no new query will be created. Whether a new query is created or not, you can use the 'id' in the returned query with the 'run' method.

The query parameters are passed as json in the body of the request.

## Request

POST /queries 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Query)

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

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Query

Datatype

Description

(object)

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Query)

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

### 409: Resource Already Exists

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py#L110 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py#L161 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/cloud-function-content-cleanup-automation/main.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py#L40 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/large_dashboard_warning_text_automation/add_warning_to_large_dashboards.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py#L26 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py#L66 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/query_task.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py#L33 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/update_explores_in_dashboards.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L228 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L300 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L350 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L523 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
  
### Ruby

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/update_look.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/update_look.rb#L23 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/update_look.rb")  
---  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L198 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L232 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L123 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L724 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L838 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L910 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L658 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L766 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L838 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L114 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L124 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
