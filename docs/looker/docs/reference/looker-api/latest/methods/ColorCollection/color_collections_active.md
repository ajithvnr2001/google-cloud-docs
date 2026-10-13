---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collections_active/
title: Get Active Color Collections \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:25.740312+00:00
---

# Get Active Color Collections  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/color_collections_active/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Active Color Collections Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Get active color collections including default, custom, and standard collections for visualization rendering and theming. Accessible to all authenticated users.

## Request

GET /color_collections/active 

Datatype

Description

Request

HTTP Request 

## Response

### 200: Active Color Collections

Datatype

Description

(object)

[ActiveColorCollections](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ActiveColorCollections)

default_collection_id

_lock_

string 

ID of default color collection

default_colors

string[] 

custom

[ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorCollection)[] 

Expand ColorCollection definition... 

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

standard

[ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ColorCollection)[] 

Expand ColorCollection definition... 

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
