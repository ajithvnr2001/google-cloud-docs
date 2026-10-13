---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/SqlInterfaceQuery/run_sql_interface_query/
title: Run SQL Interface Query \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:55.176507+00:00
---

# Run SQL Interface Query  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/SqlInterfaceQuery/run_sql_interface_query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Run SQL Interface Query Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Run a saved SQL interface query.

This runs a previously created SQL interface query.

The 'result_format' parameter specifies the desired structure and format of the response.

Supported formats:

result_format | Description  
---|---  
json_bi | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query  
  
## Request

GET /sql_interface_queries/{query_id}/run/{result_format} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

query_id

integer 

Integer id of query

result_format

string 

Format of result, options are: ["json_bi"]

## Response

### 200: Query Result

Datatype

Description

(object)

[JsonBi](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBi)

metadata

_lock_

[JsonBiMetadata](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiMetadata)

Metadata about the query

Expand JsonBiMetadata definition... 

big_query_metadata

_lock_

[JsonBiBigQueryMetadata](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiBigQueryMetadata)

Metadata returned from Bigquery. Null if any other dialect.

Expand JsonBiBigQueryMetadata definition... 

total_bytes_processed

_lock_

integer 

Total bytes processed by the BigQuery job

backend_cache_hit

_lock_

boolean 

Return whether or not query results were served from the BigQuery cache.

fields

_lock_

[JsonBiFields](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiFields)

Fields

Expand JsonBiFields definition... 

dimensions

[JsonBiField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiField)[] 

measures

[JsonBiField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiField)[] 

pivots

[JsonBiField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiField)[] 

table_calculations

[JsonBiTableCalc](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiTableCalc)[] 

pivots

[JsonBiPivots](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/JsonBiPivots)[] 

Expand JsonBiPivots definition... 

key

_lock_

string 

Pivot Column Value

data

_lock_

object 

Pivot Data

sort_values

_lock_

object 

Pivot Sort Values

is_total

_lock_

boolean 

If the value is a total

has_subtotals

_lock_

boolean 

If the query has subtotals

has_totals

_lock_

boolean 

If the query has totals

columns_truncated

_lock_

string 

If the query results hit the maximum column limit and additional columns were truncated

filter_expression

_lock_

string 

Filter expression applied to the query results

filters

_lock_

object 

Filters applied to the query results

sql

_lock_

string 

Raw sql query. Null if user does not have permission to view sql

rows

string[] 

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

### 403: Permission Denied

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

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationErrorDetail)[] 

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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
