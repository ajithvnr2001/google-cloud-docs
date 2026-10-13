---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ConversationalAnalytics/create_golden_query/
title: Create Golden Query \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:45.096116+00:00
---

# Create Golden Query  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ConversationalAnalytics/create_golden_query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Create Golden Query Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Create Golden Query

Creates a golden query.

## Request

POST /golden_queries 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[GoldenQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/GoldenQuery)

Golden Query

Expand GoldenQuery definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

integer 

Unique identifier for the golden question

query_id

_lock_

integer 

ID of the associated Looker Query resolved from the answer

questions

string[] 

answer

string 

The Explore URL representing the answer to the question

is_active

_lock_

boolean 

Whether this golden question should be utilized by the agent

created_by_user_id

_lock_

integer 

ID of the user who created the question

last_updated_by_user_id

_lock_

integer 

ID of the user who last updated the question

created_at

_lock_

string 

Time when the question was created

last_updated_at

_lock_

string 

Time when the question was last updated

explore

_lock_

string 

The explore name of the golden query

model

_lock_

string 

The LookML model name of the golden query

fields

string[] 

filters

_lock_

object 

Filters of the associated Looker Query

sorts

string[] 

limit

_lock_

string 

Limit of the associated Looker Query

client_id

_lock_

string 

Client ID of the associated Looker Query

pivots

string[] 

dynamic_fields

_lock_

string 

Dynamic fields of the associated Looker Query

## Response

### 200: Golden Query

Datatype

Description

(object)

[GoldenQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/GoldenQuery)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

integer 

Unique identifier for the golden question

query_id

_lock_

integer 

ID of the associated Looker Query resolved from the answer

questions

string[] 

answer

string 

The Explore URL representing the answer to the question

is_active

_lock_

boolean 

Whether this golden question should be utilized by the agent

created_by_user_id

_lock_

integer 

ID of the user who created the question

last_updated_by_user_id

_lock_

integer 

ID of the user who last updated the question

created_at

_lock_

string 

Time when the question was created

last_updated_at

_lock_

string 

Time when the question was last updated

explore

_lock_

string 

The explore name of the golden query

model

_lock_

string 

The LookML model name of the golden query

fields

string[] 

filters

_lock_

object 

Filters of the associated Looker Query

sorts

string[] 

limit

_lock_

string 

Limit of the associated Looker Query

client_id

_lock_

string 

Client ID of the associated Looker Query

pivots

string[] 

dynamic_fields

_lock_

string 

Dynamic fields of the associated Looker Query

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
