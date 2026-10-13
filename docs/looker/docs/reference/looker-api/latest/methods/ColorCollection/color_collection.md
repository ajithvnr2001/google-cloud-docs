---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collection/
title: Get Color Collection by ID \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:25.906539+00:00
---

# Get Color Collection by ID  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Color Collection by ID Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get a Color Collection by ID

Use this to retrieve a specific Color Collection. Get a **single** color collection by id with [ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collection)

Get all **standard** color collections with [ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collections_standard)

Get all **custom** color collections with [ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collections_custom)

**Note** : Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

## Request

GET /color_collections/{collection_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

collection_id

string 

Id of Color Collection

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: ColorCollection

Datatype

Description

(object)

[ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorCollection)

id

_lock_

string 

Unique Id

label

string 

Label of color collection

categoricalPalettes

[DiscretePalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DiscretePalette)[] 

Expand DiscretePalette definition... 

id

_lock_

string 

Unique identity string

label

string 

Label for palette

type

string 

Type of palette

colors

string[] 

sequentialPalettes

[ContinuousPalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContinuousPalette)[] 

Expand ContinuousPalette definition... 

id

_lock_

string 

Unique identity string

label

string 

Label for palette

type

string 

Type of palette

stops

[ColorStop](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorStop)[] 

Expand ColorStop definition... 

color

string 

CSS color string

offset

integer 

Offset in continuous palette (0 to 100)

divergingPalettes

[ContinuousPalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ContinuousPalette)[] 

Expand ContinuousPalette definition... 

id

_lock_

string 

Unique identity string

label

string 

Label for palette

type

string 

Type of palette

stops

[ColorStop](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorStop)[] 

Expand ColorStop definition... 

color

string 

CSS color string

offset

integer 

Offset in continuous palette (0 to 100)

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L258 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
