---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_custom_welcome_email_test/
title: Send a test welcome email to the currently logged in user with the supplied content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:26.787839+00:00
---

# Send a test welcome email to the currently logged in user with the supplied content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_custom_welcome_email_test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Send a test welcome email to the currently logged in user with the supplied content Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Requests to this endpoint will send a welcome email with the custom content provided in the body to the currently logged in user.

## Request

PUT /custom_welcome_email_test 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[WelcomeEmailTest](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WelcomeEmailTest)

Subject, header, and Body of the email to be sent.

Expand WelcomeEmailTest definition... 

content

string 

The content that would be sent in the body of a custom welcome email

subject

string 

The subject that would be sent for the custom welcome email

header

string 

The header that would be sent in the body of a custom welcome email

## Response

### 200: Send Test Welcome Email

Datatype

Description

(object)

[WelcomeEmailTest](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WelcomeEmailTest)

content

string 

The content that would be sent in the body of a custom welcome email

subject

string 

The subject that would be sent for the custom welcome email

header

string 

The header that would be sent in the body of a custom welcome email

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
