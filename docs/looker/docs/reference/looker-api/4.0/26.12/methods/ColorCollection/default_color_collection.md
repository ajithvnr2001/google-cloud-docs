---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/ColorCollection/default_color_collection/
title: Get Default Color Collection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:14.841612+00:00
---

# Get Default Color Collection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/ColorCollection/default_color_collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get Default Color Collection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Get the default color collection

Use this to retrieve the default Color Collection.

Set the default color collection with [ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/ColorCollection/set_default_color_collection)

## Request

GET /color_collections/default 

Datatype

Description

Request

HTTP Request 

## Response

### 200: ColorCollection

Datatype

Description

(object)

[ColorCollection](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ColorCollection)

id

_lock_

string 

Unique Id

label

string 

Label of color collection

categoricalPalettes

[DiscretePalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/DiscretePalette)[] 

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

[ContinuousPalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ContinuousPalette)[] 

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

[ColorStop](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ColorStop)[] 

Expand ColorStop definition... 

color

string 

CSS color string

offset

integer 

Offset in continuous palette (0 to 100)

divergingPalettes

[ContinuousPalette](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ContinuousPalette)[] 

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

[ColorStop](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ColorStop)[] 

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L175 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L185 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L302 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L314 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L287 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L297 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
  
### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L416 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
---  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L413 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L422 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
