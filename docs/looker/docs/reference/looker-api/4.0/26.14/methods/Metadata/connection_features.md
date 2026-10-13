---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Metadata/connection_features/
title: Metadata features supported by this connection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:43.123500+00:00
---

# Metadata features supported by this connection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/Metadata/connection_features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Metadata features supported by this connection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Retrieve metadata features for this connection

Returns a list of feature names with `true` (available) or `false` (not available)

## Request

GET /connections/{connection_name}/features 

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

fields

string 

Requested fields.

## Response

### 200: Connection features

Datatype

Description

(object)

[ConnectionFeatures](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/ConnectionFeatures)

dialect_name

_lock_

string 

Name of the dialect for this connection

cost_estimate

_lock_

boolean 

True for cost estimating support

multiple_databases

_lock_

boolean 

True for multiple database support

column_search

_lock_

boolean 

True for cost estimating support

persistent_table_indexes

_lock_

boolean 

True for secondary index support

persistent_derived_tables

_lock_

boolean 

True for persistent derived table support

turtles

_lock_

boolean 

True for turtles support

percentile

_lock_

boolean 

True for percentile support

distinct_percentile

_lock_

boolean 

True for distinct percentile support

stable_views

_lock_

boolean 

True for stable views support

milliseconds

_lock_

boolean 

True for millisecond support

microseconds

_lock_

boolean 

True for microsecond support

subtotals

_lock_

boolean 

True for subtotal support

location

_lock_

boolean 

True for geographic location support

timezone

_lock_

boolean 

True for timezone conversion in query support

connection_pooling

_lock_

boolean 

True for connection pooling support

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
