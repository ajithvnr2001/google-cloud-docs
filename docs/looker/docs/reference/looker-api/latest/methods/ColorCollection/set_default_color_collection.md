---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/set_default_color_collection/
title: Set Default Color Collection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:25.273082+00:00
---

# Set Default Color Collection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ColorCollection/set_default_color_collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Set Default Color Collection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Set the global default Color Collection by ID

Returns the new specified default Color Collection object. **Note** : Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

## Request

PUT /color_collections/default 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

collection_id

string 

ID of color collection to set as default

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

## Examples

### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L182 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt#L188 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestSmoke.kt")  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L310 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts#L316 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/methods.spec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L294 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts#L299 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk-node/test/sdk.apispec.ts")  
  
### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L424 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py#L426 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/tests/integration/test_methods.py")  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L419 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L425 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
