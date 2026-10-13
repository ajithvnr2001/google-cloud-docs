---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DataAction/perform_data_action/
title: Send a Data Action \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:56.557461+00:00
---

# Send a Data Action  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DataAction/perform_data_action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Send a Data Action Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Perform a data action. The data action object can be obtained from query results, and used to perform an arbitrary action.

## Request

POST /data_actions 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[DataActionRequest](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataActionRequest)

Data Action Request

Expand DataActionRequest definition... 

action

object 

The JSON describing the data action. This JSON should be considered opaque and should be passed through unmodified from the query result it came from.

form_values

object 

User input for any form values the data action might use.

## Response

### 200: Data Action Response

Datatype

Description

(object)

[DataActionResponse](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataActionResponse)

webhook_id

_lock_

string 

ID of the webhook event that sent this data action. In some error conditions, this may be null.

success

_lock_

boolean 

Whether the data action was successful.

refresh_query

_lock_

boolean 

When true, indicates that the client should refresh (rerun) the source query because the data may have been changed by the action.

validation_errors

_lock_

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationError)

Validation errors returned by the data action server.

Expand ValidationError definition... 

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

message

_lock_

string 

Optional message returned by the data action server describing the state of the action that took place. This can be used to implement custom failure messages. If a failure is related to a particular form field, the server should send back a validation error instead. The Looker web UI does not currently display any message if the action indicates 'success', but may do so in the future.

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
