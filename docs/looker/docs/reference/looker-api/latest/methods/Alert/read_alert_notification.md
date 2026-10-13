---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/read_alert_notification/
title: Read a Notification \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:07.239802+00:00
---

# Read a Notification  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Alert/read_alert_notification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Read a Notification Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

# Reads a Notification

The endpoint marks a given alert notification as read by the user, in case it wasn't already read. The AlertNotification model is updated for this purpose. It returns the notification as a response.

## Request

PATCH /alert_notifications/{alert_notification_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

alert_notification_id

string 

ID of a notification

## Response

### 200: It updates that the given alert notification has been read by the user

Datatype

Description

(object)

[AlertNotifications](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/AlertNotifications)

notification_id

_lock_

string 

ID of the notification

alert_condition_id

_lock_

string 

ID of the alert

user_id

_lock_

string 

ID of the user

is_read

boolean 

Read state of the notification

field_value

_lock_

number 

The value of the field on which the alert condition is set

threshold_value

_lock_

number 

The value of the threshold which triggers the alert notification

ran_at

_lock_

string 

The time at which the alert query ran

alert

_lock_

[MobilePayload](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/MobilePayload)

It contains the details needed for mobile alerts payload

Expand MobilePayload definition... 

title

_lock_

string 

Title of the alert

alert_id

_lock_

string 

ID of the alert

investigative_content_id

_lock_

string 

ID of the investigative content

dashboard_name

_lock_

string 

Name of the dashboard on which the alert has been set

dashboard_id

_lock_

string 

ID of the dashboard on which the alert has been set

query_slug

_lock_

string 

Slug of the query which runs the alert queries.

query_id

_lock_

string 

ID of the query

notification_type

_lock_

string 

The type of notification, 'email' or 'slack'

triggering_field_title

_lock_

string 

The title of the field on which the alert condition is set

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
