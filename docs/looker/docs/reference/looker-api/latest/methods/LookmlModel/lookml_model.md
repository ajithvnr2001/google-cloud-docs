---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model/
title: Get LookML Model \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:48.709360+00:00
---

# Get LookML Model  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get LookML Model Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get information about a lookml model.

## Request

GET /lookml_models/{lookml_model_name} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

lookml_model_name

string 

Name of lookml model.

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: LookML Model

Datatype

Description

(object)

[LookmlModel](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModel)

can

_lock_

object 

Operations the current user is able to perform on this object

allowed_db_connection_names

string[] 

explores

[LookmlModelNavExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModelNavExplore)[] 

Expand LookmlModelNavExplore definition... 

name

_lock_

string 

Name of the explore

description

_lock_

string 

Description for the explore

label

_lock_

string 

Label for the explore

hidden

_lock_

boolean 

Is this explore marked as hidden

group_label

_lock_

string 

Label used to group explores in the navigation menus

has_content

_lock_

boolean 

Does this model declaration have have lookml content?

label

_lock_

string 

UI-friendly name for this model

name

string 

Name of the model. Also used as the unique identifier

project_name

string 

Name of project containing the model

unlimited_db_connections

boolean 

Is this model allowed to use all current and future connections

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L389 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
