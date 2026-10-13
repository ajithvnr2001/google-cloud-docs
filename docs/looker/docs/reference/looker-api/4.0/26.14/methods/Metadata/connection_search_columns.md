---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Metadata/connection_search_columns/
title: Search a connection for columns \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:27.664125+00:00
---

# Search a connection for columns  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Metadata/connection_search_columns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Search a connection for columns Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Search a connection for columns matching the specified name

**Note** : `column_name` must be a valid column name. It is not a search pattern.

## Request

GET /connections/{connection_name}/search_columns 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

connection_name

string 

Name of connection

query

HTTP Query 

Expand HTTP Query definition... 

column_name

string 

Column name to find

fields

string 

Requested fields.

## Response

### 200: Column names matching search pattern

Datatype

Description

(array)

[ColumnSearch](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ColumnSearch)[] 

schema_name

_lock_

string 

Name of schema containing the table

table_name

_lock_

string 

Name of table containing the column

column_name

_lock_

string 

Name of column

data_type

_lock_

string 

Column data type

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ValidationErrorDetail)[] 

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/Error)

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
