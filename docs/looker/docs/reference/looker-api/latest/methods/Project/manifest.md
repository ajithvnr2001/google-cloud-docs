---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/manifest/
title: Get Manifest \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:40.015271+00:00
---

# Get Manifest  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/manifest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Manifest Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Get A Projects Manifest object

Returns the project with the given project id

## Request

GET /projects/{project_id}/manifest 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

project_id

string 

Project Id

## Response

### 200: Manifest

Datatype

Description

(object)

[Manifest](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Manifest)

can

_lock_

object 

Operations the current user is able to perform on this object

name

_lock_

string 

Manifest project name

imports

[ImportedProject](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ImportedProject)[] 

Expand ImportedProject definition... 

name

_lock_

string 

Dependency name

url

_lock_

string 

Url for a remote dependency

ref

_lock_

string 

Ref for a remote dependency

is_remote

_lock_

boolean 

Flag signifying if a dependency is remote or local

localization_settings

_lock_

[LocalizationSettings](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LocalizationSettings)

Localization settings for a project

Expand LocalizationSettings definition... 

default_locale

_lock_

string 

Default locale for localization

localization_level

_lock_

string 

Localization level - strict or permissive

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
