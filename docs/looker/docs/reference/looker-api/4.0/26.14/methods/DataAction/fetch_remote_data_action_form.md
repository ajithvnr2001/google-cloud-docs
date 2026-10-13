---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/DataAction/fetch_remote_data_action_form/
title: Fetch Remote Data Action Form \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:45.365185+00:00
---

# Fetch Remote Data Action Form  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/methods/DataAction/fetch_remote_data_action_form/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Fetch Remote Data Action Form Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.14 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

For some data actions, the remote server may supply a form requesting further user input. This endpoint takes a data action, asks the remote server to generate a form for it, and returns that form to you for presentation to the user.

## Request

POST /data_actions/form 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

object 

Data Action Request

## Response

### 200: Data Action Form

Datatype

Description

(object)

[DataActionForm](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/DataActionForm)

state

_lock_

[DataActionUserState](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/DataActionUserState)

User state

Expand DataActionUserState definition... 

data

_lock_

string 

User state data

refresh_time

_lock_

integer 

Time in seconds until the state needs to be refreshed

fields

[DataActionFormField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/DataActionFormField)[] 

Expand DataActionFormField definition... 

name

_lock_

string 

Name

label

_lock_

string 

Human-readable label

description

_lock_

string 

Description of field

type

_lock_

string 

Type of field.

default

_lock_

string 

Default value of the field.

oauth_url

_lock_

string 

The URL for an oauth link, if type is 'oauth_link'.

interactive

_lock_

boolean 

Whether or not a field supports interactive forms.

required

_lock_

boolean 

Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation.

options

[DataActionFormSelectOption](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.14/types/DataActionFormSelectOption)[] 

Expand DataActionFormSelectOption definition... 

name

_lock_

string 

Name

label

_lock_

string 

Human-readable label

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
