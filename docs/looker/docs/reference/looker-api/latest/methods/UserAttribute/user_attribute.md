---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/UserAttribute/user_attribute/
title: Get User Attribute \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:19.764777+00:00
---

# Get User Attribute  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/UserAttribute/user_attribute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get User Attribute Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Get information about a user attribute.

## Request

GET /user_attributes/{user_attribute_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

user_attribute_id

string 

Id of user attribute

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: User Attribute

Datatype

Description

(object)

[UserAttribute](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserAttribute)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of user attribute

label

string 

Human-friendly label for user attribute

type

string 

Type of user attribute ("string", "number", "datetime", "yesno", "zipcode", "advanced_filter_string", "advanced_filter_number", "file")

default_value

string 

Default value for when no value is set on the user

is_system

_lock_

boolean 

Attribute is a system default

is_permanent

_lock_

boolean 

Attribute is permanent and cannot be deleted

value_is_hidden

boolean 

If true, users will not be able to view values of this attribute

user_can_view

boolean 

Non-admin users can see the values of their attributes and use them in filters

user_can_edit

boolean 

Users can change the value of this attribute for themselves

hidden_value_domain_whitelist

string 

Destinations to which a hidden attribute may be sent. Once set, cannot be edited.

needed_for_ci_run

boolean 

Whether this user attribute is needed for a CI run

value_for_ci_run

string 

The value to use for this user attribute during a CI run

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

## Examples

### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L476 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
